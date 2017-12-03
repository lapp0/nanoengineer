# -*- coding: utf-8 -*-

# Copyright 2005-2007 Nanorex, Inc.  See LICENSE file for details.
# Form implementation generated from reading ui file 'JigPropDialog.ui'
#
# Created: Wed Sep 20 07:56:23 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_JigPropDialog(object):
    def setupUi(self, JigPropDialog):
        JigPropDialog.setObjectName("JigPropDialog")
        JigPropDialog.resize(QtCore.QSize(QtCore.QRect(0,0,245,145).size()).expandedTo(JigPropDialog.minimumSizeHint()))
        JigPropDialog.setSizeGripEnabled(True)

        self.vboxlayout = QtWidgets.QVBoxLayout(JigPropDialog)
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

        self.nameTextLabel = QtWidgets.QLabel(JigPropDialog)
        self.nameTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nameTextLabel.setObjectName("nameTextLabel")
        self.vboxlayout1.addWidget(self.nameTextLabel)

        self.colorTextLabel = QtWidgets.QLabel(JigPropDialog)
        self.colorTextLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.colorTextLabel.setObjectName("colorTextLabel")
        self.vboxlayout1.addWidget(self.colorTextLabel)
        self.hboxlayout.addLayout(self.vboxlayout1)

        self.vboxlayout2 = QtWidgets.QVBoxLayout()
        self.vboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.nameLineEdit = QtWidgets.QLineEdit(JigPropDialog)
        self.nameLineEdit.setEnabled(True)
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

        self.jig_color_pixmap = QtWidgets.QLabel(JigPropDialog)
        self.jig_color_pixmap.setMinimumSize(QtCore.QSize(40,0))
        self.jig_color_pixmap.setScaledContents(True)
        self.jig_color_pixmap.setObjectName("jig_color_pixmap")
        self.hboxlayout2.addWidget(self.jig_color_pixmap)

        self.choose_color_btn = QtWidgets.QPushButton(JigPropDialog)
        self.choose_color_btn.setEnabled(True)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(5),QtWidgets.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_color_btn.sizePolicy().hasHeightForWidth())
        self.choose_color_btn.setSizePolicy(sizePolicy)
        self.choose_color_btn.setObjectName("choose_color_btn")
        self.hboxlayout2.addWidget(self.choose_color_btn)
        self.hboxlayout1.addLayout(self.hboxlayout2)

        spacerItem = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.vboxlayout2.addLayout(self.hboxlayout1)
        self.hboxlayout.addLayout(self.vboxlayout2)
        self.vboxlayout.addLayout(self.hboxlayout)

        spacerItem1 = QtWidgets.QSpacerItem(20,20,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem1)

        self.hboxlayout3 = QtWidgets.QHBoxLayout()
        self.hboxlayout3.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        spacerItem2 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem2)

        self.ok_btn = QtWidgets.QPushButton(JigPropDialog)
        self.ok_btn.setAutoDefault(True)
        self.ok_btn.setDefault(True)
        self.ok_btn.setObjectName("ok_btn")
        self.hboxlayout3.addWidget(self.ok_btn)

        self.cancel_btn = QtWidgets.QPushButton(JigPropDialog)
        self.cancel_btn.setAutoDefault(True)
        self.cancel_btn.setDefault(False)
        self.cancel_btn.setObjectName("cancel_btn")
        self.hboxlayout3.addWidget(self.cancel_btn)
        self.vboxlayout.addLayout(self.hboxlayout3)

        self.retranslateUi(JigPropDialog)
        self.cancel_btn.clicked.connect(JigPropDialog.reject)
        self.ok_btn.clicked.connect(JigPropDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(JigPropDialog)
        JigPropDialog.setTabOrder(self.nameLineEdit,self.choose_color_btn)
        JigPropDialog.setTabOrder(self.choose_color_btn,self.ok_btn)
        JigPropDialog.setTabOrder(self.ok_btn,self.cancel_btn)

    def retranslateUi(self, JigPropDialog):
        JigPropDialog.setWindowTitle(QtCore.QCoreApplication.translate("JigPropDialog", "Jig Properties", None))
        self.nameTextLabel.setText(QtCore.QCoreApplication.translate("JigPropDialog", "Name:", None))
        self.colorTextLabel.setText(QtCore.QCoreApplication.translate("JigPropDialog", "Color:", None))
        self.choose_color_btn.setToolTip(QtCore.QCoreApplication.translate("JigPropDialog", "Change Color", None))
        self.choose_color_btn.setText(QtCore.QCoreApplication.translate("JigPropDialog", "Choose...", None))
        self.ok_btn.setText(QtCore.QCoreApplication.translate("JigPropDialog", "&OK", None))
        self.ok_btn.setShortcut(QtCore.QCoreApplication.translate("JigPropDialog", "Alt+O", None))
        self.cancel_btn.setText(QtCore.QCoreApplication.translate("JigPropDialog", "&Cancel", None))
        self.cancel_btn.setShortcut(QtCore.QCoreApplication.translate("JigPropDialog", "Alt+C", None))
