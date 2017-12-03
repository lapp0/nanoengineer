# -*- coding: utf-8 -*-

# Copyright 2004-2007 Nanorex, Inc.  See LICENSE file for details.
# Form implementation generated from reading ui file 'PartPropDialog.ui'
#
# Created: Wed Sep 20 08:20:23 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PartPropDialog(object):
    def setupUi(self, PartPropDialog):
        PartPropDialog.setObjectName("PartPropDialog")
        PartPropDialog.resize(QtCore.QSize(QtCore.QRect(0,0,396,402).size()).expandedTo(PartPropDialog.minimumSizeHint()))

        self.gridlayout = QtWidgets.QGridLayout(PartPropDialog)
        self.gridlayout.setContentsMargins(11, 11, 11, 11)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(4, 4, 4, 4)
        self.hboxlayout.setSpacing(72)
        self.hboxlayout.setObjectName("hboxlayout")

        self.okPushButton = QtWidgets.QPushButton(PartPropDialog)
        self.okPushButton.setMinimumSize(QtCore.QSize(0,0))
        self.okPushButton.setAutoDefault(True)
        self.okPushButton.setDefault(True)
        self.okPushButton.setObjectName("okPushButton")
        self.hboxlayout.addWidget(self.okPushButton)

        self.cancelPushButton = QtWidgets.QPushButton(PartPropDialog)
        self.cancelPushButton.setMinimumSize(QtCore.QSize(0,0))
        self.cancelPushButton.setAutoDefault(True)
        self.cancelPushButton.setDefault(False)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.hboxlayout.addWidget(self.cancelPushButton)
        self.gridlayout.addLayout(self.hboxlayout,1,0,1,1)

        self.tabWidget3 = QtWidgets.QTabWidget(PartPropDialog)
        self.tabWidget3.setObjectName("tabWidget3")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.gridlayout1 = QtWidgets.QGridLayout(self.tab)
        self.gridlayout1.setContentsMargins(0, 0, 0, 0)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.nameLabel = QtWidgets.QLabel(self.tab)
        self.nameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.hboxlayout1.addWidget(self.nameLabel)

        self.nameLineEdit = QtWidgets.QLineEdit(self.tab)
        self.nameLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.nameLineEdit.setReadOnly(True)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.hboxlayout1.addWidget(self.nameLineEdit)
        self.vboxlayout.addLayout(self.hboxlayout1)

        self.mmpformatLabel = QtWidgets.QLabel(self.tab)
        self.mmpformatLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mmpformatLabel.setObjectName("mmpformatLabel")
        self.vboxlayout.addWidget(self.mmpformatLabel)

        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.vboxlayout1 = QtWidgets.QVBoxLayout()
        self.vboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.statsLabel = QtWidgets.QLabel(self.tab)
        self.statsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.statsLabel.setObjectName("statsLabel")
        self.vboxlayout1.addWidget(self.statsLabel)

        spacerItem = QtWidgets.QSpacerItem(20,40,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem)
        self.hboxlayout2.addLayout(self.vboxlayout1)

        self.statsView = QtWidgets.QListWidget(self.tab)
        self.statsView.setObjectName("statsView")
        self.hboxlayout2.addWidget(self.statsView)
        self.vboxlayout.addLayout(self.hboxlayout2)
        self.gridlayout1.addLayout(self.vboxlayout,0,0,1,1)
        self.tabWidget3.addTab(self.tab, "")
        self.gridlayout.addWidget(self.tabWidget3,0,0,1,1)

        self.retranslateUi(PartPropDialog)
        self.okPushButton.clicked.connect(PartPropDialog.accept)
        self.cancelPushButton.clicked.connect(PartPropDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PartPropDialog)
        PartPropDialog.setTabOrder(self.nameLineEdit,self.statsView)
        PartPropDialog.setTabOrder(self.statsView,self.okPushButton)
        PartPropDialog.setTabOrder(self.okPushButton,self.cancelPushButton)
        PartPropDialog.setTabOrder(self.cancelPushButton,self.tabWidget3)

    def retranslateUi(self, PartPropDialog):
        PartPropDialog.setWindowTitle(QtCore.QCoreApplication.translate("PartPropDialog", "Part Properties", None))
        self.okPushButton.setText(QtCore.QCoreApplication.translate("PartPropDialog", "&OK", None))
        self.okPushButton.setShortcut(QtCore.QCoreApplication.translate("PartPropDialog", "Alt+O", None))
        self.cancelPushButton.setText(QtCore.QCoreApplication.translate("PartPropDialog", "&Cancel", None))
        self.cancelPushButton.setShortcut(QtCore.QCoreApplication.translate("PartPropDialog", "Alt+C", None))
        self.nameLabel.setText(QtCore.QCoreApplication.translate("PartPropDialog", "Name:", None))
        self.mmpformatLabel.setText(QtCore.QCoreApplication.translate("PartPropDialog", "MMP File Format:", None))
        self.statsLabel.setText(QtCore.QCoreApplication.translate("PartPropDialog", "Statistics:", None))
        self.tabWidget3.setTabText(self.tabWidget3.indexOf(self.tab), QtCore.QCoreApplication.translate("PartPropDialog", "General", None))
