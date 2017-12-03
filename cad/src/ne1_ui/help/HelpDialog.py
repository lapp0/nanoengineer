# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HelpDialog.ui'
#
# Created: Tue Mar 04 16:01:31 2008
#      by: PyQt4 UI code generator 4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelpDialog(object):
    def setupUi(self, HelpDialog):
        HelpDialog.setObjectName("HelpDialog")
        HelpDialog.resize(QtCore.QSize(QtCore.QRect(0,0,600,480).size()).expandedTo(HelpDialog.minimumSizeHint()))

        self.gridlayout = QtWidgets.QGridLayout(HelpDialog)
        self.gridlayout.setContentsMargins(9, 9, 9, 9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.help_tab = QtWidgets.QTabWidget(HelpDialog)
        self.help_tab.setObjectName("help_tab")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.gridlayout1 = QtWidgets.QGridLayout(self.tab)
        self.gridlayout1.setContentsMargins(0, 0, 0, 0)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.mouse_controls_textbrowser = QtWidgets.QTextBrowser(self.tab)
        self.mouse_controls_textbrowser.setObjectName("mouse_controls_textbrowser")
        self.gridlayout1.addWidget(self.mouse_controls_textbrowser,0,0,1,1)
        self.help_tab.addTab(self.tab,"")

        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")

        self.gridlayout2 = QtWidgets.QGridLayout(self.tab1)
        self.gridlayout2.setContentsMargins(0, 0, 0, 0)
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setObjectName("gridlayout2")

        self.keyboard_shortcuts_textbrowser = QtWidgets.QTextBrowser(self.tab1)
        self.keyboard_shortcuts_textbrowser.setObjectName("keyboard_shortcuts_textbrowser")
        self.gridlayout2.addWidget(self.keyboard_shortcuts_textbrowser,0,0,1,1)
        self.help_tab.addTab(self.tab1,"")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.gridlayout3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridlayout3.setContentsMargins(0, 0, 0, 0)
        self.gridlayout3.setSpacing(6)
        self.gridlayout3.setObjectName("gridlayout3")

        self.selection_shortcuts_textbrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.selection_shortcuts_textbrowser.setObjectName("selection_shortcuts_textbrowser")
        self.gridlayout3.addWidget(self.selection_shortcuts_textbrowser,0,0,1,1)
        self.help_tab.addTab(self.tab_2,"")
        self.gridlayout.addWidget(self.help_tab,0,0,1,1)

        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        spacerItem = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.close_btn = QtWidgets.QPushButton(HelpDialog)
        self.close_btn.setObjectName("close_btn")
        self.hboxlayout.addWidget(self.close_btn)
        self.gridlayout.addLayout(self.hboxlayout,1,0,1,1)

        self.retranslateUi(HelpDialog)
        self.help_tab.setCurrentIndex(2)
        self.close_btn.clicked.connect(HelpDialog.close)
        QtCore.QMetaObject.connectSlotsByName(HelpDialog)

    def retranslateUi(self, HelpDialog):
        HelpDialog.setWindowTitle(QtCore.QCoreApplication.translate("HelpDialog", "NanoEngineer-1 Help", None))
        self.help_tab.setTabText(self.help_tab.indexOf(self.tab), QtCore.QCoreApplication.translate("HelpDialog", "Mouse Controls", None))
        self.help_tab.setTabText(self.help_tab.indexOf(self.tab1), QtCore.QCoreApplication.translate("HelpDialog", "Keyboard Shortcuts", None))
        self.help_tab.setTabText(self.help_tab.indexOf(self.tab_2), QtCore.QCoreApplication.translate("HelpDialog", "Selection Shortcuts", None))
        self.close_btn.setText(QtCore.QCoreApplication.translate("HelpDialog", "Close", None))

