#!/usr/bin/env python

# Copyright 2007 Nanorex, Inc.  See LICENSE file for details.

"""
UpdateCopyright.py

This is a standalone python script intended to maintain the copyright
notices in all NE1 code.  It's intended to be used before each release
in the following way:

First, make sure you have a clean copy of all source trees.  That
means up to date with no local changes.  The 'cvs update' command
should not report any modified files.

Next, run this script with the --check option.  This will print lists
of files that meet certain criteria.  In particular, you might want to
examine the files listed as containing other copyrights.  These may
need to be verified, and perhaps updated manually.  You can make any
necessary edits now or later.

Next, run the script with the --modify option.  This will take some
time, as it runs a 'cvs log' command on each file to determine the
years in which it was modified.  New copyright lines will be written
to the files, and the changes made will be printed as context diffs.
Examine the diffs to make sure the script has done the right thing.

Finally, commit the changes to CVS.

Other options available are:

--dry-run
 Produces the diff output, but does not modify the original files.

--no-cvs
 Speeds up the run by omitting the cvs log commands for each file.
 Files are assumed to be modified in the current year only.  Old
 copyright dates are still merged into the new copyright strings, so
 this option could be used once all copyrights have been generated by
 a run without --no-cvs.  Note, however, that this will add the
 current year to a copyright line even if no checkins have occurred on
 this file in the current year.

@copyright: 2007 Nanorex, Inc.
"""

import sys
import os
import os.path
import re
import time

# command line flags
OptionCheck = False
OptionModify = False
OptionDryRun = False
OptionNoCVS = False

pathsToExclude = [
    "./src/reindent.py",  # cad, public domain
    ]

# These files must not require special comment characters.
pathsToInclude = [
    "./src/MergingParameterFiles", # sim
    "./src/merge.parameters",
    "./src/branch",                # both
    "./src/INSTALL",               # cad
    "./src/README-Pyrex",
    "./src/README-cvs-branching",
    ]

directoriesToExclude = [
    "/CVS",
    "/bin", # in cad
#    "/doc", # in cad ######################################################## temp
    "/doc/old_doc", # in cad
    "/licenses-common", # in cad
    "/licenses-Linux", # in cad
    "/licenses-Mac", # in cad
    "/licenses-Windows", # in cad
    "/src/tests", # in sim.  including could impact test comparisons
    "/src/parameters", # in sim.  lots of strange files - do by hand
    ]

# List of filename extensions to process.  Each extension is followed
# by the strings which should start and end any comment lines inserted
# into the file.
commentStringMapping = [
    "sim-params.txt", "#", "",
    ".py",   "#",    "",    # python source
    ".pyx",  "#",    "",    # pyrex source
    ".desc", "#",    "",    # plugin parameter description
    ".htm",  "<!--", "-->", # html
    ".html", "<!--", "-->", # html
    ".dwt",  "<!--", "-->", # html
    ".c",    "//",   "",    # c source
    ".cpp",  "//",   "",    # c++ source
    ".h",    "//",   "",    # c source
    ".sh",   "#",    "",    # unix shell
    ".txt",  "",     "",    # text
    "BUGS",  "",     "",
    "NOTES", "",     "",
    "README", "",    "",
    "Doxyfile", "#", "",    # project description
    "Makefile", "#", "",
    "/makethemall", "#", "", # sh script
    "/jbranch", "#", "",    # sh script
    "/rungms", "#", "",     # sh script
    "/runmac", "#", "",     # sh script
    ]

# If we're printing a message for each file we DON'T process, then we
# don't want to print such a message for any of these files.
excludeQuietly = [
    ".bmp", # binary image
    ".db",  # binary database
    ".doc", # binary word document
    ".gif", # binary image
    ".gz",  # binary archive
    ".ico", # binary image
    ".inp", # gamess input file
    ".java",# java source file (original CoNTub source)
    ".jpg", # binary image
    ".js",  # javascript -- generated by epydoc
    ".mmp", ###############
    ".moi", # ascii fragment of coordinates, no known comment structure
    ".o",   # binary
    ".parms", # ascii sim parameters intermediate -- could probably use # comment
    ".pdb", # ascii atom format -- may have comment, not sure of format
    ".png", # binary image
    ".psp", # binary image -- paint shop pro
    ".pyc", # binary compiled python
    ".so",  # binary shared library
    ".sxc", # binary -- sun xml calc
    ".ui",  # generated xml file
    ".xls", # binary spreadsheet
    ".zip", # binary archive
    ".~",   # cvs backup file
    ]

# Files which start with any of these strings should have a copyright
# inserted at the beginning, rather than after line 1 or 2.
badFirstLineStrings = [
    '"""',
    "'''",
    "/*",
    "#define",
    "#if",
    "#include",
    "//",
    "from",
    "import",
    "cdef",
    ]

# Extract year of modification from the output of "cvs log file".
cvsLogDateRegexp = re.compile(r'^date: (\d\d\d\d)-\d\d-\d\d')

# The date list regex embedded in the following regexes looks like
# this: dddd ( ,|- dddd )* a list of groups of up to four digits,
# separated by commas or dashes.

