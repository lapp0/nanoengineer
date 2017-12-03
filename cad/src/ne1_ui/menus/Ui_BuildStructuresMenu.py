# Copyright 2004-2007 Nanorex, Inc.  See LICENSE file for details.
"""
$Id$
"""

from PyQt5 import QtGui, QtWidgets
from utilities.debug_prefs import debug_pref, Choice_boolean_True

def setupUi(win):
    """
    Populates the "Build Structures" menu, a submenu of the "Tools" menu.

    @note: This also specifies the default (Build) command toolbar options
        in the flyout.

    @param win: NE1's main window object.
    @type  win: Ui_MainWindow
    """

    # Populate the "Build Structures" menu.
    # Start with "Builders", then add single shot "Generators".
    win.buildStructuresMenu.addAction(win.toolsDepositAtomAction)
    win.buildStructuresMenu.addAction(win.buildDnaAction)
    win.buildStructuresMenu.addAction(win.buildProteinAction)
    win.buildStructuresMenu.addAction(win.buildNanotubeAction)
    win.buildStructuresMenu.addAction(win.buildCrystalAction)
    win.buildStructuresMenu.addAction(win.insertGrapheneAction)

    # This adds the Atom Generator example for developers.
    # It is enabled (displayed) if the "Atom Generator" debug pref is set to True.
    # Otherwise, it is disabled (hidden) from the UI.
    win.buildStructuresMenu.addAction(win.insertAtomAction)
    return

def retranslateUi(win):
    """
    Sets text related attributes for the "Build Structures" submenu,
    which is a submenu of the "Tools" menu.

    @param win: NE1's mainwindow object.
    @type  win: U{B{QMainWindow}<http://doc.trolltech.com/4/qmainwindow.html>}
    """
    win.buildStructuresMenu.setTitle(QtCore.QCoreApplication.translate(
         "MainWindow", "Build Structures",
         None))
    return
