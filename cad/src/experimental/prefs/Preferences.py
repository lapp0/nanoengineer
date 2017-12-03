# Copyright 2005-2008 Nanorex, Inc.  See LICENSE file for details.
"""
Preferences.py

@author: Mark
@version: $Id: Preferences.py 14197 2008-09-11 04:52:29Z brucesmith $
@copyright: 2005-2008 Nanorex, Inc.  See LICENSE file for details.

History:
-Mark 2008-05-20: Created by Mark from a copy of UserPrefs.py
"""

import os, sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QButtonGroup
from PyQt5.QtWidgets import QAbstractButton
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWhatsThis
from PyQt5.QtWidgets import QTreeWidget
from PyQt5.QtCore import QSize
import string

from PreferencesDialog import PreferencesDialog
import foundation.preferences as preferences
from utilities.debug import print_compact_traceback
from utilities.debug_prefs import debug_pref, Choice_boolean_False
import foundation.env as env
from widgets.widget_helpers import RGBf_to_QColor, QColor_to_RGBf
from widgets.widget_helpers import double_fixup
from widgets.prefs_widgets import connect_colorpref_to_colorframe, \
     connect_checkbox_with_boolean_pref, connect_comboBox_with_pref, \
     connect_doubleSpinBox_with_pref, connect_spinBox_with_pref
from utilities import debug_flags
from utilities.constants import str_or_unicode
from platform_dependent.PlatformDependent import screen_pos_size
from platform_dependent.PlatformDependent import get_rootdir
from platform_dependent.Paths import get_default_plugin_path
from utilities.icon_utilities import geticon

from utilities.prefs_constants import displayCompass_prefs_key
from utilities.prefs_constants import displayCompassLabels_prefs_key
from utilities.prefs_constants import displayPOVAxis_prefs_key
from utilities.prefs_constants import displayConfirmationCorner_prefs_key
from utilities.prefs_constants import enableAntiAliasing_prefs_key
from utilities.prefs_constants import animateStandardViews_prefs_key
from utilities.prefs_constants import displayVertRuler_prefs_key
from utilities.prefs_constants import displayHorzRuler_prefs_key
from utilities.prefs_constants import rulerPosition_prefs_key
from utilities.prefs_constants import rulerColor_prefs_key
from utilities.prefs_constants import rulerOpacity_prefs_key
from utilities.prefs_constants import showRulersInPerspectiveView_prefs_key
from utilities.prefs_constants import Adjust_watchRealtimeMinimization_prefs_key
from utilities.prefs_constants import Adjust_minimizationEngine_prefs_key
from utilities.prefs_constants import electrostaticsForDnaDuringAdjust_prefs_key
from utilities.prefs_constants import Adjust_cutoverRMS_prefs_key
from utilities.prefs_constants import qutemol_enabled_prefs_key
from utilities.prefs_constants import qutemol_path_prefs_key
from utilities.prefs_constants import nanohive_enabled_prefs_key
from utilities.prefs_constants import nanohive_path_prefs_key
from utilities.prefs_constants import povray_enabled_prefs_key
from utilities.prefs_constants import povray_path_prefs_key
from utilities.prefs_constants import megapov_enabled_prefs_key
from utilities.prefs_constants import megapov_path_prefs_key
from utilities.prefs_constants import povdir_enabled_prefs_key
from utilities.prefs_constants import gamess_enabled_prefs_key
from utilities.prefs_constants import gmspath_prefs_key
from utilities.prefs_constants import gromacs_enabled_prefs_key
from utilities.prefs_constants import gromacs_path_prefs_key
from utilities.prefs_constants import cpp_enabled_prefs_key
from utilities.prefs_constants import cpp_path_prefs_key
from utilities.prefs_constants import rosetta_enabled_prefs_key
from utilities.prefs_constants import rosetta_path_prefs_key
from utilities.prefs_constants import rosetta_database_enabled_prefs_key
from utilities.prefs_constants import rosetta_dbdir_prefs_key
from utilities.prefs_constants import nv1_enabled_prefs_key
from utilities.prefs_constants import nv1_path_prefs_key
from utilities.prefs_constants import startupGlobalDisplayStyle_prefs_key
from utilities.prefs_constants import buildModeAutobondEnabled_prefs_key
from utilities.prefs_constants import buildModeWaterEnabled_prefs_key
from utilities.prefs_constants import buildModeHighlightingEnabled_prefs_key
from utilities.prefs_constants import buildModeSelectAtomsOfDepositedObjEnabled_prefs_key
from utilities.prefs_constants import light1Color_prefs_key
from utilities.prefs_constants import light2Color_prefs_key
from utilities.prefs_constants import light3Color_prefs_key
from utilities.prefs_constants import atomHighlightColor_prefs_key
from utilities.prefs_constants import bondpointHighlightColor_prefs_key
from utilities.prefs_constants import levelOfDetail_prefs_key
from utilities.prefs_constants import diBALL_AtomRadius_prefs_key
from utilities.prefs_constants import cpkScaleFactor_prefs_key
from utilities.prefs_constants import showBondStretchIndicators_prefs_key
from utilities.prefs_constants import showValenceErrors_prefs_key

#General  page prefs - paste offset scale for chunk and dna pasting prefs key
from utilities.prefs_constants import pasteOffsetScaleFactorForChunks_prefs_key
from utilities.prefs_constants import pasteOffsetScaleFactorForDnaObjects_prefs_key

# Color (page) prefs
from utilities.prefs_constants import backgroundColor_prefs_key
from utilities.prefs_constants import backgroundGradient_prefs_key
from utilities.prefs_constants import hoverHighlightingColorStyle_prefs_key
from utilities.prefs_constants import hoverHighlightingColor_prefs_key
from utilities.prefs_constants import selectionColorStyle_prefs_key
from utilities.prefs_constants import selectionColor_prefs_key
from utilities.prefs_constants import haloWidth_prefs_key

# Mouse wheel prefs
from utilities.prefs_constants import mouseWheelDirection_prefs_key
from utilities.prefs_constants import zoomInAboutScreenCenter_prefs_key
from utilities.prefs_constants import zoomOutAboutScreenCenter_prefs_key
from utilities.prefs_constants import mouseWheelTimeoutInterval_prefs_key

# DNA prefs
from utilities.prefs_constants import bdnaBasesPerTurn_prefs_key
from utilities.prefs_constants import bdnaRise_prefs_key
from utilities.prefs_constants import dnaDefaultStrand1Color_prefs_key
from utilities.prefs_constants import dnaDefaultStrand2Color_prefs_key
from utilities.prefs_constants import dnaDefaultSegmentColor_prefs_key
from utilities.prefs_constants import dnaStrutScaleFactor_prefs_key
from utilities.prefs_constants import arrowsOnBackBones_prefs_key
from utilities.prefs_constants import arrowsOnThreePrimeEnds_prefs_key
from utilities.prefs_constants import arrowsOnFivePrimeEnds_prefs_key
from utilities.prefs_constants import useCustomColorForThreePrimeArrowheads_prefs_key
from utilities.prefs_constants import dnaStrandThreePrimeArrowheadsCustomColor_prefs_key
from utilities.prefs_constants import useCustomColorForFivePrimeArrowheads_prefs_key
from utilities.prefs_constants import dnaStrandFivePrimeArrowheadsCustomColor_prefs_key

# DNA Minor Groove Error Indicator prefs
from utilities.prefs_constants import dnaDisplayMinorGrooveErrorIndicators_prefs_key
from utilities.prefs_constants import dnaMinMinorGrooveAngle_prefs_key
from utilities.prefs_constants import dnaMaxMinorGrooveAngle_prefs_key
from utilities.prefs_constants import dnaMinorGrooveErrorIndicatorColor_prefs_key

# DNA style prefs 080310 piotr
from utilities.prefs_constants import dnaStyleStrandsShape_prefs_key
from utilities.prefs_constants import dnaStyleStrandsColor_prefs_key
from utilities.prefs_constants import dnaStyleStrandsScale_prefs_key
from utilities.prefs_constants import dnaStyleStrandsArrows_prefs_key
from utilities.prefs_constants import dnaStyleAxisShape_prefs_key
from utilities.prefs_constants import dnaStyleAxisColor_prefs_key
from utilities.prefs_constants import dnaStyleAxisScale_prefs_key
from utilities.prefs_constants import dnaStyleAxisEndingStyle_prefs_key
from utilities.prefs_constants import dnaStyleStrutsShape_prefs_key
from utilities.prefs_constants import dnaStyleStrutsColor_prefs_key
from utilities.prefs_constants import dnaStyleStrutsScale_prefs_key
from utilities.prefs_constants import dnaStyleBasesShape_prefs_key
from utilities.prefs_constants import dnaStyleBasesColor_prefs_key
from utilities.prefs_constants import dnaStyleBasesScale_prefs_key

# DNA labels and base indicators. 080325 piotr
from utilities.prefs_constants import dnaStrandLabelsEnabled_prefs_key
from utilities.prefs_constants import dnaStrandLabelsColor_prefs_key
from utilities.prefs_constants import dnaStrandLabelsColorMode_prefs_key
from utilities.prefs_constants import dnaBaseIndicatorsEnabled_prefs_key
from utilities.prefs_constants import dnaBaseInvIndicatorsEnabled_prefs_key
from utilities.prefs_constants import dnaBaseIndicatorsAngle_prefs_key
from utilities.prefs_constants import dnaBaseIndicatorsColor_prefs_key
from utilities.prefs_constants import dnaBaseInvIndicatorsColor_prefs_key
from utilities.prefs_constants import dnaBaseIndicatorsDistance_prefs_key
from utilities.prefs_constants import dnaStyleBasesDisplayLetters_prefs_key
from utilities.prefs_constants import dnaBaseIndicatorsPlaneNormal_prefs_key

# Undo prefs
from utilities.prefs_constants import undoRestoreView_prefs_key
from utilities.prefs_constants import undoAutomaticCheckpoints_prefs_key
from utilities.prefs_constants import undoStackMemoryLimit_prefs_key
from utilities.prefs_constants import historyMsgSerialNumber_prefs_key
from utilities.prefs_constants import historyMsgTimestamp_prefs_key
from utilities.prefs_constants import historyHeight_prefs_key
from utilities.prefs_constants import rememberWinPosSize_prefs_key
from utilities.prefs_constants import captionFullPath_prefs_key
from utilities.prefs_constants import dynamicToolTipAtomChunkInfo_prefs_key
from utilities.prefs_constants import dynamicToolTipAtomMass_prefs_key
from utilities.prefs_constants import dynamicToolTipAtomPosition_prefs_key
from utilities.prefs_constants import dynamicToolTipAtomDistanceDeltas_prefs_key
from utilities.prefs_constants import dynamicToolTipBondLength_prefs_key
from utilities.prefs_constants import dynamicToolTipBondChunkInfo_prefs_key
from utilities.prefs_constants import dynamicToolTipAtomDistancePrecision_prefs_key
from utilities.prefs_constants import captionPrefix_prefs_key
from utilities.prefs_constants import captionSuffix_prefs_key
from utilities.prefs_constants import compassPosition_prefs_key
from utilities.prefs_constants import defaultProjection_prefs_key
from utilities.prefs_constants import displayOriginAsSmallAxis_prefs_key
from utilities.prefs_constants import displayOriginAxis_prefs_key
from utilities.prefs_constants import animateMaximumTime_prefs_key
from utilities.prefs_constants import mouseSpeedDuringRotation_prefs_key
from utilities.prefs_constants import Adjust_endRMS_prefs_key
from utilities.prefs_constants import Adjust_endMax_prefs_key
from utilities.prefs_constants import Adjust_cutoverMax_prefs_key
from utilities.prefs_constants import sponsor_permanent_permission_prefs_key
from utilities.prefs_constants import sponsor_download_permission_prefs_key
from utilities.prefs_constants import bondpointHotspotColor_prefs_key
from utilities.prefs_constants import diBALL_bondcolor_prefs_key
from utilities.prefs_constants import bondHighlightColor_prefs_key
from utilities.prefs_constants import bondStretchColor_prefs_key
from utilities.prefs_constants import bondVaneColor_prefs_key
from utilities.prefs_constants import pibondStyle_prefs_key
from utilities.prefs_constants import pibondLetters_prefs_key
from utilities.prefs_constants import linesDisplayModeThickness_prefs_key
from utilities.prefs_constants import diBALL_BondCylinderRadius_prefs_key
from utilities.prefs_constants import material_specular_highlights_prefs_key
from utilities.prefs_constants import material_specular_shininess_prefs_key
from utilities.prefs_constants import material_specular_brightness_prefs_key
from utilities.prefs_constants import material_specular_finish_prefs_key
from utilities.prefs_constants import povdir_path_prefs_key
from utilities.prefs_constants import dynamicToolTipBendAnglePrecision_prefs_key
from utilities.prefs_constants import dynamicToolTipVdwRadiiInAtomDistance_prefs_key
from utilities.prefs_constants import displayFontPointSize_prefs_key
from utilities.prefs_constants import useSelectedFont_prefs_key
from utilities.prefs_constants import displayFont_prefs_key
from utilities.prefs_constants import keepBondsDuringTransmute_prefs_key
from utilities.prefs_constants import indicateOverlappingAtoms_prefs_key
from utilities.prefs_constants import fogEnabled_prefs_key

