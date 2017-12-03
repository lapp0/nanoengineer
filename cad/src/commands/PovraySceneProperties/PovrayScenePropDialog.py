# -*- coding: utf-8 -*-
# Copyright 2006-2008 Nanorex, Inc.  See LICENSE file for details.
"""
PovrayScenePropDialog.py

Note: this file is not presently used in NE1 (as of before 080515).

@author: Mark
@version: $Id$
@copyright: 2006-2008 Nanorex, Inc.  See LICENSE file for details.

History:

This used to be made by pyuic from a .ui file,
but since then it has been hand-modified in ways
that are not possible to do using the .ui file
(though they might be doable in the subclass instead),
and the .ui file has been moved to a non-active name.
If this command is revived, either those changes need
abandoning or to be done in the subclass (if the .ui file
is also revived), or (preferably) the .ui file should be
removed and the UI rewritten to use the PM module.

The comment from pyuic claims that it was last created
from the .ui file on this date:
# Created: Wed Sep 27 14:24:15 2006
#      by: PyQt4 UI code generator 4.0.1
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from utilities.icon_utilities import geticon
#@from PM.PM_Constants import getHeaderFont
#@from PM.PM_Constants import pmLabelLeftAlignment

class Ui_PovrayScenePropDialog(object):
    def setupUi(self, PovrayScenePropDialog):
        PovrayScenePropDialog.setObjectName("PovrayScenePropDialog")
        PovrayScenePropDialog.resize(QtCore.QSize(QtCore.QRect(0,0,207,368).size()).expandedTo(PovrayScenePropDialog.minimumSizeHint()))

        self.vboxlayout = QtWidgets.QVBoxLayout(PovrayScenePropDialog)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.heading_frame = QtWidgets.QFrame(PovrayScenePropDialog)
        self.heading_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.heading_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.heading_frame.setObjectName("heading_frame")

        self.hboxlayout = QtWidgets.QHBoxLayout(self.heading_frame)
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(3)
        self.hboxlayout.setObjectName("hboxlayout")

        self.heading_pixmap = QtWidgets.QLabel(self.heading_frame)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(0),QtWidgets.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heading_pixmap.sizePolicy().hasHeightForWidth())
        self.heading_pixmap.setSizePolicy(sizePolicy)
        self.heading_pixmap.setScaledContents(True)
        self.heading_pixmap.setAlignment(QtCore.Qt.AlignVCenter)
        self.heading_pixmap.setObjectName("heading_pixmap")
        self.hboxlayout.addWidget(self.heading_pixmap)

        self.heading_label = QtWidgets.QLabel(self.heading_frame)
        #@self.heading_label.setFont(getHeaderFont())
        #@self.heading_label.setAlignment(pmLabelLeftAlignment)
        self.hboxlayout.addWidget(self.heading_label)
        self.vboxlayout.addWidget(self.heading_frame)

        self.body_frame = QtWidgets.QFrame(PovrayScenePropDialog)
        self.body_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body_frame.setObjectName("body_frame")

        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.body_frame)
        self.vboxlayout1.setContentsMargins(3, 3, 3, 3)
        self.vboxlayout1.setSpacing(3)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.sponsor_btn = QtWidgets.QPushButton(self.body_frame)
        self.sponsor_btn.setAutoDefault(False)
        self.sponsor_btn.setFlat(True)
        self.sponsor_btn.setObjectName("sponsor_btn")
        self.vboxlayout1.addWidget(self.sponsor_btn)

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        spacerItem = QtWidgets.QSpacerItem(35,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)

        self.done_btn = QtWidgets.QToolButton(self.body_frame)
        self.done_btn.setIcon(
            geticon("ui/actions/Properties Manager/Done.png"))
        self.done_btn.setObjectName("done_btn")
        self.hboxlayout1.addWidget(self.done_btn)

        self.abort_btn = QtWidgets.QToolButton(self.body_frame)
        self.abort_btn.setIcon(
            geticon("ui/actions/Properties Manager/Abort.png"))
        self.abort_btn.setObjectName("abort_btn")
        self.hboxlayout1.addWidget(self.abort_btn)

        self.restore_btn = QtWidgets.QToolButton(self.body_frame)
        self.restore_btn.setIcon(
            geticon("ui/actions/Properties Manager/Restore.png"))
        self.restore_btn.setObjectName("restore_btn")
        self.hboxlayout1.addWidget(self.restore_btn)

        self.preview_btn = QtWidgets.QToolButton(self.body_frame)
        self.preview_btn.setIcon(
            geticon("ui/actions/Properties Manager/Preview.png"))
        self.preview_btn.setObjectName("preview_btn")
        self.hboxlayout1.addWidget(self.preview_btn)

        self.whatsthis_btn = QtWidgets.QToolButton(self.body_frame)
        self.whatsthis_btn.setIcon(
            geticon("ui/actions/Properties Manager/WhatsThis.png"))
        self.whatsthis_btn.setObjectName("whatsthis_btn")
        self.hboxlayout1.addWidget(self.whatsthis_btn)

        spacerItem1 = QtWidgets.QSpacerItem(35,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.vboxlayout1.addLayout(self.hboxlayout1)

        self.name_grpbox = QtWidgets.QGroupBox(self.body_frame)
        self.name_grpbox.setObjectName("name_grpbox")

        self.vboxlayout2 = QtWidgets.QVBoxLayout(self.name_grpbox)
        self.vboxlayout2.setContentsMargins(4, 4, 4, 4)
        self.vboxlayout2.setSpacing(1)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.name_grpbox_label = QtWidgets.QLabel(self.name_grpbox)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(5),QtWidgets.QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_grpbox_label.sizePolicy().hasHeightForWidth())
        self.name_grpbox_label.setSizePolicy(sizePolicy)
        self.name_grpbox_label.setAlignment(QtCore.Qt.AlignVCenter)
        self.name_grpbox_label.setObjectName("name_grpbox_label")
        self.hboxlayout2.addWidget(self.name_grpbox_label)

        spacerItem2 = QtWidgets.QSpacerItem(67,16,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem2)

        self.grpbtn_1 = QtWidgets.QPushButton(self.name_grpbox)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(0),QtWidgets.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpbtn_1.sizePolicy().hasHeightForWidth())
        self.grpbtn_1.setSizePolicy(sizePolicy)
        self.grpbtn_1.setMaximumSize(QtCore.QSize(16,16))
        self.grpbtn_1.setIcon(
            geticon("ui/actions/Properties Manager/Group_Button.png"))
        self.grpbtn_1.setAutoDefault(False)
        self.grpbtn_1.setFlat(True)
        self.grpbtn_1.setObjectName("grpbtn_1")
        self.hboxlayout2.addWidget(self.grpbtn_1)
        self.vboxlayout2.addLayout(self.hboxlayout2)

        self.line2 = QtWidgets.QFrame(self.name_grpbox)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setMidLineWidth(0)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.vboxlayout2.addWidget(self.line2)

        self.name_linedit = QtWidgets.QLineEdit(self.name_grpbox)
        self.name_linedit.setObjectName("name_linedit")
        self.vboxlayout2.addWidget(self.name_linedit)
        self.vboxlayout1.addWidget(self.name_grpbox)

        self.output_image_grpbox = QtWidgets.QGroupBox(self.body_frame)
        self.output_image_grpbox.setCheckable(False)
        self.output_image_grpbox.setChecked(False)
        self.output_image_grpbox.setObjectName("output_image_grpbox")

        self.vboxlayout3 = QtWidgets.QVBoxLayout(self.output_image_grpbox)
        self.vboxlayout3.setContentsMargins(4, 4, 4, 4)
        self.vboxlayout3.setSpacing(1)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.hboxlayout3 = QtWidgets.QHBoxLayout()
        self.hboxlayout3.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.image_size_grpbox_label = QtWidgets.QLabel(self.output_image_grpbox)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(5),QtWidgets.QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_size_grpbox_label.sizePolicy().hasHeightForWidth())
        self.image_size_grpbox_label.setSizePolicy(sizePolicy)
        self.image_size_grpbox_label.setAlignment(QtCore.Qt.AlignVCenter)
        self.image_size_grpbox_label.setObjectName("image_size_grpbox_label")
        self.hboxlayout3.addWidget(self.image_size_grpbox_label)

        spacerItem3 = QtWidgets.QSpacerItem(40,16,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem3)

        self.grpbtn_2 = QtWidgets.QPushButton(self.output_image_grpbox)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(0),QtWidgets.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpbtn_2.sizePolicy().hasHeightForWidth())
        self.grpbtn_2.setSizePolicy(sizePolicy)
        self.grpbtn_2.setMaximumSize(QtCore.QSize(16,16))
        self.grpbtn_2.setIcon(
            geticon("ui/actions/Properties Manager/Group_Button.png"))
        self.grpbtn_2.setAutoDefault(False)
        self.grpbtn_2.setFlat(True)
        self.grpbtn_2.setObjectName("grpbtn_2")
        self.hboxlayout3.addWidget(self.grpbtn_2)
        self.vboxlayout3.addLayout(self.hboxlayout3)

        self.line3 = QtWidgets.QFrame(self.output_image_grpbox)
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setMidLineWidth(0)
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line3")
        self.vboxlayout3.addWidget(self.line3)

        self.hboxlayout4 = QtWidgets.QHBoxLayout()
        self.hboxlayout4.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.vboxlayout4 = QtWidgets.QVBoxLayout()
        self.vboxlayout4.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.output_type_label = QtWidgets.QLabel(self.output_image_grpbox)
        self.output_type_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output_type_label.setObjectName("output_type_label")
        self.vboxlayout4.addWidget(self.output_type_label)

        self.width_label = QtWidgets.QLabel(self.output_image_grpbox)
        self.width_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.width_label.setObjectName("width_label")
        self.vboxlayout4.addWidget(self.width_label)

        self.height_label = QtWidgets.QLabel(self.output_image_grpbox)
        self.height_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.height_label.setObjectName("height_label")
        self.vboxlayout4.addWidget(self.height_label)

        self.aspect_ratio_label = QtWidgets.QLabel(self.output_image_grpbox)
        self.aspect_ratio_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.aspect_ratio_label.setObjectName("aspect_ratio_label")
        self.vboxlayout4.addWidget(self.aspect_ratio_label)
        self.hboxlayout4.addLayout(self.vboxlayout4)

        self.vboxlayout5 = QtWidgets.QVBoxLayout()
        self.vboxlayout5.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout5.setSpacing(6)
        self.vboxlayout5.setObjectName("vboxlayout5")

        self.output_type_combox = QtWidgets.QComboBox(self.output_image_grpbox)
        self.output_type_combox.setObjectName("output_type_combox")
        self.vboxlayout5.addWidget(self.output_type_combox)

        self.width_spinbox = QtWidgets.QSpinBox(self.output_image_grpbox)
        self.width_spinbox.setMaximum(5000)
        self.width_spinbox.setMinimum(20)
        self.width_spinbox.setProperty("value",QtCore.QVariant(1024))
        self.width_spinbox.setObjectName("width_spinbox")
        self.vboxlayout5.addWidget(self.width_spinbox)

        self.height_spinbox = QtWidgets.QSpinBox(self.output_image_grpbox)
        self.height_spinbox.setMaximum(5000)
        self.height_spinbox.setMinimum(20)
        self.height_spinbox.setProperty("value",QtCore.QVariant(768))
        self.height_spinbox.setObjectName("height_spinbox")
        self.vboxlayout5.addWidget(self.height_spinbox)

        self.aspect_ratio_value_label = QtWidgets.QLabel(self.output_image_grpbox)
        self.aspect_ratio_value_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.aspect_ratio_value_label.setObjectName("aspect_ratio_value_label")
        self.vboxlayout5.addWidget(self.aspect_ratio_value_label)
        self.hboxlayout4.addLayout(self.vboxlayout5)
        self.vboxlayout3.addLayout(self.hboxlayout4)
        self.vboxlayout1.addWidget(self.output_image_grpbox)
        self.vboxlayout.addWidget(self.body_frame)

        spacerItem4 = QtWidgets.QSpacerItem(20,16,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem4)

        self.hboxlayout5 = QtWidgets.QHBoxLayout()
        self.hboxlayout5.setContentsMargins(4, 4, 4, 4)
        self.hboxlayout5.setSpacing(6)
        self.hboxlayout5.setObjectName("hboxlayout5")

        spacerItem5 = QtWidgets.QSpacerItem(59,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem5)

        self.cancel_btn = QtWidgets.QPushButton(PovrayScenePropDialog)
        self.cancel_btn.setAutoDefault(False)
        self.cancel_btn.setObjectName("cancel_btn")
        self.hboxlayout5.addWidget(self.cancel_btn)

        self.ok_btn = QtWidgets.QPushButton(PovrayScenePropDialog)
        self.ok_btn.setAutoDefault(False)
        self.ok_btn.setObjectName("ok_btn")
        self.hboxlayout5.addWidget(self.ok_btn)
        self.vboxlayout.addLayout(self.hboxlayout5)

        self.retranslateUi(PovrayScenePropDialog)
        QtCore.QMetaObject.connectSlotsByName(PovrayScenePropDialog)

    def retranslateUi(self, PovrayScenePropDialog):
        PovrayScenePropDialog.setWindowTitle(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "POV-Ray Scene", None))
        PovrayScenePropDialog.setWindowIcon(QtGui.QIcon("ui/border/PovrayScene"))
        self.heading_label.setText(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "POV-Ray Scene", None))
        self.done_btn.setToolTip(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "OK", None))
        self.abort_btn.setToolTip(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "Cancel", None))
        self.restore_btn.setToolTip(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "Restore Defaults", None))
        self.preview_btn.setToolTip(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "Preview", None))
        self.whatsthis_btn.setToolTip(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "What\'s This Help", None))
        self.name_grpbox_label.setText(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "POV-Ray Scene Name", None))
        self.name_linedit.setToolTip(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "Name of POV-Ray Scene node in Model Tree", None))
        self.name_linedit.setText(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "POV-Ray Scene-1.pov", None))
        self.image_size_grpbox_label.setText(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "Render Image Parameters", None))
        self.output_type_label.setText(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "Output Type :", None))
        self.width_label.setText(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "Width :", None))
        self.height_label.setText(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "Height :", None))
        self.aspect_ratio_label.setText(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "Aspect Ratio :", None))
        self.output_type_combox.setToolTip(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "Output image format", None))
        self.output_type_combox.addItem(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "PNG", None))
        self.output_type_combox.addItem(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "BMP", None))
        self.width_spinbox.setToolTip(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "Width of output image", None))
        self.width_spinbox.setSuffix(QtCore.QCoreApplication.translate("PovrayScenePropDialog", " pixels", None))
        self.height_spinbox.setToolTip(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "Height of output image", None))
        self.height_spinbox.setSuffix(QtCore.QCoreApplication.translate("PovrayScenePropDialog", " pixels", None))
        self.aspect_ratio_value_label.setText(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "1.333 to 1", None))
        self.cancel_btn.setToolTip(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "Cancel", None))
        self.cancel_btn.setText(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "Cancel", None))
        self.ok_btn.setToolTip(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "OK", None))
        self.ok_btn.setText(QtCore.QCoreApplication.translate("PovrayScenePropDialog", "OK", None))
