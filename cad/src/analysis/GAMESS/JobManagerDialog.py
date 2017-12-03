# -*- coding: utf-8 -*-

# Copyright 2005-2007 Nanorex, Inc.  See LICENSE file for details.
# Form implementation generated from reading ui file 'JobManagerDialog.ui'
#
# Created: Wed Sep 20 08:10:41 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_JobManagerDialog(object):
    def setupUi(self, JobManagerDialog):
        JobManagerDialog.setObjectName("JobManagerDialog")
        JobManagerDialog.resize(QtCore.QSize(QtCore.QRect(0,0,1009,258).size()).expandedTo(JobManagerDialog.minimumSizeHint()))

        self.vboxlayout = QtWidgets.QVBoxLayout(JobManagerDialog)
        self.vboxlayout.setContentsMargins(11, 11, 11, 11)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.groupBox1 = QtWidgets.QGroupBox(JobManagerDialog)
        self.groupBox1.setObjectName("groupBox1")

        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.groupBox1)
        self.vboxlayout1.setContentsMargins(11, 11, 11, 11)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.job_table = QtWidgets.QTableWidget(self.groupBox1)
        self.job_table.setNumRows(1)
        self.job_table.setNumCols(8)
        self.job_table.setSorting(False)
        self.job_table.setSelectionMode(QtGui.QTable.SingleRow)
        self.job_table.setObjectName("job_table")
        self.vboxlayout1.addWidget(self.job_table)

        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.start_btn = QtWidgets.QPushButton(self.groupBox1)
        self.start_btn.setEnabled(False)
        self.start_btn.setObjectName("start_btn")
        self.hboxlayout.addWidget(self.start_btn)

        self.stop_btn = QtWidgets.QPushButton(self.groupBox1)
        self.stop_btn.setEnabled(False)
        self.stop_btn.setObjectName("stop_btn")
        self.hboxlayout.addWidget(self.stop_btn)

        self.edit_btn = QtWidgets.QPushButton(self.groupBox1)
        self.edit_btn.setEnabled(False)
        self.edit_btn.setObjectName("edit_btn")
        self.hboxlayout.addWidget(self.edit_btn)

        self.view_btn = QtWidgets.QPushButton(self.groupBox1)
        self.view_btn.setEnabled(False)
        self.view_btn.setObjectName("view_btn")
        self.hboxlayout.addWidget(self.view_btn)

        self.delete_btn = QtWidgets.QPushButton(self.groupBox1)
        self.delete_btn.setEnabled(False)
        self.delete_btn.setObjectName("delete_btn")
        self.hboxlayout.addWidget(self.delete_btn)

        self.move_btn = QtWidgets.QPushButton(self.groupBox1)
        self.move_btn.setEnabled(False)
        self.move_btn.setObjectName("move_btn")
        self.hboxlayout.addWidget(self.move_btn)

        spacerItem = QtWidgets.QSpacerItem(280,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.vboxlayout.addWidget(self.groupBox1)

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.refresh_btn = QtWidgets.QPushButton(JobManagerDialog)
        self.refresh_btn.setObjectName("refresh_btn")
        self.hboxlayout1.addWidget(self.refresh_btn)

        self.filter_btn = QtWidgets.QPushButton(JobManagerDialog)
        self.filter_btn.setObjectName("filter_btn")
        self.hboxlayout1.addWidget(self.filter_btn)

        spacerItem1 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)

        self.close_btn = QtWidgets.QPushButton(JobManagerDialog)
        self.close_btn.setObjectName("close_btn")
        self.hboxlayout1.addWidget(self.close_btn)
        self.vboxlayout.addLayout(self.hboxlayout1)

        self.retranslateUi(JobManagerDialog)
        self.close_btn.clicked.connect(JobManagerDialog.close)
        QtCore.QMetaObject.connectSlotsByName(JobManagerDialog)

    def retranslateUi(self, JobManagerDialog):
        JobManagerDialog.setWindowTitle(QtCore.QCoreApplication.translate("JobManagerDialog", "NanoEngineer-1 Job Manager", None))
        self.groupBox1.setTitle(QtCore.QCoreApplication.translate("JobManagerDialog", "Jobs", None))
        self.job_table.clear()
        self.job_table.setColumnCount(0)
        self.job_table.setRowCount(0)
        self.start_btn.setText(QtCore.QCoreApplication.translate("JobManagerDialog", "Start", None))
        self.stop_btn.setText(QtCore.QCoreApplication.translate("JobManagerDialog", "Stop", None))
        self.edit_btn.setText(QtCore.QCoreApplication.translate("JobManagerDialog", "Edit", None))
        self.view_btn.setText(QtCore.QCoreApplication.translate("JobManagerDialog", "View", None))
        self.delete_btn.setText(QtCore.QCoreApplication.translate("JobManagerDialog", "Delete", None))
        self.move_btn.setText(QtCore.QCoreApplication.translate("JobManagerDialog", "Move", None))
        self.refresh_btn.setText(QtCore.QCoreApplication.translate("JobManagerDialog", "Refresh", None))
        self.filter_btn.setText(QtCore.QCoreApplication.translate("JobManagerDialog", "Filter...", None))
        self.close_btn.setText(QtCore.QCoreApplication.translate("JobManagerDialog", "Close", None))