# Cursor text prefs.
from utilities.prefs_constants import cursorTextFontSize_prefs_key
from utilities.prefs_constants import cursorTextColor_prefs_key

#global display preferences
from utilities.constants import diDEFAULT ,diTrueCPK, diLINES
from utilities.constants import diBALL, diTUBES, diDNACYLINDER

from utilities.constants import black, white, gray
from widgets.prefs_widgets import connect_doubleSpinBox_with_pref
import collections
# =
# Preferences widgets constants. I suggest that these be moved to another
# file (i.e. prefs_constants.py or another file). Discuss with Bruce. -Mark

# Setting some Qt constants just to make things more sane
CHECKED = Qt.Checked
UNCHECKED = Qt.Unchecked

# Default Plug-in paths for all of the known plugins.  Add more here.  They are
# indexed in the dictionary by the string value preferences key and sub indexed
# by platform.  This was moved here to make it easier to modify later.
# Note: This and other variables like it could be moved into another module and
# imported lazily to save on memory if and when it became useful to do so.
DEFAULT_PLUGIN_PATHS = {
    gromacs_path_prefs_key :
    {
      "win32" : "C:\\GROMACS_3.3.3\\bin\\mdrun.exe",
      "darwin" : "/Applications/GROMACS_3.3.3/bin/mdrun",
      "linux" : "/usr/local/GROMCAS_3.3.3/bin/mdrun"
    },
    cpp_path_prefs_key :
    {
      "win32" : "C:\\GROMACS_3.3.3\\MCPP\\bin\\mcpp.exe",
      "darwin" : "/Applications/GROMACS_3.3.3/mcpp/bin/mcpp",
      "linux" : "/usr/local/GROMACS_3.3.3/mcpp/bin/mcpp"
    },
    rosetta_path_prefs_key :
    {
      "win32" : "C:\\Rosetta\\rosetta.exe",
      "darwin" : "/Users/marksims/Nanorex/Rosetta/rosetta++/rosetta.mactel",
      "linux" : "/usr/local/Rosetta/Rosetta"
    },
    rosetta_dbdir_prefs_key :
    {
      "win32" : "C:\\Rosetta\\rosetta_database",
      "darwin" : "/Users/marksims/Nanorex/Rosetta/Rosetta_database",
      "linux" : "/usr/local/Rosetta/Rosetta_database"
    },
    qutemol_path_prefs_key :
    {
      "win32" : "C:\\Program Files\\Nanorex\\QuteMolX\\QuteMolX.exe",
      "darwin" : "/Applications/Nanorex/QuteMolX 0.5.1/QuteMolX.app",
      "linux" : "/usr/local/Nanorex/QuteMolX 0.5.1/QuteMolX"
    },
    povray_path_prefs_key :
    {
      "win32" :
          "C:\\Program Files\\POV-Ray for Windows v3.6\\bin\\pvengine.exe",
      "darwin" : "/usr/local/bin/pvengine",
      "linux" : "/usr/local/bin/pvengine"
    },
    megapov_path_prefs_key :
    {
      "win32" : "C:\\Program Files\\POV-Ray for Windows v3.6\\bin\\megapov.exe",
      "darwin" : "/usr/local/bin/megapov",
      "linux" : "/usr/local/bin/megapov"
    },
    povdir_path_prefs_key :
    {
      "win32" :
       "C:\\Program Files\\POV-Ray for Windows v3.6\\bin\\megapov.exe",
      "darwin" : "/usr/local/bin/megapov",
      "linux" : "/usr/local/bin/megapov"
    } }

# variable for the value which denotes the variable detail level.  This is
# stored in the database as -1, but changed for use in the combobox
VARIABLE_DETAIL_LEVEL_INDX = 3

# GDS = global display style
from PreferencesDialog import GDS_NAMES, GDS_ICONS, GDS_INDEXES

from PreferencesDialog import HIGH_ORDER_BOND_STYLES

debug_sliders = False # Do not commit as True
DEBUG = True # Do not commit as True
CURSOR_TEXT_KEY = True

def _fullkey(keyprefix, *subkeys): #e this func belongs in preferences.py
    res = keyprefix
    for subkey in subkeys:
        res += "/" + subkey
    return res

def _size_pos_keys( keyprefix):
    return _fullkey(keyprefix, "geometry", "size"), _fullkey(keyprefix, "geometry", "pos")

def _tupleFromQPoint(qpoint):
    return qpoint.x(), qpoint.y()

def _tupleFromQSize(qsize):
    return qsize.width(), qsize.height()

def _get_window_pos_size(win):
    size = _tupleFromQSize( win.size())
    pos = _tupleFromQPoint( win.pos())
    return pos, size

def save_window_pos_size( win, keyprefix): #bruce 050913 removed histmessage arg
    """
    Save the size and position of the given main window, win,
    in the preferences database, using keys based on the given keyprefix,
    which caller ought to reserve for geometry aspects of the main window.
    (#e Someday, maybe save more aspects like dock layout and splitter bar
    positions??)
    """
##    from preferences import prefs_context
##    prefs = prefs_context()
    ksize, kpos = _size_pos_keys( keyprefix)
    pos, size = _get_window_pos_size(win)
    changes = { ksize: size, kpos: pos }
    env.prefs.update( changes) # use update so it only opens/closes dbfile once
    env.history.message("saved window position %r and size %r" % (pos,size))
    return

def load_window_pos_size( win, keyprefix, defaults = None, screen = None): #bruce 050913 removed histmessage arg; 060517 revised
    """
    Load the last-saved size and position of the given main window, win,
    from the preferences database, using keys based on the given keyprefix,
    which caller ought to reserve for geometry aspects of the main window.
    (If no prefs have been stored, return reasonable or given defaults.)
       Then set win's actual position and size (using supplied defaults, and
    limited by supplied screen size, both given as ((pos_x,pos_y),(size_x,size_y)).
    (#e Someday, maybe restore more aspects like dock layout and splitter bar
    positions??)
    """
    if screen is None:
        screen = screen_pos_size()
    ((x0, y0), (w, h)) = screen
    x1 = x0 + w
    y1 = y0 + h

    pos, size = _get_prefs_for_window_pos_size( win, keyprefix, defaults)
    # now use pos and size, within limits set by screen
    px, py = pos
    sx, sy = size
    if sx > w: sx = w
    if sy > h: sy = h
    if px < x0: px = x0
    if py < y0: py = y0
    if px > x1 - sx: px = x1 - sx
    if py > y1 - sy: py = y1 - sy
    env.history.message("restoring last-saved window position %r and size %r" \
                        % ((px, py),(sx, sy)))
    win.resize(sx, sy)
    win.move(px, py)
    return

def _get_prefs_for_window_pos_size( win, keyprefix, defaults = None):
    """
    Load and return the last-saved size and position of the given main window, win,
    from the preferences database, using keys based on the given keyprefix,
    which caller ought to reserve for geometry aspects of the main window.
    (If no prefs have been stored, return reasonable or given defaults.)
    """
    #bruce 060517 split this out of load_window_pos_size
    if defaults is None:
        defaults = _get_window_pos_size(win)
    dpos, dsize = defaults
    px, py = dpos # check correctness of args, even if not used later
    sx, sy = dsize
    import foundation.preferences as preferences
    prefs = preferences.prefs_context()
    ksize, kpos = _size_pos_keys( keyprefix)
    pos = prefs.get(kpos, dpos)
    size = prefs.get(ksize, dsize)
    return pos, size

#def get_pref_or_optval(key, val, optval):
    #"""
    #Return <key>'s value. If <val> is equal to <key>'s value, return <optval>
    #instead.
    #"""
    #if env.prefs[key] == val:
        #return optval
    #else:
        #return env.prefs[key]

class Preferences(PreferencesDialog):
    """
    The Preferences dialog used for accessing and changing user
    preferences.
    """
    pagenameList = [] # List of page names in prefsStackedWidget.

#    def __init__(self, assy):
    def __init__(self):
        QDialog.__init__(self)
        super(Preferences, self).__init__()

        # Some important attrs.
 #       self.glpane = assy.o
 #       self.w = assy.w
 #       self.assy = assy
        self.pagenameList = self.getPagenameList()
        if DEBUG:
            print(self.pagenameList)
        self.changeKey = 0
        # Start of dialog setup.
        self._setupDialog_TopLevelWidgets()
        self._setupPage_General()
        self._setupPage_Graphics_Area()
        self._setupPage_Zoom_Pan_and_Rotate()
        self._setupPage_Rulers()
        self._setupPage_Atoms()
        self._setupPage_Bonds()
        self._setupPage_DNA()
        self._setupPage_DNA_Minor_Groove_Error_Indicator()
        self._setupPage_DNA_Base_Orientation_Indicators()
        self._setupPage_Adjust()
        self._setupPage_Plugins()
        self._setupPage_Undo()
        self._setupPage_Window()
        self._setupPage_Reports()
        self._setupPage_Tooltips()

        # Assign "What's This" text for all widgets.
        #from ne1_ui.prefs.WhatsThisText_for_PreferencesDialog import whatsThis_PreferencesDialog
        from WhatsThisText_for_PreferencesDialog import whatsThis_PreferencesDialog
        whatsThis_PreferencesDialog(self)

        #self._hideOrShowWidgets()
        self.show()
        return
    # End of _init_()


    # PAGE: GENERAL
    def _setupPage_General(self):
        """
        Setup the General page.
        """
        # GROUPBOX: Sponsor logos download permission
        if env.prefs[sponsor_permanent_permission_prefs_key]:
            if env.prefs[sponsor_download_permission_prefs_key]:
                _myID = 1
            else:
                _myID = 2
        else:
            _myID = 0
        self.logo_download_RadioButtonList.setDefaultCheckedId(_myID)
        _checkedButton = self.logo_download_RadioButtonList.getButtonById(_myID)
        _checkedButton.setChecked(True)

        self.logo_download_RadioButtonList.buttonGroup.buttonClicked[int].connect(self.setPrefsLogoDownloadPermissions)

        # GROUPBOX: Build Chunks Settings
        connect_checkbox_with_boolean_pref( self.autobondCheckBox, buildModeAutobondEnabled_prefs_key )
        connect_checkbox_with_boolean_pref( self.hoverHighlightCheckBox, buildModeHighlightingEnabled_prefs_key )
        connect_checkbox_with_boolean_pref( self.waterCheckBox, buildModeWaterEnabled_prefs_key )
        connect_checkbox_with_boolean_pref( self.autoSelectAtomsCheckBox, buildModeSelectAtomsOfDepositedObjEnabled_prefs_key )

        # GROUPBOX: Offset factor for pasting objects
        connect_doubleSpinBox_with_pref(self.pasteOffsetForChunks_doublespinbox,
                                        pasteOffsetScaleFactorForChunks_prefs_key)
        connect_doubleSpinBox_with_pref(self.pasteOffsetForDNA_doublespinbox,
                                        pasteOffsetScaleFactorForDnaObjects_prefs_key)
        return

    def setPrefsLogoDownloadPermissions(self, permission):
        """
        Set the sponsor logos download permissions in the persistent user
        preferences database.

        @param permission: The permission, where:
                        0 = Always ask before downloading
                        1 = Never ask before downloading
                        2 = Never download
        @type  permission: int
        """
        _permanentValue = False
        _downloadValue = True
        if permission == 1:
            _permanentValue = True
            _downloadValue = True

        elif permission == 2:
            _permanentValue = True
            _downloadValue = False

        else:
            _permanentValue = False

        env.prefs[sponsor_permanent_permission_prefs_key] = _permanentValue
        env.prefs[sponsor_download_permission_prefs_key] = _downloadValue
        return

    def setGlobalDisplayStyleAtStartUp(self, junk):
        """
        Slot method for the "Global Display Style at Start-up" combo box in
        the Preferences dialog (and not the combobox in the status bar of
        the main window).

        @param gdsIndexUnused: The current index of the combobox. It is unused.
        @type  gdsIndexUnused: int

        @note: This changes the global display style of the glpane.
        """

        # Get the GDS index from the current combox box index.
        display_style = GDS_INDEXES[self.globalDisplayStyleStartupComboBox.currentIndex()]

        if display_style == env.prefs[startupGlobalDisplayStyle_prefs_key]:
            return

        # set the pref
        env.prefs[startupGlobalDisplayStyle_prefs_key] = display_style

        # Set the current display style in the glpane.
        # (This will be noticed later by chunk.draw of affected chunks.)
