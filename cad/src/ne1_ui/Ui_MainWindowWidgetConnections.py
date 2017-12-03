# Copyright 2004-2007 Nanorex, Inc.  See LICENSE file for details.
"""
Ui_MainWindowWidgetConnections.py

Creates all signal-slot connections for all Main Window widgets used in menus
and toolbars.

@author: Mark
@version: $Id$
@copyright: 2004-2007 Nanorex, Inc.  See LICENSE file for details.

History:

2007-12-23: Moved all connect() calls from MWsemantics to here.
"""

from PyQt5 import QtCore

def setupUi(win):
    """
    Create all connects for all Main Window widgets used in menus and toolbars.

    @param win: NE1's mainwindow object.
    @type  win: U{B{QMainWindow}<http://doc.trolltech.com/4/qmainwindow.html>}
    """

    win.dispBallAction.triggered.connect(win.dispBall)
    win.dispDefaultAction.triggered.connect(win.dispDefault)
    win.dispElementColorSettingsAction.triggered.connect(win.dispElementColorSettings)
    win.dispInvisAction.triggered.connect(win.dispInvis)
    win.dispLightingAction.triggered.connect(win.dispLighting)
    win.dispLinesAction.triggered.connect(win.dispLines)
    win.dispObjectColorAction.triggered.connect(win.dispObjectColor)

    win.resetChunkColorAction.triggered.connect(win.dispResetChunkColor)
    win.dispResetAtomsDisplayAction.triggered.connect(win.dispResetAtomsDisplay)
    win.dispShowInvisAtomsAction.triggered.connect(win.dispShowInvisAtoms)
    win.dispTubesAction.triggered.connect(win.dispTubes)
    win.dispCPKAction.triggered.connect(win.dispCPK)
    win.dispHideAction.triggered.connect(win.dispHide)
    win.dispUnhideAction.triggered.connect(win.dispUnhide)
    win.dispHybridAction.triggered.connect(win.dispHybrid)

    win.editAutoCheckpointingAction.toggled[bool].connect(win.editAutoCheckpointing)
    win.editClearUndoStackAction.triggered.connect(win.editClearUndoStack)
    win.editCopyAction.triggered.connect(win.editCopy)
    win.editCutAction.triggered.connect(win.editCut)
    win.editDeleteAction.triggered.connect(win.killDo)
    win.editMakeCheckpointAction.triggered.connect(win.editMakeCheckpoint)
    win.editPasteAction.triggered.connect(win.editPaste)

    win.editDnaDisplayStyleAction.triggered.connect(win.enterDnaDisplayStyleCommand)
    win.editProteinDisplayStyleAction.triggered.connect(win.enterProteinDisplayStyleCommand)

    # editRenameAction deprecated. Use editRenameSelection. Mark 2008-11-13.
    #win.connect(win.editRenameAction,SIGNAL("triggered()"),win.editRename)
    win.editRenameSelectionAction.triggered.connect(win.editRenameSelection)
    win.editAddSuffixAction.triggered.connect(win.editAddSuffix)
    win.pasteFromClipboardAction.triggered.connect(win.editPasteFromClipboard)
    win.partLibAction.triggered.connect(win.insertPartFromPartLib)

    win.viewFullScreenAction.toggled[bool].connect(win.setViewFullScreen)
    win.viewSemiFullScreenAction.toggled[bool].connect(win.setViewSemiFullScreen)
    win.viewReportsAction.toggled[bool].connect(win.reportsDockWidget.toggle)
    win.viewRulersAction.toggled[bool].connect(win.toggleRulers)

    #Urmi background color chooser option 080522
    win.colorSchemeAction.triggered.connect(win.colorSchemeCommand)
    win.lightingSchemeAction.triggered.connect(win.lightingSchemeCommand)

    win.editPrefsAction.triggered.connect(win.editPrefs)
    win.editRedoAction.triggered.connect(win.editRedo)
    win.editUndoAction.triggered.connect(win.editUndo)

    #= Connections for the "File" menu and toolbar widgets.

    win.fileCloseAction.triggered.connect(win.fileClose)
    win.fileExitAction.triggered.connect(win.close)

    win.fileOpenAction.triggered.connect(win.fileOpen)
    win.fileSaveAction.triggered.connect(win.fileSave)
    win.fileSaveAsAction.triggered.connect(win.fileSaveAs)
    win.fileSaveSelectionAction.triggered.connect(win.fileSaveSelection)
    win.fileSetWorkingDirectoryAction.triggered.connect(win.fileSetWorkingDirectory)
    win.fileInsertMmpAction.triggered.connect(win.fileInsertMmp)
    win.fileInsertPdbAction.triggered.connect(win.fileInsertPdb)
    win.fileInsertInAction.triggered.connect(win.fileInsertIn)
    win.fileExportQuteMolXPdbAction.triggered.connect(win.fileExportQuteMolXPdb)
    win.fileExportPdbAction.triggered.connect(win.fileExportPdb)

    win.fileFetchPdbAction.triggered.connect(win.fileFetchPdb)

    win.fileExportJpgAction.triggered.connect(win.fileExportJpg)
    win.fileExportPngAction.triggered.connect(win.fileExportPng)
    win.fileExportPovAction.triggered.connect(win.fileExportPov)
    win.fileExportAmdlAction.triggered.connect(win.fileExportAmdl)

    win.helpTutorialsAction.triggered.connect(win.helpTutorials)
    win.helpAboutAction.triggered.connect(win.helpAbout)
    win.helpGraphicsCardAction.triggered.connect(win.helpGraphicsCard)
    win.helpKeyboardShortcutsAction.triggered.connect(win.helpKeyboardShortcuts)
    win.helpSelectionShortcutsAction.triggered.connect(win.helpSelectionShortcuts)
    win.helpMouseControlsAction.triggered.connect(win.helpMouseControls)
    win.helpWhatsThisAction.triggered.connect(win.helpWhatsThis)

    win.buildDnaAction.triggered.connect(win.activateDnaTool)
    win.buildNanotubeAction.triggered.connect(win.activateNanotubeTool)
    win.insertCommentAction.triggered.connect(win.insertComment)
    win.insertGrapheneAction.triggered.connect(win.insertGraphene)

    win.jigsAnchorAction.triggered.connect(win.makeAnchor)
    win.jigsAngleAction.triggered.connect(win.makeMeasureAngle)
    win.jigsAtomSetAction.triggered.connect(win.makeAtomSet)
    win.jigsDihedralAction.triggered.connect(win.makeMeasureDihedral)
    win.jigsDistanceAction.triggered.connect(win.makeMeasureDistance)
    win.jigsESPImageAction.triggered.connect(win.makeESPImage)
    win.jigsGamessAction.triggered.connect(win.makeGamess)
    win.jigsGridPlaneAction.triggered.connect(win.makeGridPlane)

    win.referencePlaneAction.triggered.connect(win.createPlane)
    win.referenceLineAction.triggered.connect(win.createPolyLine)

    win.jigsLinearMotorAction.triggered.connect(win.makeLinearMotor)

    win.jigsMotorAction.triggered.connect(win.makeRotaryMotor)

    win.jigsStatAction.triggered.connect(win.makeStat)
    win.jigsThermoAction.triggered.connect(win.makeThermo)
    win.modifyAlignCommonAxisAction.triggered.connect(win.modifyAlignCommonAxis)
    win.modifyCenterCommonAxisAction.triggered.connect(win.modifyCenterCommonAxis)
    win.modifyDehydrogenateAction.triggered.connect(win.modifyDehydrogenate)
    win.modifyDeleteBondsAction.triggered.connect(win.modifyDeleteBonds)
    win.modifyHydrogenateAction.triggered.connect(win.modifyHydrogenate)
    win.modifyInvertAction.triggered.connect(win.modifyInvert)
    win.modifyMergeAction.triggered.connect(win.modifyMerge)
    win.makeChunkFromSelectedAtomsAction.triggered.connect(win.makeChunkFromAtom)
    win.modifyAdjustAllAction.triggered.connect(win.modifyAdjustAll)
    win.modifyAdjustSelAction.triggered.connect(win.modifyAdjustSel)
    win.modifyPassivateAction.triggered.connect(win.modifyPassivate)
    win.modifySeparateAction.triggered.connect(win.modifySeparate)
    win.modifyStretchAction.triggered.connect(win.modifyStretch)
    win.panToolAction.toggled[bool].connect(win.panTool)
    win.rotateToolAction.toggled[bool].connect(win.rotateTool)
    win.saveNamedViewAction.triggered.connect(win.saveNamedView)
    win.selectAllAction.triggered.connect(win.selectAll)
    win.selectConnectedAction.triggered.connect(win.selectConnected)
    win.selectContractAction.triggered.connect(win.selectContract)
    win.selectDoublyAction.triggered.connect(win.selectDoubly)
    win.selectExpandAction.triggered.connect(win.selectExpand)
    win.selectInvertAction.triggered.connect(win.selectInvert)
    win.selectNoneAction.triggered.connect(win.selectNone)
    win.selectLockAction.toggled[bool].connect(win.selectLock)
    win.selectByNameAction.toggled[bool].connect(win.toggle_selectByNameDockWidget)

    ##win.connect(win.helpTipAction,SIGNAL("triggered()"), win.toggleQuickHelpTip)

    win.viewOrientationAction.toggled[bool].connect(win.showOrientationWindow)

    ##When Standard Views button is clicked, show its QMenu.-- By default, nothing happens if you click on the
    ##toolbutton with submenus. The menus are displayed only when you click on the small downward arrow
    ## of the tool button. Therefore the following slot is added. Also QWidgetAction is used
    ## for it to add this feature (see Ui_ViewToolBar for details) ninad 070109
    win.standardViews_btn.pressed.connect(win.showStandardViewsMenu)

    win.viewBackAction.triggered.connect(win.viewBack)
    win.viewBottomAction.triggered.connect(win.viewBottom)
    win.setViewFitToWindowAction.triggered.connect(win.setViewFitToWindow)
    win.viewFrontAction.triggered.connect(win.viewFront)
    win.setViewHomeAction.triggered.connect(win.setViewHome)
    win.setViewHomeToCurrentAction.triggered.connect(win.setViewHomeToCurrent)
    win.viewLeftAction.triggered.connect(win.viewLeft)
    win.viewRotateMinus90Action.triggered.connect(win.viewRotateMinus90)
    win.viewNormalToAction.triggered.connect(win.viewNormalTo)
    win.viewFlipViewVertAction.triggered.connect(win.viewFlipViewVert)
    win.viewFlipViewHorzAction.triggered.connect(win.viewFlipViewHorz)
    win.setViewOrthoAction.triggered.connect(win.setViewOrtho)
    win.viewParallelToAction.triggered.connect(win.viewParallelTo)
    win.setViewPerspecAction.triggered.connect(win.setViewPerspec)
    win.viewRotatePlus90Action.triggered.connect(win.viewRotatePlus90)
    win.setViewRecenterAction.triggered.connect(win.setViewRecenter)
    win.viewRightAction.triggered.connect(win.viewRight)
    win.viewTopAction.triggered.connect(win.viewTop)
    win.simMoviePlayerAction.triggered.connect(win.simMoviePlayer)
    win.simNanoHiveAction.triggered.connect(win.simNanoHive)
    win.simPlotToolAction.triggered.connect(win.simPlot)
    win.simSetupAction.triggered.connect(win.simSetup)
    win.rosettaSetupAction.triggered.connect(win.rosettaSetup)

    win.buildCrystalAction.triggered.connect(win.enterBuildCrystalCommand)

    win.setStereoViewAction.triggered.connect(win.stereoSettings)

    win.toolsDepositAtomAction.triggered.connect(win.toolsBuildAtoms)


    win.toolsExtrudeAction.triggered.connect(win.toolsExtrude)
    win.toolsFuseChunksAction.triggered.connect(win.toolsFuseChunks)

    #Move and Rotate Components mode
    win.toolsMoveMoleculeAction.triggered.connect(win.toolsMoveMolecule)
    win.rotateComponentsAction.triggered.connect(win.toolsRotateComponents)

    win.toolsSelectMoleculesAction.triggered.connect(win.toolsSelectMolecules)
    win.zoomToAreaAction.toggled[bool].connect(win.zoomToArea)
    win.zoomInOutAction.toggled[bool].connect(win.zoomInOut)
    win.viewQuteMolAction.triggered.connect(win.viewQuteMol)
    win.viewRaytraceSceneAction.triggered.connect(win.viewRaytraceScene)
    win.insertPovraySceneAction.triggered.connect(win.insertPovrayScene)
    win.dispSurfaceAction.triggered.connect(win.dispSurface)
    win.dispCylinderAction.triggered.connect(win.dispCylinder)
    win.dispDnaCylinderAction.triggered.connect(win.dispDnaCylinder)
    win.simMinimizeEnergyAction.triggered.connect(win.simMinimizeEnergy)
    win.checkAtomTypesAction.triggered.connect(win.modifyCheckAtomTypes)
    win.fileImportOpenBabelAction.triggered.connect(win.fileOpenBabelImport)
    win.fileImportIOSAction.triggered.connect(win.fileIOSImport)
    win.fileExportOpenBabelAction.triggered.connect(win.fileOpenBabelExport)
    win.fileExportIOSAction.triggered.connect(win.fileIOSExport)
    win.viewIsometricAction.triggered.connect(win.viewIsometric)
    win.modifyMirrorAction.triggered.connect(win.modifyMirror)
    win.setViewZoomtoSelectionAction.triggered.connect(win.setViewZoomToSelection)

    # Atom Generator example for developers. Mark and Jeff. 2007-06-13
    #@ Jeff - add a link to the public wiki page when ready. Mark 2007-06-13.
    win.insertAtomAction.triggered.connect(win.insertAtom)

    win.buildProteinAction.triggered.connect(win.activateProteinTool)

    win.fileExitAction.activated.connect(win.close)
