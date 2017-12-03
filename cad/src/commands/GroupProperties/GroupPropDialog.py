# -*- coding: utf-8 -*-

# Copyright 2004-2007 Nanorex, Inc.  See LICENSE file for details.
# Form implementation generated from reading ui file 'GroupPropDialog.ui'
#
# Created: Wed Sep 20 07:22:13 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GroupPropDialog(object):
    def setupUi(self, GroupPropDialog):
        GroupPropDialog.setObjectName("GroupPropDialog")
        GroupPropDialog.resize(QtCore.QSize(QtCore.QRect(0,0,258,357).size()).expandedTo(GroupPropDialog.minimumSizeHint()))

        self.gridlayout = QtWidgets.QGridLayout(GroupPropDialog)
        self.gridlayout.setContentsMargins(11, 11, 11, 11)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.nameLabel = QtWidgets.QLabel(GroupPropDialog)
        self.nameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.hboxlayout.addWidget(self.nameLabel)

        self.nameLineEdit = QtWidgets.QLineEdit(GroupPropDialog)
        self.nameLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nameLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.hboxlayout.addWidget(self.nameLineEdit)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.mmpformatLabel = QtWidgets.QLabel(GroupPropDialog)
        self.mmpformatLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mmpformatLabel.setObjectName("mmpformatLabel")
        self.vboxlayout.addWidget(self.mmpformatLabel)

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.statsView = QtWidgets.QListWidget(GroupPropDialog)
        self.statsView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.statsView.setObjectName("statsView")
        self.hboxlayout1.addWidget(self.statsView)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.gridlayout.addLayout(self.vboxlayout,0,0,1,1)

        spacerItem = QtWidgets.QSpacerItem(20,16,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem,1,0,1,1)

        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.okPushButton = QtWidgets.QPushButton(GroupPropDialog)
        self.okPushButton.setAutoDefault(True)
        self.okPushButton.setDefault(True)
        self.okPushButton.setObjectName("okPushButton")
        self.hboxlayout2.addWidget(self.okPushButton)

        self.cancelPushButton = QtWidgets.QPushButton(GroupPropDialog)
        self.cancelPushButton.setAutoDefault(True)
        self.cancelPushButton.setDefault(False)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.hboxlayout2.addWidget(self.cancelPushButton)
        self.gridlayout.addLayout(self.hboxlayout2,2,0,1,1)

        self.retranslateUi(GroupPropDialog)
        self.okPushButton.clicked.connect(GroupPropDialog.accept)
        self.cancelPushButton.clicked.connect(GroupPropDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(GroupPropDialog)
        GroupPropDialog.setTabOrder(self.nameLineEdit,self.okPushButton)
        GroupPropDialog.setTabOrder(self.okPushButton,self.cancelPushButton)
        GroupPropDialog.setTabOrder(self.cancelPushButton,self.statsView)

    def retranslateUi(self, GroupPropDialog):
        GroupPropDialog.setWindowTitle(QtCore.QCoreApplication.translate("GroupPropDialog", "Group Properties", None))
        GroupPropDialog.setWindowIcon(QtGui.QIcon("ui/border/GroupProp"))
        self.nameLabel.setText(QtCore.QCoreApplication.translate("GroupPropDialog", "Name:", None))
        self.mmpformatLabel.setText(QtCore.QCoreApplication.translate("GroupPropDialog", "Group Statistics:", None))
        self.okPushButton.setText(QtCore.QCoreApplication.translate("GroupPropDialog", "&OK", None))
        self.okPushButton.setShortcut(QtCore.QCoreApplication.translate("GroupPropDialog", "Alt+O", None))
        self.cancelPushButton.setText(QtCore.QCoreApplication.translate("GroupPropDialog", "&Cancel", None))
        self.cancelPushButton.setShortcut(QtCore.QCoreApplication.translate("GroupPropDialog", "Alt+C", None))