#UNCOMMENT LATER
#        self.glpane.setGlobalDisplayStyle(display_style)
#        self.glpane.gl_update()
        return

    # PAGE: GRAPHICS AREA
    def _setupPage_Graphics_Area(self):
        """
        Setup the Graphics Area page
        """

        display_style = env.prefs[ startupGlobalDisplayStyle_prefs_key ]
        self.globalDisplayStyleStartupComboBox.setCurrentIndex(GDS_INDEXES.index(display_style))
        self.globalDisplayStyleStartupComboBox.currentIndexChanged[int].connect(self.setGlobalDisplayStyleAtStartUp)

        # GROUPBOX: Compass display settings
        # Check if the compass is set to display
        if env.prefs[displayCompass_prefs_key]:
            self.display_compass_CheckBox.setCheckState(CHECKED)
        else:
            self.display_compass_CheckBox.setCheckState(UNCHECKED)
        # Call the display_compass function no matter what it know's what to do.
        self.display_compass(env.prefs[displayCompass_prefs_key])
        self.display_compass_CheckBox.toggled[bool].connect(self.display_compass)
        connect_comboBox_with_pref(self.compass_location_ComboBox, compassPosition_prefs_key)
        connect_checkbox_with_boolean_pref(self.display_compass_labels_checkbox, displayCompassLabels_prefs_key)

        # GROUPBOX: Axes
        connect_checkbox_with_boolean_pref(self.display_origin_axis_checkbox, displayOriginAxis_prefs_key)
        connect_checkbox_with_boolean_pref(self.display_pov_axis_checkbox, displayPOVAxis_prefs_key)

        # GROUPBOX: Cursor text settings
        self.set_cursor_text_font_size()
        self.cursor_text_font_size_SpinBox.valueChanged[double].connect(self.set_cursor_text_font_size)
        self.cursor_text_reset_Button.clicked.connect(self.reset_cursor_text_font_size)
        self.cursor_text_color_ComboBox.setColor(env.prefs[cursorTextColor_prefs_key], default = True)
        self.cursor_text_color_ComboBox.editingFinished.connect(self.set_cursor_text_color)

        # GROUPBOX: Other graphics options groupbox
        connect_checkbox_with_boolean_pref(self.display_confirmation_corner_CheckBox, displayConfirmationCorner_prefs_key)
        connect_checkbox_with_boolean_pref(self.anti_aliasing_CheckBox, enableAntiAliasing_prefs_key)
        return

    def set_cursor_text_font_size(self, font_size = -1):
        """
        Slot for cursor text font size doubleSpinBox.  If passed a positive
        number for font_size, it sets the value of the environment pref.  If
        called with a negative number, it sets the spinbox to the environment
        pref.  In either case, it will then determine if the value is equal to
        the default and enable/disable the reset button.
        """
        if font_size >0:
            env.prefs[cursorTextFontSize_prefs_key] = font_size
        else:
            self.cursor_text_font_size_SpinBox.setValue(
                env.prefs[cursorTextFontSize_prefs_key])
        if env.prefs.has_default_value(cursorTextFontSize_prefs_key):
            self.cursor_text_reset_Button.setEnabled(False)
        else:
            self.cursor_text_reset_Button.setEnabled(True)

    def reset_cursor_text_font_size(self, test = 0):
        """
        Slot to reset the cursor text font size.
        """
        if not env.prefs.has_default_value(cursorTextFontSize_prefs_key):
            _tmp = env.prefs.get_default_value(cursorTextFontSize_prefs_key)
            self.cursor_text_font_size_SpinBox.setValue(_tmp)
            env.prefs[cursorTextFontSize_prefs_key] = _tmp
        self.cursor_text_reset_Button.setEnabled(False)
        return

    def set_cursor_text_color(self):
        """
        Slot to set the cursor text color combobox.
        """
        _newColor = self.cursor_text_color_ComboBox.getColor()
        env.prefs[cursorTextColor_prefs_key] = _newColor
        return

    def display_compass(self, val):
        """
        Slot for the Display Compass checkbox, which enables/disables the
        Display Compass Labels checkbox.
        """
        val = not not val
        # Enable or disable the appropriate things
        self.compass_location_ComboBox.setEnabled(val)
        self.compass_location_ComboBox.labelWidget.setEnabled(val)
        self.display_compass_labels_checkbox.setEnabled(val)
        # If the value is different from the saved value, then save the new one.
        # This method is called at startup, so this could be used simply to
        # set the initial state of the
        if val != env.prefs[displayCompass_prefs_key]:
            env.prefs[displayCompass_prefs_key] = val
        return

    #PAGE: ZOOM, PAN, AND ROTATE
    def _setupPage_Zoom_Pan_and_Rotate(self):
        """
        Setup the Zoom, Pan and Rotate page.
        """
        # GROUPBOX: View rotation settings
        connect_checkbox_with_boolean_pref(self.animate_views_CheckBox, animateStandardViews_prefs_key)
        self.view_animation_speed_Slider.setValue(int (env.prefs[animateMaximumTime_prefs_key] * -100))
        self.mouse_rotation_speed_Slider.setValue(int (env.prefs[mouseSpeedDuringRotation_prefs_key] * 100))
        if env.prefs.has_default_value(animateMaximumTime_prefs_key):
            self.view_animation_speed_reset_ToolButton.setEnabled(False)
        if env.prefs.has_default_value(mouseSpeedDuringRotation_prefs_key):
            self.mouse_rotation_speed_reset_ToolButton.setEnabled(False)
        self.view_animation_speed_Slider.sliderReleased.connect(self.set_view_animation_speed)
        self.view_animation_speed_reset_ToolButton.clicked.connect(self.reset_view_animation_speed)
        self.mouse_rotation_speed_Slider.sliderReleased.connect(self.set_mouse_rotation_speed)
        self.mouse_rotation_speed_reset_ToolButton.clicked.connect(self.reset_mouse_rotation_speed)

        # GROUPBOX: Mouse wheel zoom settings
        connect_comboBox_with_pref(self.zoom_directon_ComboBox, mouseWheelDirection_prefs_key)
        connect_comboBox_with_pref(self.zoom_in_center_ComboBox, zoomInAboutScreenCenter_prefs_key)
        connect_comboBox_with_pref(self.zoom_out_center_ComboBox, zoomOutAboutScreenCenter_prefs_key)
        connect_doubleSpinBox_with_pref(self.hover_highlighting_timeout_SpinBox, mouseWheelTimeoutInterval_prefs_key)
        return

    def set_view_animation_speed(self):
        """
        Slot for setting the view animation speed slider.
        """
        env.prefs[animateMaximumTime_prefs_key] = \
           self.view_animation_speed_Slider.value() / -100.0
        self.view_animation_speed_reset_ToolButton.setEnabled(True)
        return

    def reset_view_animation_speed(self):
        """
        Slot for resetting the view animation speed slider through the
        view animation speed reset toolbutton.
        """
        env.prefs.restore_defaults([animateMaximumTime_prefs_key])
        self.view_animation_speed_Slider.setValue(int (env.prefs[animateMaximumTime_prefs_key] * -100))
        self.view_animation_speed_reset_ToolButton.setEnabled(False)

    def set_mouse_rotation_speed(self):
        """
        Slot for setting the mouse rotation speed slider.
        """
        env.prefs[mouseSpeedDuringRotation_prefs_key] = \
           self.mouse_rotation_speed_Slider.value() / 100.0
        self.mouse_rotation_speed_reset_ToolButton.setEnabled(True)
        return

    def reset_mouse_rotation_speed(self):
        """
        Slot for resetting the mouse rotation speed slider through the
        mouse rotation speed reset toolbutton.
        """
        env.prefs.restore_defaults([mouseSpeedDuringRotation_prefs_key])
        self.mouse_rotation_speed_Slider.setValue(int (env.prefs[mouseSpeedDuringRotation_prefs_key] * 100))
        self.mouse_rotation_speed_reset_ToolButton.setEnabled(False)

    # PAGE: RULERS

    def _setupPage_Rulers(self):
        """
        Setup the "Rulers" page.
        """
        # GROUPBOX: Rulers
        if env.prefs[displayVertRuler_prefs_key] and env.prefs[displayHorzRuler_prefs_key]:
            self.display_rulers_ComboBox.setCurrentIndex(0)
        elif not env.prefs[displayHorzRuler_prefs_key]:
            self.display_rulers_ComboBox.setCurrentIndex(1)
        elif not env.prefs[displayVertRuler_prefs_key]:
            self.display_rulers_ComboBox.setCurrentIndex(2)

        self.display_rulers_ComboBox.currentIndexChanged[int].connect(self.set_ruler_display)
        connect_comboBox_with_pref(self.origin_rulers_ComboBox, rulerPosition_prefs_key)
        self.ruler_color_ColorComboBox.setColor(env.prefs[rulerColor_prefs_key], default = True)
        self.ruler_color_ColorComboBox.editingFinished.connect(self.set_ruler_color)
        self.ruler_opacity_SpinBox.setValue(int(env.prefs[rulerOpacity_prefs_key] * 100))
        self.ruler_opacity_SpinBox.valueChanged[int].connect(self.set_ruler_opacity)
        connect_checkbox_with_boolean_pref(self.show_rulers_in_perspective_view_CheckBox,\
                                           showRulersInPerspectiveView_prefs_key)
        return

    def set_ruler_display(self, indx):
        """
        Slot for setting which rulers should be displayed.
        indx == 0: verticle and horizontal are displayed.
        indx == 1: Just verticle is displayed
        indx == other (normally 2): Just horizontal is displayed
        """
        if indx == 0:
            env.prefs[displayVertRuler_prefs_key] = True
            env.prefs[displayHorzRuler_prefs_key] = True
        elif indx == 1:
            env.prefs[displayVertRuler_prefs_key] = True
            env.prefs[displayHorzRuler_prefs_key] = False
        else:
            env.prefs[displayVertRuler_prefs_key] = False
            env.prefs[displayHorzRuler_prefs_key] = True
        return

    def set_ruler_color(self):
        """
        Slot to set the ruler color from the ruler color colorcombobox.
        """
        _newColor = self.ruler_color_ColorComboBox.getColor()
        env.prefs[rulerColor_prefs_key] = _newColor
        return

    def set_ruler_opacity(self, opacity):
        """
        Change the ruler opacity.
        """
        env.prefs[rulerOpacity_prefs_key] = opacity * 0.01
        return


    # PAGE: ATOMS ============================================================
    def _setupPage_Atoms(self):
        """
        Setup the "Atoms" page.
        """

        # GROUPBOX: Colors
        # "Change Element Colors" button.
        self.change_element_colors_PushButton.clicked.connect(self.change_element_colors)

        # GROUPBOX: Colors sub
        self.atom_highlighting_ColorComboBox.setColor(env.prefs[atomHighlightColor_prefs_key], default = True)
        self.atom_highlighting_ColorComboBox.editingFinished.connect(self.set_atom_highlighting_color)
        self.bondpoint_highlighting_ColorComboBox.setColor(env.prefs[bondpointHighlightColor_prefs_key], default = True)
        self.bondpoint_highlighting_ColorComboBox.editingFinished.connect(self.set_bondpoint_highlighting_color)
        self.bondpoint_hotspots_ColorComboBox.setColor(env.prefs[bondpointHotspotColor_prefs_key], default = True)
        self.bondpoint_hotspots_ColorComboBox.editingFinished.connect(self.set_bondpoint_hotspots_color)
        self.restore_element_colors_PushButton.clicked.connect(self.reset_atom_and_bondpoint_colors)

        #GROUPBOX: Miscellaneous atom options
        lod = env.prefs[levelOfDetail_prefs_key]
        if lod == -1:
            lod = VARIABLE_DETAIL_LEVEL_INDX
        self.atoms_detail_level_ComboBox.setCurrentIndex(lod)
        self.atoms_detail_level_ComboBox.currentIndexChanged[int].connect(self.set_level_of_detail)
        self.set_ball_and_stick_atom_scale(env.prefs[diBALL_AtomRadius_prefs_key])
        self.set_CPK_atom_scale(env.prefs[cpkScaleFactor_prefs_key])
        self.ball_and_stick_atom_scale_SpinBox.setValue(round(env.prefs[diBALL_AtomRadius_prefs_key] * 100.0))
        self.CPK_atom_scale_doubleSpinBox.setValue(env.prefs[cpkScaleFactor_prefs_key])
        self.ball_and_stick_atom_scale_SpinBox.valueChanged[int].connect(self.set_ball_and_stick_atom_scale)
        self.CPK_atom_scale_doubleSpinBox.valueChanged[double].connect(self.set_CPK_atom_scale)
        self.ball_and_stick_atom_scale_reset_ToolButton.clicked.connect(self.reset_ball_and_stick_atom_scale)
        self.CPK_atom_scale_reset_ToolButton.clicked.connect(self.reset_CPK_atom_scale)
        connect_checkbox_with_boolean_pref(self.overlapping_atom_indicators_CheckBox,
                                           indicateOverlappingAtoms_prefs_key)
        connect_checkbox_with_boolean_pref(self.force_to_keep_bonds_during_transmute_CheckBox,
                                           keepBondsDuringTransmute_prefs_key)
        return

    def set_atom_highlighting_color(self):
        """
        Slot for the atom highlighting colorcombobox.
        """
        _newColor = self.atom_highlighting_ColorComboBox.getColor()
        env.prefs[atomHighlightColor_prefs_key] = _newColor
        return

    def set_bondpoint_highlighting_color(self):
        """
        Slot for the bondpoint highlighting colorcombobox.
        """
        _newColor = self.bondpoint_highlighting_ColorComboBox.getColor()
        env.prefs[bondpointHighlightColor_prefs_key] = _newColor
        return

    def set_bondpoint_hotspots_color(self):
        """
        Slot for the bondpoint hotspots colorcombobox.
        """
        _newColor = self.bondpoint_hotspots_ColorComboBox.getColor()
        env.prefs[bondpointHotspotColor_prefs_key] = _newColor
        return

    def reset_atom_and_bondpoint_colors(self):
        """
        Slot for the restore element colors pushbutton.  This will reset the
        atom highlighting, bondpoint highlighting, and bondpoint hotspots
        colorcomboboxes
        """
        env.prefs.restore_defaults([atomHighlightColor_prefs_key,
                                    bondpointHighlightColor_prefs_key,
                                    bondpointHotspotColor_prefs_key])
        self.atom_highlighting_ColorComboBox.setColor(env.prefs.get_default_value(atomHighlightColor_prefs_key))
        self.bondpoint_highlighting_ColorComboBox.setColor(env.prefs.get_default_value(bondpointHighlightColor_prefs_key))
        self.bondpoint_hotspots_ColorComboBox.setColor(env.prefs.get_default_value(bondpointHotspotColor_prefs_key))
        return

    def change_element_colors(self):
        """
        Display the Element Color Settings Dialog.
        Note: This dialog has not been converted to using PM_Widgets
        """
        # Since the prefs dialog is modal, the element color settings dialog must be modal.
        self.w.showElementColorSettings(self)
        return

    def set_level_of_detail(self, level_of_detail_item): #bruce 060215 revised this
        """
        Change the level of detail, where <level_of_detail_item> is a value
        between 0 and 3 where:
            - 0 = low
            - 1 = medium
            - 2 = high
            - 3 = variable (based on number of atoms in the part)

        @note: the prefs db value for 'variable' is -1, to allow for higher LOD
               levels in the future.
        """
        lod = level_of_detail_item
        if level_of_detail_item == VARIABLE_DETAIL_LEVEL_INDX:
            lod = -1
        env.prefs[levelOfDetail_prefs_key] = lod