# This regex recognizes existing copyright lines, including an
# optional (c), which will be removed.
copyrightRegex = re.compile(r'Copyright\s+(?:\(c\))?\s*(\d{1,4}(\s*(\,|\-)\s*\d{1,4})*)\s+Nanorex\,\s+Inc\.')

# This regex recognizes the @copyright: epydoc field.
epydocCopyrightRegex = re.compile(r'^(.*\@copyright\:\s*)(\d{1,4}(\s*(\,|\-)\s*\d{1,4})*)(\s+Nanorex\,\s+Inc\..*)')

# This is used to extract parts of the above date range lists.  Group
# 1 is the first date, group 2 is the separator, group 3 is the
# remainder.  If there's no separator, then the whole string should
# just be the year.
dateRangeRegex = re.compile(r'(\d{1,4})\s*(\,|\-)\s*(.*)')

blankLineRegex = re.compile(r'^\s*$')

anyCopyrightRegex = re.compile(r'copyright', re.IGNORECASE)

def printExcluding(path):
    for extension in excludeQuietly:
        if (path.endswith(extension)):
            return
    FileSetExcluded.add(path)

def visitFilesRecursively(path, functionToApply):
    extensionsToInclude = commentStringMapping[::3]
    for (path, dirs, files) in os.walk(path):
        skipDirectory = False
        for excludeDir in directoriesToExclude:
            if (path.endswith(excludeDir)):
                skipDirectory = True
                break
        if (skipDirectory):
            del dirs[:]
            continue
        for file in files:
            # ignore hidden files, which start with .
            if (file.startswith(".")):
                continue

            filename = "%s%s%s" % (path, os.sep, file)

            exclude = False
            for exclusion in pathsToExclude:
                if (filename == exclusion):
                    printExcluding(filename)
                    exclude = True
                    break
            if (exclude):
                continue

            exclude = True
            for extension in extensionsToInclude:
                if (filename.endswith(extension)):
                    functionToApply(filename)
                    exclude = False
                    break
            if (exclude):
                printExcluding(filename)

    for filename in pathsToInclude:
        if (os.path.exists(filename)):
            FileSetExcluded.remove(filename)
            functionToApply(filename)

# Returns a set of years in which modification to the given file were
# performed, according to the output of "cvs log path".
def determineModificationYears(path):
    if (OptionNoCVS):
        return set([ThisYear])

    dir = os.path.dirname(path)
    file = os.path.basename(path)
    cvsCommand = "cvs log %s" % file

    os.chdir(dir)
    results = os.popen(cvsCommand)
    os.chdir(WorkingDirectory)

    # If the file has not been checked in, cvs will complain, and this
    # routine will return an empty set.  When yearSetToYearRanges is
    # passed this empty set, it will add ThisYear, which should be
    # correct.

    years = set()
    for line in results:
        match = re.match(cvsLogDateRegexp, line)
        if (match):
            year = match.group(1)
            years.add(year)
    results.close()
    return years

# helper function factored out of yearSetToYearRanges()
def appendDate(s, start, previous, current):
    # We've seen a range of dates from start to previous, then a gap,
    # followed by current (which will become start on the next call).
    # If start == previous, there was only one date before the first
    # gap, so we don't generate the range.  If current == previous,
    # the list ends with a range, so we don't generate the gap.
    if (previous > start):
        s = s + "-"
        s = s + str(previous)
    if (current > previous):
        s = s + ", "
        s = s + str(current)
    return s

# Given a set of years, returns a string representing that set.  Years
# in the result are sorted, ranges are indicated by "YYYY-ZZZZ", gaps
# between ranges are indicated by "YYYY, ZZZZ".  Typical output might
# be "2001-2003, 2005, 2007".
def yearSetToYearRanges(yearSet):
    yearList = list(yearSet)
    yearList.sort()
    if (len(yearList) == 0):
        return ThisYear
    result = yearList[0]
    start = int(yearList[0])
    previous = start
    current = start
    for i in range(1, len(yearList)):
        current = int(yearList[i])
        if (current == previous + 1):
            previous = current
            # keep accumulating more of this range
            continue
        result = appendDate(result, start, previous, current)
        start = current
        previous = current
    result = appendDate(result, start, previous, current)
    return result

def daterangeToSet(dateRange):
    years = set()
    lastSeparator = ','
    lastYear = 2007
    while (True):
        match = re.search(dateRangeRegex, dateRange)
        if (match):
            nextYear = int(match.group(1))
            nextSeparator = match.group(2)
            remainder = match.group(3)
        else:
            nextYear = int(dateRange)


        if (nextYear < 100):
            if (nextYear > 50):
                nextYear = nextYear + 1900
            else:
                nextYear = nextYear + 2000

        if (lastSeparator == ','):
            years.add(str(nextYear))
        else:
            for year in range(lastYear, nextYear):
                years.add(str(year+1))

        if (match):
            lastYear = nextYear
            lastSeparator = nextSeparator
            dateRange = remainder
        else:
            return years

