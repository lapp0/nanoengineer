# -*- coding: utf-8 -*-

# Copyright 2005-2007 Nanorex, Inc.  See LICENSE file for details.
# Form implementation generated from reading ui file 'NanoHiveDialog.ui'
#
# Created: Wed Sep 20 10:17:46 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NanoHiveDialog(object):
    def setupUi(self, NanoHiveDialog):
        NanoHiveDialog.setObjectName("NanoHiveDialog")
        NanoHiveDialog.resize(QtCore.QSize(QtCore.QRect(0,0,355,782).size()).expandedTo(NanoHiveDialog.minimumSizeHint()))
        NanoHiveDialog.setModal(True)

        self.gridlayout = QtWidgets.QGridLayout(NanoHiveDialog)
        self.gridlayout.setContentsMargins(11, 11, 11, 11)
        self.gridlayout.setSpacing(21)
        self.gridlayout.setObjectName("gridlayout")

        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.namelbl = QtWidgets.QLabel(NanoHiveDialog)
        self.namelbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.namelbl.setObjectName("namelbl")
        self.vboxlayout.addWidget(self.namelbl)

        self.vboxlayout1 = QtWidgets.QVBoxLayout()
        self.vboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.desclbl = QtWidgets.QLabel(NanoHiveDialog)
        self.desclbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.desclbl.setObjectName("desclbl")
        self.vboxlayout1.addWidget(self.desclbl)

        spacerItem = QtWidgets.QSpacerItem(20,16,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem)
        self.vboxlayout.addLayout(self.vboxlayout1)
        self.hboxlayout.addLayout(self.vboxlayout)

        self.vboxlayout2 = QtWidgets.QVBoxLayout()
        self.vboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.name_linedit = QtWidgets.QLineEdit(NanoHiveDialog)
        self.name_linedit.setObjectName("name_linedit")
        self.vboxlayout2.addWidget(self.name_linedit)

        self.description_textedit = QtWidgets.QTextEdit(NanoHiveDialog)
        self.description_textedit.setMinimumSize(QtCore.QSize(0,0))
        self.description_textedit.setTextFormat(QtCore.Qt.PlainText)
        self.description_textedit.setObjectName("description_textedit")
        self.vboxlayout2.addWidget(self.description_textedit)
        self.hboxlayout.addLayout(self.vboxlayout2)
        self.gridlayout.addLayout(self.hboxlayout,0,0,1,1)

        self.parms_grpbox = QtWidgets.QGroupBox(NanoHiveDialog)
        self.parms_grpbox.setObjectName("parms_grpbox")

        self.gridlayout1 = QtWidgets.QGridLayout(self.parms_grpbox)
        self.gridlayout1.setContentsMargins(11, 11, 11, 11)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.vboxlayout3 = QtWidgets.QVBoxLayout()
        self.vboxlayout3.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.textLabel5 = QtWidgets.QLabel(self.parms_grpbox)
        self.textLabel5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel5.setObjectName("textLabel5")
        self.vboxlayout3.addWidget(self.textLabel5)

        self.textLabel2 = QtWidgets.QLabel(self.parms_grpbox)
        self.textLabel2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel2.setObjectName("textLabel2")
        self.vboxlayout3.addWidget(self.textLabel2)

        self.textLabel3 = QtWidgets.QLabel(self.parms_grpbox)
        self.textLabel3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel3.setObjectName("textLabel3")
        self.vboxlayout3.addWidget(self.textLabel3)
        self.hboxlayout1.addLayout(self.vboxlayout3)

        self.vboxlayout4 = QtWidgets.QVBoxLayout()
        self.vboxlayout4.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.nframes_spinbox = QtWidgets.QSpinBox(self.parms_grpbox)
        self.nframes_spinbox.setMaximum(90000)
        self.nframes_spinbox.setMinimum(1)
        self.nframes_spinbox.setSingleStep(15)
        self.nframes_spinbox.setProperty("value",QtCore.QVariant(900))
        self.nframes_spinbox.setObjectName("nframes_spinbox")
        self.vboxlayout4.addWidget(self.nframes_spinbox)

        self.stepsper_spinbox = QtWidgets.QSpinBox(self.parms_grpbox)
        self.stepsper_spinbox.setMaximum(99999)
        self.stepsper_spinbox.setMinimum(1)
        self.stepsper_spinbox.setProperty("value",QtCore.QVariant(10))
        self.stepsper_spinbox.setObjectName("stepsper_spinbox")
        self.vboxlayout4.addWidget(self.stepsper_spinbox)

        self.temp_spinbox = QtWidgets.QSpinBox(self.parms_grpbox)
        self.temp_spinbox.setMaximum(99999)
        self.temp_spinbox.setProperty("value",QtCore.QVariant(300))
        self.temp_spinbox.setObjectName("temp_spinbox")
        self.vboxlayout4.addWidget(self.temp_spinbox)
        self.hboxlayout1.addLayout(self.vboxlayout4)

        self.vboxlayout5 = QtWidgets.QVBoxLayout()
        self.vboxlayout5.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout5.setSpacing(6)
        self.vboxlayout5.setObjectName("vboxlayout5")

        spacerItem1 = QtWidgets.QSpacerItem(255,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.vboxlayout5.addItem(spacerItem1)

        self.textLabel2_2 = QtWidgets.QLabel(self.parms_grpbox)
        self.textLabel2_2.setObjectName("textLabel2_2")
        self.vboxlayout5.addWidget(self.textLabel2_2)

        self.textLabel3_2 = QtWidgets.QLabel(self.parms_grpbox)
        self.textLabel3_2.setObjectName("textLabel3_2")
        self.vboxlayout5.addWidget(self.textLabel3_2)
        self.hboxlayout1.addLayout(self.vboxlayout5)
        self.gridlayout1.addLayout(self.hboxlayout1,0,0,1,1)
        self.gridlayout.addWidget(self.parms_grpbox,1,0,1,1)

        self.buttonGroup1 = QtWidgets.QGroupBox(NanoHiveDialog)
        self.buttonGroup1.setObjectName("buttonGroup1")

        self.gridlayout2 = QtWidgets.QGridLayout(self.buttonGroup1)
        self.gridlayout2.setContentsMargins(11, 11, 11, 11)
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setObjectName("gridlayout2")

        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.MPQC_GD_checkbox = QtWidgets.QCheckBox(self.buttonGroup1)
        self.MPQC_GD_checkbox.setObjectName("MPQC_GD_checkbox")
        self.hboxlayout2.addWidget(self.MPQC_GD_checkbox)

        self.MPQC_GD_options_btn = QtWidgets.QPushButton(self.buttonGroup1)
        self.MPQC_GD_options_btn.setEnabled(False)
        self.MPQC_GD_options_btn.setObjectName("MPQC_GD_options_btn")
        self.hboxlayout2.addWidget(self.MPQC_GD_options_btn)
        self.gridlayout2.addLayout(self.hboxlayout2,1,0,1,1)

        self.hboxlayout3 = QtWidgets.QHBoxLayout()
        self.hboxlayout3.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.MPQC_ESP_checkbox = QtWidgets.QCheckBox(self.buttonGroup1)
        self.MPQC_ESP_checkbox.setObjectName("MPQC_ESP_checkbox")
        self.hboxlayout3.addWidget(self.MPQC_ESP_checkbox)

        self.ESP_image_combox = QtWidgets.QComboBox(self.buttonGroup1)
        self.ESP_image_combox.setEnabled(False)
        self.ESP_image_combox.setObjectName("ESP_image_combox")
        self.hboxlayout3.addWidget(self.ESP_image_combox)
        self.gridlayout2.addLayout(self.hboxlayout3,0,0,1,1)

        self.AIREBO_checkbox = QtWidgets.QCheckBox(self.buttonGroup1)
        self.AIREBO_checkbox.setObjectName("AIREBO_checkbox")
        self.gridlayout2.addWidget(self.AIREBO_checkbox,2,0,1,1)
        self.gridlayout.addWidget(self.buttonGroup1,2,0,1,1)

        self.buttonGroup1_2 = QtWidgets.QGroupBox(NanoHiveDialog)
        self.buttonGroup1_2.setObjectName("buttonGroup1_2")

        self.vboxlayout6 = QtWidgets.QVBoxLayout(self.buttonGroup1_2)
        self.vboxlayout6.setContentsMargins(11, 11, 11, 11)
        self.vboxlayout6.setSpacing(6)
        self.vboxlayout6.setObjectName("vboxlayout6")

        self.Measurements_to_File_checkbox = QtWidgets.QCheckBox(self.buttonGroup1_2)
        self.Measurements_to_File_checkbox.setObjectName("Measurements_to_File_checkbox")
        self.vboxlayout6.addWidget(self.Measurements_to_File_checkbox)

        self.POVRayVideo_checkbox = QtWidgets.QCheckBox(self.buttonGroup1_2)
        self.POVRayVideo_checkbox.setObjectName("POVRayVideo_checkbox")
        self.vboxlayout6.addWidget(self.POVRayVideo_checkbox)
        self.gridlayout.addWidget(self.buttonGroup1_2,3,0,1,1)

        self.nh_instance_grpbox = QtWidgets.QGroupBox(NanoHiveDialog)
        self.nh_instance_grpbox.setObjectName("nh_instance_grpbox")

        self.gridlayout3 = QtWidgets.QGridLayout(self.nh_instance_grpbox)
        self.gridlayout3.setContentsMargins(11, 11, 11, 11)
        self.gridlayout3.setSpacing(6)
        self.gridlayout3.setObjectName("gridlayout3")

        self.nh_instance_combox = QtWidgets.QComboBox(self.nh_instance_grpbox)
        self.nh_instance_combox.setObjectName("nh_instance_combox")
        self.gridlayout3.addWidget(self.nh_instance_combox,0,0,1,1)

        spacerItem2 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.gridlayout3.addItem(spacerItem2,0,1,1,1)
        self.gridlayout.addWidget(self.nh_instance_grpbox,4,0,1,1)

        spacerItem3 = QtWidgets.QSpacerItem(20,16,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem3,5,0,1,1)

        self.hboxlayout4 = QtWidgets.QHBoxLayout()
        self.hboxlayout4.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.run_sim_btn = QtWidgets.QPushButton(NanoHiveDialog)
        self.run_sim_btn.setDefault(True)
        self.run_sim_btn.setObjectName("run_sim_btn")
        self.hboxlayout4.addWidget(self.run_sim_btn)

        self.cancel_btn = QtWidgets.QPushButton(NanoHiveDialog)
        self.cancel_btn.setDefault(False)
        self.cancel_btn.setObjectName("cancel_btn")
        self.hboxlayout4.addWidget(self.cancel_btn)
        self.gridlayout.addLayout(self.hboxlayout4,6,0,1,1)

        self.retranslateUi(NanoHiveDialog)
        self.run_sim_btn.clicked.connect(NanoHiveDialog.accept)
        self.cancel_btn.clicked.connect(NanoHiveDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NanoHiveDialog)

    def retranslateUi(self, NanoHiveDialog):
        NanoHiveDialog.setWindowTitle(QtCore.QCoreApplication.translate("NanoHiveDialog", "Nano-Hive Setup", None))
        self.namelbl.setText(QtCore.QCoreApplication.translate("NanoHiveDialog", "Name :", None))
        self.desclbl.setText(QtCore.QCoreApplication.translate("NanoHiveDialog", "Description :", None))
        self.parms_grpbox.setTitle(QtCore.QCoreApplication.translate("NanoHiveDialog", "Parameters", None))
        self.textLabel5.setText(QtCore.QCoreApplication.translate("NanoHiveDialog", "Total Frames:", None))
        self.textLabel2.setText(QtCore.QCoreApplication.translate("NanoHiveDialog", "Steps per Frame :", None))
        self.textLabel3.setText(QtCore.QCoreApplication.translate("NanoHiveDialog", "Temperature :", None))
        self.textLabel2_2.setText(QtCore.QCoreApplication.translate("NanoHiveDialog", "0.1 femtosecond", None))
        self.textLabel3_2.setText(QtCore.QCoreApplication.translate("NanoHiveDialog", "Kelvin", None))
        self.buttonGroup1.setTitle(QtCore.QCoreApplication.translate("NanoHiveDialog", "Physical Interaction Plugins", None))
        self.MPQC_GD_checkbox.setText(QtCore.QCoreApplication.translate("NanoHiveDialog", "MPQC - Gradient Dynamics", None))
        self.MPQC_GD_options_btn.setText(QtCore.QCoreApplication.translate("NanoHiveDialog", "Options...", None))
        self.MPQC_ESP_checkbox.setText(QtCore.QCoreApplication.translate("NanoHiveDialog", "MPQC - ESP Plane", None))
        self.ESP_image_combox.addItem(QtCore.QCoreApplication.translate("NanoHiveDialog", "(No ESP Image jigs)", None))
        self.AIREBO_checkbox.setText(QtCore.QCoreApplication.translate("NanoHiveDialog", "AIREBO", None))
        self.buttonGroup1_2.setTitle(QtCore.QCoreApplication.translate("NanoHiveDialog", "Results Plugins", None))
        self.Measurements_to_File_checkbox.setText(QtCore.QCoreApplication.translate("NanoHiveDialog", "Measurement Set to File", None))
        self.POVRayVideo_checkbox.setText(QtCore.QCoreApplication.translate("NanoHiveDialog", "POV-Ray Video", None))
        self.nh_instance_grpbox.setTitle(QtCore.QCoreApplication.translate("NanoHiveDialog", "Nano-Hive Instance", None))
        self.nh_instance_combox.addItem(QtCore.QCoreApplication.translate("NanoHiveDialog", "My Computer", None))
        self.run_sim_btn.setText(QtCore.QCoreApplication.translate("NanoHiveDialog", "Run Simulation", None))
        self.cancel_btn.setText(QtCore.QCoreApplication.translate("NanoHiveDialog", "Cancel", None))
