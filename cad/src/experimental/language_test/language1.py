# -*- coding: utf_8 -*-
# This file was created using a text editor that displayed unicode
# characters using their native format.  The characters in the
# shelfname string below are taking from a Korean newspaper.
# I have no idea what they mean.

shelfname = "C:\\Documents and Settings\\배드민턴\\Nanorex"
print("ShelfName = %r" % shelfname.encode("utf_8"))
print("ShelfName = " + shelfname.encode("utf_8"))
print(shelfname.encode("utf_8"))
print("ShelfName = %s".encode("utf_8") % shelfname.encode("utf_8"))
try:
    shelfname = "C:\\Documents and Settings\\배드민턴\\Nanorex"
    print("ShelfName = %s" % shelfname.encode("utf_8"))
except:
    pass
