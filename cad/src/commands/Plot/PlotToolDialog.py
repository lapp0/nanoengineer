# -*- coding: utf-8 -*-

# Copyright 2005-2007 Nanorex, Inc.  See LICENSE file for details.
# Form implementation generated from reading ui file 'PlotToolDialog.ui'
#
# Created: Wed Sep 20 07:07:09 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlotToolDialog(object):
    def setupUi(self, PlotToolDialog):
        PlotToolDialog.setObjectName("PlotToolDialog")
        PlotToolDialog.resize(QtCore.QSize(QtCore.QRect(0,0,264,150).size()).expandedTo(PlotToolDialog.minimumSizeHint()))

        self.gridlayout = QtWidgets.QGridLayout(PlotToolDialog)
        self.gridlayout.setContentsMargins(11, 11, 11, 11)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.gridlayout1 = QtWidgets.QGridLayout()
        self.gridlayout1.setContentsMargins(0, 0, 0, 0)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.plot_btn = QtWidgets.QPushButton(PlotToolDialog)
        self.plot_btn.setObjectName("plot_btn")
        self.hboxlayout.addWidget(self.plot_btn)

        self.done_btn = QtWidgets.QPushButton(PlotToolDialog)
        self.done_btn.setObjectName("done_btn")
        self.hboxlayout.addWidget(self.done_btn)
        self.gridlayout1.addLayout(self.hboxlayout,2,0,1,1)

        self.plot_combox = QtWidgets.QComboBox(PlotToolDialog)
        self.plot_combox.setObjectName("plot_combox")
        self.gridlayout1.addWidget(self.plot_combox,1,0,1,1)

        self.textLabel1 = QtWidgets.QLabel(PlotToolDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout1.addWidget(self.textLabel1,0,0,1,1)
        self.vboxlayout.addLayout(self.gridlayout1)

        spacerItem = QtWidgets.QSpacerItem(20,16,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.open_trace_file_btn = QtWidgets.QPushButton(PlotToolDialog)
        self.open_trace_file_btn.setObjectName("open_trace_file_btn")
        self.hboxlayout1.addWidget(self.open_trace_file_btn)

        self.open_gnuplot_btn = QtWidgets.QPushButton(PlotToolDialog)
        self.open_gnuplot_btn.setObjectName("open_gnuplot_btn")
        self.hboxlayout1.addWidget(self.open_gnuplot_btn)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.gridlayout.addLayout(self.vboxlayout,0,0,1,1)

        self.retranslateUi(PlotToolDialog)
        self.done_btn.clicked.connect(PlotToolDialog.close)
        QtCore.QMetaObject.connectSlotsByName(PlotToolDialog)
        PlotToolDialog.setTabOrder(self.plot_combox,self.plot_btn)
        PlotToolDialog.setTabOrder(self.plot_btn,self.done_btn)
        PlotToolDialog.setTabOrder(self.done_btn,self.open_trace_file_btn)
        PlotToolDialog.setTabOrder(self.open_trace_file_btn,self.open_gnuplot_btn)

    def retranslateUi(self, PlotToolDialog):
        PlotToolDialog.setWindowTitle(QtCore.QCoreApplication.translate("PlotToolDialog", "Make Graphs", None))
        self.plot_btn.setText(QtCore.QCoreApplication.translate("PlotToolDialog", "Make Graph", None))
        self.done_btn.setText(QtCore.QCoreApplication.translate("PlotToolDialog", "Done", None))
        self.textLabel1.setText(QtCore.QCoreApplication.translate("PlotToolDialog", "Select jig to graph:", None))
        self.open_trace_file_btn.setText(QtCore.QCoreApplication.translate("PlotToolDialog", "Open Trace File", None))
        self.open_gnuplot_btn.setText(QtCore.QCoreApplication.translate("PlotToolDialog", "Open GNUplot File", None))
