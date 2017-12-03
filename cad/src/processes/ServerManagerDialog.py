# -*- coding: utf-8 -*-

# Copyright 2005-2007 Nanorex, Inc.  See LICENSE file for details.
# Form implementation generated from reading ui file 'ServerManagerDialog.ui'
#
# Created: Wed Sep 20 09:07:05 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ServerManagerDialog(object):
    def setupUi(self, ServerManagerDialog):
        ServerManagerDialog.setObjectName("ServerManagerDialog")
        ServerManagerDialog.resize(QtCore.QSize(QtCore.QRect(0,0,673,677).size()).expandedTo(ServerManagerDialog.minimumSizeHint()))

        self.vboxlayout = QtWidgets.QVBoxLayout(ServerManagerDialog)
        self.vboxlayout.setContentsMargins(11, 11, 11, 11)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.server_listview = QtWidgets.QListWidget(ServerManagerDialog)
        self.server_listview.setObjectName("server_listview")
        self.hboxlayout.addWidget(self.server_listview)

        self.frame4 = QtWidgets.QFrame(ServerManagerDialog)
        self.frame4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame4.setObjectName("frame4")

        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.frame4)
        self.vboxlayout1.setContentsMargins(11, 11, 11, 11)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.textLabel1 = QtWidgets.QLabel(self.frame4)
        self.textLabel1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.textLabel1.setObjectName("textLabel1")
        self.vboxlayout1.addWidget(self.textLabel1)

        self.name_linedit = QtWidgets.QLineEdit(self.frame4)
        self.name_linedit.setObjectName("name_linedit")
        self.vboxlayout1.addWidget(self.name_linedit)

        self.textLabel1_3 = QtWidgets.QLabel(self.frame4)
        self.textLabel1_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.textLabel1_3.setObjectName("textLabel1_3")
        self.vboxlayout1.addWidget(self.textLabel1_3)

        self.ipaddress_linedit = QtWidgets.QLineEdit(self.frame4)
        self.ipaddress_linedit.setObjectName("ipaddress_linedit")
        self.vboxlayout1.addWidget(self.ipaddress_linedit)

        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.textLabel1_2 = QtWidgets.QLabel(self.frame4)
        self.textLabel1_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.textLabel1_2.setObjectName("textLabel1_2")
        self.gridlayout.addWidget(self.textLabel1_2,0,0,1,1)

        self.method_combox = QtWidgets.QComboBox(self.frame4)
        self.method_combox.setObjectName("method_combox")
        self.gridlayout.addWidget(self.method_combox,1,1,1,1)

        self.textLabel1_6 = QtWidgets.QLabel(self.frame4)
        self.textLabel1_6.setObjectName("textLabel1_6")
        self.gridlayout.addWidget(self.textLabel1_6,0,1,1,1)

        self.platform_combox = QtWidgets.QComboBox(self.frame4)
        self.platform_combox.setObjectName("platform_combox")
        self.gridlayout.addWidget(self.platform_combox,1,0,1,1)
        self.vboxlayout1.addLayout(self.gridlayout)

        self.textLabel1_4 = QtWidgets.QLabel(self.frame4)
        self.textLabel1_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.textLabel1_4.setObjectName("textLabel1_4")
        self.vboxlayout1.addWidget(self.textLabel1_4)

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.engine_combox = QtWidgets.QComboBox(self.frame4)
        self.engine_combox.setObjectName("engine_combox")
        self.hboxlayout1.addWidget(self.engine_combox)

        spacerItem = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.vboxlayout1.addLayout(self.hboxlayout1)

        self.textLabel1_5 = QtWidgets.QLabel(self.frame4)
        self.textLabel1_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.textLabel1_5.setObjectName("textLabel1_5")
        self.vboxlayout1.addWidget(self.textLabel1_5)

        self.program_linedit = QtWidgets.QLineEdit(self.frame4)
        self.program_linedit.setObjectName("program_linedit")
        self.vboxlayout1.addWidget(self.program_linedit)

        self.textLabel1_2_2 = QtWidgets.QLabel(self.frame4)
        self.textLabel1_2_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.textLabel1_2_2.setObjectName("textLabel1_2_2")
        self.vboxlayout1.addWidget(self.textLabel1_2_2)

        self.username_linedit = QtWidgets.QLineEdit(self.frame4)
        self.username_linedit.setObjectName("username_linedit")
        self.vboxlayout1.addWidget(self.username_linedit)

        self.textLabel1_2_2_2 = QtWidgets.QLabel(self.frame4)
        self.textLabel1_2_2_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.textLabel1_2_2_2.setObjectName("textLabel1_2_2_2")
        self.vboxlayout1.addWidget(self.textLabel1_2_2_2)

        self.password_linedit = QtWidgets.QLineEdit(self.frame4)
        self.password_linedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_linedit.setObjectName("password_linedit")
        self.vboxlayout1.addWidget(self.password_linedit)
        self.hboxlayout.addWidget(self.frame4)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.new_btn = QtWidgets.QPushButton(ServerManagerDialog)
        self.new_btn.setEnabled(True)
        self.new_btn.setObjectName("new_btn")
        self.hboxlayout2.addWidget(self.new_btn)

        self.del_btn = QtWidgets.QPushButton(ServerManagerDialog)
        self.del_btn.setObjectName("del_btn")
        self.hboxlayout2.addWidget(self.del_btn)

        self.test_btn = QtWidgets.QPushButton(ServerManagerDialog)
        self.test_btn.setObjectName("test_btn")
        self.hboxlayout2.addWidget(self.test_btn)

        self.exit_btn = QtWidgets.QPushButton(ServerManagerDialog)
        self.exit_btn.setObjectName("exit_btn")
        self.hboxlayout2.addWidget(self.exit_btn)
        self.vboxlayout.addLayout(self.hboxlayout2)

        self.retranslateUi(ServerManagerDialog)
        self.exit_btn.clicked.connect(ServerManagerDialog.close)
        QtCore.QMetaObject.connectSlotsByName(ServerManagerDialog)

    def retranslateUi(self, ServerManagerDialog):
        ServerManagerDialog.setWindowTitle(QtCore.QCoreApplication.translate("ServerManagerDialog", "Server Manager", None))
        self.textLabel1.setText(QtCore.QCoreApplication.translate("ServerManagerDialog", "Server Name :", None))
        self.name_linedit.setText(QtCore.QCoreApplication.translate("ServerManagerDialog", "localhost", None))
        self.textLabel1_3.setText(QtCore.QCoreApplication.translate("ServerManagerDialog", "IP Address :", None))
        self.ipaddress_linedit.setText(QtCore.QCoreApplication.translate("ServerManagerDialog", "127.0.0.1", None))
        self.textLabel1_2.setText(QtCore.QCoreApplication.translate("ServerManagerDialog", "Platform :", None))
        self.method_combox.addItem(QtCore.QCoreApplication.translate("ServerManagerDialog", "Local access", None))
        self.method_combox.addItem(QtCore.QCoreApplication.translate("ServerManagerDialog", "Ssh/scp", None))
        self.method_combox.addItem(QtCore.QCoreApplication.translate("ServerManagerDialog", "Rsh/rcp", None))
        self.method_combox.addItem(QtCore.QCoreApplication.translate("ServerManagerDialog", "Telnet/ftp", None))
        self.textLabel1_6.setText(QtCore.QCoreApplication.translate("ServerManagerDialog", "Method:", None))
        self.platform_combox.addItem(QtCore.QCoreApplication.translate("ServerManagerDialog", "Linux", None))
        self.platform_combox.addItem(QtCore.QCoreApplication.translate("ServerManagerDialog", "Mac OS", None))
        self.platform_combox.addItem(QtCore.QCoreApplication.translate("ServerManagerDialog", "Windows", None))
        self.textLabel1_4.setText(QtCore.QCoreApplication.translate("ServerManagerDialog", "Engine :", None))
        self.engine_combox.addItem(QtCore.QCoreApplication.translate("ServerManagerDialog", "PC GAMESS", None))
        self.engine_combox.addItem(QtCore.QCoreApplication.translate("ServerManagerDialog", "nanoSIM-1", None))
        self.engine_combox.addItem(QtCore.QCoreApplication.translate("ServerManagerDialog", "GAMESS", None))
        self.textLabel1_5.setText(QtCore.QCoreApplication.translate("ServerManagerDialog", "Executing Program :", None))
        self.program_linedit.setText(QtCore.QCoreApplication.translate("ServerManagerDialog", "C:\\PCGAMESS", None))
        self.textLabel1_2_2.setText(QtCore.QCoreApplication.translate("ServerManagerDialog", "Username :", None))
        self.username_linedit.setText(QtCore.QCoreApplication.translate("ServerManagerDialog", "nanorex", None))
        self.textLabel1_2_2_2.setText(QtCore.QCoreApplication.translate("ServerManagerDialog", "Password :", None))
        self.password_linedit.setText(QtCore.QCoreApplication.translate("ServerManagerDialog", "nanorex", None))
        self.new_btn.setText(QtCore.QCoreApplication.translate("ServerManagerDialog", "New", None))
        self.del_btn.setText(QtCore.QCoreApplication.translate("ServerManagerDialog", "Delete", None))
        self.test_btn.setText(QtCore.QCoreApplication.translate("ServerManagerDialog", "Test", None))
        self.exit_btn.setText(QtCore.QCoreApplication.translate("ServerManagerDialog", "Exit", None))
