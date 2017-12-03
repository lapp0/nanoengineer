# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PreferencesDialog.ui'
#
# Created: Wed Aug 27 16:00:53 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        PreferencesDialog.setObjectName("PreferencesDialog")
        PreferencesDialog.resize(QtCore.QSize(QtCore.QRect(0,0,594,574).size()).expandedTo(PreferencesDialog.minimumSizeHint()))

        self.vboxlayout = QtWidgets.QVBoxLayout(PreferencesDialog)
        self.vboxlayout.setSpacing(4)
        self.vboxlayout.setContentsMargins(2, 2, 2, 2)
        self.vboxlayout.setObjectName("vboxlayout")

        self.tabWidget = QtWidgets.QTabWidget(PreferencesDialog)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

#        self.hboxlayout = QtGui.QHBoxLayout(self.tab)
        self.pref_splitter = QtWidgets.QSplitter(self.tab)
#        self.hboxlayout.setSpacing(4)
#        self.hboxlayout.setMargin(2)
#        self.hboxlayout.setObjectName("hboxlayout")
        self.pref_splitter.setObjectName("pref_splitter")

        self.categoriesTreeWidget = QtWidgets.QTreeWidget(self.pref_splitter)
        self.categoriesTreeWidget.setMinimumWidth(100)
#        self.categoriesTreeWidget.setMaximumWidth(250)
        self.categoriesTreeWidget.setObjectName("categoriesTreeWidget")
#        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
#        sizePolicy.setHorizontalStretch(0)
#        sizePolicy.setVerticalStretch(0)
#        self.categoriesTreeWidget.setSizePolicy(sizePolicy)
#        self.hboxlayout.addWidget(self.categoriesTreeWidget)
        self.pref_splitter.addWidget(self.categoriesTreeWidget)

        self.prefsStackedWidget = QtWidgets.QStackedWidget(self.pref_splitter)
#        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
#        self.prefsStackedWidget.setSizePolicy(sizePolicy)
        self.prefsStackedWidget.setObjectName("prefsStackedWidget")

#        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
#        self.pref_splitter.setSizePolicy(sizePolicy)

        self.pref_splitter.addWidget(self.prefsStackedWidget)
        self.tabWidget.addTab(self.tab,"")
        self.vboxlayout.addWidget(self.tabWidget)

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.whatsThisToolButton = QtWidgets.QToolButton(PreferencesDialog)
        self.whatsThisToolButton.setObjectName("whatsThisToolButton")
        self.hboxlayout1.addWidget(self.whatsThisToolButton)

        spacerItem = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)

        self.okButton = QtWidgets.QPushButton(PreferencesDialog)
        self.okButton.setObjectName("okButton")
        self.hboxlayout1.addWidget(self.okButton)
        self.vboxlayout.addLayout(self.hboxlayout1)

        self.retranslateUi(PreferencesDialog)
        self.tabWidget.setCurrentIndex(0)
        self.prefsStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)

    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(QtCore.QCoreApplication.translate("PreferencesDialog", "Preferences", None))
        self.categoriesTreeWidget.headerItem().setText(0,QtCore.QCoreApplication.translate("PreferencesDialog", "Categories", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtCore.QCoreApplication.translate("PreferencesDialog", "System Options", None))
        self.okButton.setText(QtCore.QCoreApplication.translate("PreferencesDialog", "OK", None))

