# Copyright 2004-2007 Nanorex, Inc.  See LICENSE file for details.
"""
$Id$
"""

from PyQt5 import QtGui, QtWidgets

def setupUi(win):
    """
    Populates the "File" menu which appears in the main window menu bar.

    @param win: NE1's main window object.
    @type  win: Ui_MainWindow
    """

    # Populate the "Import" submenu.
    win.importMenu.addAction(win.fileInsertMmpAction)
    win.importMenu.addAction(win.fileInsertPdbAction)
    win.importMenu.addAction(win.fileInsertInAction)
    win.importMenu.addSeparator()
    win.importMenu.addAction(win.fileImportOpenBabelAction)
    win.importMenu.addAction(win.fileImportIOSAction)

    #Populate the Fetch submenu
    win.fetchMenu.addAction(win.fileFetchPdbAction)

    # Populate the "Export" submenu.
    win.exportMenu.addAction(win.fileExportPdbAction)
    win.exportMenu.addAction(win.fileExportQuteMolXPdbAction)
    win.exportMenu.addSeparator()
    win.exportMenu.addAction(win.fileExportJpgAction)
    win.exportMenu.addAction(win.fileExportPngAction)
    win.exportMenu.addAction(win.fileExportPovAction)
    win.exportMenu.addAction(win.fileExportAmdlAction)
    win.exportMenu.addSeparator()
    win.exportMenu.addAction(win.fileExportOpenBabelAction)
    win.exportMenu.addAction(win.fileExportIOSAction)

    # Populate the "File" menu.
    win.fileMenu.addAction(win.fileOpenAction)
    win.fileMenu.addAction(win.fileCloseAction)
    win.fileMenu.addSeparator()
    win.fileMenu.addAction(win.fileSaveAction)
    win.fileMenu.addAction(win.fileSaveAsAction)
    win.fileMenu.addSeparator()
    win.fileMenu.addMenu(win.importMenu)
    win.fileMenu.addMenu(win.exportMenu)

    from utilities.GlobalPreferences import ENABLE_PROTEINS
    if ENABLE_PROTEINS:
        win.fileMenu.addMenu(win.fetchMenu)

    win.fileMenu.addSeparator()
    win.fileMenu.addAction(win.fileExitAction)

    # Create and add the "Open Recent Files" submenu.
    win.createOpenRecentFilesMenu()

def retranslateUi(win):
    """
    Sets text related attributes for the "File" menu.

    @param win: NE1's mainwindow object.
    @type  win: U{B{QMainWindow}<http://doc.trolltech.com/4/qmainwindow.html>}
    """
    win.fileMenu.setTitle(
        QtCore.QCoreApplication.translate(
            "MainWindow", "&File",
            None))
    win.importMenu.setTitle(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Import",
            None))
    win.exportMenu.setTitle(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Export",
            None))
    win.fetchMenu.setTitle(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Fetch",
            None))
    win.openRecentFilesMenu.setTitle(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Open Recent Files",
            None))
