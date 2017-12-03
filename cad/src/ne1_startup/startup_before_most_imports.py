# Copyright 2004-2008 Nanorex, Inc.  See LICENSE file for details.
"""
startup_before_most_imports.py - some application startup functions
which need to be run before most imports are done, and which therefore
need to be careful about doing imports themselves.

@version: $Id$
@copyright: 2004-2008 Nanorex, Inc.  See LICENSE file for details.

History:

bruce 050902 made startup_funcs.py by moving some code out of main.py,
and adding some stub functions which will be filled in later.

bruce 071005 moved these functions from startup_funcs.py into
this new file startup/startup_before_most_imports.py.
"""

import sys, os

import utilities.EndUser as EndUser

# NOTE: this module (or EndUser) must not do toplevel imports of our other
# source modules, because it contains functions which need to be called
# by main_startup before most imports are done.



def before_creating_app():
    """
    Do other things that should be done before creating the application object.
    """
    # the default (1000) bombs with large molecules
    sys.setrecursionlimit(5000)



# end
