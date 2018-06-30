# Copyright 2004-2007 Nanorex, Inc.  See LICENSE file for details.
"""
$Id$
"""

from PyQt5 import QtGui, QtWidgets, QtCore

def setupUi(win):
    """
    Populates the "Dimensions" menu, a submenu of the "Tools" menu.

    @param win: NE1's main window object.
    @type  win: Ui_MainWindow
    """

    # Populate the "Dimensions" menu.
    win.dimensionsMenu.addAction(win.jigsDistanceAction)
    win.dimensionsMenu.addAction(win.jigsAngleAction)
    win.dimensionsMenu.addAction(win.jigsDihedralAction)

def retranslateUi(win):
    """
    Sets text related attributes for the "Dimensions" submenu,
    which is a submenu of the "Tools" menu.

    @param win: NE1's mainwindow object.
    @type  win: U{B{QMainWindow}<http://doc.trolltech.com/4/qmainwindow.html>}
    """
    win.dimensionsMenu.setTitle(
        QtCore.QCoreApplication.translate(
            "MainWindow", "&Dimensions",
            None))
