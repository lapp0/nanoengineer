# -*- coding: utf-8 -*-

# Copyright 2004-2007 Nanorex, Inc.  See LICENSE file for details.
# Form implementation generated from reading ui file 'RotaryMotorPropDialog.ui'
#
# Created: Wed Sep 20 10:35:36 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RotaryMotorPropDialog(object):
    def setupUi(self, RotaryMotorPropDialog):
        RotaryMotorPropDialog.setObjectName("RotaryMotorPropDialog")
        RotaryMotorPropDialog.resize(QtCore.QSize(QtCore.QRect(0,0,298,424).size()).expandedTo(RotaryMotorPropDialog.minimumSizeHint()))
        #RotaryMotorPropDialog.setSizeGripEnabled(True)

        self.vboxlayout = QtWidgets.QVBoxLayout(RotaryMotorPropDialog)
        self.vboxlayout.setContentsMargins(11, 11, 11, 11)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.vboxlayout1 = QtWidgets.QVBoxLayout()
        self.vboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.nameTextLabel = QtWidgets.QLabel(RotaryMotorPropDialog)
        self.nameTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nameTextLabel.setObjectName("nameTextLabel")
        self.vboxlayout1.addWidget(self.nameTextLabel)

        self.textLabel1 = QtWidgets.QLabel(RotaryMotorPropDialog)

        font = QtGui.QFont(self.textLabel1.font())
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.textLabel1.setFont(font)
        self.textLabel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1.setObjectName("textLabel1")
        self.vboxlayout1.addWidget(self.textLabel1)

        self.textLabel1_2_3 = QtWidgets.QLabel(RotaryMotorPropDialog)
        self.textLabel1_2_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1_2_3.setObjectName("textLabel1_2_3")
        self.vboxlayout1.addWidget(self.textLabel1_2_3)

        self.textLabel1_2 = QtWidgets.QLabel(RotaryMotorPropDialog)
        self.textLabel1_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1_2.setObjectName("textLabel1_2")
        self.vboxlayout1.addWidget(self.textLabel1_2)
        self.hboxlayout1.addLayout(self.vboxlayout1)

        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.nameLineEdit = QtWidgets.QLineEdit(RotaryMotorPropDialog)
        self.nameLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.nameLineEdit.setReadOnly(False)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.gridlayout.addWidget(self.nameLineEdit,0,0,1,2)

        self.torqueLineEdit = QtWidgets.QLineEdit(RotaryMotorPropDialog)
        self.torqueLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.torqueLineEdit.setObjectName("torqueLineEdit")
        self.gridlayout.addWidget(self.torqueLineEdit,1,0,1,1)

        self.speedLineEdit = QtWidgets.QLineEdit(RotaryMotorPropDialog)
        self.speedLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.speedLineEdit.setObjectName("speedLineEdit")
        self.gridlayout.addWidget(self.speedLineEdit,3,0,1,1)

        self.textLabel1_4 = QtWidgets.QLabel(RotaryMotorPropDialog)
        self.textLabel1_4.setObjectName("textLabel1_4")
        self.gridlayout.addWidget(self.textLabel1_4,1,1,1,1)

        self.textLabel2 = QtWidgets.QLabel(RotaryMotorPropDialog)
        self.textLabel2.setObjectName("textLabel2")
        self.gridlayout.addWidget(self.textLabel2,3,1,1,1)

        self.textLabel2_2 = QtWidgets.QLabel(RotaryMotorPropDialog)
        self.textLabel2_2.setObjectName("textLabel2_2")
        self.gridlayout.addWidget(self.textLabel2_2,2,1,1,1)

        self.initialSpeedLineEdit = QtWidgets.QLineEdit(RotaryMotorPropDialog)
        self.initialSpeedLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.initialSpeedLineEdit.setObjectName("initialSpeedLineEdit")
        self.gridlayout.addWidget(self.initialSpeedLineEdit,2,0,1,1)
        self.hboxlayout1.addLayout(self.gridlayout)
        self.hboxlayout.addLayout(self.hboxlayout1)

        spacerItem = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.vboxlayout2 = QtWidgets.QVBoxLayout()
        self.vboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.dampers_textlabel = QtWidgets.QLabel(RotaryMotorPropDialog)
        self.dampers_textlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dampers_textlabel.setObjectName("dampers_textlabel")
        self.vboxlayout2.addWidget(self.dampers_textlabel)

        self.textLabel1_5 = QtWidgets.QLabel(RotaryMotorPropDialog)
        self.textLabel1_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1_5.setObjectName("textLabel1_5")
        self.vboxlayout2.addWidget(self.textLabel1_5)
        self.hboxlayout2.addLayout(self.vboxlayout2)

        self.vboxlayout3 = QtWidgets.QVBoxLayout()
        self.vboxlayout3.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.dampers_checkbox = QtWidgets.QCheckBox(RotaryMotorPropDialog)
        self.dampers_checkbox.setObjectName("dampers_checkbox")
        self.vboxlayout3.addWidget(self.dampers_checkbox)

        self.enable_minimize_checkbox = QtWidgets.QCheckBox(RotaryMotorPropDialog)
        self.enable_minimize_checkbox.setObjectName("enable_minimize_checkbox")
        self.vboxlayout3.addWidget(self.enable_minimize_checkbox)
        self.hboxlayout2.addLayout(self.vboxlayout3)

        spacerItem1 = QtWidgets.QSpacerItem(20,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem1)
        self.vboxlayout.addLayout(self.hboxlayout2)

        self.groupBox1 = QtWidgets.QGroupBox(RotaryMotorPropDialog)
        self.groupBox1.setObjectName("groupBox1")

        self.gridlayout1 = QtWidgets.QGridLayout(self.groupBox1)
        self.gridlayout1.setContentsMargins(11, 11, 11, 11)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.hboxlayout3 = QtWidgets.QHBoxLayout()
        self.hboxlayout3.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.hboxlayout4 = QtWidgets.QHBoxLayout()
        self.hboxlayout4.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.jig_color_pixmap = QtWidgets.QLabel(self.groupBox1)
        self.jig_color_pixmap.setMinimumSize(QtCore.QSize(40,0))
        self.jig_color_pixmap.setScaledContents(True)
        self.jig_color_pixmap.setObjectName("jig_color_pixmap")
        self.hboxlayout4.addWidget(self.jig_color_pixmap)

        self.choose_color_btn = QtWidgets.QPushButton(self.groupBox1)
        self.choose_color_btn.setEnabled(True)
        self.choose_color_btn.setAutoDefault(False)
        self.choose_color_btn.setObjectName("choose_color_btn")
        self.hboxlayout4.addWidget(self.choose_color_btn)
        self.hboxlayout3.addLayout(self.hboxlayout4)

        spacerItem2 = QtWidgets.QSpacerItem(46,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem2)
        self.gridlayout1.addLayout(self.hboxlayout3,3,1,1,2)

        self.textLabel1_2_2_2 = QtWidgets.QLabel(self.groupBox1)
        self.textLabel1_2_2_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1_2_2_2.setObjectName("textLabel1_2_2_2")
        self.gridlayout1.addWidget(self.textLabel1_2_2_2,2,0,1,1)

        self.textLabel1_3 = QtWidgets.QLabel(self.groupBox1)
        self.textLabel1_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1_3.setObjectName("textLabel1_3")
        self.gridlayout1.addWidget(self.textLabel1_3,0,0,1,1)

        self.textLabel1_2_2 = QtWidgets.QLabel(self.groupBox1)
        self.textLabel1_2_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1_2_2.setObjectName("textLabel1_2_2")
        self.gridlayout1.addWidget(self.textLabel1_2_2,1,0,1,1)

        self.colorTextLabel = QtWidgets.QLabel(self.groupBox1)
        self.colorTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.colorTextLabel.setObjectName("colorTextLabel")
        self.gridlayout1.addWidget(self.colorTextLabel,3,0,1,1)

        self.lengthLineEdit = QtWidgets.QLineEdit(self.groupBox1)
        self.lengthLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.lengthLineEdit.setObjectName("lengthLineEdit")
        self.gridlayout1.addWidget(self.lengthLineEdit,0,1,1,1)

        self.sradiusLineEdit = QtWidgets.QLineEdit(self.groupBox1)
        self.sradiusLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.sradiusLineEdit.setObjectName("sradiusLineEdit")
        self.gridlayout1.addWidget(self.sradiusLineEdit,2,1,1,1)

        self.radiusLineEdit = QtWidgets.QLineEdit(self.groupBox1)
        self.radiusLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.radiusLineEdit.setObjectName("radiusLineEdit")
        self.gridlayout1.addWidget(self.radiusLineEdit,1,1,1,1)

        self.textLabel3_2 = QtWidgets.QLabel(self.groupBox1)
        self.textLabel3_2.setObjectName("textLabel3_2")
        self.gridlayout1.addWidget(self.textLabel3_2,1,2,1,1)

        self.textLabel3 = QtWidgets.QLabel(self.groupBox1)
        self.textLabel3.setObjectName("textLabel3")
        self.gridlayout1.addWidget(self.textLabel3,0,2,1,1)

        self.textLabel3_3 = QtWidgets.QLabel(self.groupBox1)
        self.textLabel3_3.setObjectName("textLabel3_3")
        self.gridlayout1.addWidget(self.textLabel3_3,2,2,1,1)
        self.vboxlayout.addWidget(self.groupBox1)

        spacerItem3 = QtWidgets.QSpacerItem(20,16,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem3)

        self.hboxlayout5 = QtWidgets.QHBoxLayout()
        self.hboxlayout5.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout5.setSpacing(6)
        self.hboxlayout5.setObjectName("hboxlayout5")

        spacerItem4 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem4)

        self.ok_btn = QtWidgets.QPushButton(RotaryMotorPropDialog)
        self.ok_btn.setAutoDefault(False)
        self.ok_btn.setDefault(False)
        self.ok_btn.setObjectName("ok_btn")
        self.hboxlayout5.addWidget(self.ok_btn)

        self.cancel_btn = QtWidgets.QPushButton(RotaryMotorPropDialog)
        self.cancel_btn.setAutoDefault(False)
        self.cancel_btn.setObjectName("cancel_btn")
        self.hboxlayout5.addWidget(self.cancel_btn)
        self.vboxlayout.addLayout(self.hboxlayout5)
        #self.textLabel1.setBuddy(RotaryMotorPropDialog.lineEdit9)
        #self.textLabel1_2_3.setBuddy(RotaryMotorPropDialog.lineEdit9_2)
        #self.textLabel1_2.setBuddy(RotaryMotorPropDialog.lineEdit9_2)

        self.retranslateUi(RotaryMotorPropDialog)
        self.cancel_btn.clicked.connect(RotaryMotorPropDialog.reject)
        self.ok_btn.clicked.connect(RotaryMotorPropDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(RotaryMotorPropDialog)
        RotaryMotorPropDialog.setTabOrder(self.nameLineEdit,self.torqueLineEdit)
        RotaryMotorPropDialog.setTabOrder(self.torqueLineEdit,self.initialSpeedLineEdit)
        RotaryMotorPropDialog.setTabOrder(self.initialSpeedLineEdit,self.speedLineEdit)
        RotaryMotorPropDialog.setTabOrder(self.speedLineEdit,self.enable_minimize_checkbox)
        RotaryMotorPropDialog.setTabOrder(self.enable_minimize_checkbox,self.lengthLineEdit)
        RotaryMotorPropDialog.setTabOrder(self.lengthLineEdit,self.radiusLineEdit)
        RotaryMotorPropDialog.setTabOrder(self.radiusLineEdit,self.sradiusLineEdit)
        RotaryMotorPropDialog.setTabOrder(self.sradiusLineEdit,self.choose_color_btn)
        RotaryMotorPropDialog.setTabOrder(self.choose_color_btn,self.ok_btn)
        RotaryMotorPropDialog.setTabOrder(self.ok_btn,self.cancel_btn)

    def retranslateUi(self, RotaryMotorPropDialog):
        RotaryMotorPropDialog.setWindowTitle(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Rotary Motor Properties", None))
        RotaryMotorPropDialog.setWindowIcon(QtGui.QIcon("ui/border/RotaryMotor"))
        self.nameTextLabel.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Name :", None))
        self.textLabel1.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Torque :", None))
        self.textLabel1_2_3.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Initial Speed :", None))
        self.textLabel1_2.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Final Speed :", None))
        self.nameLineEdit.setToolTip(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Name of rotary motor.", None))
        self.torqueLineEdit.setToolTip(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Simulations will begin with the motor\'s torque set to this value.", None))
        self.speedLineEdit.setToolTip(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "The final velocity of the motor\'s flywheel.", None))
        self.textLabel1_4.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "nN-nm", None))
        self.textLabel2.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "GHz", None))
        self.textLabel2_2.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "GHz", None))
        self.initialSpeedLineEdit.setToolTip(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "The beginning velocity of the motor\'s flywheel.", None))
        self.dampers_textlabel.setToolTip(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "If checked, dampers are enabled in the simulator.", None))
        self.dampers_textlabel.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Dampers :", None))
        self.textLabel1_5.setToolTip(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "If checked, the torque value is applied to the motor\'s atoms during minimization.", None))
        self.textLabel1_5.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Enable in Minimize (experimental) :", None))
        self.dampers_checkbox.setToolTip(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "If checked, dampers are enabled in the simulator.", None))
        self.enable_minimize_checkbox.setToolTip(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "If checked, the torque value is applied to the motor\'s atoms during minimization.", None))
        self.groupBox1.setTitle(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Size and Color", None))
        self.choose_color_btn.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Choose...", None))
        self.textLabel1_2_2_2.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Spoke Radius :", None))
        self.textLabel1_3.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Motor Length :", None))
        self.textLabel1_2_2.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Motor Radius :", None))
        self.colorTextLabel.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Color :", None))
        self.textLabel3_2.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Angstroms", None))
        self.textLabel3.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Angstroms", None))
        self.textLabel3_3.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Angstroms", None))
        self.ok_btn.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "&OK", None))
        self.ok_btn.setShortcut(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Alt+O", None))
        self.cancel_btn.setText(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "&Cancel", None))
        self.cancel_btn.setShortcut(QtCore.QCoreApplication.translate("RotaryMotorPropDialog", "Alt+C", None))