# Given a path name for a file, looks up the extension in
# commentStringMapping, and returns the beginning and end of line
# comment strings for that file type.
def getCommentStrings(path):
    for i in range(0, len(commentStringMapping), 3):
        if (path.endswith(commentStringMapping[i])):
            return (commentStringMapping[i+1], commentStringMapping[i+2])
    return ("", "")

def writeCopyrightLine(f, path, dateString):
    (commentStart, commentEnd) = getCommentStrings(path)
    f.write("%s Copyright %s Nanorex, Inc.  See LICENSE file for details. %s\n" % (commentStart, dateString, commentEnd))

def processFile(path):
    newFilename = path + ".new"

    years = determineModificationYears(path)
    finalDateRange = yearSetToYearRanges(years)

    file = open(path, 'r')

    line = file.readline()

    if (not line):
        # empty file
        return

    newFile = open(newFilename, 'w')

    if (not re.search(copyrightRegex, line)):
        firstLineOK = True
        for bad in badFirstLineStrings:
            if (line.startswith(bad)):
                firstLineOK = False
                break
        if (firstLineOK):
            newFile.write(line)
            line = file.readline()

    if (not re.search(copyrightRegex, line)):
        if (re.search(blankLineRegex, line)):
            newFile.write(line)
            line = file.readline()

    match = re.search(copyrightRegex, line)
    if (match):
        daterange = match.group(1)
        years = years | daterangeToSet(daterange)
        finalDateRange = yearSetToYearRanges(years)
        writeCopyrightLine(newFile, path, finalDateRange)
    else:
        writeCopyrightLine(newFile, path, finalDateRange)
        newFile.write(line)
    line = file.readline()
    while (line):
        match = re.search(epydocCopyrightRegex, line)
        if (match):
            line = match.group(1) + finalDateRange + match.group(match.lastindex) + "\n"
        newFile.write(line)
        line = file.readline()

    file.close()
    newFile.close()
    os.system("diff -c %s %s" % (path, newFilename))
    if (OptionDryRun):
        os.remove(newFilename)
    else:
        os.rename(newFilename, path)

def checkFile(path):
    newFilename = path + ".new"

    file = open(path, 'r')

    line = file.readline()

    if (not line):
        FileSetEmpty.add(path)
        return

    if (not re.search(copyrightRegex, line)):
        firstLineOK = True
        for bad in badFirstLineStrings:
            if (line.startswith(bad)):
                firstLineOK = False
                break
        if (firstLineOK):
            line = file.readline()

    if (not re.search(copyrightRegex, line)):
        if (re.search(blankLineRegex, line)):
            line = file.readline()

    match = re.search(copyrightRegex, line)
    if (match):
        FileSetHasInitialCopyright.add(path)
    else:
        FileSetNeedsInitialCopyright.add(path)

    line = file.readline()
    while (line):
        match = re.search(epydocCopyrightRegex, line)
        if (match):
            FileSetHasEpydocCopyright.add(path)
        else:
            match = re.search(anyCopyrightRegex, line)
            if (match):
                FileSetHasOtherCopyright.add(path)

        line = file.readline()

    file.close()

def printFileSet(headerString, fileSet):
    fileList = list(fileSet)
    if (len(fileList) == 0):
        return
    fileList.sort()
    print(headerString)
    for file in fileList:
        print(" " + file + " \\")
    print("")

if (__name__ == '__main__'):

    ThisYear = time.strftime("%Y")

    for i in range(1, len(sys.argv)):
        if (sys.argv[i] == "--check"):
            OptionCheck = True
        elif (sys.argv[i] == "--modify"):
            OptionModify = True
        elif (sys.argv[i] == "--dry-run"):
            OptionDryRun = True
        elif (sys.argv[i] == "--no-cvs"):
            OptionNoCVS = True
        else:
            print("UpdateCopyright.py: unrecognized option: " + sys.argv[i], file=sys.stderr)
            sys.exit(1)

    optionCount = 0
    if (OptionCheck):
        optionCount += 1
    if (OptionModify):
        optionCount += 1
    if (OptionDryRun):
        optionCount += 1
    if (optionCount != 1):
        print("UpdateCopyright.py:", file=sys.stderr)
        print(" you must specify exactly one of:", file=sys.stderr)
        print("  --check, --modify, --dry-run", file=sys.stderr)
        sys.exit(1)

    WorkingDirectory = os.getcwd()
    FileSetExcluded = set()
    if (OptionCheck):
        FileSetEmpty = set()
        FileSetHasInitialCopyright = set()
        FileSetNeedsInitialCopyright = set()
        FileSetHasEpydocCopyright = set()
        FileSetHasOtherCopyright = set()

        visitFilesRecursively(".", checkFile)

        printFileSet("Excluded files:", FileSetExcluded)
        printFileSet("Empty files:", FileSetEmpty)
        printFileSet("Has initial copyright:", FileSetHasInitialCopyright)
        printFileSet("Needs initial copyright:", FileSetNeedsInitialCopyright)
        printFileSet("Has Epydoc copyright:", FileSetHasEpydocCopyright)
        printFileSet("Has other copyright:", FileSetHasOtherCopyright)

    if (OptionModify or OptionDryRun):
        visitFilesRecursively(".", processFile)