#        self.glpane.gl_update()
        # the redraw this causes will (as of tonight) always recompute the correct drawLevel (in Part._recompute_drawLevel),
        # and chunks will invalidate their display lists as needed to accomodate the change. [bruce 060215]
        return

    def set_ball_and_stick_atom_scale(self, value):
        """
        Slot for ball_and_stick_atom_scale_SpinBox.  Also enables and disables
        the reset button.
        """
        if env.prefs[diBALL_AtomRadius_prefs_key] != value:
            env.prefs[diBALL_AtomRadius_prefs_key] = round(float(value) / 100.0, 2)
        if env.prefs.has_default_value(diBALL_AtomRadius_prefs_key):
            self.ball_and_stick_atom_scale_reset_ToolButton.setEnabled(False)
        else:
            self.ball_and_stick_atom_scale_reset_ToolButton.setEnabled(True)
        return

    def set_CPK_atom_scale(self, value):
        """
        Slot for CPK_atom_scale_doubleSpinBox.  Also enables and disables the
        reset button.
        """
        if env.prefs[cpkScaleFactor_prefs_key] != value:
            env.prefs[cpkScaleFactor_prefs_key] = value
        # direct comparison with has_default_value didn't work on this level
        # of precision
        if round(env.prefs.get_default_value(cpkScaleFactor_prefs_key), 3 ) \
           == round(value, 3):
            self.CPK_atom_scale_reset_ToolButton.setEnabled(False)
        else:
            self.CPK_atom_scale_reset_ToolButton.setEnabled(True)
        return

    def reset_ball_and_stick_atom_scale(self):
        """
        Slot for ball_and_stick_atom_scale_reset_ToolButton.
        """
        _resetValue = env.prefs.get_default_value(diBALL_AtomRadius_prefs_key)
        _resetValue = int((_resetValue + .005) * 100)
        self.set_ball_and_stick_atom_scale(_resetValue)
        self.ball_and_stick_atom_scale_SpinBox.setValue(_resetValue,
                                                              blockSignals = True)
        return

    def reset_CPK_atom_scale(self):
        """
        Slot for CPK_atom_scale_reset_ToolButton.
        """
        _resetValue = env.prefs.get_default_value(cpkScaleFactor_prefs_key)
        self.set_CPK_atom_scale(_resetValue)
        self.CPK_atom_scale_doubleSpinBox.setValue(_resetValue,
                                                   blockSignals = True)
        return

    # PAGE: BONDS ============================================================

    def _setupPage_Bonds(self):
        """
        Setup the "Bonds" page.
        """
        # GROUPBOX Colors
        self.bond_highlighting_ColorComboBox.setColor(env.prefs[bondHighlightColor_prefs_key])
        self.bond_highlighting_ColorComboBox.editingFinished.connect(self.set_bond_highlighting_color)
        self.ball_and_stick_cylinder_ColorComboBox.setColor(env.prefs[diBALL_bondcolor_prefs_key])
        self.ball_and_stick_cylinder_ColorComboBox.editingFinished.connect(self.set_ball_and_stick_cylinder_color)
        self.bond_stretch_ColorComboBox.setColor(env.prefs[bondStretchColor_prefs_key])
        self.bond_stretch_ColorComboBox.editingFinished.connect(self.set_bond_stretch_color)
        self.vane_ribbon_ColorComboBox.setColor(env.prefs[bondVaneColor_prefs_key])
        self.vane_ribbon_ColorComboBox.editingFinished.connect(self.set_vane_ribbon_color)
        self.restore_bond_colors_PushButton.clicked.connect(self.reset_default_colors)
        # GROUPBOX Miscellaneous bond settings
        self.set_ball_and_stick_bond_scale(env.prefs[diBALL_BondCylinderRadius_prefs_key] * 100)
        self.set_bond_line_thickness(env.prefs[linesDisplayModeThickness_prefs_key])
        self.ball_and_stick_bond_scale_SpinBox.setValue(round(env.prefs[diBALL_BondCylinderRadius_prefs_key] * 100))
        self.bond_line_thickness_SpinBox.setValue(env.prefs[linesDisplayModeThickness_prefs_key])
        self.ball_and_stick_bond_scale_SpinBox.valueChanged[int].connect(self.set_ball_and_stick_bond_scale)
        self.bond_line_thickness_SpinBox.valueChanged[int].connect(self.set_bond_line_thickness)
        # GROUPBOX: High order bonds (sub box)
        if env.prefs[pibondStyle_prefs_key] == "multicyl":
            _myID = 0
        elif env.prefs[pibondStyle_prefs_key] == "vane":
            _myID = 1
        else:
            _myID = 2
        _checkedButton = self.high_order_bonds_RadioButtonList.getButtonById(_myID)
        _checkedButton.setChecked(True)
        self.high_order_bonds_RadioButtonList.buttonGroup.buttonClicked[int].connect(self.set_high_order_bonds)
        connect_checkbox_with_boolean_pref(self.show_bond_type_letters_CheckBox, pibondLetters_prefs_key)
        connect_checkbox_with_boolean_pref(self.show_valence_errors_CheckBox, showValenceErrors_prefs_key)
        connect_checkbox_with_boolean_pref(self.show_bond_stretch_indicators_CheckBox, showBondStretchIndicators_prefs_key)
        return

    def set_bond_highlighting_color(self):
        """
        Slot for bond_highlighting_ColorComboBox
        """
        _newColor = self.bond_highlighting_ColorComboBox.getColor()
        env.prefs[bondHighlightColor_prefs_key] = _newColor
        return

    def set_ball_and_stick_cylinder_color(self):
        """
        Slot for ball_and_stick_cylinder_ColorComboBox
        """
        _newColor = self.ball_and_stick_cylinder_ColorComboBox.getColor()
        env.prefs[diBALL_bondcolor_prefs_key] = _newColor
        return

    def set_bond_stretch_color(self):
        """
        Slot for bond_stretch_ColorComboBox
        """
        _newColor = self.bond_stretch_ColorComboBox.getColor()
        env.prefs[bondStretchColor_prefs_key] = _newColor
        return

    def set_vane_ribbon_color(self):
        """
        Slot for vane_ribbon_ColorComboBox
        """
        _newColor = self.vane_ribbon_ColorComboBox.getColor()
        env.prefs[bondVaneColor_prefs_key] = _newColor
        return

    def reset_default_colors(self):
        """
        Slot for restore_bond_colors_PushButton.  This will reset the preference
        keys and their respective colorcomboboxes back to the database default
        values
        """
        env.prefs.restore_defaults([bondHighlightColor_prefs_key,
                                    bondStretchColor_prefs_key,
                                    bondVaneColor_prefs_key,
                                    diBALL_bondcolor_prefs_key])
        self.bond_highlighting_ColorComboBox.setColor(env.prefs.get_default_value(bondHighlightColor_prefs_key))
        self.ball_and_stick_cylinder_ColorComboBox.setColor(env.prefs.get_default_value(diBALL_bondcolor_prefs_key))
        self.bond_stretch_ColorComboBox.setColor(env.prefs.get_default_value(bondStretchColor_prefs_key))
        self.vane_ribbon_ColorComboBox.setColor(env.prefs.get_default_value(bondVaneColor_prefs_key))
        return

    def set_ball_and_stick_bond_scale(self, value):
        """
        Slot for ball_and_stick_bond_scale_SpinBox
        """
        if env.prefs[diBALL_BondCylinderRadius_prefs_key] != value:
            env.prefs[diBALL_BondCylinderRadius_prefs_key] = round(float(value) / 100.0, 2)
        #if env.prefs.has_default_value(diBALL_BondCylinderRadius_prefs_key):
            #self.ball_and_stick_atom_scale_reset_ToolButton.setEnabled(False)
        #else:
            #self.ball_and_stick_atom_scale_reset_ToolButton.setEnabled(True)
        return

    def set_bond_line_thickness(self, value):
        """
        Slot for bond_line_thickness_SpinBox
        """
        if env.prefs[linesDisplayModeThickness_prefs_key] != value:
            env.prefs[linesDisplayModeThickness_prefs_key] = value
        #if env.prefs.has_default_value(linesDisplayModeThickness_prefs_key):
            #self.ball_and_stick_atom_scale_reset_ToolButton.setEnabled(False)
        #else:
            #self.ball_and_stick_atom_scale_reset_ToolButton.setEnabled(True)
        return

    def set_high_order_bonds(self, value):
        """
        Slot for high_order_bonds_RadioButtonList
        """
        env.prefs[pibondStyle_prefs_key] = HIGH_ORDER_BOND_STYLES[value][3]
        return

    # PAGE: DNA ==============================================================
    def _setupPage_DNA(self):
        """
        Setup the "DNA" page.
        """
        # GROUPBOX: DNA default values
        # Uncomment next line when a DB Pref is made for it.
        #connect_comboBox_with_pref(self.conformation_ComboBox, <SOME_VALUE>)

        connect_doubleSpinBox_with_pref(self.bases_per_turn_DoubleSpinBox,
                                        bdnaBasesPerTurn_prefs_key)
        connect_doubleSpinBox_with_pref(self.rise_DoubleSpinBox, bdnaRise_prefs_key)
        self.strand1_ColorComboBox.setColor(env.prefs[dnaDefaultStrand1Color_prefs_key])
        self.strand1_ColorComboBox.editingFinished.connect(self.set_strand1_color)
        self.strand2_ColorComboBox.setColor(env.prefs[dnaDefaultStrand2Color_prefs_key])
        self.strand1_ColorComboBox.editingFinished.connect(self.set_strand2_color)
        self.segment_ColorComboBox.setColor(env.prefs[dnaDefaultSegmentColor_prefs_key])
        self.segment_ColorComboBox.editingFinished.connect(self.set_segment_color)
        self.restore_DNA_colors_PushButton.clicked.connect(self.reset_DNA_colors)
        # GROUPBOX: Strand arrowhead display options
        connect_checkbox_with_boolean_pref(self.show_arrows_on_backbones_CheckBox,
                                           arrowsOnBackBones_prefs_key)
        connect_checkbox_with_boolean_pref(self.show_arrows_on_3prime_ends_CheckBox,
                                           arrowsOnThreePrimeEnds_prefs_key)
        connect_checkbox_with_boolean_pref(self.show_arrows_on_5prime_ends_CheckBox,
                                           arrowsOnFivePrimeEnds_prefs_key)
        self.three_prime_end_custom_ColorComboBox.setColor(env.prefs[dnaStrandThreePrimeArrowheadsCustomColor_prefs_key])
        self.three_prime_end_custom_ColorComboBox.editingFinished.connect(self.set_three_prime_end_color)
        self.five_prime_end_custom_ColorComboBox.setColor(env.prefs[dnaStrandFivePrimeArrowheadsCustomColor_prefs_key])
        self.five_prime_end_custom_ColorComboBox.editingFinished.connect(self.set_five_prime_end_color)
        return

    def set_strand1_color(self):
        """
        Slot for strand1_ColorComboBox
        """
        _newColor = self.strand1_ColorComboBox.getColor()
        env.prefs[dnaDefaultStrand1Color_prefs_key] = _newColor
        return

    def set_strand2_color(self):
        """
        Slot for strand2_ColorComboBox
        """
        _newColor = self.strand2_ColorComboBox.getColor()
        env.prefs[dnaDefaultStrand2Color_prefs_key] = _newColor
        return

    def set_segment_color(self):
        """
        Slot for segment_ColorComboBox
        """
        _newColor = self.segment_ColorComboBox.getColor()
        env.prefs[dnaDefaultSegmentColor_prefs_key] = _newColor
        return

    def reset_DNA_colors(self):
        """
        Slot for restore_DNA_colors_PushButton
        """
        env.prefs.restore_defaults([dnaDefaultStrand1Color_prefs_key,
                                    dnaDefaultStrand2Color_prefs_key,
                                    dnaDefaultSegmentColor_prefs_key])
        self.strand1_ColorComboBox.setColor(env.prefs.get_default_value(dnaDefaultStrand1Color_prefs_key))
        self.strand2_ColorComboBox.setColor(env.prefs.get_default_value(dnaDefaultStrand2Color_prefs_key))
        self.segment_ColorComboBox.setColor(env.prefs.get_default_value(dnaDefaultSegmentColor_prefs_key))
        return

    def set_three_prime_end_color(self):
        """
        Slot for three_prime_end_custom_ColorComboBox
        """
        _newColor = self.three_prime_end_custom_ColorComboBox.getColor()
        env.prefs[dnaStrandThreePrimeArrowheadsCustomColor_prefs_key] = _newColor
        return

    def set_five_prime_end_color(self):
        """
        Slot for ifive_prime_end_custom_ColorComboBox
        """
        _newColor = self.five_prime_end_custom_ColorComboBox.getColor()
        env.prefs[dnaStrandFivePrimeArrowheadsCustomColor_prefs_key] = _newColor
        return

    # PAGE: DNA MINOR GROOVE ERROR INDICATOR
    def _setupPage_DNA_Minor_Groove_Error_Indicator(self):
        """
        Setup the "DNA Minor_Groove Error Indicator" page.
        """
        self.set_DNA_minor_groove_error_indicator_status()
        self.minor_groove_error_indicatiors_CheckBox.toggled[bool].connect(self.set_DNA_minor_groove_error_indicator_status)
        # GROUPBOX: connect_doubleSpinBox_with_pref
        connect_spinBox_with_pref(self.minor_groove_error_minimum_angle_SpinBox,
                                  dnaMinMinorGrooveAngle_prefs_key)
        connect_spinBox_with_pref(self.minor_groove_error_maximum_angle_SpinBox,
                                  dnaMaxMinorGrooveAngle_prefs_key)
        self.minor_groove_error_color_ColorComboBox.setColor(env.prefs[dnaMinorGrooveErrorIndicatorColor_prefs_key])
        self.minor_groove_error_color_ColorComboBox.editingFinished.connect(self.set_minor_groove_error_color)
        self.minor_groove_error_reset_PushButton.clicked.connect(self.reset_minor_groove_error_prefs)
        return

    def set_DNA_minor_groove_error_indicator_status(self, status = None):
        """
        Slot for minor_groove_error_indicatiors_CheckBox.  This also
        enables/disables the associated groupbox and it's child widgets.
        """
        if (status == None and env.prefs[dnaDisplayMinorGrooveErrorIndicators_prefs_key]) \
           or status:
            self.minor_groove_error_parameters_GroupBox.setEnabled(True)
            self.minor_groove_error_indicatiors_CheckBox.setCheckState(CHECKED)
            env.prefs[dnaDisplayMinorGrooveErrorIndicators_prefs_key] = True
        else:
            self.minor_groove_error_parameters_GroupBox.setEnabled(False)
            self.minor_groove_error_indicatiors_CheckBox.setCheckState(UNCHECKED)
            env.prefs[dnaDisplayMinorGrooveErrorIndicators_prefs_key] = False
        return

    def set_minor_groove_error_color(self):
        """
        Slot for minor_groove_error_color_ColorComboBox
        """
        _newColor = self.minor_groove_error_color_ColorComboBox.getColor()
        env.prefs[dnaMinorGrooveErrorIndicatorColor_prefs_key] = _newColor
        return

    def reset_minor_groove_error_prefs(self):
        """
        Slot for minor_groove_error_reset_PushButton.  This is a reset button
        for the widgets in the groupbox and their associated attributes.
        """
        self.minor_groove_error_color_ColorComboBox.setColor(env.prefs.get_default_value(dnaMinorGrooveErrorIndicatorColor_prefs_key))
        self.minor_groove_error_minimum_angle_SpinBox.setValue(env.prefs.get_default_value(dnaMinMinorGrooveAngle_prefs_key))
        self.minor_groove_error_maximum_angle_SpinBox.setValue(env.prefs.get_default_value(dnaMaxMinorGrooveAngle_prefs_key))
        env.prefs.restore_defaults([dnaMinorGrooveErrorIndicatorColor_prefs_key,
                                    dnaMinMinorGrooveAngle_prefs_key,
                                    dnaMaxMinorGrooveAngle_prefs_key])
        return

    # PAGE: DNA BASE ORIENTATION INDICATORS
    def _setupPage_DNA_Base_Orientation_Indicators(self):
        self.set_DNA_base_orientation_indicator_status()
        self.base_orientation_indicatiors_CheckBox.toggled[bool].connect(self.set_DNA_base_orientation_indicator_status)
        #GROUPBOX: Base orientation indicator parameters
        connect_comboBox_with_pref(self.plane_normal_ComboBox,
                                   dnaBaseIndicatorsPlaneNormal_prefs_key)
        self.indicators_color_ColorComboBox.setColor(env.prefs[dnaBaseIndicatorsColor_prefs_key])
        self.indicators_color_ColorComboBox.editingFinished.connect(self.set_indicators_color)
        self.inverse_indicators_color_ColorComboBox.setColor(env.prefs[dnaBaseInvIndicatorsColor_prefs_key])
        self.inverse_indicators_color_ColorComboBox.editingFinished.connect(self.set_inverse_indicators_color)
        connect_checkbox_with_boolean_pref(self.enable_inverse_indicatiors_CheckBox,
                                           dnaBaseInvIndicatorsEnabled_prefs_key)
        connect_doubleSpinBox_with_pref(self.angle_threshold_DoubleSpinBox,
                                        dnaBaseIndicatorsAngle_prefs_key)
        connect_spinBox_with_pref(self.terminal_base_distance_SpinBox,
                                  dnaBaseIndicatorsDistance_prefs_key)
        return

    def set_DNA_base_orientation_indicator_status(self, status = None):
        """
        Slot for base_orientation_indicatiors_CheckBox.  Also, this will
        enable/disable the associated groupbox and it's child widgets.
        """
        if (status == None and env.prefs[dnaBaseIndicatorsEnabled_prefs_key]) \
           or status:
            self.base_orientation_GroupBox.setEnabled(True)
            self.base_orientation_indicatiors_CheckBox.setCheckState(CHECKED)
            env.prefs[dnaBaseIndicatorsEnabled_prefs_key] = True
        else:
            self.base_orientation_GroupBox.setEnabled(False)
            self.base_orientation_indicatiors_CheckBox.setCheckState(UNCHECKED)
            env.prefs[dnaBaseIndicatorsEnabled_prefs_key] = False
        return

    def set_indicators_color(self):
        """
        Slot for indicators_color_ColorComboBox
        """
        _newColor = self.indicators_color_ColorComboBox.getColor()
        env.prefs[dnaBaseIndicatorsColor_prefs_key] = _newColor
        return

    def set_inverse_indicators_color(self):
        """
        Slot for inverse_indicators_color_ColorComboBox
        """
        _newColor = self.inverse_indicators_color_ColorComboBox.getColor()
        env.prefs[dnaBaseInvIndicatorsColor_prefs_key] = _newColor
        return

    # PAGE: ADJUST
    def _setupPage_Adjust(self):
        """
        Setup the "Adjust" page.
        """
        # GROUPBOX: Adjust physics engine
        connect_comboBox_with_pref(self.physics_engine_choice_ComboBox,
                                   Adjust_minimizationEngine_prefs_key)
        connect_checkbox_with_boolean_pref(self.enable_electrostatics_CheckBox,
            electrostaticsForDnaDuringAdjust_prefs_key)
        # GROUPBOX: Pysics engine animation options
        self.watch_motion_in_realtime_CheckBox.setChecked(
            env.prefs[Adjust_watchRealtimeMinimization_prefs_key])
        self.set_and_enable_realtime(
            env.prefs[Adjust_watchRealtimeMinimization_prefs_key])
        self.watch_motion_in_realtime_CheckBox.toggled[bool].connect(self.set_and_enable_realtime)
        self.constant_animation_update_RadioButton.setChecked(True)
        # GROUPBOX: Convergence criteria
        connect_doubleSpinBox_with_pref(self.endRMS_DoubleSpinBox,
                                        Adjust_endRMS_prefs_key)
        connect_doubleSpinBox_with_pref(self.endmax_DoubleSpinBox,
                                        Adjust_endMax_prefs_key)
        connect_doubleSpinBox_with_pref(self.cutoverRMS_DoubleSpinBox,
                                        Adjust_cutoverRMS_prefs_key)
        connect_doubleSpinBox_with_pref(self.cutoverMax_DoubleSpinBox,
                                        Adjust_cutoverMax_prefs_key)
        self.endRMS_DoubleSpinBox.setSpecialValueText("Automatic")
        self.endmax_DoubleSpinBox.setSpecialValueText("Automatic")
        self.cutoverRMS_DoubleSpinBox.setSpecialValueText("Automatic")
        self.cutoverMax_DoubleSpinBox.setSpecialValueText("Automatic")
        return

    def set_and_enable_realtime(self, state):
        if env.prefs[Adjust_watchRealtimeMinimization_prefs_key] != state:
            env.prefs[Adjust_watchRealtimeMinimization_prefs_key] = state
        self.animation_detail_level_RadioButtonList.setEnabled(state)
        return

    # PAGE: PLUGINS ==========================================================
    def _setupPage_Plugins(self):
        """
        Setup the "Plug-ins" page.
        """
        # GROUPBOX: Location of executables
        pluginList = [ "QuteMolX", \
                       "POV-Ray", \
                       "MegaPOV", \
                       "POV include dir", \
                       "GROMACS", \
                       "cpp",
                       "Rosetta",
                       "Rosetta DB"]

        # signal-slot connections.
        for name in pluginList:
            _pluginFunctionName = "".join([ x for x in name.lower().replace(" ","_") \
                                              if (x in string.ascii_letters or\
                                                  x in string.digits \
                                                  or x == "_") ])
            _fname = "enable_%s" % _pluginFunctionName
            if hasattr(self, _fname):
                fcall = getattr(self, _fname)
                if isinstance(fcall, collections.Callable):
                    if DEBUG:
                        print("method defined: %s" % _fname)
                    self.checkboxes[name].toggled[bool].connect(\
                                                 fcall)
                else:
                    print("Attribute %s exists, but is not a callable method.")
            else:
                if DEBUG:
                    print("method missing: %s" % _fname)
            #_fname = "set_%s_path" % _pluginFunctionName
            #if hasattr(self, _fname):
                #fcall = getattr(self, _fname)
                #if callable(fcall):
                    #if DEBUG:
                        #print "method defined: %s" % _fname
                    #self.connect(self.choosers[name].lineEdit,\
                                               #SIGNAL("edtingFinished()"), \
                                               #fcall)
                #else:
                    #print "Attribute %s exists, but is not a callable method."
            #else:
                #if DEBUG:
                    #print "method missing: %s" % _fname

        self.choosers["QuteMolX"].lineEdit.editingFinished.connect(self.set_qutemolx_path)
        self.choosers["POV-Ray"].lineEdit.editingFinished.connect(self.set_povray_path)
        self.choosers["MegaPOV"].lineEdit.editingFinished.connect(self.set_megapov_path)
        self.choosers["POV include dir"].lineEdit.editingFinished.connect(self.set_pov_include_dir)
        self.choosers["GROMACS"].lineEdit.editingFinished.connect(self.set_gromacs_path)
        self.choosers["cpp"].lineEdit.editingFinished.connect(self.set_cpp_path)
        self.choosers["Rosetta"].lineEdit.editingFinished.connect(self.set_rosetta_path)
        self.choosers["Rosetta DB"].lineEdit.editingFinished.connect(self.set_rosetta_db_path)
        return


    def _hideOrShowWidgets(self):
        """
        Permanently hides some widgets in the Preferences dialog.
        This provides an easy and convenient way of hiding widgets that have
        been added but not fully implemented. It is also possible to
        show hidden widgets that have a debug pref set to enable them.
        """
        gms_and_esp_widgetList = [self.nanohive_lbl,
                                  self.nanohive_checkbox,
                                  self.nanohive_path_lineedit,
                                  self.nanohive_choose_btn,
                                  self.gamess_checkbox,
                                  self.gamess_lbl,
                                  self.gamess_path_lineedit,
                                  self.gamess_choose_btn]

        for widget in gms_and_esp_widgetList:
            if debug_pref("Show GAMESS and ESP Image UI options",
                          Choice_boolean_False,
                          prefs_key = True):
                widget.show()
            else:
                widget.hide()

        # NanoVision-1
        nv1_widgetList = [self.nv1_checkbox,
                          self.nv1_label,
                          self.nv1_path_lineedit,
                          self.nv1_choose_btn]

        for widget in nv1_widgetList:
            widget.hide()

        # Rosetta
        rosetta_widgetList = [self.rosetta_checkbox,
                              self.rosetta_label,
                              self.rosetta_path_lineedit,
                              self.rosetta_choose_btn,
                              self.rosetta_db_checkbox,
                              self.rosetta_db_label,
                              self.rosetta_db_path_lineedit,
                              self.rosetta_db_choose_btn]

        from utilities.GlobalPreferences import ENABLE_PROTEINS
        for widget in rosetta_widgetList:
            if ENABLE_PROTEINS:
                widget.show()
            else:
                widget.hide()
        return


    ########## Slot methods for "Plug-ins" page widgets ################

    # GROMACS slots #######################################

    def set_gromacs_path(self):
        """
        Slot for GROMACS path line editor.
        """
        setPath = str_or_unicode(self.choosers["GROMACS"].text)
        env.prefs[gromacs_path_prefs_key] = setPath
        prefs = preferences.prefs_context()
        prefs[gromacs_path_prefs_key] = setPath
        return setPath

    def enable_gromacs(self, enable = True):
        """
        If True, GROMACS path is set in Preferences>Plug-ins

        @param enable: Is the path set?
        @type  enable: bool
        """

        state = self.checkboxes["GROMACS"].checkState()
        if enable:
            if (state != CHECKED):
                self.checkboxes["GROMACS"].setCheckState(CHECKED)
            self.choosers["GROMACS"].setEnabled(True)
            env.prefs[gromacs_enabled_prefs_key] = True

            # Sets the GROMACS (executable) path to the standard location, if it exists.
            if not env.prefs[gromacs_path_prefs_key]:
                _tmppaths = DEFAULT_PLUGIN_PATHS[gromacs_path_prefs_key]
                env.prefs[gromacs_path_prefs_key] = get_default_plugin_path( \
                    _tmppaths["win32"], _tmppaths["darwin"], _tmppaths["linux"])

            self.choosers["GROMACS"].setText(env.prefs[gromacs_path_prefs_key])

        else:
            if (state != UNCHECKED):
                self.checkboxes["GROMACS"].setCheckState(UNCHECKED)
            self.choosers["GROMACS"].setEnabled(False)
            #self.gromacs_path_lineedit.setText("")
            #env.prefs[gromacs_path_prefs_key] = ''
            env.prefs[gromacs_enabled_prefs_key] = False

    # cpp slots #######################################

    def set_cpp_path(self):
        """
        Slot for cpp path line editor.
        """
        setPath = str_or_unicode(self.choosers["cpp"].text)
        env.prefs[cpp_path_prefs_key] = setPath
        prefs = preferences.prefs_context()
        prefs[cpp_path_prefs_key] = setPath
        return setPath

    def enable_cpp(self, enable = True):
        """
        Enables/disables cpp plugin.

        @param enable: Enabled when True. Disables when False.
        @type  enable: bool
        """
        state = self.checkboxes["cpp"].checkState()
        if enable:
            if (state != CHECKED):
                self.checkboxes["cpp"].setCheckState(CHECKED)
            self.choosers["cpp"].setEnabled(True)
            env.prefs[cpp_enabled_prefs_key] = True

            # Sets the cpp path to the standard location, if it exists.
            if not env.prefs[cpp_path_prefs_key]:
                _tmppaths = DEFAULT_PLUGIN_PATHS[cpp_path_prefs_key]
                env.prefs[cpp_path_prefs_key] = get_default_plugin_path( \
                    _tmppaths["win32"], _tmppaths["darwin"], _tmppaths["linux"])

            self.choosers["cpp"].setText(env.prefs[cpp_path_prefs_key])

        else:
            if (state != UNCHECKED):
                self.checkboxes["cpp"].setCheckState(UNCHECKED)
            self.choosers["cpp"].setEnabled(False)
            #self.cpp_path_lineedit.setText("")
            #env.prefs[cpp_path_prefs_key] = ''
            env.prefs[cpp_enabled_prefs_key] = False


    # Rosetta slots #######################################

    def set_rosetta_path(self):
        """
        Slot for Rosetta path line editor.
        """
        setPath = str_or_unicode(self.choosers["Rosetta"].text)
        env.prefs[rosetta_path_prefs_key] = setPath
        prefs = preferences.prefs_context()
        prefs[rosetta_path_prefs_key] = setPath
        return setPath

    def enable_rosetta(self, enable = True):
        """
        If True, rosetta path is set in Preferences > Plug-ins

        @param enable: Is the path set?
        @type  enable: bool
        """

        state = self.checkboxes["Rosetta"].checkState()
        if enable:
            if (state != CHECKED):
                self.checkboxes["Rosetta"].setCheckState(CHECKED)
            self.choosers["Rosetta"].setEnabled(True)
            env.prefs[rosetta_enabled_prefs_key] = True

            # Sets the rosetta (executable) path to the standard location, if it exists.
            if not env.prefs[rosetta_path_prefs_key]:
                _tmppaths = DEFAULT_PLUGIN_PATHS[rosetta_path_prefs_key]
                env.prefs[rosetta_path_prefs_key] = get_default_plugin_path( \
                    _tmppaths["win32"], _tmppaths["darwin"], _tmppaths["linux"])

            self.choosers["Rosetta"].setText(env.prefs[rosetta_path_prefs_key])

        else:
            if (state != UNCHECKED):
                self.checkboxes["Rosetta"].setCheckState(UNCHECKED)
            self.choosers["Rosetta"].setEnabled(False)
            env.prefs[rosetta_enabled_prefs_key] = False
        return

    # Rosetta DB slots #######################################

    def set_rosetta_db_path(self):
        """
        Slot for Rosetta db path line editor.
        """
        setPath = str_or_unicode(self.choosers["Rosetta DB"].text)
        env.prefs[rosetta_dbdir_prefs_key] = setPath
        prefs = preferences.prefs_context()
        prefs[rosetta_dbdir_prefs_key] = setPath
        return setPath

    def enable_rosetta_db(self, enable = True):
        """
        If True, rosetta db path is set in Preferences > Plug-ins

        @param enable: Is the path set?
        @type  enable: bool
        """

        state = self.checkboxes["Rosetta DB"].checkState()
        if enable:
            if (state != CHECKED):
                self.checkboxes["Rosetta DB"].setCheckState(CHECKED)
            self.choosers["Rosetta DB"].setEnabled(True)
            env.prefs[rosetta_database_enabled_prefs_key] = True

            # Sets the rosetta (executable) path to the standard location, if it exists.
            if not env.prefs[rosetta_dbdir_prefs_key]:
                _tmppaths = DEFAULT_PLUGIN_PATHS[rosetta_dbdir_prefs_key]
                env.prefs[rosetta_dbdir_prefs_key] = get_default_plugin_path( \
                    _tmppaths["win32"], _tmppaths["darwin"], _tmppaths["linux"])

            self.choosers["Rosetta DB"].setText(env.prefs[rosetta_dbdir_prefs_key])

        else:
            if (state != UNCHECKED):
                self.checkboxes["Rosetta DB"].setCheckState(UNCHECKED)
            self.choosers["Rosetta DB"].setEnabled(False)
            env.prefs[rosetta_database_enabled_prefs_key] = False
        return

    # QuteMolX slots #######################################

    def set_qutemolx_path(self):
        """
        Slot for QuteMolX path "Choose" button.
        """
        setPath = str_or_unicode(self.choosers["QuteMolX"].text)
        env.prefs[qutemol_path_prefs_key] = setPath
        prefs = preferences.prefs_context()
        prefs[qutemol_path_prefs_key] = setPath

        return setPath

    def enable_qutemolx(self, enable = True):
        """
        Enables/disables QuteMolX plugin.

        @param enable: Enabled when True. Disables when False.
        @type  enable: bool
        """
        if enable:
            self.choosers["QuteMolX"].setEnabled(1)
            env.prefs[qutemol_enabled_prefs_key] = True

            # Sets the QuteMolX (executable) path to the standard location, if it exists.
            if not env.prefs[qutemol_path_prefs_key]:
                _tmppaths = DEFAULT_PLUGIN_PATHS[qutemol_path_prefs_key]
                env.prefs[qutemol_path_prefs_key] = get_default_plugin_path( \
                    _tmppaths["win32"], _tmppaths["darwin"], _tmppaths["linux"])

            self.choosers["QuteMolX"].setText(env.prefs[qutemol_path_prefs_key])

        else:
            self.choosers["QuteMolX"].setEnabled(0)
            #env.prefs[qutemol_path_prefs_key] = ''
            env.prefs[qutemol_enabled_prefs_key] = False

    # POV-Ray slots #####################################

    def set_povray_path(self):
        """
        Slot for POV-Ray path line editor.
        """
        setPath = str_or_unicode(self.choosers["POV-Ray"].text)
        env.prefs[povray_path_prefs_key] = setPath
        prefs = preferences.prefs_context()
        prefs[povray_path_prefs_key] = setPath
        return setPath

    def enable_povray(self, enable = True):
        """
        Enables/disables POV-Ray plugin.

        @param enable: Enabled when True. Disables when False.
        @type  enable: bool
        """
        if enable:
            self.choosers["POV-Ray"].setEnabled(1)
            env.prefs[povray_enabled_prefs_key] = True

            # Sets the POV-Ray (executable) path to the standard location, if it exists.
            if not env.prefs[povray_path_prefs_key]:
                _tmppaths = DEFAULT_PLUGIN_PATHS[povray_path_prefs_key]
                env.prefs[povray_path_prefs_key] = get_default_plugin_path( \
                    _tmppaths["win32"], _tmppaths["darwin"], _tmppaths["linux"])

            self.choosers["POV-Ray"].setText(env.prefs[povray_path_prefs_key])

        else:
            self.choosers["POV-Ray"].setEnabled(0)
            #self.povray_path_lineedit.setText("")
            #env.prefs[povray_path_prefs_key] = ''
            env.prefs[povray_enabled_prefs_key] = False
        self._update_povdir_enables() #bruce 060710

    # MegaPOV slots #####################################

    def set_megapov_path(self):
        """
        Slot for MegaPOV path line editor.
        """
        setPath = str_or_unicode(self.choosers["MegaPOV"].text)
        env.prefs[megapov_path_prefs_key] = setPath
        prefs = preferences.prefs_context()
        prefs[megapov_path_prefs_key] = setPath
        return setPath

    def enable_megapov(self, enable = True):
        """
        Enables/disables MegaPOV plugin.

        @param enable: Enabled when True. Disables when False.
        @type  enable: bool
        """
        if enable:
            self.choosers["MegaPOV"].setEnabled(1)
            env.prefs[megapov_enabled_prefs_key] = True

            # Sets the MegaPOV (executable) path to the standard location, if it exists.
            if not env.prefs[megapov_path_prefs_key]:
                _tmppaths = DEFAULT_PLUGIN_PATHS[megapov_path_prefs_key]
                env.prefs[megapov_path_prefs_key] = get_default_plugin_path( \
                    _tmppaths["win32"], _tmppaths["darwin"], _tmppaths["linux"])

            self.choosers["MegaPOV"].setText(env.prefs[megapov_path_prefs_key])

        else:
            self.choosers["MegaPOV"].setEnabled(0)
            #self.megapov_path_lineedit.setText("")
            #env.prefs[megapov_path_prefs_key] = ''
            env.prefs[megapov_enabled_prefs_key] = False
        self._update_povdir_enables() #bruce 060710

    # POV-Ray include slots #######################################

    # pov include directory [bruce 060710 for Mac A8; will be A8.1 in Windows, not sure about Linux]

    def _update_povdir_enables(self): #bruce 060710
        """
        [private method]
        Call this whenever anything changes regarding when to enable the povdir checkbox, line edit, or choose button.
        We enable the checkbox when either of the POV-Ray or MegaPOV plugins is enabled.
        We enable the line edit and choose button when that condition holds and when the checkbox is checked.
        We update this when any relevant checkbox changes, or when showing this page.
        This will work by reading prefs values, so only call it from slot methods after they have updated prefs values.
        """
        enable_checkbox = env.prefs[povray_enabled_prefs_key] or env.prefs[megapov_enabled_prefs_key]
        self.checkboxes["POV include dir"].setEnabled(enable_checkbox)
        self.choosers["POV include dir"].setEnabled(enable_checkbox)
        enable_edits = enable_checkbox and env.prefs[povdir_enabled_prefs_key]
            # note: that prefs value should and presumably does agree with self.povdir_checkbox.isChecked()
        return

    def enable_pov_include_dir(self, enable = True): #bruce 060710
        """
        Slot method for povdir checkbox.
        povdir is enabled when enable = True.
        povdir is disabled when enable = False.
        """
        env.prefs[povdir_enabled_prefs_key] = not not enable
        self._update_povdir_enables()
        if enable:
            self.choosers["POV include dir"].setEnabled(1)
            env.prefs[povdir_enabled_prefs_key] = True

            # Sets the MegaPOV (executable) path to the standard location, if it exists.
            #if not env.prefs[povdir_path_prefs_key]:
                #_tmppaths = DEFAULT_PLUGIN_PATHS[povdir_path_prefs_key]
                #env.prefs[povdir_path_prefs_key] = get_default_plugin_path( \
                    #_tmppaths["win32"], _tmppaths["darwin"], _tmppaths["linux"])

            self.choosers["POV include dir"].setText(env.prefs[povdir_path_prefs_key])

        else:
            self.choosers["POV include dir"].setEnabled(0)
            #self.megapov_path_lineedit.setText("")
            #env.prefs[megapov_path_prefs_key] = ''
            env.prefs[povdir_enabled_prefs_key] = False#        self.povdir_lineedit.setText(env.prefs[povdir_path_prefs_key])
        return

    def set_pov_include_dir(self): #bruce 060710
        """
        Slot for Pov include dir "Choose" button.
        """
        setPath = str_or_unicode(self.choosers["POV include dir"].text)
        env.prefs[povdir_path_prefs_key] = setPath
        prefs = preferences.prefs_context()
        prefs[povdir_path_prefs_key] = setPath
        return setPath
        #povdir_path = get_dirname_and_save_in_prefs(self, povdir_path_prefs_key, 'Choose Custom POV-Ray Include directory')
        ## note: return value can't be ""; if user cancels, value is None;
        ## to set "" you have to edit the lineedit text directly, but this doesn't work since
        ## no signal is caught to save that into the prefs db!
        ## ####@@@@ we ought to catch that signal... is it returnPressed?? would that be sent if they were editing it, then hit ok?
        ## or if they clicked elsewhere? (currently that fails to remove focus from the lineedits, on Mac, a minor bug IMHO)
        ## (or uncheck the checkbox for the same effect). (#e do we want a "clear" button, for A8.1?)

        #if povdir_path:
            #self.povdir_lineedit.setText(env.prefs[povdir_path_prefs_key])
            ## the function above already saved it in prefs, under the same condition
        #return

    def povdir_lineedit_textChanged(self, *args): #bruce 060710
        if debug_povdir_signals():
            print("povdir_lineedit_textChanged",args)
            # this happens on programmatic changes, such as when the page is shown or the choose button slot sets the text
        try:
            # note: Ideally we'd only do this when return was pressed, mouse was clicked elsewhere (with that also removing keyfocus),
            # other keyfocus removals, including dialog ok or cancel. That is mostly nim,
            # so we have to do it all the time for now -- this is the only way for the user to set the text to "".
            # (This even runs on programmatic sets of the text. Hope that's ok.)
            env.prefs[povdir_path_prefs_key] = path = str_or_unicode( self.povdir_lineedit.text() ).strip()
            if debug_povdir_signals():
                print("debug fyi: set pov include dir to [%s]" % (path,))
        except:
            if env.debug():
                print_compact_traceback("bug, ignored: ")
        return

    #def povdir_lineedit_returnPressed(self, *args): #bruce 060710
        #if debug_povdir_signals():
            #print "povdir_lineedit_returnPressed",args
            ## this happens when return is pressed in the widget, but NOT when user clicks outside it
            ## or presses OK on the dialog -- which means it's useless when taken alone,
            ## in case user edits text and then presses ok without ever pressing return.

    ########## End of slot methods for "Plug-ins" page widgets ###########

    ########## Slot methods for "General" (former name "Caption") page widgets ################


    # PAGE: UNDO

    def _setupPage_Undo(self):
        """
        Setup the "Undo" page.
        """
        connect_checkbox_with_boolean_pref(self.undo_restore_view_CheckBox,
                                           undoRestoreView_prefs_key)
        connect_checkbox_with_boolean_pref(
            self.undo_automatic_checkpoints_CheckBox,
            undoAutomaticCheckpoints_prefs_key)
        connect_spinBox_with_pref(self.undo_stack_memory_limit_SpinBox,
                                  undoStackMemoryLimit_prefs_key)
        return

    # PAGE: WINDOW
    def _setupPage_Window(self):
        """
        Setup the "Window" page.
        """
        # GROUPBOX: Window Postion and Size
        self.current_size_save_Button.clicked.connect(self.save_window_size)
        self.restore_saved_size_Button.clicked.connect(self.restore_saved_size)
        self.current_height_SpinBox.valueChanged[int].connect(self.change_window_size)
        self.current_width_SpinBox.valueChanged[int].connect(self.change_window_size)
        ((x0, y0), (w, h)) = screen_pos_size()
        self.current_width_SpinBox.setRange(1, w)
        self.current_height_SpinBox.setRange(1, h)
        if not DEBUG:
            pos, size = _get_window_pos_size(self.w)
            self.current_width_spinbox.setValue(size[0])
            self.current_height_spinbox.setValue(size[1])
            from utilities.prefs_constants import mainwindow_geometry_prefs_key_prefix
            keyprefix = mainwindow_geometry_prefs_key_prefix
            pos, size = _get_prefs_for_window_pos_size( self.w, keyprefix)
        else:
            self.current_width_SpinBox.setValue(640)
            self.current_height_SpinBox.setValue(480)
            size = [640, 480]

        self.update_saved_size(size[0], size[1])
        connect_checkbox_with_boolean_pref(self.save_size_on_quit_CheckBox,
                                           rememberWinPosSize_prefs_key)
        # GROUPBOX: Window caption format
        self.caption_prefix_LineEdit.setText(env.prefs[captionPrefix_prefs_key])
        self.caption_suffix_LineEdit.setText(env.prefs[captionSuffix_prefs_key])
        self.caption_prefix_save_ToolButton.clicked.connect(self.set_caption_prefix)
        self.caption_suffix_save_ToolButton.clicked.connect(self.set_caption_suffix)
        connect_checkbox_with_boolean_pref(self.display_full_path_CheckBox,
                                           captionFullPath_prefs_key)
        # GROUPBOX: Custom Font
        self.set_use_custom_font_status()
        self.use_custom_font_CheckBox.toggled[bool].connect(self.set_use_custom_font_status)
        font_family = env.prefs[displayFont_prefs_key]
        font_size = env.prefs[displayFontPointSize_prefs_key]
        font = QFont(font_family, font_size)
        self.custom_fontComboBox.setCurrentFont(font)
        self.custom_font_size_SpinBox.setValue(font_size)
        self.custom_fontComboBox.currentFontChanged [QFont].connect(self.change_font)
        self.custom_font_size_SpinBox.valueChanged[int].connect(self.set_fontsize)
        self.make_default_font_PushButton.clicked.connect(self.change_selected_font_to_default_font)
        return

    def change_window_size(self, val = 0):
        """
        Slot for both the width and height spinboxes that change the current
        window size.

        Also called from other slots to change the window size based on new
        values in spinboxes. <val> is not used.
        """
        w = self.current_width_spinbox.value()
        h = self.current_height_spinbox.value()
        if not DEBUG:
            self.w.resize(w,h)
        return

    def update_saved_size(self, w, h):
        """
        Helper function to update the "Saved size" label.
        """
        _text = "Saved size: %d pixels x %d pixels  " % (w, h)
        self.saved_size_label.setText(_text)
        return

    def save_window_size(self):
        """
        Slot for current_size_save_Button
        """
        if not DEBUG:
            from utilities.prefs_constants import mainwindow_geometry_prefs_key_prefix
            keyprefix = mainwindow_geometry_prefs_key_prefix
            save_window_pos_size( self.w, keyprefix) # prints history message
            size = self.w.size()
            self.update_saved_size(size.width(), size.height())
        else:
            width = self.current_width_SpinBox.value()
            height = self.current_height_SpinBox.value()
            self.update_saved_size(width, height)
        return

    def restore_saved_size(self):
        """
        Restore the window size, but not the position, from the prefs db.
        """
        if not DEBUG:
            from utilities.prefs_constants import mainwindow_geometry_prefs_key_prefix
            keyprefix = mainwindow_geometry_prefs_key_prefix
            pos, size = _get_prefs_for_window_pos_size( self.w, keyprefix)
        else:
            size = [640, 480]
        w = size[0]
        h = size[1]
        self.update_saved_size(w, h)
        self.current_width_SpinBox.setValue(w)
        self.current_height_SpinBox.setValue(h)
        self.change_window_size()
        return

    def change_window_size(self, val = 0):
        """
        Slot for both the width and height spinboxes that change the current
        window size.

        Also called from other slots to change the window size based on new
        values in spinboxes. <val> is not used.
        """
        w = self.current_width_SpinBox.value()
        h = self.current_height_SpinBox.value()
        #UNCOMMENT before committing to normal tree
