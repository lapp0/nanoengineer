# Copyright 2004-2007 Nanorex, Inc.  See LICENSE file for details.
"""
Ui_MainWindowWidgets.py

Creates all widgets use by the Main Window, including:
- QAction used as menu items for menus in the main menu bar
- QActions, QToolButtons, etc. in main toolbars
- QAction for the Command toolbar

@author: Mark
@version: $Id$
@copyright: 2004-2007 Nanorex, Inc.  See LICENSE file for details.

History:

2007-12-23: Moved all QActions from menu and toolbar setupUi() functions here.
"""
import foundation.env as env
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QToolButton
from utilities.icon_utilities import geticon
from utilities.prefs_constants import displayRulers_prefs_key
from ne1_ui.NE1_QWidgetAction import NE1_QWidgetAction
# Dock widgets
from ne1_ui.Ui_ReportsDockWidget import Ui_ReportsDockWidget

def setupUi(win):
    """
    Creates all the QActions used in the main menubar and toolbars.

    @param win: NE1's mainwindow object.
    @type  win: U{B{QMainWindow}<http://doc.trolltech.com/4/qmainwindow.html>}
    """

    MainWindow = win

    # Create the NE1 main menu bar.
    win.MenuBar = QtWidgets.QMenuBar(MainWindow)
    win.MenuBar.setEnabled(True)
    win.MenuBar.setObjectName("MenuBar")

    #= File (menu and toolbar) widgets.

    # Create the "File" menu.
    win.fileMenu = QtWidgets.QMenu(win.MenuBar)
    win.fileMenu.setObjectName("fileMenu")

    # Create the "Import" menu, a submenu of the "File" menu.
    win.importMenu = QtWidgets.QMenu(win.fileMenu)
    win.importMenu.setObjectName("importMenu")

    # Create the "Export" menu, a submenu of the "File" menu.
    win.exportMenu = QtWidgets.QMenu(win.fileMenu)
    win.exportMenu.setObjectName("exportMenu")

    #Create the "Fetch" menu, a submenu of file menu
    win.fetchMenu = QtWidgets.QMenu(win.fileMenu)
    win.fetchMenu.setObjectName("fetchMenu")

    win.fileOpenAction = QtWidgets.QAction(MainWindow)
    win.fileOpenAction.setIcon(geticon("ui/actions/File/Open.png"))
    win.fileOpenAction.setObjectName("fileOpenAction")

    win.fileCloseAction = QtWidgets.QAction(MainWindow)
    win.fileCloseAction.setObjectName("fileCloseAction")

    win.fileSaveAction = QtWidgets.QAction(MainWindow)
    win.fileSaveAction.setIcon(geticon("ui/actions/File/Save.png"))
    win.fileSaveAction.setObjectName("fileSaveAction")

    win.fileSaveAsAction = QtWidgets.QAction(MainWindow)
    win.fileSaveAsAction.setObjectName("fileSaveAsAction")

    win.fileImportOpenBabelAction = QtWidgets.QAction(MainWindow)
    win.fileImportOpenBabelAction.setObjectName("fileImportOpenBabelAction")

    win.fileImportIOSAction = QtWidgets.QAction(MainWindow)
    win.fileImportIOSAction.setObjectName("fileImportIOSAction")

    win.fileFetchPdbAction = QtWidgets.QAction(MainWindow)
    win.fileFetchPdbAction.setObjectName("fileFetchPdbAction")

    win.fileExportPdbAction = QtWidgets.QAction(MainWindow)
    win.fileExportPdbAction.setObjectName("fileExportPdbAction")

    win.fileExportQuteMolXPdbAction = QtWidgets.QAction(MainWindow)
    win.fileExportQuteMolXPdbAction.setObjectName("fileExportQuteMolXPdbAction")

    win.fileExportJpgAction = QtWidgets.QAction(MainWindow)
    win.fileExportJpgAction.setObjectName("fileExportJpgAction")

    win.fileExportPngAction = QtWidgets.QAction(MainWindow)
    win.fileExportPngAction.setObjectName("fileExportPngAction")

    win.fileExportPovAction = QtWidgets.QAction(MainWindow)
    win.fileExportPovAction.setObjectName("fileExportPovAction")

    win.fileExportAmdlAction = QtWidgets.QAction(MainWindow)
    win.fileExportAmdlAction.setObjectName("fileExportAmdlAction")

    win.fileExportOpenBabelAction = QtWidgets.QAction(MainWindow)
    win.fileExportOpenBabelAction.setObjectName("fileExportOpenBabelAction")

    win.fileExportIOSAction = QtWidgets.QAction(MainWindow)
    win.fileExportIOSAction.setObjectName("fileExportIOSAction")


    # This action (i.e. the "Set Working Directory" menu item) was removed from
    # the File menu for Alpha 9 since it was deemed undesireable.
    # If you want a full explanation, ask me. Mark 2007-12-30.
    win.fileSetWorkingDirectoryAction = QtWidgets.QAction(MainWindow)
    win.fileSetWorkingDirectoryAction.setObjectName("fileSetWorkingDirectoryAction")

    win.fileExitAction = QtWidgets.QAction(MainWindow)
    win.fileExitAction.setObjectName("fileExitAction")

    # "Save Selection" is not implemented yet (NIY). Mark 2007-12-20.
    win.fileSaveSelectionAction = QtWidgets.QAction(MainWindow)
    win.fileSaveSelectionAction.setObjectName("fileSaveSelectionAction")

    #= Edit (menu and toolbar) widgets.

    # Create the "Edit" menu.
    win.editMenu = QtWidgets.QMenu(win.MenuBar)
    win.editMenu.setObjectName("editMenu")

    win.editUndoAction = QtWidgets.QAction(MainWindow)
    win.editUndoAction.setIcon(geticon("ui/actions/Edit/Undo.png"))
    win.editUndoAction.setVisible(True)
    win.editUndoAction.setObjectName("editUndoAction")

    win.editRedoAction = QtWidgets.QAction(MainWindow)
    win.editRedoAction.setChecked(False)
    win.editRedoAction.setIcon(geticon("ui/actions/Edit/Redo.png"))
    win.editRedoAction.setVisible(True)
    win.editRedoAction.setObjectName("editRedoAction")

    win.editMakeCheckpointAction = QtWidgets.QAction(MainWindow)
    win.editMakeCheckpointAction.setIcon(
        geticon("ui/actions/Edit/Make_Checkpoint.png"))
    win.editMakeCheckpointAction.setObjectName("editMakeCheckpointAction")

    win.editAutoCheckpointingAction = QtWidgets.QAction(MainWindow)
    win.editAutoCheckpointingAction.setCheckable(True)
    win.editAutoCheckpointingAction.setChecked(True)
    win.editAutoCheckpointingAction.setObjectName("editAutoCheckpointingAction")

    win.editClearUndoStackAction = QtWidgets.QAction(MainWindow)
    win.editClearUndoStackAction.setObjectName("editClearUndoStackAction")

    win.editCutAction = QtWidgets.QAction(MainWindow)
    win.editCutAction.setEnabled(True)
    win.editCutAction.setIcon(geticon("ui/actions/Edit/Cut.png"))
    win.editCutAction.setObjectName("editCutAction")

    win.editCopyAction = QtWidgets.QAction(MainWindow)
    win.editCopyAction.setEnabled(True)
    win.editCopyAction.setIcon(geticon("ui/actions/Edit/Copy.png"))
    win.editCopyAction.setObjectName("editCopyAction")

    win.editPasteAction = QtWidgets.QAction(MainWindow)
    win.editPasteAction.setIcon(geticon("ui/actions/Edit/Paste_Off.png"))
    win.editPasteAction.setObjectName("editPasteAction")

    win.pasteFromClipboardAction = QtWidgets.QAction(MainWindow)
    win.pasteFromClipboardAction.setIcon(geticon(
        "ui/actions/Properties Manager/clipboard-full.png"))

    win.pasteFromClipboardAction.setObjectName("pasteFromClipboardAction")
    win.pasteFromClipboardAction.setText("Paste from clipboard...")

    win.editDeleteAction = QtWidgets.QAction(MainWindow)
    win.editDeleteAction.setIcon(geticon("ui/actions/Edit/Delete.png"))
    win.editDeleteAction.setObjectName("editDeleteAction")

    # editRenameAction has been deprecated. Use editRenameSelectionAction.
    # Mark 2008-11-13.
    win.editRenameAction = QtWidgets.QAction(MainWindow)
    win.editRenameAction.setIcon(geticon("ui/actions/Edit/Rename.png"))
    win.editRenameAction.setObjectName("editRenameAction")

    win.editRenameSelectionAction = QtWidgets.QAction(MainWindow)
    win.editRenameSelectionAction.setIcon(
        geticon("ui/actions/Edit/Rename.png"))
    win.editRenameSelectionAction.setObjectName("editRenameSelectionAction")

    win.editAddSuffixAction = QtWidgets.QAction(MainWindow)
    win.editAddSuffixAction.setIcon(geticon("ui/actions/Edit/Add_Suffixes.png"))
    win.editAddSuffixAction.setObjectName("editAddSuffixAction")

    win.dispObjectColorAction = QtWidgets.QAction(MainWindow)
    win.dispObjectColorAction.setIcon(geticon("ui/actions/Edit/Edit_Color.png"))
    win.dispObjectColorAction.setObjectName("dispObjectColorAction")

    win.editDnaDisplayStyleAction = QtWidgets.QAction(MainWindow)
    win.editDnaDisplayStyleAction.setText("DNA Display Style")
    win.editDnaDisplayStyleAction.setIcon(
        geticon("ui/actions/Edit/EditDnaDisplayStyle.png"))

    win.editProteinDisplayStyleAction = QtWidgets.QAction(MainWindow)
    win.editProteinDisplayStyleAction.setText("Protein Display Style")
    win.editProteinDisplayStyleAction.setIcon(
        geticon("ui/actions/Edit/EditProteinDisplayStyle.png"))

    win.resetChunkColorAction = QtWidgets.QAction(MainWindow)
    win.resetChunkColorAction.setIcon(
        geticon("ui/actions/Edit/Reset_Chunk_Color.png"))
    win.resetChunkColorAction.setObjectName("resetChunkColorAction")

    #= View (menu and toolbar) actions.

    # Create the "View" menu.
    win.viewMenu = QtWidgets.QMenu(win.MenuBar)
    win.viewMenu.setObjectName("viewMenu")

    # Create the "Display" menu, a submenu of the "View" menu.
    win.displayMenu = QtWidgets.QMenu(win.viewMenu)
    win.displayMenu.setObjectName("displayMenu")

    # Create the "Modify" menu, a submenu of the "View" menu.
    win.modifyMenu = QtWidgets.QMenu(win.viewMenu)
    win.modifyMenu.setObjectName("viewMenu")

    # Note: The "Toolbars" submenu is created in Ui_ViewMenu.setupIu().

    #== View > Modify (menu and toolbar) actions.
    win.viewOrientationAction = QtWidgets.QAction(MainWindow)
    win.viewOrientationAction.setCheckable(True)
    win.viewOrientationAction.setIcon(
        geticon("ui/actions/View/Modify/Orientation.png"))
    win.viewOrientationAction.setObjectName("viewOrientationAction")

    win.setViewFitToWindowAction = QtWidgets.QAction(MainWindow)
    win.setViewFitToWindowAction.setIcon(
        geticon("ui/actions/View/Modify/Zoom_To_Fit.png"))
    win.setViewFitToWindowAction.setObjectName("setViewFitToWindowAction")

    win.setViewZoomtoSelectionAction = QtWidgets.QAction(MainWindow)
    win.setViewZoomtoSelectionAction.setIcon(
        geticon("ui/actions/View/Modify/Zoom_To_Selection.png"))
    win.setViewZoomtoSelectionAction.setObjectName("setViewZoomtoSelectionAction")

    win.zoomToAreaAction = QtWidgets.QAction(MainWindow)
    win.zoomToAreaAction.setCheckable(True)
    win.zoomToAreaAction.setIcon(
        geticon("ui/actions/View/Modify/ZoomToArea.png"))
    win.zoomToAreaAction.setObjectName("zoomToAreaAction")

    win.zoomInOutAction = QtWidgets.QAction(MainWindow)
    win.zoomInOutAction.setCheckable(True)
    win.zoomInOutAction.setIcon(
        geticon("ui/actions/View/Modify/Zoom_In_Out.png"))
    win.zoomInOutAction.setObjectName("zoomInOutAction")

    win.setViewRecenterAction = QtWidgets.QAction(MainWindow)
    win.setViewRecenterAction.setEnabled(True)
    win.setViewRecenterAction.setIcon(
        geticon("ui/actions/View/Modify/Recenter.png"))
    win.setViewRecenterAction.setObjectName("setViewRecenterAction")

    win.panToolAction = QtWidgets.QAction(MainWindow)
    win.panToolAction.setCheckable(True)
    win.panToolAction.setIcon(geticon("ui/actions/View/Modify/Pan.png"))
    win.panToolAction.setObjectName("panToolAction")

    win.rotateToolAction = QtWidgets.QAction(MainWindow)
    win.rotateToolAction.setCheckable(True)
    win.rotateToolAction.setIcon(geticon("ui/actions/View/Modify/Rotate.png"))
    win.rotateToolAction.setObjectName("rotateToolAction")

    win.setViewHomeAction = QtWidgets.QAction(MainWindow)
    win.setViewHomeAction.setIcon(geticon("ui/actions/View/Modify/Home.png"))
    win.setViewHomeAction.setObjectName("setViewHomeAction")

    win.setViewHomeToCurrentAction = QtWidgets.QAction(MainWindow)
    win.setViewHomeToCurrentAction.setObjectName("setViewHomeToCurrentAction")

    #= View toolbar QActions.
    win.viewNormalToAction = QtWidgets.QAction(MainWindow)
    win.viewNormalToAction.setIcon(
        geticon("ui/actions/View/Set_View_Normal_To.png"))
    win.viewNormalToAction.setObjectName("NormalTo")

    win.viewParallelToAction = QtWidgets.QAction(MainWindow)
    win.viewParallelToAction.setIcon(
        geticon("ui/actions/View/Set_View_Parallel_To.png"))
    win.viewParallelToAction.setObjectName("ParallelTo")

    win.saveNamedViewAction = QtWidgets.QAction(MainWindow)
    win.saveNamedViewAction.setIcon(
        geticon("ui/actions/View/Modify/Save_Named_View.png"))
    win.saveNamedViewAction.setObjectName("saveNamedViewAction")

    win.viewFrontAction = QtWidgets.QAction(MainWindow)
    win.viewFrontAction.setEnabled(True)
    win.viewFrontAction.setIcon(geticon("ui/actions/View/Front.png"))
    win.viewFrontAction.setObjectName("Front")

    win.viewBackAction = QtWidgets.QAction(MainWindow)
    win.viewBackAction.setIcon(geticon("ui/actions/View/Back.png"))
    win.viewBackAction.setObjectName("Back")

    win.viewRightAction = QtWidgets.QAction(MainWindow)
    win.viewRightAction.setIcon(geticon("ui/actions/View/Right.png"))
    win.viewRightAction.setObjectName("Right")

    win.viewLeftAction = QtWidgets.QAction(MainWindow)
    win.viewLeftAction.setIcon(geticon("ui/actions/View/Left.png"))
    win.viewLeftAction.setObjectName("Left")

    win.viewTopAction = QtWidgets.QAction(MainWindow)
    win.viewTopAction.setIcon(geticon("ui/actions/View/Top.png"))
    win.viewTopAction.setObjectName("Top")

    win.viewBottomAction = QtWidgets.QAction(MainWindow)
    win.viewBottomAction.setEnabled(True)
    win.viewBottomAction.setIcon(geticon("ui/actions/View/Bottom.png"))
    win.viewBottomAction.setObjectName("Bottom")

    win.viewIsometricAction = QtWidgets.QAction(MainWindow)
    win.viewIsometricAction.setIcon(geticon("ui/actions/View/Isometric.png"))
    win.viewIsometricAction.setObjectName("Isometric")

    win.viewFlipViewVertAction = QtWidgets.QAction(MainWindow)
    win.viewFlipViewVertAction.setIcon(
        geticon("ui/actions/View/FlipViewVert.png"))
    win.viewFlipViewVertAction.setObjectName("FlipViewVert")

    win.viewFlipViewHorzAction = QtWidgets.QAction(MainWindow)
    win.viewFlipViewHorzAction.setIcon(
        geticon("ui/actions/View/FlipViewHorz.png"))
    win.viewFlipViewHorzAction.setObjectName("FlipViewHorz")

    win.viewRotatePlus90Action = QtWidgets.QAction(MainWindow)
    win.viewRotatePlus90Action.setIcon(
        geticon("ui/actions/View/Rotate_View_+90.png"))
    win.viewRotatePlus90Action.setObjectName("RotatePlus90")

    win.viewRotateMinus90Action = QtWidgets.QAction(MainWindow)
    win.viewRotateMinus90Action.setIcon(
        geticon("ui/actions/View/Rotate_View_-90.png"))
    win.viewRotateMinus90Action.setObjectName("RotateMinus90")

    win.viewDefviewAction = QtWidgets.QAction(MainWindow)
    win.viewDefviewAction.setObjectName("viewDefviewAction")

    #== View > Display (menu and toolbar) actions.
    win.dispDefaultAction = QtWidgets.QAction(MainWindow)
    win.dispDefaultAction.setIcon(
        geticon("ui/actions/View/Display/Default.png"))
    win.dispDefaultAction.setObjectName("dispDefaultAction")

    win.dispInvisAction = QtWidgets.QAction(MainWindow)
    win.dispInvisAction.setIcon(
        geticon("ui/actions/View/Display/Invisible.png"))
    win.dispInvisAction.setObjectName("dispInvisAction")

    win.dispLinesAction = QtWidgets.QAction(MainWindow)
    win.dispLinesAction.setIcon(
        geticon("ui/actions/View/Display/Lines.png"))
    win.dispLinesAction.setObjectName("dispLinesAction")

    win.dispTubesAction = QtWidgets.QAction(MainWindow)
    win.dispTubesAction.setEnabled(True)
    win.dispTubesAction.setIcon(
        geticon("ui/actions/View/Display/Tubes.png"))
    win.dispTubesAction.setObjectName("dispTubesAction")

    win.dispCPKAction = QtWidgets.QAction(MainWindow)
    win.dispCPKAction.setIcon(geticon("ui/actions/View/Display/CPK.png"))
    win.dispCPKAction.setObjectName("dispCPKAction")

    win.dispBallAction = QtWidgets.QAction(MainWindow)
    win.dispBallAction.setIcon(
        geticon("ui/actions/View/Display/Ball_and_Stick.png"))
    win.dispBallAction.setObjectName("dispBallAction")

    #@ This QAction is unused. See comments at the top of Ui_ViewMenu.py.
    win.dispHybridAction = QtWidgets.QAction(MainWindow)
    win.dispHybridAction.setIcon(
        geticon("ui/actions/View/Display/Hybrid.png"))
    win.dispHybridAction.setCheckable(True)
    win.dispHybridAction.setObjectName("dispHybridAction")

    win.dispCylinderAction = QtWidgets.QAction(MainWindow)
    win.dispCylinderAction.setIcon(
        geticon("ui/actions/View/Display/Cylinder.png"))
    win.dispCylinderAction.setObjectName("dispCylinderAction")

    win.dispDnaCylinderAction = QtWidgets.QAction(MainWindow)
    win.dispDnaCylinderAction.setIcon(
        geticon("ui/actions/View/Display/DnaCylinder.png"))
    win.dispDnaCylinderAction.setObjectName("dispDnaCylinderAction")

    win.dispHideAction = QtWidgets.QAction(MainWindow)
    win.dispHideAction.setIcon(
        geticon("ui/actions/View/Display/Hide.png"))
    win.dispHideAction.setObjectName("dispHideAction")

    win.dispUnhideAction = QtWidgets.QAction(MainWindow)
    win.dispUnhideAction.setIcon(
        geticon("ui/actions/View/Display/Unhide.png"))
    win.dispUnhideAction.setObjectName("dispUnhideAction")

    # This is currently NIY. Mark 2007-12-28
    win.dispSurfaceAction = QtWidgets.QAction(MainWindow)
    win.dispSurfaceAction.setIcon(
        geticon("ui/actions/View/Display/Surface.png"))
    win.dispSurfaceAction.setObjectName("dispSurfaceAction")

    win.setViewPerspecAction = QtWidgets.QAction(MainWindow)
    win.setViewPerspecAction.setCheckable(True)

    win.setViewOrthoAction = QtWidgets.QAction(MainWindow)
    win.setViewOrthoAction.setCheckable(True)

    win.orthoPerpActionGroup = QtWidgets.QActionGroup(MainWindow)
    win.orthoPerpActionGroup.setExclusive(True)
    win.orthoPerpActionGroup.addAction(win.setViewPerspecAction)
    win.orthoPerpActionGroup.addAction(win.setViewOrthoAction)

    # piotr 080516 added stereo view action
    win.setStereoViewAction = QtWidgets.QAction(MainWindow)
    win.setStereoViewAction.setIcon(
        geticon("ui/actions/View/Stereo_View.png"))
    win.setStereoViewAction.setObjectName("setStereoViewAction")

    win.viewQuteMolAction = QtWidgets.QAction(MainWindow)
    win.viewQuteMolAction.setIcon(
        geticon("ui/actions/View/Display/QuteMol.png"))
    win.viewQuteMolAction.setObjectName("viewQuteMolAction")

    win.viewRaytraceSceneAction = QtWidgets.QAction(MainWindow)
    win.viewRaytraceSceneAction.setIcon(
        geticon("ui/actions/View/Display/Raytrace_Scene.png"))
    win.viewRaytraceSceneAction.setObjectName("viewRaytraceSceneAction")

    win.dispSetEltable1Action = QtWidgets.QAction(MainWindow)
    win.dispSetEltable1Action.setObjectName("dispSetEltable1Action")

    win.dispSetEltable2Action = QtWidgets.QAction(MainWindow)
    win.dispSetEltable2Action.setObjectName("dispSetEltable2Action")

    win.dispResetAtomsDisplayAction = QtWidgets.QAction(MainWindow)
    win.dispResetAtomsDisplayAction.setObjectName("dispResetAtomsDisplayAction")

    win.dispShowInvisAtomsAction = QtWidgets.QAction(MainWindow)
    win.dispShowInvisAtomsAction.setObjectName("dispShowInvisAtomsAction")

    win.dispElementColorSettingsAction = QtWidgets.QAction(MainWindow)
    win.dispElementColorSettingsAction.setObjectName("dispElementColorSettingsAction")
    win.dispElementColorSettingsAction.setIcon(
        geticon("ui/actions/View/Display/Element_Color_Settings.png"))

    win.dispLightingAction = QtWidgets.QAction(MainWindow)
    win.dispLightingAction.setObjectName("dispLightingAction")

    win.viewSemiFullScreenAction = QtWidgets.QAction(MainWindow)
    win.viewSemiFullScreenAction.setText('Semi-Full Screen')
    win.viewSemiFullScreenAction.setCheckable(True)
    win.viewSemiFullScreenAction.setChecked(False)
    win.viewSemiFullScreenAction.setShortcut('F11')

    win.viewFullScreenAction = QtWidgets.QAction(MainWindow)
    win.viewFullScreenAction.setText('Full Screen')
    win.viewFullScreenAction.setCheckable(True)
    win.viewFullScreenAction.setChecked(False)
    win.viewFullScreenAction.setShortcut('F12')

    win.viewReportsAction = QtWidgets.QAction(MainWindow)
    win.viewReportsAction.setCheckable(True)
    win.viewReportsAction.setChecked(True)
    win.viewReportsAction.setText('Reports')

    win.viewRulersAction = QtWidgets.QAction(MainWindow)
    win.viewRulersAction.setCheckable(True)
    win.viewRulersAction.setChecked(env.prefs[displayRulers_prefs_key])
    win.viewRulersAction.setText('Rulers')


    #= Insert (menu and toolbar) widgets.

    # Create the "Insert" menu.
    win.insertMenu = QtWidgets.QMenu(win.MenuBar)
    win.insertMenu.setObjectName("Insert")

    # Create the "Reference Geometry" menu, a submenu of the "Insert" menu.
    #win.referenceGeometryMenu = QtGui.QMenu(win.insertMenu)
    #win.referenceGeometryMenu.setObjectName("referenceGeometryMenu")

    win.jigsAtomSetAction = NE1_QWidgetAction(MainWindow,
                                                win = MainWindow)
    win.jigsAtomSetAction.setIcon(geticon("ui/actions/Tools/Atom_Set.png"))
    win.jigsAtomSetAction.setObjectName("jigsAtomSetAction")

    win.fileInsertMmpAction = NE1_QWidgetAction(MainWindow,
                                                  win = MainWindow)
    win.fileInsertMmpAction.setObjectName("fileInsertMmpAction")
    win.fileInsertMmpAction.setIcon(
        geticon('ui/actions/Insert/MMP.png'))

    win.fileInsertPdbAction = NE1_QWidgetAction(MainWindow,
                                                  win = MainWindow)
    win.fileInsertPdbAction.setObjectName("fileInsertPdbAction")
    win.fileInsertPdbAction.setIcon(geticon('ui/actions/Insert/PDB.png'))

    win.fileInsertInAction = NE1_QWidgetAction(MainWindow,
                                                  win = MainWindow)
    win.fileInsertInAction.setObjectName("fileInsertInAction")

    win.partLibAction = NE1_QWidgetAction(MainWindow,
                                            win = MainWindow)
    win.partLibAction.setObjectName("partLibAction")
    win.partLibAction.setIcon(geticon('ui/actions/Insert/Part_Library.png'))

    win.insertCommentAction = NE1_QWidgetAction(MainWindow,
                                                  win = MainWindow)
    win.insertCommentAction.setIcon(
        geticon("ui/actions/Insert/Comment.png"))
    win.insertCommentAction.setObjectName("insertCommentAction")

    win.insertPovraySceneAction = NE1_QWidgetAction(MainWindow,
                                                      win = MainWindow)
    win.insertPovraySceneAction.setIcon(
        geticon("ui/actions/Insert/POV-Ray_Scene.png"))
    win.insertPovraySceneAction.setObjectName("insertPovraySceneAction")

    win.jigsGridPlaneAction = NE1_QWidgetAction(MainWindow,
                                                  win = MainWindow)
    win.jigsGridPlaneAction.setIcon(
        geticon("ui/actions/Insert/Reference Geometry/Grid_Plane.png"))
    win.jigsGridPlaneAction.setObjectName("jigsGridPlaneAction")

    win.referencePlaneAction = NE1_QWidgetAction(MainWindow,
                                                   win = MainWindow)
    win.referencePlaneAction.setIcon(
        geticon("ui/actions/Insert/Reference Geometry/Plane.png"))
    win.referencePlaneAction.setObjectName("referencePlaneAction")

    win.referenceLineAction = NE1_QWidgetAction(MainWindow,
                                                  win = MainWindow)
    win.referenceLineAction.setIcon(
        geticon("ui/actions/Insert/Reference Geometry/Plane.png"))
    win.referenceLineAction.setObjectName("referenceLineAction")
    win.referenceLineAction.setText("Line...")

    #= Tools (menu and toolbar) widgets.

    # Create the "Tools" menu.
    win.toolsMenu = QtWidgets.QMenu(win.MenuBar)
    win.toolsMenu.setObjectName("Tools")

    # Create the "Build Structures" menu, a submenu of the "Tools" menu.
    win.buildStructuresMenu = QtWidgets.QMenu(win.toolsMenu)
    win.buildStructuresMenu.setObjectName("buildStructuresMenu")

    # Create the "Build Tools" menu, a submenu of the "Tools" menu.
    win.buildToolsMenu = QtWidgets.QMenu(win.toolsMenu)
    win.buildToolsMenu.setObjectName("buildToolsMenu")

    # Create the "Dimensions" menu, a submenu of the "Tools" menu.
    win.dimensionsMenu = QtWidgets.QMenu(win.toolsMenu)
    win.dimensionsMenu.setObjectName("dimensionsMenu")

    # Create the "Selection" menu, a submenu of the "Tools" menu.
    win.selectionMenu = QtWidgets.QMenu(win.toolsMenu)
    win.selectionMenu.setObjectName("selectionMenu")

    win.editPrefsAction = NE1_QWidgetAction(MainWindow,
                                              win = MainWindow)
    win.editPrefsAction.setIcon(geticon("ui/actions/Tools/Options.png"))
    win.editPrefsAction.setObjectName("editPrefsAction")

     #Urmi background color scheme option 080522
    win.colorSchemeAction =  QtWidgets.QAction(MainWindow)
    win.colorSchemeAction.setIcon(geticon("ui/actions/View/ColorScheme.png"))
    win.colorSchemeAction.setObjectName("colorSchemeAction")

    win.lightingSchemeAction = QtWidgets.QAction(MainWindow)
    win.lightingSchemeAction.setIcon(geticon("ui/actions/View/LightingScheme.png"))
    win.lightingSchemeAction.setObjectName("lightingSchemeAction")

    win.modifyAdjustSelAction = NE1_QWidgetAction(MainWindow,
                                                    win = MainWindow)
    win.modifyAdjustSelAction.setEnabled(True)
    win.modifyAdjustSelAction.setIcon(
        geticon("ui/actions/Tools/Adjust_Selection.png"))
    win.modifyAdjustSelAction.setObjectName("modifyAdjustSelAction")

    win.modifyAdjustAllAction = NE1_QWidgetAction(MainWindow,
                                                    win = MainWindow)
    win.modifyAdjustAllAction.setIcon(
        geticon("ui/actions/Tools/Adjust_All.png"))
    win.modifyAdjustAllAction.setObjectName("modifyAdjustAllAction")

    win.simMinimizeEnergyAction = NE1_QWidgetAction(MainWindow,
                                                      win = MainWindow)
    win.simMinimizeEnergyAction.setIcon(
        geticon("ui/actions/Simulation/Minimize_Energy.png"))
    win.simMinimizeEnergyAction.setObjectName("simMinimizeEnergyAction")

    win.checkAtomTypesAction = NE1_QWidgetAction(MainWindow,
                                                      win = MainWindow)
    win.checkAtomTypesAction.setObjectName("checkAtomTypesAction")

    win.toolsExtrudeAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.toolsExtrudeAction.setCheckable(True)
    win.toolsExtrudeAction.setIcon(
        geticon("ui/actions/Insert/Features/Extrude.png"))

    win.toolsFuseChunksAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.toolsFuseChunksAction.setCheckable(1) # make the Fuse Mode button checkable
    win.toolsFuseChunksAction.setIcon(
        geticon("ui/actions/Tools/Build Tools/Fuse_Chunks.png"))

    win.modifyMirrorAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.modifyMirrorAction.setIcon(
        geticon("ui/actions/Tools/Build Tools/Mirror.png"))
    win.modifyMirrorAction.setObjectName("modifyMirrorAction")

    win.modifyInvertAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.modifyInvertAction.setIcon(
        geticon("ui/actions/Tools/Build Tools/Invert.png"))
    win.modifyInvertAction.setObjectName("modifyInvertAction")

    win.modifyStretchAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.modifyStretchAction.setIcon(
        geticon("ui/actions/Tools/Build Tools/Stretch.png"))
    win.modifyStretchAction.setObjectName("modifyStretchAction")

    #== "Tools > Build Structures" (menu and toolbar) widgets.

    win.toolsDepositAtomAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.toolsDepositAtomAction.setCheckable(1) # make the build button checkable
    win.toolsDepositAtomAction.setIcon(
        geticon("ui/actions/Tools/Build Structures/BuildAtoms.png"))

    win.buildCrystalAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.buildCrystalAction.setCheckable(1) # make the crystal button checkable
    win.buildCrystalAction.setIcon(
        geticon("ui/actions/Tools/Build Structures/Build Crystal.png"))

    win.insertGrapheneAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.insertGrapheneAction.setIcon(
        geticon("ui/actions/Tools/Build Structures/Graphene.png"))
    win.insertGrapheneAction.setObjectName("insertGrapheneAction")

    win.nanotubeGeneratorAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.nanotubeGeneratorAction.setIcon(
        geticon("ui/actions/Tools/Build Structures/Nanotube.png"))
    win.nanotubeGeneratorAction.setObjectName("nanotubeGeneratorAction")

    win.buildNanotubeAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.buildNanotubeAction.setIcon(
        geticon("ui/actions/Tools/Build Structures/Nanotube.png"))
    win.buildNanotubeAction.setObjectName("buildNanotubeAction")

    win.buildDnaAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.buildDnaAction.setIcon(
        geticon("ui/actions/Tools/Build Structures/DNA.png"))
    win.buildDnaAction.setObjectName("buildDnaAction")

    # Atom Generator (Developer Example). Mark 2007-06-08
    win.insertAtomAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.insertAtomAction.setIcon(
        geticon("ui/actions/Command Toolbar/BuildAtoms/InsertAtom.png"))
    win.insertAtomAction.setObjectName("insertAtomAction")

    # Peptide Generator, piotr 080304
    win.buildProteinAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.buildProteinAction.setIcon(
        geticon("ui/actions/Tools/Build Structures/Peptide.png"))
    win.buildProteinAction.setObjectName("buildProteinAction")

    #== "Tools > Build Tools" (menu and toolbar) widgets.

    win.modifyHydrogenateAction = NE1_QWidgetAction(MainWindow,
                                                    win = MainWindow)
    win.modifyHydrogenateAction.setIcon(
        geticon("ui/actions/Tools/Build Tools/Hydrogenate.png"))
    win.modifyHydrogenateAction.setObjectName("modifyHydrogenateAction")

    win.modifyDehydrogenateAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.modifyDehydrogenateAction.setIcon(
        geticon("ui/actions/Tools/Build Tools/Dehydrogenate.png"))
    win.modifyDehydrogenateAction.setObjectName("modifyDehydrogenateAction")

    win.modifyPassivateAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.modifyPassivateAction.setIcon(
        geticon("ui/actions/Tools/Build Tools/Passivate.png"))
    win.modifyPassivateAction.setObjectName("modifyPassivateAction")

    win.modifyDeleteBondsAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.modifyDeleteBondsAction.setIcon(
        geticon("ui/actions/Tools/Build Tools/Delete_Bonds.png"))
    win.modifyDeleteBondsAction.setObjectName("modifyDeleteBondsAction")

    win.modifySeparateAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.modifySeparateAction.setIcon(
        geticon("ui/actions/Tools/Build Tools/Separate.png"))
    win.modifySeparateAction.setObjectName("modifySeparateAction")

    win.modifyMergeAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.modifyMergeAction.setIcon(geticon(
        "ui/actions/Tools/Build Tools/Combine_Chunks.png"))
    win.modifyMergeAction.setObjectName("modifyMergeAction")

    win.makeChunkFromSelectedAtomsAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.makeChunkFromSelectedAtomsAction.setIcon(geticon(
        "ui/actions/Tools/Build Tools/New_Chunk.png"))
    win.makeChunkFromSelectedAtomsAction.setObjectName(
        "makeChunkFromSelectedAtomsAction")

    win.modifyAlignCommonAxisAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.modifyAlignCommonAxisAction.setIcon(
        geticon("ui/actions/Tools/Build Tools/AlignToCommonAxis.png"))
    win.modifyAlignCommonAxisAction.setObjectName("modifyAlignCommonAxisAction")

    win.modifyCenterCommonAxisAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.modifyCenterCommonAxisAction.setObjectName(
        "modifyCenterCommonAxisAction")

    #= "Tools > Dimensions" (menu and toolbar) widgets.

    win.jigsDistanceAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.jigsDistanceAction.setIcon(
        geticon("ui/actions/Tools/Dimensions/Measure_Distance.png"))
    win.jigsDistanceAction.setObjectName("jigsDistanceAction")

    win.jigsAngleAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.jigsAngleAction.setIcon(
        geticon("ui/actions/Tools/Dimensions/Measure_Angle.png"))
    win.jigsAngleAction.setObjectName("jigsAngleAction")

    win.jigsDihedralAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.jigsDihedralAction.setIcon(
        geticon("ui/actions/Tools/Dimensions/Measure_Dihedral.png"))
    win.jigsDihedralAction.setObjectName("jigsDihedralAction")

    #= "Tools > Select" (menu and toolbar) widgets.

    win.selectAllAction = QtWidgets.QAction(MainWindow)
    win.selectAllAction.setEnabled(True)
    win.selectAllAction.setIcon(
        geticon("ui/actions/Tools/Select/Select_All.png"))
    win.selectAllAction.setObjectName("selectAllAction")

    win.selectNoneAction = QtWidgets.QAction(MainWindow)
    win.selectNoneAction.setIcon(
        geticon("ui/actions/Tools/Select/Select_None.png"))
    win.selectNoneAction.setObjectName("selectNoneAction")

    win.selectInvertAction = QtWidgets.QAction(MainWindow)
    win.selectInvertAction.setIcon(
        geticon("ui/actions/Tools/Select/Select_Invert.png"))
    win.selectInvertAction.setObjectName("selectInvertAction")

    win.selectConnectedAction = QtWidgets.QAction(MainWindow)
    win.selectConnectedAction.setIcon(
        geticon("ui/actions/Tools/Select/Select_Connected.png"))
    win.selectConnectedAction.setObjectName("selectConnectedAction")

    win.selectDoublyAction = QtWidgets.QAction(MainWindow)
    win.selectDoublyAction.setIcon(
        geticon("ui/actions/Tools/Select/Select_Doubly.png"))
    win.selectDoublyAction.setObjectName("selectDoublyAction")

    win.selectExpandAction = QtWidgets.QAction(MainWindow)
    win.selectExpandAction.setIcon(
        geticon("ui/actions/Tools/Select/Expand.png"))
    win.selectExpandAction.setObjectName("selectExpandAction")

    win.selectContractAction = QtWidgets.QAction(MainWindow)
    win.selectContractAction.setIcon(
        geticon("ui/actions/Tools/Select/Contract.png"))
    win.selectContractAction.setObjectName("selectContractAction")

    win.selectLockAction = QtWidgets.QAction(MainWindow)
    win.selectLockAction.setIcon(
        geticon("ui/actions/Tools/Select/Selection_Unlocked.png"))
    win.selectLockAction.setObjectName("selectLockAction")
    win.selectLockAction.setCheckable(True)

    win.selectByNameAction = QtWidgets.QAction(MainWindow)
    win.selectByNameAction.setIcon(
        geticon("ui/actions/Tools/Select/Select_By_Name.png"))
    win.selectByNameAction.setObjectName("selectByNameAction")
    win.selectByNameAction.setCheckable(True)

    #= "Simulation" (menu and toolbar) widgets.

    # Create the "Simulation" menu
    win.simulationMenu = QtWidgets.QMenu(win.MenuBar)
    win.simulationMenu.setObjectName("simulationMenu")

    # Create the "Measurements" menu. #@ Not used??? MAS
    win.measurementsMenu = QtWidgets.QMenu()
    win.measurementsMenu.setObjectName("measurementsMenu")
    win.measurementsMenu.setIcon(
        geticon("ui/actions/Tools/Dimensions/Dimension.png"))

    win.simSetupAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.simSetupAction.setCheckable(True)
    win.simSetupAction.setChecked(False)
    win.simSetupAction.setEnabled(True)
    win.simSetupAction.setIcon(
        geticon("ui/actions/Simulation/RunDynamics.png"))
    win.simSetupAction.setObjectName("simSetupAction")

    win.simMoviePlayerAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.simMoviePlayerAction.setIcon(
        geticon("ui/actions/Simulation/PlayMovie.png"))

    win.rosettaSetupAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.rosettaSetupAction.setCheckable(True)
    win.rosettaSetupAction.setChecked(False)
    win.rosettaSetupAction.setEnabled(True)
    win.rosettaSetupAction.setIcon(
        geticon("ui/actions/Simulation/Rosetta.png"))
    win.rosettaSetupAction.setObjectName("rosettaSetupAction")

    win.simPlotToolAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.simPlotToolAction.setIcon(
        geticon("ui/actions/Simulation/PlotGraphs.png"))
    win.simPlotToolAction.setObjectName("simPlotToolAction")

    win.jigsMotorAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.jigsMotorAction.setIcon(
        geticon("ui/actions/Simulation/RotaryMotor.png"))
    win.jigsMotorAction.setObjectName("jigsMotorAction")

    win.jigsLinearMotorAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.jigsLinearMotorAction.setIcon(
        geticon("ui/actions/Simulation/LinearMotor.png"))
    win.jigsLinearMotorAction.setObjectName("jigsLinearMotorAction")

    win.jigsStatAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.jigsStatAction.setIcon(
        geticon("ui/actions/Simulation/Thermostat.png"))
    win.jigsStatAction.setObjectName("jigsStatAction")

    win.jigsThermoAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.jigsThermoAction.setIcon(
        geticon("ui/actions/Simulation/Measurements/Thermometer.png"))
    win.jigsThermoAction.setObjectName("jigsThermoAction")

    win.jigsAnchorAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.jigsAnchorAction.setIcon(
        geticon("ui/actions/Simulation/Anchor.png"))
    win.jigsAnchorAction.setObjectName("jigsAnchorAction")

    win.simulationJigsAction = QtWidgets.QAction(win)
    win.simulationJigsAction.setIcon(
        geticon("ui/actions/Simulation/SimulationJigs.png"))
    win.simulationJigsAction.setObjectName("simulationJigsAction")

    win.jigsGamessAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.jigsGamessAction.setEnabled(True)
    win.jigsGamessAction.setIcon(
        geticon("ui/actions/Simulation/GAMESS.png"))
    win.jigsGamessAction.setObjectName("jigsGamessAction")

    win.jigsESPImageAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.jigsESPImageAction.setIcon(
        geticon("ui/actions/Simulation/ESP_Image.png"))
    win.jigsESPImageAction.setObjectName("jigsESPImageAction")

    # This only shows up if the user enables the NH1 plugin (via Preferences)
    # which is hidden since NH1 doesn't work with NE1.
    # See UserPrefs.enable_nanohive().
    win.simNanoHiveAction = QtWidgets.QAction(MainWindow)
    win.simNanoHiveAction.setVisible(False)
    win.simNanoHiveAction.setObjectName("simNanoHiveAction")

    #= Rendering menu.

    # Create the "Tools" menu.
    win.renderingMenu = QtWidgets.QMenu(win.MenuBar)
    win.renderingMenu.setObjectName("Rendering")

    #= "Help" (menu and toolbar) widgets.

    win.helpMenu = QtWidgets.QMenu(win.MenuBar)
    win.helpMenu.setObjectName("helpMenu")

    win.helpTutorialsAction = QtWidgets.QAction(MainWindow)
    win.helpTutorialsAction.setObjectName("helpAboutAction")

    win.helpMouseControlsAction = QtWidgets.QAction(MainWindow)
    win.helpMouseControlsAction.setObjectName("helpMouseControlsAction")

    win.helpKeyboardShortcutsAction = QtWidgets.QAction(MainWindow)
    win.helpKeyboardShortcutsAction.setObjectName("helpKeyboardShortcutsAction")

    win.helpSelectionShortcutsAction = QtWidgets.QAction(MainWindow)
    win.helpSelectionShortcutsAction.setObjectName("helpSelectionShortcutsAction")

    win.helpGraphicsCardAction = QtWidgets.QAction(MainWindow)
    win.helpGraphicsCardAction.setObjectName("helpGraphicsCardAction")

    win.helpWhatsThisAction = QtWidgets.QAction(MainWindow)
    win.helpWhatsThisAction.setIcon(geticon("ui/actions/Help/WhatsThis.png"))
    win.helpWhatsThisAction.setObjectName("helpWhatsThisAction")

    win.helpAboutAction = QtWidgets.QAction(MainWindow)
    win.helpAboutAction.setObjectName("helpAboutAction")

    #= Widgets for toolbars

    # "Standard" toolbar widgets.

    # Action items from the Tools menu  @@@ninad061110
    # Not decided whether select chunks and move chunks options
    # will be a part of Tools Menu

    win.toolsSelectMoleculesAction = QtWidgets.QAction(MainWindow)
    win.toolsSelectMoleculesAction.setCheckable(1) # make the select chunks button checkable
    win.toolsSelectMoleculesAction.setIcon(
        geticon("ui/actions/Misc/SelectChunks.png"))

    # Define an action grop for move molecules (translate and rotate components)
    # actions ...to make them mutually exclusive.
    # -- ninad 070309
    win.toolsMoveRotateActionGroup = QtWidgets.QActionGroup(MainWindow)
    win.toolsMoveRotateActionGroup.setExclusive(True)

    win.toolsMoveMoleculeAction = NE1_QWidgetAction(win.toolsMoveRotateActionGroup,
                                                      win = MainWindow)
    win.toolsMoveMoleculeAction.setCheckable(1) # make the Move mode button checkable
    win.toolsMoveMoleculeAction.setIcon(
        geticon("ui/actions/Command Toolbar/MoveCommands/Translate.png"))

    win.rotateComponentsAction = NE1_QWidgetAction(win.toolsMoveRotateActionGroup,
                                                     win = MainWindow)
    win.rotateComponentsAction.setCheckable(1) # make the Move mode button checkable
    win.rotateComponentsAction.setIcon(
        geticon("ui/actions/Command Toolbar/MoveCommands/Rotate.png"))

    #= "View" toolbars.

    # Create "Standard Views" dropdown menu for the "View" toolbar.
    win.standardViewsMenu = QtWidgets.QMenu("Standard Views")

    # Populate the "Standard Views" menu.
    win.standardViewsMenu.addAction(win.viewFrontAction)
    win.standardViewsMenu.addAction(win.viewBackAction)
    win.standardViewsMenu.addAction(win.viewLeftAction)
    win.standardViewsMenu.addAction(win.viewRightAction)
    win.standardViewsMenu.addAction(win.viewTopAction)
    win.standardViewsMenu.addAction(win.viewBottomAction)
    win.standardViewsMenu.addAction(win.viewIsometricAction)

    win.standardViewsAction = NE1_QWidgetAction(MainWindow, win = MainWindow)
    win.standardViewsAction.setEnabled(True)
    win.standardViewsAction.setIcon(
        geticon("ui/actions/View/Standard_Views.png"))
    win.standardViewsAction.setObjectName("standardViews")
    win.standardViewsAction.setText("Standard Views")
    win.standardViewsAction.setMenu(win.standardViewsMenu)

    win.standardViews_btn = QtWidgets.QToolButton()
    win.standardViews_btn.setPopupMode(QToolButton.MenuButtonPopup)
    win.standardViewsAction.setDefaultWidget(win.standardViews_btn)
    win.standardViews_btn.setDefaultAction(win.standardViewsAction)


    # Dock widgets
    win.reportsDockWidget = Ui_ReportsDockWidget(win)

