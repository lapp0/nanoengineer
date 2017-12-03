# -*- coding: utf-8 -*-

# Copyright 2005-2007 Nanorex, Inc.  See LICENSE file for details.
# Form implementation generated from reading ui file 'ThermoPropDialog.ui'
#
# Created: Wed Sep 20 08:56:21 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ThermoPropDialog(object):
    def setupUi(self, ThermoPropDialog):
        ThermoPropDialog.setObjectName("ThermoPropDialog")
        ThermoPropDialog.resize(QtCore.QSize(QtCore.QRect(0,0,307,170).size()).expandedTo(ThermoPropDialog.minimumSizeHint()))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(7),QtWidgets.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ThermoPropDialog.sizePolicy().hasHeightForWidth())
        ThermoPropDialog.setSizePolicy(sizePolicy)
        ThermoPropDialog.setSizeGripEnabled(True)

        self.vboxlayout = QtWidgets.QVBoxLayout(ThermoPropDialog)
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

        self.nameTextLabel = QtWidgets.QLabel(ThermoPropDialog)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(5),QtWidgets.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameTextLabel.sizePolicy().hasHeightForWidth())
        self.nameTextLabel.setSizePolicy(sizePolicy)
        self.nameTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nameTextLabel.setObjectName("nameTextLabel")
        self.vboxlayout1.addWidget(self.nameTextLabel)

        self.molnameTextLabel = QtWidgets.QLabel(ThermoPropDialog)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(5),QtWidgets.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.molnameTextLabel.sizePolicy().hasHeightForWidth())
        self.molnameTextLabel.setSizePolicy(sizePolicy)
        self.molnameTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.molnameTextLabel.setObjectName("molnameTextLabel")
        self.vboxlayout1.addWidget(self.molnameTextLabel)

        self.colorTextLabel = QtWidgets.QLabel(ThermoPropDialog)
        self.colorTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.colorTextLabel.setObjectName("colorTextLabel")
        self.vboxlayout1.addWidget(self.colorTextLabel)
        self.hboxlayout.addLayout(self.vboxlayout1)

        self.vboxlayout2 = QtWidgets.QVBoxLayout()
        self.vboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.nameLineEdit = QtWidgets.QLineEdit(ThermoPropDialog)
        self.nameLineEdit.setEnabled(True)
        self.nameLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.vboxlayout2.addWidget(self.nameLineEdit)

        self.molnameLineEdit = QtWidgets.QLineEdit(ThermoPropDialog)
        self.molnameLineEdit.setEnabled(True)
        self.molnameLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.molnameLineEdit.setReadOnly(True)
        self.molnameLineEdit.setObjectName("molnameLineEdit")
        self.vboxlayout2.addWidget(self.molnameLineEdit)

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.jig_color_pixmap = QtWidgets.QLabel(ThermoPropDialog)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(5),QtWidgets.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jig_color_pixmap.sizePolicy().hasHeightForWidth())
        self.jig_color_pixmap.setSizePolicy(sizePolicy)
        self.jig_color_pixmap.setMinimumSize(QtCore.QSize(40,0))
        self.jig_color_pixmap.setScaledContents(True)
        self.jig_color_pixmap.setObjectName("jig_color_pixmap")
        self.hboxlayout2.addWidget(self.jig_color_pixmap)

        self.choose_color_btn = QtWidgets.QPushButton(ThermoPropDialog)
        self.choose_color_btn.setEnabled(True)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(1),QtWidgets.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_color_btn.sizePolicy().hasHeightForWidth())
        self.choose_color_btn.setSizePolicy(sizePolicy)
        self.choose_color_btn.setAutoDefault(False)
        self.choose_color_btn.setObjectName("choose_color_btn")
        self.hboxlayout2.addWidget(self.choose_color_btn)
        self.hboxlayout1.addLayout(self.hboxlayout2)

        spacerItem = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.vboxlayout2.addLayout(self.hboxlayout1)
        self.hboxlayout.addLayout(self.vboxlayout2)
        self.vboxlayout.addLayout(self.hboxlayout)

        spacerItem1 = QtWidgets.QSpacerItem(20,25,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem1)

        self.hboxlayout3 = QtWidgets.QHBoxLayout()
        self.hboxlayout3.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        spacerItem2 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem2)

        self.ok_btn = QtWidgets.QPushButton(ThermoPropDialog)
        self.ok_btn.setMinimumSize(QtCore.QSize(0,0))
        self.ok_btn.setAutoDefault(False)
        self.ok_btn.setDefault(False)
        self.ok_btn.setObjectName("ok_btn")
        self.hboxlayout3.addWidget(self.ok_btn)

        self.cancel_btn = QtWidgets.QPushButton(ThermoPropDialog)
        self.cancel_btn.setMinimumSize(QtCore.QSize(0,0))
        self.cancel_btn.setAutoDefault(False)
        self.cancel_btn.setDefault(False)
        self.cancel_btn.setObjectName("cancel_btn")
        self.hboxlayout3.addWidget(self.cancel_btn)
        self.vboxlayout.addLayout(self.hboxlayout3)

        self.retranslateUi(ThermoPropDialog)
        self.cancel_btn.clicked.connect(ThermoPropDialog.reject)
        self.ok_btn.clicked.connect(ThermoPropDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(ThermoPropDialog)
        ThermoPropDialog.setTabOrder(self.nameLineEdit,self.molnameLineEdit)
        ThermoPropDialog.setTabOrder(self.molnameLineEdit,self.choose_color_btn)
        ThermoPropDialog.setTabOrder(self.choose_color_btn,self.ok_btn)
        ThermoPropDialog.setTabOrder(self.ok_btn,self.cancel_btn)

    def retranslateUi(self, ThermoPropDialog):
        ThermoPropDialog.setWindowTitle(QtCore.QCoreApplication.translate("ThermoPropDialog", "Thermometer Properties", None))
        self.nameTextLabel.setText(QtCore.QCoreApplication.translate("ThermoPropDialog", "Name:", None))
        self.molnameTextLabel.setText(QtCore.QCoreApplication.translate("ThermoPropDialog", "Attached to:", None))
        self.colorTextLabel.setText(QtCore.QCoreApplication.translate("ThermoPropDialog", "Color:", None))
        self.choose_color_btn.setToolTip(QtCore.QCoreApplication.translate("ThermoPropDialog", "Change color", None))
        self.choose_color_btn.setText(QtCore.QCoreApplication.translate("ThermoPropDialog", "Choose...", None))
        self.ok_btn.setText(QtCore.QCoreApplication.translate("ThermoPropDialog", "&OK", None))
        self.ok_btn.setShortcut(QtCore.QCoreApplication.translate("ThermoPropDialog", "Alt+O", None))
        self.cancel_btn.setText(QtCore.QCoreApplication.translate("ThermoPropDialog", "&Cancel", None))
        self.cancel_btn.setShortcut(QtCore.QCoreApplication.translate("ThermoPropDialog", "Alt+C", None))