#        self.w.resize(w,h)
        return

    def set_caption_prefix(self):
        """
        Slot for caption_prefix_save_ToolButton.  The caption is only saved
        to the database if the user clicks on this button.  The contents of the
        associated LineEdit are read and stored in the database.
        """
        prefix = str_or_unicode(self.caption_prefix_LineEdit.text())
        prefix = prefix.strip()
        if prefix:
            prefix = prefix + ' '
        env.prefs[captionPrefix_prefs_key] = prefix
        self.caption_prefix_LineEdit.setText(env.prefs[captionPrefix_prefs_key])
        return

    def set_caption_suffix(self):
        """
        Slot for caption_suffix_save_ToolButton.  The caption is only saved
        to the database if the user clicks on this button.  The contents of the
        associated LineEdit are read and stored in the database.
        """
        suffix = str_or_unicode(self.caption_suffix_LineEdit.text())
        suffix = suffix.strip()
        if suffix:
            suffix = ' ' + suffix
        env.prefs[captionSuffix_prefs_key] = suffix
        self.caption_suffix_LineEdit.setText(env.prefs[captionSuffix_prefs_key])
        return

    def set_use_custom_font_status(self, status = None):
        """
        Slot for use_custom_font_CheckBox.  This will enable/disable all the
        other widgets in this groupbox
        """
        if (status == None and env.prefs[useSelectedFont_prefs_key]) \
           or status:
            self.custom_fontComboBox.setEnabled(True)
            self.custom_font_size_SpinBox.setEnabled(True)
            self.custom_fontComboBox.labelWidget.setEnabled(True)
            self.custom_font_size_SpinBox.labelWidget.setEnabled(True)
            self.make_default_font_PushButton.setEnabled(True)
            self.use_custom_font_CheckBox.setCheckState(CHECKED)
            env.prefs[useSelectedFont_prefs_key] = True
        else:
            self.custom_fontComboBox.setEnabled(False)
            self.custom_font_size_SpinBox.setEnabled(False)
            self.custom_fontComboBox.labelWidget.setEnabled(False)
            self.custom_font_size_SpinBox.labelWidget.setEnabled(False)
            self.make_default_font_PushButton.setEnabled(False)
            self.use_custom_font_CheckBox.setCheckState(UNCHECKED)
            env.prefs[useSelectedFont_prefs_key] = False
        return

    def change_font(self, font):
        """
        Slot for the Font combobox.
        Called whenever the font is changed.
        """
        env.prefs[displayFont_prefs_key] = str_or_unicode(font.family())
        self.set_font()
        return

    def set_font(self):
        """
        Set the current display font using the font prefs.
        """

        use_selected_font = env.prefs[useSelectedFont_prefs_key]

        if use_selected_font:
            font = self.custom_fontComboBox.currentFont()
            font_family = str_or_unicode(font.family())
            fontsize = self.custom_font_size_SpinBox.value()
            font.setPointSize(fontsize)
            env.prefs[displayFont_prefs_key] = font_family
            env.prefs[displayFontPointSize_prefs_key] = fontsize
            if debug_flags.atom_debug:
                print("set_font(): Using selected font: ", font.family(), ", size=", font.pointSize())

        else: # Use default font
