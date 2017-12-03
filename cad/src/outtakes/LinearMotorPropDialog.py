# -*- coding: utf-8 -*-

# Copyright 2004-2007 Nanorex, Inc.  See LICENSE file for details.
# Form implementation generated from reading ui file 'LinearMotorPropDialog.ui'
#
# Created: Wed Sep 20 10:14:34 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LinearMotorPropDialog(object):
    def setupUi(self, LinearMotorPropDialog):
        LinearMotorPropDialog.setObjectName("LinearMotorPropDialog")
        LinearMotorPropDialog.resize(QtCore.QSize(QtCore.QRect(0,0,295,372).size()).expandedTo(LinearMotorPropDialog.minimumSizeHint()))
        LinearMotorPropDialog.setSizeGripEnabled(True)

        self.gridlayout = QtWidgets.QGridLayout(LinearMotorPropDialog)
        self.gridlayout.setContentsMargins(11, 11, 11, 11)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.groupBox3 = QtWidgets.QGroupBox(LinearMotorPropDialog)
        self.groupBox3.setObjectName("groupBox3")

        self.gridlayout1 = QtWidgets.QGridLayout(self.groupBox3)
        self.gridlayout1.setContentsMargins(11, 11, 11, 11)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.widthLineEdit = QtWidgets.QLineEdit(self.groupBox3)
        self.widthLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.widthLineEdit.setObjectName("widthLineEdit")
        self.gridlayout1.addWidget(self.widthLineEdit,1,1,1,1)

        self.textLabel3 = QtWidgets.QLabel(self.groupBox3)
        self.textLabel3.setObjectName("textLabel3")
        self.gridlayout1.addWidget(self.textLabel3,0,2,1,1)

        self.sradiusLineEdit = QtWidgets.QLineEdit(self.groupBox3)
        self.sradiusLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.sradiusLineEdit.setObjectName("sradiusLineEdit")
        self.gridlayout1.addWidget(self.sradiusLineEdit,2,1,1,1)

        self.lengthLineEdit = QtWidgets.QLineEdit(self.groupBox3)
        self.lengthLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.lengthLineEdit.setObjectName("lengthLineEdit")
        self.gridlayout1.addWidget(self.lengthLineEdit,0,1,1,1)

        self.textLabel3_3 = QtWidgets.QLabel(self.groupBox3)
        self.textLabel3_3.setObjectName("textLabel3_3")
        self.gridlayout1.addWidget(self.textLabel3_3,2,2,1,1)

        self.textLabel3_2 = QtWidgets.QLabel(self.groupBox3)
        self.textLabel3_2.setObjectName("textLabel3_2")
        self.gridlayout1.addWidget(self.textLabel3_2,1,2,1,1)

        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.jig_color_pixmap = QtWidgets.QLabel(self.groupBox3)
        self.jig_color_pixmap.setMinimumSize(QtCore.QSize(40,0))
        self.jig_color_pixmap.setScaledContents(True)
        self.jig_color_pixmap.setObjectName("jig_color_pixmap")
        self.hboxlayout1.addWidget(self.jig_color_pixmap)

        self.choose_color_btn = QtWidgets.QPushButton(self.groupBox3)
        self.choose_color_btn.setEnabled(True)
        self.choose_color_btn.setAutoDefault(False)
        self.choose_color_btn.setObjectName("choose_color_btn")
        self.hboxlayout1.addWidget(self.choose_color_btn)
        self.hboxlayout.addLayout(self.hboxlayout1)

        spacerItem = QtWidgets.QSpacerItem(46,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.gridlayout1.addLayout(self.hboxlayout,3,1,1,2)

        self.textLabel1_3 = QtWidgets.QLabel(self.groupBox3)
        self.textLabel1_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1_3.setObjectName("textLabel1_3")
        self.gridlayout1.addWidget(self.textLabel1_3,0,0,1,1)

        self.textLabel1_2_2 = QtWidgets.QLabel(self.groupBox3)
        self.textLabel1_2_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1_2_2.setObjectName("textLabel1_2_2")
        self.gridlayout1.addWidget(self.textLabel1_2_2,1,0,1,1)

        self.textLabel1_2_2_2 = QtWidgets.QLabel(self.groupBox3)
        self.textLabel1_2_2_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1_2_2_2.setObjectName("textLabel1_2_2_2")
        self.gridlayout1.addWidget(self.textLabel1_2_2_2,2,0,1,1)

        self.colorTextLabel = QtWidgets.QLabel(self.groupBox3)
        self.colorTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.colorTextLabel.setObjectName("colorTextLabel")
        self.gridlayout1.addWidget(self.colorTextLabel,3,0,1,1)
        self.gridlayout.addWidget(self.groupBox3,2,0,1,1)

        spacerItem1 = QtWidgets.QSpacerItem(20,16,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem1,3,0,1,1)

        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        spacerItem2 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem2)

        self.ok_btn = QtWidgets.QPushButton(LinearMotorPropDialog)
        self.ok_btn.setAutoDefault(False)
        self.ok_btn.setDefault(False)
        self.ok_btn.setObjectName("ok_btn")
        self.hboxlayout2.addWidget(self.ok_btn)

        self.cancel_btn = QtWidgets.QPushButton(LinearMotorPropDialog)
        self.cancel_btn.setAutoDefault(False)
        self.cancel_btn.setObjectName("cancel_btn")
        self.hboxlayout2.addWidget(self.cancel_btn)
        self.gridlayout.addLayout(self.hboxlayout2,4,0,1,1)

        self.hboxlayout3 = QtWidgets.QHBoxLayout()
        self.hboxlayout3.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.nameTextLabel = QtWidgets.QLabel(LinearMotorPropDialog)
        self.nameTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nameTextLabel.setObjectName("nameTextLabel")
        self.vboxlayout.addWidget(self.nameTextLabel)

        self.textLabel1 = QtWidgets.QLabel(LinearMotorPropDialog)

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
        self.vboxlayout.addWidget(self.textLabel1)

        self.textLabel1_2 = QtWidgets.QLabel(LinearMotorPropDialog)
        self.textLabel1_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1_2.setObjectName("textLabel1_2")
        self.vboxlayout.addWidget(self.textLabel1_2)
        self.hboxlayout3.addLayout(self.vboxlayout)

        self.gridlayout2 = QtWidgets.QGridLayout()
        self.gridlayout2.setContentsMargins(0, 0, 0, 0)
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setObjectName("gridlayout2")

        self.forceLineEdit = QtWidgets.QLineEdit(LinearMotorPropDialog)
        self.forceLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.forceLineEdit.setObjectName("forceLineEdit")
        self.gridlayout2.addWidget(self.forceLineEdit,1,0,1,1)

        self.textLabel2 = QtWidgets.QLabel(LinearMotorPropDialog)
        self.textLabel2.setObjectName("textLabel2")
        self.gridlayout2.addWidget(self.textLabel2,2,1,1,1)

        self.textLabel1_4 = QtWidgets.QLabel(LinearMotorPropDialog)
        self.textLabel1_4.setObjectName("textLabel1_4")
        self.gridlayout2.addWidget(self.textLabel1_4,1,1,1,1)

        self.nameLineEdit = QtWidgets.QLineEdit(LinearMotorPropDialog)
        self.nameLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.nameLineEdit.setReadOnly(False)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.gridlayout2.addWidget(self.nameLineEdit,0,0,1,2)

        self.stiffnessLineEdit = QtWidgets.QLineEdit(LinearMotorPropDialog)
        self.stiffnessLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.stiffnessLineEdit.setObjectName("stiffnessLineEdit")
        self.gridlayout2.addWidget(self.stiffnessLineEdit,2,0,1,1)
        self.hboxlayout3.addLayout(self.gridlayout2)

        spacerItem3 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem3)
        self.gridlayout.addLayout(self.hboxlayout3,0,0,1,1)

        self.hboxlayout4 = QtWidgets.QHBoxLayout()
        self.hboxlayout4.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.textLabel1_5 = QtWidgets.QLabel(LinearMotorPropDialog)
        self.textLabel1_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1_5.setObjectName("textLabel1_5")
        self.hboxlayout4.addWidget(self.textLabel1_5)

        self.enable_minimize_checkbox = QtWidgets.QCheckBox(LinearMotorPropDialog)
        self.enable_minimize_checkbox.setObjectName("enable_minimize_checkbox")
        self.hboxlayout4.addWidget(self.enable_minimize_checkbox)

        spacerItem4 = QtWidgets.QSpacerItem(92,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem4)
        self.gridlayout.addLayout(self.hboxlayout4,1,0,1,1)
        #self.textLabel1.setBuddy(LinearMotorPropDialog.lineEdit9)
        #self.textLabel1_2.setBuddy(LinearMotorPropDialog.lineEdit9_2)

        self.retranslateUi(LinearMotorPropDialog)
        self.cancel_btn.clicked.connect(LinearMotorPropDialog.reject)
        self.ok_btn.clicked.connect(LinearMotorPropDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(LinearMotorPropDialog)
        LinearMotorPropDialog.setTabOrder(self.nameLineEdit,self.forceLineEdit)
        LinearMotorPropDialog.setTabOrder(self.forceLineEdit,self.stiffnessLineEdit)
        LinearMotorPropDialog.setTabOrder(self.stiffnessLineEdit,self.enable_minimize_checkbox)
        LinearMotorPropDialog.setTabOrder(self.enable_minimize_checkbox,self.lengthLineEdit)
        LinearMotorPropDialog.setTabOrder(self.lengthLineEdit,self.widthLineEdit)
        LinearMotorPropDialog.setTabOrder(self.widthLineEdit,self.sradiusLineEdit)
        LinearMotorPropDialog.setTabOrder(self.sradiusLineEdit,self.choose_color_btn)
        LinearMotorPropDialog.setTabOrder(self.choose_color_btn,self.ok_btn)
        LinearMotorPropDialog.setTabOrder(self.ok_btn,self.cancel_btn)

    def retranslateUi(self, LinearMotorPropDialog):
        LinearMotorPropDialog.setWindowTitle(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Linear Motor Properties", None))
        LinearMotorPropDialog.setWindowIcon(QtGui.QIcon("ui/border/LinearMotor"))
        self.groupBox3.setTitle(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Size and Color", None))
        self.textLabel3.setText(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Angstroms", None))
        self.textLabel3_3.setText(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Angstroms", None))
        self.textLabel3_2.setText(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Angstroms", None))
        self.choose_color_btn.setText(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Choose...", None))
        self.textLabel1_3.setText(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Motor Length:", None))
        self.textLabel1_2_2.setText(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Motor Width:", None))
        self.textLabel1_2_2_2.setText(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Spoke Radius:", None))
        self.colorTextLabel.setText(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Color:", None))
        self.ok_btn.setText(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "&OK", None))
        self.ok_btn.setShortcut(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Alt+O", None))
        self.cancel_btn.setText(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "&Cancel", None))
        self.cancel_btn.setShortcut(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Alt+C", None))
        self.nameTextLabel.setText(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Name:", None))
        self.textLabel1.setText(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Force:", None))
        self.textLabel1_2.setText(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Stiffness:", None))
        self.forceLineEdit.setToolTip(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Simulations will begin with the motor\'s force set to this value.", None))
        self.textLabel2.setText(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "N/m", None))
        self.textLabel1_4.setText(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "pN", None))
        self.nameLineEdit.setToolTip(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Name of Linear Motor", None))
        self.stiffnessLineEdit.setToolTip(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Simulations will begin with the motor\'s stiffness set to this value.", None))
        self.textLabel1_5.setToolTip(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "If checked, the force value is applied to the motor\'s atoms during minimization.", None))
        self.textLabel1_5.setText(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "Enable in Minimize (experimental) :", None))
        self.enable_minimize_checkbox.setToolTip(QtCore.QCoreApplication.translate("LinearMotorPropDialog", "If checked, the force value is applied to the motor\'s atoms during minimization.", None))
