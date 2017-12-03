# -*- coding: utf-8 -*-

# Copyright 2004-2007 Nanorex, Inc.  See LICENSE file for details.
# Form implementation generated from reading ui file 'StatPropDialog.ui'
#
# Created: Wed Sep 20 09:07:17 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatPropDialog(object):
    def setupUi(self, StatPropDialog):
        StatPropDialog.setObjectName("StatPropDialog")
        StatPropDialog.resize(QtCore.QSize(QtCore.QRect(0,0,299,202).size()).expandedTo(StatPropDialog.minimumSizeHint()))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(7),QtWidgets.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StatPropDialog.sizePolicy().hasHeightForWidth())
        StatPropDialog.setSizePolicy(sizePolicy)
        StatPropDialog.setSizeGripEnabled(True)

        self.vboxlayout = QtWidgets.QVBoxLayout(StatPropDialog)
        self.vboxlayout.setContentsMargins(11, 11, 11, 11)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.vboxlayout1 = QtWidgets.QVBoxLayout()
        self.vboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.nameTextLabel = QtWidgets.QLabel(StatPropDialog)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(5),QtWidgets.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameTextLabel.sizePolicy().hasHeightForWidth())
        self.nameTextLabel.setSizePolicy(sizePolicy)
        self.nameTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nameTextLabel.setObjectName("nameTextLabel")
        self.vboxlayout1.addWidget(self.nameTextLabel)

        self.temp_lbl = QtWidgets.QLabel(StatPropDialog)
        self.temp_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temp_lbl.setObjectName("temp_lbl")
        self.vboxlayout1.addWidget(self.temp_lbl)

        self.molnameTextLabel = QtWidgets.QLabel(StatPropDialog)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(5),QtWidgets.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.molnameTextLabel.sizePolicy().hasHeightForWidth())
        self.molnameTextLabel.setSizePolicy(sizePolicy)
        self.molnameTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.molnameTextLabel.setObjectName("molnameTextLabel")
        self.vboxlayout1.addWidget(self.molnameTextLabel)

        self.colorTextLabel = QtWidgets.QLabel(StatPropDialog)
        self.colorTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.colorTextLabel.setObjectName("colorTextLabel")
        self.vboxlayout1.addWidget(self.colorTextLabel)
        self.hboxlayout.addLayout(self.vboxlayout1)

        self.vboxlayout2 = QtWidgets.QVBoxLayout()
        self.vboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.nameLineEdit = QtWidgets.QLineEdit(StatPropDialog)
        self.nameLineEdit.setEnabled(True)
        self.nameLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.vboxlayout2.addWidget(self.nameLineEdit)

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.tempSpinBox = QtWidgets.QSpinBox(StatPropDialog)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(1),QtWidgets.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tempSpinBox.sizePolicy().hasHeightForWidth())
        self.tempSpinBox.setSizePolicy(sizePolicy)
        self.tempSpinBox.setMaximum(9999)
        self.tempSpinBox.setProperty("value",QtCore.QVariant(300))
        self.tempSpinBox.setObjectName("tempSpinBox")
        self.hboxlayout2.addWidget(self.tempSpinBox)

        self.K_lbl = QtWidgets.QLabel(StatPropDialog)
        self.K_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.K_lbl.setObjectName("K_lbl")
        self.hboxlayout2.addWidget(self.K_lbl)
        self.hboxlayout1.addLayout(self.hboxlayout2)

        spacerItem = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.vboxlayout2.addLayout(self.hboxlayout1)

        self.molnameLineEdit = QtWidgets.QLineEdit(StatPropDialog)
        self.molnameLineEdit.setEnabled(True)
        self.molnameLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.molnameLineEdit.setReadOnly(True)
        self.molnameLineEdit.setObjectName("molnameLineEdit")
        self.vboxlayout2.addWidget(self.molnameLineEdit)

        self.hboxlayout3 = QtWidgets.QHBoxLayout()
        self.hboxlayout3.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.hboxlayout4 = QtWidgets.QHBoxLayout()
        self.hboxlayout4.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.jig_color_pixmap = QtWidgets.QLabel(StatPropDialog)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(5),QtWidgets.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jig_color_pixmap.sizePolicy().hasHeightForWidth())
        self.jig_color_pixmap.setSizePolicy(sizePolicy)
        self.jig_color_pixmap.setMinimumSize(QtCore.QSize(40,0))
        self.jig_color_pixmap.setScaledContents(True)
        self.jig_color_pixmap.setObjectName("jig_color_pixmap")
        self.hboxlayout4.addWidget(self.jig_color_pixmap)

        self.choose_color_btn = QtWidgets.QPushButton(StatPropDialog)
        self.choose_color_btn.setEnabled(True)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(1),QtWidgets.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_color_btn.sizePolicy().hasHeightForWidth())
        self.choose_color_btn.setSizePolicy(sizePolicy)
        self.choose_color_btn.setAutoDefault(False)
        self.choose_color_btn.setObjectName("choose_color_btn")
        self.hboxlayout4.addWidget(self.choose_color_btn)
        self.hboxlayout3.addLayout(self.hboxlayout4)

        spacerItem1 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem1)
        self.vboxlayout2.addLayout(self.hboxlayout3)
        self.hboxlayout.addLayout(self.vboxlayout2)
        self.vboxlayout.addLayout(self.hboxlayout)

        spacerItem2 = QtWidgets.QSpacerItem(20,20,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem2)

        self.hboxlayout5 = QtWidgets.QHBoxLayout()
        self.hboxlayout5.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout5.setSpacing(6)
        self.hboxlayout5.setObjectName("hboxlayout5")

        spacerItem3 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem3)

        self.ok_btn = QtWidgets.QPushButton(StatPropDialog)
        self.ok_btn.setMinimumSize(QtCore.QSize(0,0))
        self.ok_btn.setAutoDefault(False)
        self.ok_btn.setDefault(False)
        self.ok_btn.setObjectName("ok_btn")
        self.hboxlayout5.addWidget(self.ok_btn)

        self.cancel_btn = QtWidgets.QPushButton(StatPropDialog)
        self.cancel_btn.setMinimumSize(QtCore.QSize(0,0))
        self.cancel_btn.setAutoDefault(False)
        self.cancel_btn.setDefault(False)
        self.cancel_btn.setObjectName("cancel_btn")
        self.hboxlayout5.addWidget(self.cancel_btn)
        self.vboxlayout.addLayout(self.hboxlayout5)

        self.retranslateUi(StatPropDialog)
        self.cancel_btn.clicked.connect(StatPropDialog.reject)
        self.ok_btn.clicked.connect(StatPropDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(StatPropDialog)
        StatPropDialog.setTabOrder(self.nameLineEdit,self.tempSpinBox)
        StatPropDialog.setTabOrder(self.tempSpinBox,self.molnameLineEdit)
        StatPropDialog.setTabOrder(self.molnameLineEdit,self.choose_color_btn)
        StatPropDialog.setTabOrder(self.choose_color_btn,self.ok_btn)
        StatPropDialog.setTabOrder(self.ok_btn,self.cancel_btn)

    def retranslateUi(self, StatPropDialog):
        StatPropDialog.setWindowTitle(QtCore.QCoreApplication.translate("StatPropDialog", "Stat Properties", None))
        self.nameTextLabel.setText(QtCore.QCoreApplication.translate("StatPropDialog", "Name :", None))
        self.temp_lbl.setText(QtCore.QCoreApplication.translate("StatPropDialog", "Temperature :", None))
        self.molnameTextLabel.setText(QtCore.QCoreApplication.translate("StatPropDialog", "Attached to :", None))
        self.colorTextLabel.setText(QtCore.QCoreApplication.translate("StatPropDialog", "Color :", None))
        self.K_lbl.setText(QtCore.QCoreApplication.translate("StatPropDialog", "Kelvin", None))
        self.choose_color_btn.setToolTip(QtCore.QCoreApplication.translate("StatPropDialog", "Change color", None))
        self.choose_color_btn.setText(QtCore.QCoreApplication.translate("StatPropDialog", "Choose...", None))
        self.ok_btn.setText(QtCore.QCoreApplication.translate("StatPropDialog", "&OK", None))
        self.ok_btn.setShortcut(QtCore.QCoreApplication.translate("StatPropDialog", "Alt+O", None))
        self.cancel_btn.setText(QtCore.QCoreApplication.translate("StatPropDialog", "&Cancel", None))
        self.cancel_btn.setShortcut(QtCore.QCoreApplication.translate("StatPropDialog", "Alt+C", None))