#            font = self.w.defaultFont
            if debug_flags.atom_debug:
                print("set_font(): Using default font: ", font.family(), ", size=", font.pointSize())

        # Set font
#        self.w.setFont(font)
        return

    def set_fontsize(self, pointsize):
        """
        Slot for the Font size spinbox.
        """
        env.prefs[displayFontPointSize_prefs_key] = pointsize
#        self.set_font()
        return

    def change_selected_font_to_default_font(self):
        """
        Slot for "Make the selected font the default font" button.
        The default font will be displayed in the Font and Size
        widgets.
        """
        font = self.w.defaultFont
        env.prefs[displayFont_prefs_key] = str_or_unicode(font.family())
        env.prefs[displayFontPointSize_prefs_key] = font.pointSize()
        self.set_font_widgets(setFontFromPrefs = True) # Also sets the current display font.

        if debug_flags.atom_debug:
            print("change_selected_font_to_default_font(): " \
                  "Button clicked. Default font: ", font.family(), \
                  ", size=", font.pointSize())
        return

    def set_font_widgets(self, setFontFromPrefs = True):
        """
        Update font widgets based on font prefs.
        Unconnects signals from slots, updates widgets, then reconnects slots.

        @param setFontFromPrefs: when True (default), sets the display font
                                (based on font prefs).
        @type  setFontFromPrefs: bool
        """

        if debug_flags.atom_debug:
            print("set_font_widgets(): Here!")

        if env.prefs[displayFont_prefs_key] == "defaultFont":
            # Set the font and point size prefs to the application's default font.
            # This code only called the first time NE1 is run (or the prefs db does not exist)
            font = self.w.defaultFont
            font_family = str_or_unicode(font.family())
                # Note: when this used str() rather than str_or_unicode(),
                # it prevented NE1 from running on some international systems
                # (when it had never run before and needed to initialize this
                #  prefs value).
                # We can now reproduce the bug (see bug 2883 for details),
                # so I am using str_or_unicode to try to fix it. [bruce 080529]
            font_size = font.pointSize()
            env.prefs[displayFont_prefs_key] = font_family
            env.prefs[displayFontPointSize_prefs_key] = font_size
            if debug_flags.atom_debug:
                print("set_font_widgets(): No prefs db. " \
                      "Using default font: ", font.family(), \
                      ", size=", font.pointSize())

        else:
            font_family = env.prefs[displayFont_prefs_key]
            font_size = env.prefs[displayFontPointSize_prefs_key]
            font = QFont(font_family, font_size)
        return

    # PAGE: REPORTS
    def _setupPage_Reports(self):
        """
        Setup the "Reports" page.
        """
        # GROUPBOX: History Preferences
        connect_checkbox_with_boolean_pref(
            self.history_include_message_serial_CheckBox,
            historyMsgSerialNumber_prefs_key)
        connect_checkbox_with_boolean_pref(
            self.history_include_message_timestamp_CheckBox,
            historyMsgTimestamp_prefs_key)
        return

    # PAGE: TOOLTIPS
    def _setupPage_Tooltips(self):
        """
        Setup the "Tooltips" page.
        """
        # GROUPBOX: Atom tooltip options
        connect_checkbox_with_boolean_pref(self.atom_chunk_information_CheckBox,
                                           dynamicToolTipAtomChunkInfo_prefs_key)
        connect_checkbox_with_boolean_pref(self.atom_mass_information_CheckBox,
                                           dynamicToolTipAtomMass_prefs_key)
        connect_checkbox_with_boolean_pref(self.atom_XYZ_coordinates_CheckBox,
                                           dynamicToolTipAtomPosition_prefs_key)
        connect_checkbox_with_boolean_pref(self.atom_XYZ_distance_CheckBox,
                                           dynamicToolTipAtomDistanceDeltas_prefs_key)
        connect_checkbox_with_boolean_pref(self.atom_include_vdw_CheckBox,
                                           dynamicToolTipVdwRadiiInAtomDistance_prefs_key)
        connect_spinBox_with_pref(self.atom_distance_precision_SpinBox,
                                  dynamicToolTipAtomDistancePrecision_prefs_key)
        connect_spinBox_with_pref(self.atom_angle_precision_SpinBox,
                                  dynamicToolTipBendAnglePrecision_prefs_key)
        # GROUPBOX: Bond tooltip options
        connect_checkbox_with_boolean_pref(
            self.bond_distance_between_atoms_CheckBox,
           dynamicToolTipBondLength_prefs_key)
        connect_checkbox_with_boolean_pref(self.bond_chunk_information_CheckBox,
                                           dynamicToolTipBondChunkInfo_prefs_key)
        return

    ########## Slot methods for top level widgets ################

    def getPagenameList(self):
        """
        Returns a list of page names (i.e. the "stack of widgets") inside
        prefsStackedWidget.

        @return: List of page names.
        @rtype:  List

        @attention: Qt Designer assigns the QStackedWidget property
                    "currentPageName" (which is not a formal attr)
                    to the QWidget (page) attr "objectName".

        @see: U{B{QStackedWidget}<http://doc.trolltech.com/4/qstackedwidget.html>}.
        """
        _pagenameList = []

        for _widgetIndex in range(self.prefsStackedWidget.count()):
            _widget = self.prefsStackedWidget.widget(_widgetIndex)
            _pagename = str(_widget.objectName())
            _pagenameList.append(_pagename)

        return _pagenameList

    def accept(self):
        """
        The slot method for the 'OK' button.
        """
        QDialog.accept(self)
        return

    def reject(self):
        """
        The slot method for the "Cancel" button.
        """
        # The Cancel button has been removed, but this still gets called
        # when the user hits the dialog's "Close" button in the dialog's
        # window border (upper right X).
        # Since I've not implemented 'Cancel', it is safer to go ahead and
        # save all preferences anyway.  Otherwise, any changed preferences
        # will not be persistent (after this session).
        # This will need to be removed when we implement a true cancel function.
        # Mark 050629.
        QDialog.reject(self)
        return

    pass # end of class Preferences

# end

if __name__ == "__main__":
    _iconprefix = "/Users/derrickhendricks/trunks/trunk/cad/src"
    app = QtWidgets.QApplication(sys.argv)
    p = Preferences()
    sys.exit(app.exec_())
