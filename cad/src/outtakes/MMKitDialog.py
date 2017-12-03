# Copyright 2004-2007 Nanorex, Inc.  See LICENSE file for details.
"""
MMKitDialog.py

THIS FILE HAS BEEN DEPRECATED.

SEE NEW IMPLEMETATION IN --
Ui_BuildAtomsPropertyManager.py,
BuildAtomsPropertyManager.py,
Ui_PartLibPropertyManager.py,
PartLibPropertyManager.py,
Ui_PastePropertyManager.py
PastePropertyManager.py

$Id$

History:

-Originally created by Mark and Huaicai using Qt3 designer
Till Alpha8,  MMKit existed  as a Dialog.
-October 2006 Will ported MMKitDialog from Qt3 to Qt4
-October 2006 onwards Ninad integrated Build Dashboard and MMKitDialog
and converted it into a 'Property Manager' with further enhancements.

As of 20070717 it is still refered as MMKitDialog. Should really be called
'Build Atoms Property Manager' -- ninad 20070717

mark 2007-05-29: Fixed sizePolicy for all widgets so everything behaves itself
                 in a fixed width Property Manager (for Alpha 9).
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit

from foundation.Utility import geticon, getpixmap
import foundation.env as env
from PropMgrBaseClass import getPalette

from PropertyManagerMixin import pmVBoxLayout
from PropertyManagerMixin import pmAddHeader
from PropertyManagerMixin import pmAddSponsorButton
from PropertyManagerMixin import pmAddTopRowButtons
from PropertyManagerMixin import pmMessageGroupBox
from PropertyManagerMixin import pmAddBottomSpacer

from PM.PropMgr_Constants import pmDoneButton
from PM.PropMgr_Constants import pmWhatsThisButton
from PM.PropMgr_Constants import pmMainVboxLayoutMargin
from PM.PropMgr_Constants import pmMainVboxLayoutSpacing
from PM.PropMgr_Constants import pmHeaderFrameMargin
from PM.PropMgr_Constants import pmHeaderFrameSpacing
from PM.PropMgr_Constants import getHeaderFont
from PM.PropMgr_Constants import pmLabelLeftAlignment
from PM.PropMgr_Constants import pmSponsorFrameMargin
from PM.PropMgr_Constants import pmSponsorFrameSpacing
from PM.PropMgr_Constants import pmGroupBoxSpacing
from PM.PropMgr_Constants import pmTopRowBtnsMargin
from PM.PropMgr_Constants import pmTopRowBtnsSpacing
from PM.PropMgr_Constants import pmMessageTextEditColor
from PM.PropMgr_Constants import pmGrpBoxVboxLayoutMargin
from PM.PropMgr_Constants import pmGrpBoxVboxLayoutSpacing
from PM.PropMgr_Constants import pmMMKitPageMargin
from PM.PropMgr_Constants import pmMMKitButtonFont
from PM.PropMgr_Constants import pmMMKitButtonFontPointSize
from PM.PropMgr_Constants import pmMMKitButtonFontBold
from PM.PropMgr_Constants import pmMMKitButtonHeight
from PM.PropMgr_Constants import pmMMKitButtonWidth
from utilities.prefs_constants import buildModeAutobondEnabled_prefs_key
from utilities.prefs_constants import buildModeHighlightingEnabled_prefs_key
from utilities.prefs_constants import buildModeWaterEnabled_prefs_key

class Ui_MMKitDialog(object):
    """
    THIS CLASS HAS BEEN DEPRECATED.

    SEE NEW IMPLEMETATION IN --
    Ui_BuildAtomsPropertyManager.py,
    BuildAtomsPropertyManager.py,
    Ui_PartLibPropertyManager.py,
    PartLibPropertyManager.py,
    Ui_PastePropertyManager.py
    PastePropertyManager.py
    """
    def setupUi(self, MMKitDialog):
        # Note: MMKitDialog (which as a local variable should not be named with an initial capital)
        # is an object of class MMKit, which inherits from PropertyManagerMixin,
        # and some methods from PropertyManagerMixin are used on it herein,
        # for example, inside self.ui_message_GroupBox(). [bruce 070618 comment]
        MMKitDialog.setObjectName("MMKitDialog")

        pmVBoxLayout(MMKitDialog)
        pmAddHeader(MMKitDialog)
        pmAddSponsorButton(MMKitDialog)
        pmAddTopRowButtons(MMKitDialog,
                           showFlags = pmDoneButton | pmWhatsThisButton)

        self.MessageGroupBox = pmMessageGroupBox(self, title="Message")
        self.pmVBoxLayout.addWidget(self.MessageGroupBox)
        pmAddBottomSpacer(self.MessageGroupBox, self.pmVBoxLayout)

        self.ui_bondTools_grpBox(MMKitDialog)
        pmAddBottomSpacer(self.bondTools_grpBox, self.pmVBoxLayout)

        self.ui_preview_GroupBox(MMKitDialog)
        pmAddBottomSpacer(self.thumbView_groupBox, self.pmVBoxLayout)

        self.ui_MMKit_GroupBox(MMKitDialog)
        pmAddBottomSpacer(self.MMKit_groupBox, self.pmVBoxLayout)

        self.ui_selectionFilter_GroupBox(MMKitDialog)
        pmAddBottomSpacer(self.selectionFilter_groupBox, self.pmVBoxLayout)

        self.ui_advancedOptions_groupBox(MMKitDialog)
        pmAddBottomSpacer(self.advancedOptions_groupBox, self.pmVBoxLayout, last=True)

        ######################################################.

        self.retranslateUi(MMKitDialog)

        QtCore.QMetaObject.connectSlotsByName(MMKitDialog)

        # End of MMKitDialog ####################################

    def ui_bondTools_grpBox(self, MMKitDialog):
        #Start Atom Bond tools Groupbox

        self.bondTools_grpBox = QtWidgets.QGroupBox(MMKitDialog)
        self.bondTools_grpBox.setObjectName("bondTools_grpBox")

        self.bondTools_grpBox.setAutoFillBackground(True)
        palette = MMKitDialog.getGroupBoxPalette()
        self.bondTools_grpBox.setPalette(palette)

        styleSheet = MMKitDialog.getGroupBoxStyleSheet()
        self.bondTools_grpBox.setStyleSheet(styleSheet)

        self.vboxlayout_grpbox1 = QtWidgets.QVBoxLayout(self.bondTools_grpBox)
        self.vboxlayout_grpbox1.setContentsMargins(pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin)
        self.vboxlayout_grpbox1.setSpacing(pmGrpBoxVboxLayoutSpacing)
        self.vboxlayout_grpbox1.setObjectName("vboxlayout_grpbox1")

        self.bondTool_groupBoxButton = MMKitDialog.getGroupBoxTitleButton(
            "Bonds Tool",
            self.bondTools_grpBox)

        self.vboxlayout_grpbox1.addWidget(self.bondTool_groupBoxButton)


        self.bondToolWidget = QtWidgets.QWidget(self.bondTools_grpBox)

        hlo_bondtool = QtWidgets.QHBoxLayout(self.bondToolWidget)
        hlo_bondtool.setContentsMargins(2, 2, 2, 2)
        hlo_bondtool.setSpacing(2)


        for action in self.parentMode.bond1Action, self.parentMode.bond2Action, \
            self.parentMode.bond3Action, self.parentMode.bondaAction, \
            self.parentMode.bondgAction, self.parentMode.cutBondsAction:

            btn = QtWidgets.QToolButton()
            btn.setDefaultAction(action)
            btn.setIconSize(QtCore.QSize(22,22))
            btn.setAutoRaise(1)
            action.setCheckable(True)
            self.parentMode.bondToolsActionGroup.addAction(action)
            hlo_bondtool.addWidget(btn)

        self.vboxlayout_grpbox1.addWidget(self.bondToolWidget)

        # End Atom Bond Tools Groupbox
        self.pmVBoxLayout.addWidget(self.bondTools_grpBox)

        # Height is fixed. Mark 2007-05-29.
        self.bondTools_grpBox.setSizePolicy(
                QSizePolicy(QSizePolicy.Policy(QSizePolicy.Preferred),
                            QSizePolicy.Policy(QSizePolicy.Fixed)))

    def ui_preview_GroupBox(self, MMKitDialog):
        # Start MMKit ThumbView  (Preview) GroupBox

        self.thumbView_groupBox = QtWidgets.QGroupBox(MMKitDialog)
        self.thumbView_groupBox.setObjectName("thumbView_groupBox")

        self.thumbView_groupBox.setAutoFillBackground(True)
        palette = MMKitDialog.getGroupBoxPalette()
        self.thumbView_groupBox.setPalette(palette)

        styleSheet = MMKitDialog.getGroupBoxStyleSheet()
        self.thumbView_groupBox.setStyleSheet(styleSheet)


        self.vboxlayout_grpbox2 = QtWidgets.QVBoxLayout(self.thumbView_groupBox)
        self.vboxlayout_grpbox2.setContentsMargins(pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin)
        self.vboxlayout_grpbox2.setSpacing(pmGrpBoxVboxLayoutSpacing)
        self.vboxlayout_grpbox2.setObjectName("vboxlayout_grpbox2")

        self.thumbView_groupBoxButton = MMKitDialog.getGroupBoxTitleButton("Preview", self.thumbView_groupBox)

        self.vboxlayout_grpbox2.addWidget(self.thumbView_groupBoxButton)


        self.elementFrame = QtWidgets.QFrame(self.thumbView_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(3),QtWidgets.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.elementFrame.sizePolicy().hasHeightForWidth())
        self.elementFrame.setSizePolicy(sizePolicy)
        self.elementFrame.setMinimumSize(QtCore.QSize(150,150))
        self.elementFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.elementFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.elementFrame.setObjectName("elementFrame")

        self.vboxlayout_grpbox2.addWidget(self.elementFrame)

        #End  MMKit ThumbView  (Preview) GroupBox
        self.pmVBoxLayout.addWidget(self.thumbView_groupBox)

        # Height is fixed. Mark 2007-05-29.
        self.thumbView_groupBox.setSizePolicy(
                QSizePolicy(QSizePolicy.Policy(QSizePolicy.Preferred),
                            QSizePolicy.Policy(QSizePolicy.Fixed)))

    def ui_MMKit_GroupBox(self, MMKitDialog):
        #Start MMKit groupbox (includes atom, clipboard and library tabs)
        self.MMKit_groupBox = QtWidgets.QGroupBox(MMKitDialog)
        self.MMKit_groupBox.setObjectName("MMKit_groupBox")

        self.MMKit_groupBox.setAutoFillBackground(True)
        palette = MMKitDialog.getGroupBoxPalette()
        self.MMKit_groupBox.setPalette(palette)

        styleSheet = MMKitDialog.getGroupBoxStyleSheet()
        self.MMKit_groupBox.setStyleSheet(styleSheet)

        self.MMKitGrpBox_VBoxLayout = QtWidgets.QVBoxLayout(self.MMKit_groupBox)
        self.MMKitGrpBox_VBoxLayout.setContentsMargins(pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin)
        self.MMKitGrpBox_VBoxLayout.setSpacing(pmGrpBoxVboxLayoutSpacing)
        self.MMKitGrpBox_VBoxLayout.setObjectName("MMKitGrpBox_VBoxLayout")

        self.MMKitGrpBox_TitleButton = MMKitDialog.getGroupBoxTitleButton("MMKit", self.MMKit_groupBox)

        self.MMKitGrpBox_VBoxLayout.addWidget(self.MMKitGrpBox_TitleButton)

        self.mmkit_tab = QtWidgets.QTabWidget(self.MMKit_groupBox)
        self.mmkit_tab.setEnabled(True)

        # Height is fixed. Mark 2007-05-29.
        self.mmkit_tab.setSizePolicy(
                QSizePolicy(QSizePolicy.Policy(QSizePolicy.Preferred),
                            QSizePolicy.Policy(QSizePolicy.Fixed)))

        self.mmkit_tab.setObjectName("mmkit_tab")

        self.atomsPage = QtWidgets.QWidget()
        self.atomsPage.setObjectName("atomsPage")

        self.mmkit_tab.addTab(self.atomsPage, "")

        self.atomsPageFrame = QtWidgets.QFrame(self.atomsPage)

        # atomsPageFrame needs to be reviewed carefully. Mark 2007-06-20
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(3),QtWidgets.QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.atomsPageFrame.sizePolicy().hasHeightForWidth())
        self.atomsPageFrame.setSizePolicy(sizePolicy)
        self.atomsPageFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.atomsPageFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.atomsPageFrame.setMinimumSize(QtCore.QSize(100,100))
        self.atomsPageFrame.setObjectName("atomsPageFrame")

        self.atomsPage_VBoxLayout = QtWidgets.QVBoxLayout(self.atomsPageFrame)
        self.atomsPage_VBoxLayout.setContentsMargins(pmMMKitPageMargin) # Was 4. Mark 2007-05-30, pmMMKitPageMargin) # Was 4. Mark 2007-05-30, pmMMKitPageMargin) # Was 4. Mark 2007-05-30, pmMMKitPageMargin) # Was 4. Mark 2007-05-30)
        self.atomsPage_VBoxLayout.setSpacing(2)

        # Element Button GroupBox begins here. #####################

        self.elementButtonGroup = QtWidgets.QGroupBox(self.atomsPageFrame)

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.elementButtonGroup.setSizePolicy(sizePolicy)
        self.elementButtonGroup.setMinimumSize(
            QtCore.QSize(pmMMKitButtonWidth  * 4,
                         pmMMKitButtonHeight * 4 + 4))
        self.elementButtonGroup.setObjectName("elementButtonGroup")

        self.MMKit_GridLayout = QtWidgets.QGridLayout(self.elementButtonGroup)
        self.MMKit_GridLayout.setContentsMargins(1) # Was 0. Mark 2007-05-30, 1) # Was 0. Mark 2007-05-30, 1) # Was 0. Mark 2007-05-30, 1) # Was 0. Mark 2007-05-30)
        self.MMKit_GridLayout.setSpacing(0)
        self.MMKit_GridLayout.setObjectName("MMKit_GridLayout")

        # Font for toolbuttons.
        font = QFont(self.atomsPageFrame.font())
        font.setFamily(pmMMKitButtonFont)
        font.setPointSize(pmMMKitButtonFontPointSize)
        font.setBold(pmMMKitButtonFontBold)
        #font.setWeight(75)
        #font.setItalic(False)
        #font.setUnderline(False)
        #font.setStrikeOut(False)

        # All this would be much nicer using a dictionary in a loop.
        # Later, when time permits. Mark 2007-05-30.

        self.toolButton1 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton1.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton1.setCheckable(True)
        self.toolButton1.setFont(font)
        self.toolButton1.setObjectName("toolButton1")
        self.MMKit_GridLayout.addWidget(self.toolButton1,0,4,1,1)

        self.toolButton2 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton2.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton2.setCheckable(True)
        self.toolButton2.setFont(font)
        self.toolButton2.setObjectName("toolButton2")
        self.MMKit_GridLayout.addWidget(self.toolButton2,0,5,1,1)

        self.toolButton6 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton6.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton6.setCheckable(True)
        self.toolButton6.setFont(font)
        self.toolButton6.setObjectName("toolButton6")
        self.MMKit_GridLayout.addWidget(self.toolButton6,1,1,1,1)

        self.toolButton7 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton7.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton7.setCheckable(True)
        self.toolButton7.setFont(font)
        self.toolButton7.setObjectName("toolButton7")
        self.MMKit_GridLayout.addWidget(self.toolButton7,1,2,1,1)

        self.toolButton8 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton8.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton8.setCheckable(True)
        self.toolButton8.setFont(font)
        self.toolButton8.setObjectName("toolButton8")
        self.MMKit_GridLayout.addWidget(self.toolButton8,1,3,1,1)

        self.toolButton10 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton10.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton10.setCheckable(True)
        self.toolButton10.setFont(font)
        self.toolButton10.setObjectName("toolButton10")
        self.MMKit_GridLayout.addWidget(self.toolButton10,1,5,1,1)

        self.toolButton9 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton9.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton9.setCheckable(True)
        self.toolButton9.setFont(font)
        self.toolButton9.setObjectName("toolButton9")
        self.MMKit_GridLayout.addWidget(self.toolButton9,1,4,1,1)

        self.toolButton13 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton13.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton13.setCheckable(True)
        self.toolButton13.setFont(font)
        self.toolButton13.setObjectName("toolButton13")
        self.MMKit_GridLayout.addWidget(self.toolButton13,2,0,1,1)

        self.toolButton17 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton17.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton17.setCheckable(True)
        self.toolButton17.setFont(font)
        self.toolButton17.setObjectName("toolButton17")
        self.MMKit_GridLayout.addWidget(self.toolButton17,2,4,1,1)

        self.toolButton5 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton5.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton5.setCheckable(True)
        self.toolButton5.setFont(font)
        self.toolButton5.setObjectName("toolButton5")
        self.MMKit_GridLayout.addWidget(self.toolButton5,1,0,1,1)

        self.toolButton10_2 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton10_2.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton10_2.setCheckable(True)
        self.toolButton10_2.setFont(font)
        self.toolButton10_2.setObjectName("toolButton10_2")
        self.MMKit_GridLayout.addWidget(self.toolButton10_2,2,5,1,1)

        self.toolButton15 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton15.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton15.setCheckable(True)
        self.toolButton15.setFont(font)
        self.toolButton15.setObjectName("toolButton15")
        self.MMKit_GridLayout.addWidget(self.toolButton15,2,2,1,1)

        self.toolButton16 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton16.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton16.setCheckable(True)
        self.toolButton16.setFont(font)
        self.toolButton16.setObjectName("toolButton16")
        self.MMKit_GridLayout.addWidget(self.toolButton16,2,3,1,1)

        self.toolButton14 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton14.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton14.setCheckable(True)
        self.toolButton14.setFont(font)
        self.toolButton14.setObjectName("toolButton14")
        self.MMKit_GridLayout.addWidget(self.toolButton14,2,1,1,1)

        self.toolButton33 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton33.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton33.setCheckable(True)
        self.toolButton33.setFont(font)
        self.toolButton33.setObjectName("toolButton33")
        self.MMKit_GridLayout.addWidget(self.toolButton33,3,2,1,1)

        self.toolButton34 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton34.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton34.setCheckable(True)
        self.toolButton34.setFont(font)
        self.toolButton34.setObjectName("toolButton34")
        self.MMKit_GridLayout.addWidget(self.toolButton34,3,3,1,1)

        self.toolButton35 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton35.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton35.setCheckable(True)
        self.toolButton35.setFont(font)
        self.toolButton35.setObjectName("toolButton35")
        self.MMKit_GridLayout.addWidget(self.toolButton35,3,4,1,1)

        self.toolButton32 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton32.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton32.setCheckable(True)
        self.toolButton32.setFont(font)
        self.toolButton32.setObjectName("toolButton32")
        self.MMKit_GridLayout.addWidget(self.toolButton32,3,1,1,1)

        self.toolButton36 = QtWidgets.QToolButton(self.elementButtonGroup)
        self.toolButton36.setFixedSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.toolButton36.setCheckable(True)
        self.toolButton36.setFont(font)
        self.toolButton36.setObjectName("toolButton36")
        self.MMKit_GridLayout.addWidget(self.toolButton36,3,5,1,1)

        self.atomsPage_VBoxLayout.addWidget(self.elementButtonGroup)

        # Height is fixed (i.e. locked). Mark 2007-05-29.
        self.elementButtonGroup.setSizePolicy(
                QSizePolicy(QSizePolicy.Policy(QSizePolicy.Preferred),
                            QSizePolicy.Policy(QSizePolicy.Fixed)))

        # Atomic Hybrid label
        self.atomic_hybrids_label = QtWidgets.QLabel(self.atomsPageFrame)
        self.atomic_hybrids_label.setText("Atomic Hybrids :")
        self.atomsPage_VBoxLayout.addWidget(self.atomic_hybrids_label)

        # Elements Button GroupBox ends here. #######################

        # This special HBoxLayout contains both the hybrid button group and a
        # vert spacer (width = 0) to keep the Qt layout working properly
        # in certain situations like that described in bug 2407.
        # Mark 2007-06-20.
        self.special_HBoxLayout = QtWidgets.QHBoxLayout()
        self.special_HBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.special_HBoxLayout.setSpacing(6)
        self.special_HBoxLayout.setObjectName("special_HBoxLayout")
        self.atomsPage_VBoxLayout.addLayout(self.special_HBoxLayout)

        # Hybrid GroupBox begins here ###############################

        self.hybrid_btngrp = QtWidgets.QGroupBox(self.atomsPageFrame)
        self.hybrid_btngrp.setObjectName("hybrid_btngrp")
        self.special_HBoxLayout.addWidget(self.hybrid_btngrp)

        self.hybridBtns_HBoxLayout = QtWidgets.QHBoxLayout(self.hybrid_btngrp)
        self.hybridBtns_HBoxLayout.setContentsMargins(2, 2, 2, 2)
        self.hybridBtns_HBoxLayout.setSpacing(0)
        self.hybridBtns_HBoxLayout.setObjectName("hybridBtns_HBoxLayout")

        self.sp3_btn = QtWidgets.QToolButton(self.hybrid_btngrp)
        self.sp3_btn.setMinimumSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.sp3_btn.setMaximumSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.sp3_btn.setCheckable(True)
        self.sp3_btn.setObjectName("sp3_btn")
        self.hybridBtns_HBoxLayout.addWidget(self.sp3_btn)

        self.sp2_btn = QtWidgets.QToolButton(self.hybrid_btngrp)
        self.sp2_btn.setMinimumSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.sp2_btn.setMaximumSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.sp2_btn.setCheckable(True)
        self.sp2_btn.setObjectName("sp2_btn")
        self.hybridBtns_HBoxLayout.addWidget(self.sp2_btn)

        self.sp_btn = QtWidgets.QToolButton(self.hybrid_btngrp)
        self.sp_btn.setMinimumSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.sp_btn.setMaximumSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.sp_btn.setCheckable(True)
        self.sp_btn.setObjectName("sp_btn")
        self.hybridBtns_HBoxLayout.addWidget(self.sp_btn)

        self.graphitic_btn = QtWidgets.QToolButton(self.hybrid_btngrp)
        self.graphitic_btn.setMinimumSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.graphitic_btn.setMaximumSize(QtCore.QSize(pmMMKitButtonWidth,pmMMKitButtonHeight))
        self.graphitic_btn.setCheckable(True)
        self.graphitic_btn.setObjectName("graphitic_btn")
        self.hybridBtns_HBoxLayout.addWidget(self.graphitic_btn)

        # This VSpacer is needed to help (but not completely) fix bug 2407. It
        # maintains the height of the layout(s) containing the hybrid button
        # group when it is hidden using hide(). Without this spacer the layout
        # gets screwed up in special situations like that described in bug 2407.
        # The + 10 below is needed to account for the margin (4 pixels) and
        # the additional 6 just help (I have a theory that the height of the
        # frame containing the label above the hybrid group box shrinks when
        # the label is hidden by inserting a space character). I'm
        # not going to worry about this now. +10 works well enough.
        # Mark 2007-06-20.
        VSpacer = QtWidgets.QSpacerItem(0, pmMMKitButtonHeight + 10,
                                        QtWidgets.QSizePolicy.Fixed,
                                        QtWidgets.QSizePolicy.Fixed)
        #self.hybridBtns_HBoxLayout.addItem(VSpacer)
        self.special_HBoxLayout.addItem(VSpacer)

        self.hybridBtns_HBoxLayout.addStretch(0)

        # Height is fixed. Mark 2007-05-29.
        self.hybrid_btngrp.setSizePolicy(
                QSizePolicy(QSizePolicy.Policy(QSizePolicy.MinimumExpanding),
                            QSizePolicy.Policy(QSizePolicy.Fixed)))

        # This spacer keeps the MMKit button grid compressed when
        # the hybrid button group is hidden.
        self.atomsPageBottomVSpacer = \
            QtWidgets.QSpacerItem(5, 0,
                              QtWidgets.QSizePolicy.Fixed,
                              QtWidgets.QSizePolicy.MinimumExpanding)

        self.atomsPage_VBoxLayout.addItem(self.atomsPageBottomVSpacer)

        # Clipboard page begins here ############################################

        self.clipboardPage = QtWidgets.QWidget()
        self.clipboardPage.setObjectName("clipboardPage")

        self.gridlayout3 = QtWidgets.QGridLayout(self.clipboardPage)
        self.gridlayout3.setContentsMargins(pmMMKitPageMargin) # Was 4. Mark 2007-05-30, pmMMKitPageMargin) # Was 4. Mark 2007-05-30, pmMMKitPageMargin) # Was 4. Mark 2007-05-30, pmMMKitPageMargin) # Was 4. Mark 2007-05-30)
        self.gridlayout3.setSpacing(2)
        self.gridlayout3.setObjectName("gridlayout3")

        self.chunkListBox = QtWidgets.QListWidget(self.clipboardPage)

        self.chunkListBox.setMinimumSize(QtCore.QSize(100,100))

        # Height is fixed. Mark 2007-05-29.
        self.chunkListBox.setSizePolicy(
                QSizePolicy(QSizePolicy.Policy(QSizePolicy.MinimumExpanding),
                            QSizePolicy.Policy(QSizePolicy.Fixed)))

        self.chunkListBox.setObjectName("chunkListBox")
        self.gridlayout3.addWidget(self.chunkListBox,0,0,1,1)
        self.mmkit_tab.addTab(self.clipboardPage, "")

        self.libraryPage = QtWidgets.QWidget()
        #self.libraryPage = QtGui.QScrollArea()
        #self.libraryPageWidget = QtGui.QWidget()
        #self.libraryPage.setWidget(self.libraryPageWidget)
        self.libraryPage.setObjectName("libraryPage")
        self.mmkit_tab.addTab(self.libraryPage, "")

        self.MMKitGrpBox_VBoxLayout.addWidget(self.mmkit_tab)

        self.transmuteAtomsAction = QtWidgets.QWidgetAction(self.w)
        self.transmuteAtomsAction.setText("Transmute Atoms")
        self.transmuteAtomsAction.setIcon(geticon(
            'ui/actions/Toolbars/Smart/Transmute_Atoms'))
        self.transmuteAtomsAction.setCheckable(False)

        transmuteBtn_HBoxLayout = QtWidgets.QHBoxLayout()

        self.transmuteBtn = QtWidgets.QToolButton(self.MMKit_groupBox)
        self.transmuteBtn.setDefaultAction(self.transmuteAtomsAction)
        self.transmuteBtn.setFixedSize(QtCore.QSize(36, 36))
        self.transmuteBtn.setIconSize(QtCore.QSize(22,22))
        transmuteBtn_HBoxLayout.addWidget(self.transmuteBtn)

        self.browseButton = QtWidgets.QPushButton(MMKitDialog)
        transmuteBtn_HBoxLayout.addWidget(self.browseButton)

        self.defaultPartLibButton = QtWidgets.QPushButton(MMKitDialog)
        transmuteBtn_HBoxLayout.addWidget(self.defaultPartLibButton)

        self.atomsPageSpacer = QtWidgets.QSpacerItem(0, 5,
                                             QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)

        transmuteBtn_HBoxLayout.addItem(self.atomsPageSpacer)

        self.MMKitGrpBox_VBoxLayout.addLayout(transmuteBtn_HBoxLayout)

        self.transmuteCB = QtWidgets.QCheckBox(" Force to Keep Bonds", self.MMKit_groupBox)

        self.MMKitGrpBox_VBoxLayout.addWidget(self.transmuteCB)

        #End MMKit groupbox
        self.pmVBoxLayout.addWidget(self.MMKit_groupBox)

        # This line is important. Without it, the MMKit groupbox is
        # too wide by default and causes a horizontal scrollbar
        # to be displayed at the bottom of the PropMgr. Mark 2007-05-30
        self.MMKit_groupBox.setMinimumWidth(200)

        # Height is fixed. Mark 2007-05-29.
        self.MMKit_groupBox.setSizePolicy(
                QSizePolicy(QSizePolicy.Policy(QSizePolicy.MinimumExpanding),
                            QSizePolicy.Policy(QSizePolicy.Fixed)))

    def ui_selectionFilter_GroupBox(self, MMKitDialog):
        #Start Selection Filter GroupBox
        self.selectionFilter_groupBox = QtWidgets.QGroupBox(MMKitDialog)
        self.selectionFilter_groupBox.setObjectName("selectionFilter_groupBox")

        self.selectionFilter_groupBox.setAutoFillBackground(True)
        palette = MMKitDialog.getGroupBoxPalette()
        self.selectionFilter_groupBox.setPalette(palette)

        styleSheet = MMKitDialog.getGroupBoxStyleSheet()
        self.selectionFilter_groupBox.setStyleSheet(styleSheet)

        self.hboxlayout_selfilter = QtWidgets.QHBoxLayout()
        self.hboxlayout_selfilter.setContentsMargins(pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin)
        self.hboxlayout_selfilter.setSpacing(6)
        self.hboxlayout_selfilter.setObjectName("hboxlayout_selfilter")

        self.vboxlayout_selfilter = QtWidgets.QVBoxLayout(self.selectionFilter_groupBox)
        self.vboxlayout_selfilter.setContentsMargins(pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin)
        self.vboxlayout_selfilter.setSpacing(6)
        self.vboxlayout_selfilter.setObjectName("vboxlayout_selfilter")

        self.filterCB = MMKitDialog.getGroupBoxTitleCheckBox("Selection Filter ", self.selectionFilter_groupBox )

        self.vboxlayout_selfilter.addWidget(self.filterCB)

        self.selectionFilter_label = QtWidgets.QLabel(self.selectionFilter_groupBox)
        self.vboxlayout_selfilter.addWidget(self.selectionFilter_label)

        self.filterlistLE = QLineEdit(self.selectionFilter_groupBox)
        self.filterlistLE.setReadOnly(1)
        self.filterlistLE.setEnabled(0)

        if self.filterCB.isChecked():
            self.filterlistLE.show()
            self.selectionFilter_label.show()
        else:
            self.filterlistLE.hide()
            self.selectionFilter_label.hide()

        self.vboxlayout_selfilter.addWidget(self.filterlistLE)
        #End Selection filter GroupBox
        self.pmVBoxLayout.addWidget(self.selectionFilter_groupBox)

        # Height is fixed. Mark 2007-05-29.
        self.selectionFilter_groupBox.setSizePolicy(
                QSizePolicy(QSizePolicy.Policy(QSizePolicy.Preferred),
                            QSizePolicy.Policy(QSizePolicy.Fixed)))

    def ui_advancedOptions_groupBox(self, MMKitDialog):
        #Start Advanced Options GroupBox
        self.advancedOptions_groupBox = QtWidgets.QGroupBox(MMKitDialog)
        self.advancedOptions_groupBox.setObjectName("advancedOptions_groupBox")

        self.advancedOptions_groupBox.setAutoFillBackground(True)
        palette = MMKitDialog.getGroupBoxPalette()
        self.advancedOptions_groupBox.setPalette(palette)

        styleSheet = MMKitDialog.getGroupBoxStyleSheet()
        self.advancedOptions_groupBox.setStyleSheet(styleSheet)

        self.vboxlayout_grpbox4 = QtWidgets.QVBoxLayout(self.advancedOptions_groupBox)
        self.vboxlayout_grpbox4.setContentsMargins(pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin, pmGrpBoxVboxLayoutMargin)
        self.vboxlayout_grpbox4.setSpacing(pmGrpBoxVboxLayoutSpacing)
        self.vboxlayout_grpbox4.setObjectName("vboxlayout_grpbox4")

        self.advancedOptions_groupBoxButton = MMKitDialog.getGroupBoxTitleButton("Advanced Options",
                                                                                 self.advancedOptions_groupBox)

        self.vboxlayout_grpbox4.addWidget(self.advancedOptions_groupBoxButton)

        self.autobondCB = QtWidgets.QCheckBox("Autobond", self.advancedOptions_groupBox )
        self.autobondCB.setChecked(env.prefs[buildModeAutobondEnabled_prefs_key])
        self.vboxlayout_grpbox4.addWidget(self.autobondCB)

        self.highlightingCB = QtWidgets.QCheckBox("Highlighting", self.advancedOptions_groupBox )
        self.highlightingCB.setChecked(env.prefs[buildModeHighlightingEnabled_prefs_key])
        self.vboxlayout_grpbox4.addWidget(self.highlightingCB)

        self.waterCB = QtWidgets.QCheckBox("Water", self.advancedOptions_groupBox )
        self.waterCB.setChecked(env.prefs[buildModeWaterEnabled_prefs_key])
        self.vboxlayout_grpbox4.addWidget(self.waterCB)

        #End Advanced Options GroupBox
        self.pmVBoxLayout.addWidget(self.advancedOptions_groupBox)

        # Height is fixed. Mark 2007-05-29.
        self.advancedOptions_groupBox.setSizePolicy(
                QSizePolicy(QSizePolicy.Policy(QSizePolicy.Preferred),
                            QSizePolicy.Policy(QSizePolicy.Fixed)))

    def retranslateUi(self, MMKitDialog):
        MMKitDialog.setWindowTitle(QtCore.QCoreApplication.translate("MMKitDialog",
                                                                "MMKit", None))
        MMKitDialog.setWindowIcon(QtGui.QIcon("ui/border/MMKit"))

        self.elementFrame.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Preview window of active object.", None))
        self.toolButton1.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Hydrogen", None))
        self.toolButton1.setText(QtCore.QCoreApplication.translate("MMKitDialog", "H", None))
        self.toolButton1.setShortcut(QtCore.QCoreApplication.translate("MMKitDialog", "H", None))
        self.toolButton2.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Helium", None))
        self.toolButton2.setText(QtCore.QCoreApplication.translate("MMKitDialog", "He", None))
        self.toolButton6.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Carbon", None))
        self.toolButton6.setText(QtCore.QCoreApplication.translate("MMKitDialog", "C", None))
        self.toolButton6.setShortcut(QtCore.QCoreApplication.translate("MMKitDialog", "C", None))
        self.toolButton7.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Nitrogen", None))
        self.toolButton7.setText(QtCore.QCoreApplication.translate("MMKitDialog", "N", None))
        self.toolButton7.setShortcut(QtCore.QCoreApplication.translate("MMKitDialog", "N", None))
        self.toolButton8.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Oxygen", None))
        self.toolButton8.setText(QtCore.QCoreApplication.translate("MMKitDialog", "O", None))
        self.toolButton8.setShortcut(QtCore.QCoreApplication.translate("MMKitDialog", "O", None))
        self.toolButton10.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Neon", None))
        self.toolButton10.setText(QtCore.QCoreApplication.translate("MMKitDialog", "Ne", None))
        self.toolButton9.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Fluorine", None))
        self.toolButton9.setText(QtCore.QCoreApplication.translate("MMKitDialog", "F", None))
        self.toolButton9.setShortcut(QtCore.QCoreApplication.translate("MMKitDialog", "F", None))
        self.toolButton13.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Aluminum", None))
        self.toolButton13.setText(QtCore.QCoreApplication.translate("MMKitDialog", "Al", None))
        self.toolButton13.setShortcut(QtCore.QCoreApplication.translate("MMKitDialog", "A", None))
        self.toolButton17.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Chlorine", None))
        self.toolButton17.setText(QtCore.QCoreApplication.translate("MMKitDialog", "Cl", None))
        self.toolButton17.setShortcut(QtCore.QCoreApplication.translate("MMKitDialog", "L", None))
        self.toolButton5.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Boron", None))
        self.toolButton5.setText(QtCore.QCoreApplication.translate("MMKitDialog", "B", None))
        self.toolButton5.setShortcut(QtCore.QCoreApplication.translate("MMKitDialog", "B", None))
        self.toolButton10_2.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Argon", None))
        self.toolButton10_2.setText(QtCore.QCoreApplication.translate("MMKitDialog", "Ar", None))
        self.toolButton15.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Phosphorus", None))
        self.toolButton15.setText(QtCore.QCoreApplication.translate("MMKitDialog", "P", None))
        self.toolButton15.setShortcut(QtCore.QCoreApplication.translate("MMKitDialog", "P", None))
        self.toolButton16.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Sulfur", None))
        self.toolButton16.setText(QtCore.QCoreApplication.translate("MMKitDialog", "S", None))
        self.toolButton16.setShortcut(QtCore.QCoreApplication.translate("MMKitDialog", "S", None))
        self.toolButton14.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Silicon", None))
        self.toolButton14.setText(QtCore.QCoreApplication.translate("MMKitDialog", "Si", None))
        self.toolButton14.setShortcut(QtCore.QCoreApplication.translate("MMKitDialog", "Q", None))
        self.toolButton33.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Arsenic", None))
        self.toolButton33.setText(QtCore.QCoreApplication.translate("MMKitDialog", "As", None))
        self.toolButton34.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Selenium", None))
        self.toolButton34.setText(QtCore.QCoreApplication.translate("MMKitDialog", "Se", None))
        self.toolButton35.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Bromine", None))
        self.toolButton35.setText(QtCore.QCoreApplication.translate("MMKitDialog", "Br", None))
        self.toolButton32.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Germanium", None))
        self.toolButton32.setText(QtCore.QCoreApplication.translate("MMKitDialog", "Ge", None))
        self.toolButton36.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Krypton", None))
        self.toolButton36.setText(QtCore.QCoreApplication.translate("MMKitDialog", "Kr", None))
        self.sp3_btn.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "sp3", None))
        self.sp3_btn.setShortcut(QtCore.QCoreApplication.translate("MMKitDialog", "3", None))
        self.sp2_btn.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "sp2", None))
        self.sp2_btn.setShortcut(QtCore.QCoreApplication.translate("MMKitDialog", "2", None))
        self.sp_btn.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "sp", None))
        self.sp_btn.setShortcut(QtCore.QCoreApplication.translate("MMKitDialog", "1", None))
        self.graphitic_btn.setToolTip(QtCore.QCoreApplication.translate("MMKitDialog", "Graphitic", None))
        self.graphitic_btn.setShortcut(QtCore.QCoreApplication.translate("MMKitDialog", "4", None))
        self.mmkit_tab.setTabText(self.mmkit_tab.indexOf(self.atomsPage), QtCore.QCoreApplication.translate("MMKitDialog", "", None))
        self.mmkit_tab.setTabText(self.mmkit_tab.indexOf(self.clipboardPage), QtCore.QCoreApplication.translate("MMKitDialog", "", None))
        self.mmkit_tab.setTabText(self.mmkit_tab.indexOf(self.libraryPage), QtCore.QCoreApplication.translate("MMKitDialog", "", None))
        self.selectionFilter_label.setText(QtCore.QCoreApplication.translate("selectionFilter_groupBox",
                                                                        "Apply Filter To:",
                                                                        None))

        self.browseButton.setToolTip(QtCore.QCoreApplication.translate(
            "MMKitDialog",
            "Open file chooser dialog to select a new directory.",
            None))

        self.browseButton.setText(QtCore.QCoreApplication.translate(
            "MMKitDialog", "Browse...",None))

        self.defaultPartLibButton.setText(QtCore.QCoreApplication.translate(
            "MMKitDialog", "Default Dir", None))

        self.defaultPartLibButton.setToolTip(QtCore.QCoreApplication.translate(
            "MMKitDialog", "Reset the partlib directory path to program default",
            None))

