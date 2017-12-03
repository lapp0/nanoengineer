# Copyright 2005-2007 Nanorex, Inc.  See LICENSE file for details.
"""
$Id$
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChunkPropDialog(object):
    def setupUi(self, ChunkPropDialog):
        ChunkPropDialog.setObjectName("ChunkPropDialog")
        ChunkPropDialog.resize(QtCore.QSize(QtCore.QRect(0,0,243,354).size()).expandedTo(ChunkPropDialog.minimumSizeHint()))

        self.vboxlayout = QtWidgets.QVBoxLayout(ChunkPropDialog)
        self.vboxlayout.setContentsMargins(11, 11, 11, 11)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.atomsTextBrowser = QtWidgets.QTextBrowser(ChunkPropDialog)
        self.atomsTextBrowser.setObjectName("atomsTextBrowser")
        self.gridlayout.addWidget(self.atomsTextBrowser,1,1,1,1)

        self.vboxlayout1 = QtWidgets.QVBoxLayout()
        self.vboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.textLabel2 = QtWidgets.QLabel(ChunkPropDialog)
        self.textLabel2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel2.setObjectName("textLabel2")
        self.vboxlayout1.addWidget(self.textLabel2)

        spacerItem = QtWidgets.QSpacerItem(20,113,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem)
        self.gridlayout.addLayout(self.vboxlayout1,1,0,1,1)

        self.nameLineEdit = QtWidgets.QLineEdit(ChunkPropDialog)
        self.nameLineEdit.setAlignment(QtCore.Qt.AlignLeading)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.gridlayout.addWidget(self.nameLineEdit,0,1,1,1)

        self.textLabel1 = QtWidgets.QLabel(ChunkPropDialog)
        self.textLabel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout.addWidget(self.textLabel1,0,0,1,1)
        self.vboxlayout.addLayout(self.gridlayout)

        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.colorTextLabel = QtWidgets.QLabel(ChunkPropDialog)
        self.colorTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.colorTextLabel.setObjectName("colorTextLabel")
        self.hboxlayout.addWidget(self.colorTextLabel)

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.chunk_color_frame = QtWidgets.QLabel(ChunkPropDialog)
        self.chunk_color_frame.setAutoFillBackground(True)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(5),QtWidgets.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chunk_color_frame.sizePolicy().hasHeightForWidth())
        self.chunk_color_frame.setSizePolicy(sizePolicy)
        self.chunk_color_frame.setMinimumSize(QtCore.QSize(40,0))
        self.chunk_color_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.chunk_color_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.chunk_color_frame.setScaledContents(True)
        self.chunk_color_frame.setObjectName("chunk_color_frame")
        self.hboxlayout1.addWidget(self.chunk_color_frame)

        self.choose_color_btn = QtWidgets.QPushButton(ChunkPropDialog)
        self.choose_color_btn.setEnabled(True)
        self.choose_color_btn.setAutoDefault(False)
        self.choose_color_btn.setObjectName("choose_color_btn")
        self.hboxlayout1.addWidget(self.choose_color_btn)

        spacerItem1 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.hboxlayout.addLayout(self.hboxlayout1)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.reset_color_btn = QtWidgets.QPushButton(ChunkPropDialog)
        self.reset_color_btn.setEnabled(True)
        self.reset_color_btn.setAutoDefault(False)
        self.reset_color_btn.setObjectName("reset_color_btn")
        self.vboxlayout.addWidget(self.reset_color_btn)

        self.make_atoms_visible_btn = QtWidgets.QPushButton(ChunkPropDialog)
        self.make_atoms_visible_btn.setEnabled(True)
        self.make_atoms_visible_btn.setAutoDefault(False)
        self.make_atoms_visible_btn.setObjectName("make_atoms_visible_btn")
        self.vboxlayout.addWidget(self.make_atoms_visible_btn)

        spacerItem2 = QtWidgets.QSpacerItem(20,20,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem2)

        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        spacerItem3 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem3)

        self.ok_btn = QtWidgets.QPushButton(ChunkPropDialog)
        self.ok_btn.setMinimumSize(QtCore.QSize(0,0))
        self.ok_btn.setDefault(True)
        self.ok_btn.setObjectName("ok_btn")
        self.hboxlayout2.addWidget(self.ok_btn)

        self.cancel_btn = QtWidgets.QPushButton(ChunkPropDialog)
        self.cancel_btn.setMinimumSize(QtCore.QSize(0,0))
        self.cancel_btn.setDefault(False)
        self.cancel_btn.setObjectName("cancel_btn")
        self.hboxlayout2.addWidget(self.cancel_btn)
        self.vboxlayout.addLayout(self.hboxlayout2)

        self.retranslateUi(ChunkPropDialog)

        ChunkPropDialog.setTabOrder(self.nameLineEdit,self.atomsTextBrowser)
        ChunkPropDialog.setTabOrder(self.atomsTextBrowser,self.choose_color_btn)
        ChunkPropDialog.setTabOrder(self.choose_color_btn,self.reset_color_btn)
        ChunkPropDialog.setTabOrder(self.reset_color_btn,self.make_atoms_visible_btn)
        ChunkPropDialog.setTabOrder(self.make_atoms_visible_btn,self.ok_btn)
        ChunkPropDialog.setTabOrder(self.ok_btn,self.cancel_btn)

    def retranslateUi(self, ChunkPropDialog):
        ChunkPropDialog.setWindowTitle(QtCore.QCoreApplication.translate("ChunkPropDialog", "Chunk Properties", None))
        ChunkPropDialog.setWindowIcon(QtGui.QIcon("ui/border/Chunk"))
        self.textLabel2.setText(QtCore.QCoreApplication.translate("ChunkPropDialog", "Atoms:", None))
        self.textLabel1.setText(QtCore.QCoreApplication.translate("ChunkPropDialog", "Name:", None))
        self.colorTextLabel.setText(QtCore.QCoreApplication.translate("ChunkPropDialog", "Chunk Color:", None))
        self.choose_color_btn.setToolTip(QtCore.QCoreApplication.translate("ChunkPropDialog", "Change chunk color", None))
        self.choose_color_btn.setText(QtCore.QCoreApplication.translate("ChunkPropDialog", "Choose...", None))
        self.reset_color_btn.setText(QtCore.QCoreApplication.translate("ChunkPropDialog", "Reset Chunk Color to Default", None))
        self.make_atoms_visible_btn.setText(QtCore.QCoreApplication.translate("ChunkPropDialog", "Make Invisible Atoms Visible", None))
        self.ok_btn.setText(QtCore.QCoreApplication.translate("ChunkPropDialog", "&OK", None))
        self.ok_btn.setShortcut(QtCore.QCoreApplication.translate("ChunkPropDialog", "Alt+O", None))
        self.cancel_btn.setText(QtCore.QCoreApplication.translate("ChunkPropDialog", "&Cancel", None))
        self.cancel_btn.setShortcut(QtCore.QCoreApplication.translate("ChunkPropDialog", "Alt+C", None))