def retranslateUi(win):
    """
    Sets text related attributes for all main window QAction widgets.

    @param win: NE1's mainwindow object.
    @type  win: U{B{QMainWindow}<http://doc.trolltech.com/4/qmainwindow.html>}
    """
    """
    This function centralizes and sets UI text for main window QAction widgets
    for the purpose of making it easier for the programmer to translate the
    UI into other languages using Qt Linguist.

    @param MainWindow: The main window
    @type  MainWindow: U{B{QMainWindow}<http://doc.trolltech.com/4/qmainwindow.html>}

    @see: U{B{The Qt Linquist Manual}<http://doc.trolltech.com/4/linguist-manual.html>}

    @attention: It is never OK to set the shortcut "Ctrl+H or Cmd+H on Mac)"
    via setShortcut() since this shortcut is reserved on Mac OS X for hiding a
    window.
    """

    #= File (menu and toolbar) actions.
    win.fileOpenAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "&Open...", None))
    win.fileOpenAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Open", None))
    win.fileOpenAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Open(Ctrl+O)", None))
    win.fileOpenAction.setShortcut(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Ctrl+O", None))
    win.fileCloseAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "&Close and begin new model", None))
    win.fileCloseAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Close", None))
    win.fileSaveAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "&Save", None))
    win.fileSaveAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Save (Ctrl+S)", None))
    win.fileSaveAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Save", None))
    win.fileSaveAction.setShortcut(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Ctrl+S", None))
    win.fileSaveAsAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Save &As...", None))
    win.fileSaveAsAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Save As", None))
    win.fileImportOpenBabelAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Open Babel import...",
            None))
    win.fileImportOpenBabelAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Open Babel",
            None))
    win.fileImportOpenBabelAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Open Babel import", None))

    win.fileImportIOSAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "IOS import...",
            None))
    win.fileImportIOSAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "IOS",
            None))
    win.fileImportIOSAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "IOS import", None))

    win.fileExportPdbAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Protein Data Bank...",
            None))

    win.fileExportQuteMolXPdbAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Protein Data Bank for QuteMolX...",
            None))

    win.fileExportJpgAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "JPEG image...",
            None))

    win.fileExportPngAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "PNG image...",
            None))

    win.fileExportPovAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "POV-Ray...",
            None))

    win.fileExportAmdlAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Animation Master Model...",
            None))

    win.fileExportOpenBabelAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Open Babel export...",
            None))
    win.fileExportOpenBabelAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Open Babel",
            None))
    win.fileExportOpenBabelAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Open Babel export", None))

    #ios export
    win.fileExportIOSAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "IOS export...",
            None))
    win.fileExportIOSAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "IOS",
            None))
    win.fileExportIOSAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "IOS export", None))

    #fetch pdb
    win.fileFetchPdbAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "PDB file from RCSB...",
            None))
    win.fileFetchPdbAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Fetch PDB",
            None))
    win.fileFetchPdbAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Fetch a PDB file from RCSB", None))

    win.fileExitAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "E&xit", None))
    win.fileExitAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Exit", None))

    #= Edit (menu and toolbar) actions.
    win.editUndoAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "&Undo",
            None))
    win.editUndoAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Undo",
            None))
    win.editUndoAction.setShortcut(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Ctrl+Z",
            None))
    win.editUndoAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Undo (Ctrl+Z)", None))
    win.editRedoAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "&Redo",
            None))
    win.editRedoAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Redo",
            None))

    # Redo is a special case between Mac OS X and the other platforms:
    # - Cmd+Shift+Z on Mac
    # - Ctrl+Y on Windows and Linux
    # We take care of tooltips and keyboard shortcut settings here.
    # -Mark 2008-05-05.
    from platform_dependent.PlatformDependent import is_macintosh
    if is_macintosh():
        redo_accel = "Cmd+Shift+Z"
    else:
        redo_accel = "Ctrl+Y"
    win.editRedoAction.setShortcut(
        QtCore.QCoreApplication.translate(
            "MainWindow", redo_accel,
            None))
    win.editRedoAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Redo (" + redo_accel + ")",
            None))
    win.editCutAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "&Cut",
            None))
    win.editCutAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Cut",
            None))
    win.editCutAction.setShortcut(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Ctrl+X",
            None))
    win.editCutAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Cut (Ctrl+X)", None))
    win.editCopyAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "C&opy",
            None))
    win.editCopyAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Copy",
            None))
    win.editCopyAction.setShortcut(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Ctrl+C",
            None))
    win.editCopyAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Copy (Ctrl+V)", None))
    win.editPasteAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "&Paste",
            None))
    win.editPasteAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Paste",
            None))
    win.editPasteAction.setShortcut(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Ctrl+V",
            None))
    win.editDeleteAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "&Delete",
            None))
    win.editDeleteAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Delete",
            None))
    win.editDeleteAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Delete (Del)",
            None))
    win.editRenameAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Rename",
            None))
    win.editRenameAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Rename",
            None))
    win.editRenameAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Rename (Shift+R)",
            None))
    win.editRenameAction.setShortcut(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Shift+R",
            None))
    win.editRenameSelectionAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Rename Selection",
            None))
    win.editRenameSelectionAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Rename Selection",
            None))
    win.editRenameSelectionAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Rename Selection",
            None))

    win.editAddSuffixAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Add Suffixes",
            None))
    win.editAddSuffixAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Add Suffixes",
            None))
    win.editAddSuffixAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Add Suffixes",
            None))

    win.editMakeCheckpointAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Make Checkpoint",
            None))
    win.editAutoCheckpointingAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Automatic Checkpointing",
            None))
    win.editClearUndoStackAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Clear Undo Stack",
            None))
    win.dispObjectColorAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Change Color of Selection...",
            None))
    win.dispObjectColorAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Change Color of Selected Objects",
            None))
    win.dispObjectColorAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Change Color",
            None))






    #= View (menu and toolbar) actions.
    win.viewOrientationAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Orientation Manager...",
            None))
    win.viewOrientationAction.setShortcut(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Space",
            None))
    win.setViewFitToWindowAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "&Zoom to Fit",
            None))
    win.setViewFitToWindowAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Zoom to Fit",
            None))
    win.setViewFitToWindowAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Zoom to Fit (Ctrl+F)",
            None))
    win.setViewFitToWindowAction.setShortcut(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Ctrl+F",
            None))
    win.zoomToAreaAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "&Zoom to Area",
            None))
    win.zoomToAreaAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Zoom to Area",
            None))
    win.setViewZoomtoSelectionAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Zoom To Selection",
            None))
    win.setViewZoomtoSelectionAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Zoom To Selection",
            None))
    win.setViewZoomtoSelectionAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Zoom to Selection",
            None))

    win.zoomInOutAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Zoom",
            None))
    win.zoomInOutAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Zoom",
            None))
    win.zoomInOutAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Zoom In . (dot) | Zoom Out , (comma)",
            None))

    win.panToolAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&Pan", None))
    win.panToolAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Pan ", None))
    win.rotateToolAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Rotate", None))
    win.rotateToolAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Rotate", None))
    win.setViewHomeAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&Home", None))
    win.setViewHomeAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Home", None))
    win.setViewHomeAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Home View (Home)", None))
    win.setViewHomeAction.setShortcut(QtCore.QCoreApplication.translate("MainWindow", "Home", None))
    win.setViewRecenterAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&Recenter", None))
    win.setViewRecenterAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Recenter", None))
    win.setViewRecenterAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Recenter (Ctrl+R)", None))
    win.setViewRecenterAction.setShortcut(QtCore.QCoreApplication.translate("MainWindow", "Ctrl+R", None))
    win.setViewHomeToCurrentAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Replace 'Home View' with the current view", None))
    win.setViewHomeToCurrentAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Replace 'Home View' with the current view", None))
    win.setViewHomeToCurrentAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Replace 'Home View' with the current view (Ctrl+Home)", None))
    win.setViewHomeToCurrentAction.setShortcut(QtCore.QCoreApplication.translate("MainWindow", "Ctrl+Home", None))
    win.saveNamedViewAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Save Named View", None))
    win.saveNamedViewAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Save Named View", None))

    #VIEW > DISPLAY MENU ITEMS
    win.dispBallAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Ball and Stick", None))
    win.dispBallAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Ball and Stick", None))
    win.dispBallAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow",
            "Apply <b>Ball and Stick</b> display style to the selection",
            None))
    win.dispDefaultAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Default", None))
    win.dispDefaultAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Default", None))
    win.dispDefaultAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow",
            "Apply <b>Default</b> display setting to the selection",
            None))
    win.dispInvisAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Invisible", None))
    win.dispInvisAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Invisible", None))
    win.dispLinesAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Lines", None))
    win.dispLinesAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Lines", None))
    win.dispLinesAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow",
            "Apply <b>Lines</b> display style to the selection",
            None))
    win.dispTubesAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Tubes", None))
    win.dispTubesAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Tubes", None))
    win.dispTubesAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow",
            "Apply <b>Tubes</b> display style to the selection",
            None))
    win.dispCPKAction.setText(QtCore.QCoreApplication.translate("MainWindow", "CPK", None))
    win.dispCPKAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "CPK", None))
    win.dispCPKAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow",
            "Apply <b>CPK</b> display style to the selection",
            None))
    win.dispHybridAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Hybrid Display", None))
    win.dispHybridAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Hybrid", None))
    win.dispSurfaceAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Surface", None))
    win.dispSurfaceAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow",
            "Apply <b>Surface</b> display style to the selection",
            None))
    win.dispCylinderAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Cylinder", None))
    win.dispCylinderAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow",
            "Apply <b>Cylinder</b> display style to the selection",
            None))
    win.dispDnaCylinderAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "DNA Cylinder", None))
    win.dispDnaCylinderAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow",
            "Apply <b>DNA Cylinder</b> display style to the selection",
            None))
    win.dispHideAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Hide", None))
    win.dispHideAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Hide", None))
    win.dispUnhideAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Unhide", None))
    win.dispUnhideAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Unhide", None))

    # FOLLOWING VIEW MENU ITEMS NEED SORTING
    win.viewFrontAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&Front", None))
    win.viewFrontAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Front", None))
    win.viewFrontAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Front View", None))
    win.viewBackAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&Back", None))
    win.viewBackAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Back", None))
    win.viewBackAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Back View", None))
    win.viewTopAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&Top", None))
    win.viewTopAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Top", None))
    win.viewTopAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Top View", None))
    win.viewBottomAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Botto&m", None))
    win.viewBottomAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Bottom", None))
    win.viewBottomAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Bottom View", None))
    win.viewRightAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&Right", None))
    win.viewRightAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Right", None))
    win.viewRightAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Right View", None))
    win.viewRightAction.setStatusTip(QtCore.QCoreApplication.translate("MainWindow", "Right View", None))
    win.viewLeftAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&Left", None))
    win.viewLeftAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Left", None))
    win.viewLeftAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Left View", None))

    win.viewFlipViewVertAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Flip View Vertically", None))
    win.viewFlipViewVertAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Flip View Vertically", None))
    win.viewFlipViewVertAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Flip View Vertically", None))
    win.viewFlipViewVertAction.setStatusTip(QtCore.QCoreApplication.translate("MainWindow", "Flip View Vertically", None))

    win.viewFlipViewHorzAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Flip View Horizontally", None))
    win.viewFlipViewHorzAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Flip View Horizontally", None))
    win.viewFlipViewHorzAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Flip View Horizontally", None))
    win.viewFlipViewHorzAction.setStatusTip(QtCore.QCoreApplication.translate("MainWindow", "Flip View Horizontally", None))

    win.viewIsometricAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&Isometric", None))
    win.viewIsometricAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Isometric", None))
    win.resetChunkColorAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&Reset Color of Selected Chunks", None))
    win.resetChunkColorAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Reset Color of Selected Chunks", None))

    #= Insert (menu and toolbar) actions.
    win.jigsAtomSetAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow",  "Atom Set",  None))

    win.fileInsertMmpAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", "MMP file",
        None))

    win.fileInsertMmpAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "MMP file",
        None))

    win.fileInsertMmpAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow", "Insert Molecular Machine Part (MMP) file",
        None))

    win.fileInsertPdbAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", "PDB file",
        None))

    win.fileInsertPdbAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "PDB file",
        None))

    win.fileInsertPdbAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow", "Insert Protein Data Bank (PDB) file",
        None))

    win.fileInsertInAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", "IN file",
        None))

    win.fileInsertInAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "IN file",
        None))

    win.fileInsertInAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow", "Insert AMBER .in file fragment",
        None))

    win.insertCommentAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "Comment",
        None))

    win.insertPovraySceneAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "POV-Ray Scene",
        None))

    win.insertPovraySceneAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow", "Insert POV-Ray Scene file",
        None))

    win.jigsGridPlaneAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "Grid Plane",
        None))

    win.referencePlaneAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "Plane",
        None))

    # Part Lib
    win.partLibAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", "Part Library",
        None))

    win.partLibAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "Part from Part Library",
        None))

    win.partLibAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow", "Insert Part from Part Library",
        None))

    #= Tools (menu and toolbar) actions.
    win.modifyAdjustSelAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Adjust Selection",
        None))

    win.modifyAdjustSelAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Adjust Selection",
        None))

    win.modifyAdjustSelAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Adjust Selection",
        None))

    win.modifyAdjustAllAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Adjust All",
        None))

    win.modifyAdjustAllAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Adjust All",
        None))

    win.simMinimizeEnergyAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Minimize Energy",
        None))

    win.checkAtomTypesAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Check AMBER AtomTypes",
        None))

    win.toolsExtrudeAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Extrude",
        None))

    win.toolsFuseChunksAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Fuse",
        None))

    win.toolsFuseChunksAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Fuse Chunks",
        None))

    win.toolsExtrudeAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Extrude",
        None))

    win.editPrefsAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Preferences...",
        None))

    win.colorSchemeAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Color Scheme",
            None))

    win.lightingSchemeAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Lighting Scheme",
        None))

    win.modifyMirrorAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Mirror",
        None))

    win.modifyMirrorAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Mirror Chunks",
        None))

    win.modifyInvertAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", "&Invert",
        None))

    win.modifyInvertAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Invert",
        None))

    win.editPrefsAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Preferences...",
        None))

    win.editPrefsAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Preferences",
        None))

    #Urmi background color chooser option 080522

    win.colorSchemeAction.setToolTip(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Color Scheme",
            None))
    win.colorSchemeAction.setIconText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Color Scheme",
            None))

    win.lightingSchemeAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Lighting Scheme",
        None))
    win.lightingSchemeAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Lighting Scheme",
        None))

    #= Tools > Build Structures (menu and toolbar) actions.
    win.toolsDepositAtomAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Atoms",
            None))
    win.toolsDepositAtomAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Build Atoms",
        None))
    win.buildCrystalAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Crystal",
        None))
    win.buildCrystalAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Build Crystal",
        None))
    win.nanotubeGeneratorAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Nanotube",
        None))
    win.nanotubeGeneratorAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Generate Nanotube (old)",
        None))
    win.insertGrapheneAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Graphene",
        None))
    win.insertGrapheneAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Generate Graphene",
        None))
    win.buildDnaAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "DNA",
        None))
    win.buildDnaAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "DNA",
        None))
    win.buildDnaAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Build DNA",
        None))
    win.buildNanotubeAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Nanotube",
        None))
    win.buildNanotubeAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Nanotube",
        None))
    win.buildNanotubeAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Build Nanotube",
        None))

    # Atom Generator example for developers.
    win.insertAtomAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Insert Atom",
        None))
    win.insertAtomAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Insert Atom (Developer Example)",
        None))

    # Peptide Generator. piotr 080304
    # piotr 080710 : Use "Peptide" label instead of "Protein"
    # if the "Enable Proteins" debug pref is set to False.
    # This should be moved to "interactive builders" sections
    # on the Build Structures toolbar.
    from utilities.GlobalPreferences import ENABLE_PROTEINS
    if ENABLE_PROTEINS:
        win.buildProteinAction.setIconText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Protein",
            None))
        win.buildProteinAction.setToolTip(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Build Protein",
            None))
    else:
        win.buildProteinAction.setIconText(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Peptide",
            None))
        win.buildProteinAction.setToolTip(QtCore.QCoreApplication.translate(
            "MainWindow",
            "Generate Peptide",
            None))

    #= "Tools > Build Tools" (menu and toolbar) actions.

    win.modifyHydrogenateAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&Hydrogenate",
                                                                     None))
    win.modifyHydrogenateAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Hydrogenate",
                                                                         None))
    win.modifyHydrogenateAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Hydrogenate",
                                                                        None))
    win.modifyDehydrogenateAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&Dehydrogenate",
                                                                       None))
    win.modifyDehydrogenateAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Dehydrogenate",
                                                                           None))
    win.modifyPassivateAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&Passivate",
                                                                   None))
    win.modifyPassivateAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Passivate",
                                                                       None))
    win.modifyPassivateAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Passivate",
                                                                      None))
    win.modifyDeleteBondsAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", "Cut &Bonds",None))
    win.modifyDeleteBondsAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "Cut Bonds",None))
    win.modifyMergeAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow","Combine",None))

    win.modifyMergeAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow","Combine Selected Chunks",None))

    win.makeChunkFromSelectedAtomsAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow","New Chunk",None))

    win.makeChunkFromSelectedAtomsAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow","Create a new chunk for selected atoms",None))

    win.modifySeparateAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow",  "&Separate", None))
    win.modifySeparateAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "Separate", None))
    win.modifyAlignCommonAxisAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", "Align to &Common Axis",None))
    win.modifyAlignCommonAxisAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "Align to Common Axis",None))
    win.modifyCenterCommonAxisAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "Center on Common Axis",None))

    #TOOLS > DIMENSIONS MENU
    win.jigsDistanceAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Measure Distance", None))
    win.jigsDistanceAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Measure Distance", None))
    win.jigsAngleAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Measure Angle", None))
    win.jigsAngleAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Measure Angle", None))
    win.jigsDihedralAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Measure Dihedral", None))
    win.jigsDihedralAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Measure Dihedral", None))

    #TOOLS > SELECT  MENU ITEMS
    win.selectAllAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&All", None))
    win.selectAllAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "All", None))
    win.selectAllAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Select All (Ctrl+A)", None))
    win.selectAllAction.setShortcut(QtCore.QCoreApplication.translate("MainWindow", "Ctrl+A", None))
    win.selectNoneAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&None", None))
    win.selectNoneAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "None", None))
    win.selectNoneAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Select None (Ctrl+N)", None))
    win.selectNoneAction.setShortcut(QtCore.QCoreApplication.translate("MainWindow", "Ctrl+N", None))
    win.selectInvertAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&Invert", None))
    win.selectInvertAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Invert", None))
    win.selectInvertAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Invert Selection (Ctrl+Shift+I)", None))
    win.selectInvertAction.setShortcut(QtCore.QCoreApplication.translate("MainWindow", "Ctrl+Shift+I", None))
    win.selectConnectedAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&Connected", None))
    win.selectConnectedAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Connected", None))
    win.selectConnectedAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Select Connected (Ctrl+Shift+C)", None))
    win.selectConnectedAction.setShortcut(QtCore.QCoreApplication.translate("MainWindow", "Ctrl+Shift+C", None))
    win.selectDoublyAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&Doubly", None))
    win.selectDoublyAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Doubly", None))
    win.selectDoublyAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Select Doubly", None))
    win.selectExpandAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Expand", None))
    win.selectExpandAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Expand Selection (Ctrl+D)", None))
    win.selectExpandAction.setShortcut(QtCore.QCoreApplication.translate("MainWindow", "Ctrl+D", None))
    win.selectContractAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Contract", None))
    win.selectContractAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Contract Selection (Ctrl+Shift+D)", None))
    win.selectContractAction.setShortcut(QtCore.QCoreApplication.translate("MainWindow", "Ctrl+Shift+D", None))
    win.selectLockAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Lock", None))
    win.selectLockAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Selection Lock (Ctrl+L)", None))
    win.selectLockAction.setShortcut(QtCore.QCoreApplication.translate("MainWindow", "Ctrl+L", None))

    win.selectByNameAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow",
        "Select By Name",
        None))

    #= "Simulation" (menu and toolbar) actions.
    win.simSetupAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", " Run Dynamics...", None))
    win.simSetupAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "Run Dynamics", None))
    win.simSetupAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow", "Run Dynamics", None))
    win.simMoviePlayerAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", "Play Movie",None))
    win.simMoviePlayerAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow", "Play Movie",None))

    win.rosettaSetupAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", " Rosetta", None))
    win.rosettaSetupAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "Rosetta", None))
    win.rosettaSetupAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow", "Rosetta", None))

    win.simPlotToolAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", "Plot Graphs", None))
    win.simPlotToolAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "Plot Graphs", None))
    win.jigsESPImageAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", "ESP Image", None))
    win.jigsESPImageAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "ESP Image", None))
    win.simulationJigsAction.setToolTip(QtCore.QCoreApplication.translate(
        "MainWindow", "Simulation Jigs", None))

    import sys
    if sys.platform == "win32":
        gms_str = "PC GAMESS"
    else:
        gms_str = "GAMESS"

    win.jigsGamessAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", gms_str, None))
    win.jigsGamessAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", gms_str, None))

    # Simulation Jigs
    win.jigsLinearMotorAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", "&Linear Motor", None))
    win.jigsLinearMotorAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "Linear Motor", None))
    win.jigsStatAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", "Thermo&stat", None))
    win.jigsStatAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "Thermostat", None))
    win.jigsAnchorAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", "&Anchor", None))
    win.jigsAnchorAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "Anchor", None))
    win.jigsMotorAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", "&Rotary Motor", None))
    win.jigsMotorAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "Rotary Motor", None))

    #= "Simuation > Measurements" (menu and toolbar) actions.
    win.jigsThermoAction.setText(QtCore.QCoreApplication.translate(
        "MainWindow", "&Thermometer", None))
    win.jigsThermoAction.setIconText(QtCore.QCoreApplication.translate(
        "MainWindow", "Thermometer", None))

    #= "Help" (menu and toolbar) actions.
    win.helpAboutAction.setText(QtCore.QCoreApplication.translate("MainWindow", "&About NanoEngineer-1", None))
    win.helpAboutAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "About NanoEngineer-1", None))

    win.helpWhatsThisAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Enter \"What\'s This\" help mode", None))
    win.helpWhatsThisAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "What\'s This", None))
    win.helpGraphicsCardAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Graphics Card Info...", None))
    win.helpGraphicsCardAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Graphics Card Info", None))

    win.helpMouseControlsAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Mouse Controls...", None))
    win.helpMouseControlsAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Mouse Controls", None))
    win.helpKeyboardShortcutsAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Keyboard Shortcuts...", None))
    win.helpKeyboardShortcutsAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Keyboard Shortcuts", None))
    win.helpSelectionShortcutsAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Selection Shortcuts...", None))
    win.helpSelectionShortcutsAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Selection Shortcuts", None))

    win.helpTutorialsAction.setText(QtCore.QCoreApplication.translate("MainWindow", "NanoEngineer-1 Tutorials...", None))
    win.helpTutorialsAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "NanoEngineer-1 Tutorials...", None))

    # Other QActions not used in menus. These QActions are used in toolbars,
    # context menus, etc.
    win.viewDefviewAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Orientations", None))
    win.viewDefviewAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Orientations", None))
    win.viewDefviewAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Default Views", None))




    win.modifyStretchAction.setText(QtCore.QCoreApplication.translate("MainWindow", "S&tretch", None))
    win.modifyStretchAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Stretch", None))

    win.dispSetEltable1Action.setText(QtCore.QCoreApplication.translate("MainWindow", "Set Atom Colors to Default", None))
    win.dispSetEltable1Action.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Set Atom Colors to Default", None))
    win.dispSetEltable2Action.setText(QtCore.QCoreApplication.translate("MainWindow", "Set Atom Colors to Alternate", None))
    win.dispSetEltable2Action.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Set Atom Colors to Alternate", None))

    win.dispElementColorSettingsAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Element Color Settings...", None))
    win.dispElementColorSettingsAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Element Color Settings...", None))

    win.dispLightingAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Lighting...", None))
    win.dispLightingAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Lighting", None))
    win.dispResetAtomsDisplayAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Reset Atoms Display", None))
    win.dispResetAtomsDisplayAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Reset Atoms Display", None))
    win.dispShowInvisAtomsAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Show Invisible Atoms", None))
    win.dispShowInvisAtomsAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Show Invisible Atoms", None))

    win.simNanoHiveAction.setText(QtCore.QCoreApplication.translate("MainWindow", "Nano-Hive...", None))
    win.simNanoHiveAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Nano-Hive", None))

    win.fileSaveSelectionAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Save Selection...", None))
    win.viewRotatePlus90Action.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Rotate View +90", None))
    win.viewRotateMinus90Action.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Rotate View -90", None))

    win.viewNormalToAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Set View Normal To", None))
    win.viewNormalToAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Set View Normal To", None))
    win.viewParallelToAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "Set View Parallel To", None))
    win.viewParallelToAction.setToolTip(QtCore.QCoreApplication.translate("MainWindow", "Set View Parallel To", None))

    win.viewQuteMolAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "QuteMolX", None))
    win.viewRaytraceSceneAction.setIconText(QtCore.QCoreApplication.translate("MainWindow", "POV-Ray", None))

    win.setViewPerspecAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Perspective",
            None))
    win.setViewOrthoAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Orthographic",
            None))

    win.setStereoViewAction.setText(
        QtCore.QCoreApplication.translate(
            "MainWindow", "Stereo View",
            None))

    #= Toolbar stuff

    #= "Standard" toolbar widgets
    win.toolsSelectMoleculesAction.setText(
        QtCore.QCoreApplication.translate("MainWindow", "Select Chunks",
                                     None))
    win.toolsSelectMoleculesAction.setToolTip(
        QtCore.QCoreApplication.translate("MainWindow", "Select Chunks",
                                     None))
    win.toolsMoveMoleculeAction.setText(
        QtCore.QCoreApplication.translate("MainWindow", "Translate",
                                     None))
    win.toolsMoveMoleculeAction.setToolTip(
        QtCore.QCoreApplication.translate("MainWindow", "Translate Selection",
                                     None))
    win.rotateComponentsAction.setText(
        QtCore.QCoreApplication.translate("MainWindow", "Rotate",
                                     None))
    win.rotateComponentsAction.setToolTip(
        QtCore.QCoreApplication.translate("MainWindow", "Rotate Selection",
                                     None))
