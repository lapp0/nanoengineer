# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SimSetupDialog.ui'
#
# Created: Fri Jun 06 12:02:42 2008
#      by: PyQt4 UI code generator 4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SimSetupDialog(object):
    def setupUi(self, SimSetupDialog):
        SimSetupDialog.setObjectName("SimSetupDialog")
        SimSetupDialog.resize(QtCore.QSize(QtCore.QRect(0,0,250,350).size()).expandedTo(SimSetupDialog.minimumSizeHint()))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(5),QtWidgets.QSizePolicy.Policy(3))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SimSetupDialog.sizePolicy().hasHeightForWidth())
        SimSetupDialog.setSizePolicy(sizePolicy)
        SimSetupDialog.setMinimumSize(QtCore.QSize(0,350))
        SimSetupDialog.setModal(True)

        self.gridlayout = QtWidgets.QGridLayout(SimSetupDialog)
        self.gridlayout.setContentsMargins(9, 9, 9, 9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.whatsthis_btn = QtWidgets.QToolButton(SimSetupDialog)
        self.whatsthis_btn.setObjectName("whatsthis_btn")
        self.hboxlayout.addWidget(self.whatsthis_btn)

        spacerItem = QtWidgets.QSpacerItem(21,25,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.cancel_btn = QtWidgets.QPushButton(SimSetupDialog)
        self.cancel_btn.setDefault(False)
        self.cancel_btn.setObjectName("cancel_btn")
        self.hboxlayout.addWidget(self.cancel_btn)

        self.run_sim_btn = QtWidgets.QPushButton(SimSetupDialog)
        self.run_sim_btn.setDefault(True)
        self.run_sim_btn.setObjectName("run_sim_btn")
        self.hboxlayout.addWidget(self.run_sim_btn)
        self.gridlayout.addLayout(self.hboxlayout,4,0,1,1)

        spacerItem1 = QtWidgets.QSpacerItem(20,16,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem1,3,0,1,1)

        self.parms_grpbox = QtWidgets.QGroupBox(SimSetupDialog)
        self.parms_grpbox.setObjectName("parms_grpbox")

        self.vboxlayout = QtWidgets.QVBoxLayout(self.parms_grpbox)
        self.vboxlayout.setContentsMargins(4, 4, 4, 4)
        self.vboxlayout.setSpacing(4)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(4)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.vboxlayout1 = QtWidgets.QVBoxLayout()
        self.vboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout1.setSpacing(4)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.textLabel5 = QtWidgets.QLabel(self.parms_grpbox)
        self.textLabel5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel5.setObjectName("textLabel5")
        self.vboxlayout1.addWidget(self.textLabel5)

        self.textLabel2 = QtWidgets.QLabel(self.parms_grpbox)
        self.textLabel2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel2.setObjectName("textLabel2")
        self.vboxlayout1.addWidget(self.textLabel2)

        self.textLabel3 = QtWidgets.QLabel(self.parms_grpbox)
        self.textLabel3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textLabel3.setObjectName("textLabel3")
        self.vboxlayout1.addWidget(self.textLabel3)
        self.hboxlayout1.addLayout(self.vboxlayout1)

        self.vboxlayout2 = QtWidgets.QVBoxLayout()
        self.vboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout2.setSpacing(4)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.totalFramesSpinBox = QtWidgets.QSpinBox(self.parms_grpbox)
        self.totalFramesSpinBox.setMaximum(1000000)
        self.totalFramesSpinBox.setMinimum(1)
        self.totalFramesSpinBox.setSingleStep(15)
        self.totalFramesSpinBox.setProperty("value",QtCore.QVariant(900))
        self.totalFramesSpinBox.setObjectName("totalFramesSpinBox")
        self.vboxlayout2.addWidget(self.totalFramesSpinBox)

        self.stepsPerFrameDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.parms_grpbox)
        self.stepsPerFrameDoubleSpinBox.setDecimals(2)
        self.stepsPerFrameDoubleSpinBox.setSingleStep(0.1)
        self.stepsPerFrameDoubleSpinBox.setProperty("value",QtCore.QVariant(1.0))
        self.stepsPerFrameDoubleSpinBox.setObjectName("stepsPerFrameDoubleSpinBox")
        self.vboxlayout2.addWidget(self.stepsPerFrameDoubleSpinBox)

        self.temperatureSpinBox = QtWidgets.QSpinBox(self.parms_grpbox)
        self.temperatureSpinBox.setMaximum(99999)
        self.temperatureSpinBox.setProperty("value",QtCore.QVariant(300))
        self.temperatureSpinBox.setObjectName("temperatureSpinBox")
        self.vboxlayout2.addWidget(self.temperatureSpinBox)
        self.hboxlayout1.addLayout(self.vboxlayout2)

        spacerItem2 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem2)
        self.vboxlayout.addLayout(self.hboxlayout1)

        self.potential_energy_checkbox = QtWidgets.QCheckBox(self.parms_grpbox)
        self.potential_energy_checkbox.setObjectName("potential_energy_checkbox")
        self.vboxlayout.addWidget(self.potential_energy_checkbox)
        self.gridlayout.addWidget(self.parms_grpbox,0,0,1,1)

        self.watch_motion_groupbox = QtWidgets.QGroupBox(SimSetupDialog)
        self.watch_motion_groupbox.setCheckable(True)
        self.watch_motion_groupbox.setChecked(True)
        self.watch_motion_groupbox.setObjectName("watch_motion_groupbox")

        self.gridlayout1 = QtWidgets.QGridLayout(self.watch_motion_groupbox)
        self.gridlayout1.setContentsMargins(4, 4, 4, 4)
        self.gridlayout1.setSpacing(2)
        self.gridlayout1.setObjectName("gridlayout1")

        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout2.setSpacing(4)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.update_every_rbtn = QtWidgets.QRadioButton(self.watch_motion_groupbox)
        self.update_every_rbtn.setObjectName("update_every_rbtn")
        self.hboxlayout2.addWidget(self.update_every_rbtn)

        self.update_number_spinbox = QtWidgets.QSpinBox(self.watch_motion_groupbox)
        self.update_number_spinbox.setMaximum(9999)
        self.update_number_spinbox.setMinimum(1)
        self.update_number_spinbox.setProperty("value",QtCore.QVariant(1))
        self.update_number_spinbox.setObjectName("update_number_spinbox")
        self.hboxlayout2.addWidget(self.update_number_spinbox)

        self.update_units_combobox = QtWidgets.QComboBox(self.watch_motion_groupbox)
        self.update_units_combobox.setObjectName("update_units_combobox")
        self.hboxlayout2.addWidget(self.update_units_combobox)

        spacerItem3 = QtWidgets.QSpacerItem(71,16,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem3)
        self.gridlayout1.addLayout(self.hboxlayout2,1,0,1,1)

        self.update_asap_rbtn = QtWidgets.QRadioButton(self.watch_motion_groupbox)
        self.update_asap_rbtn.setChecked(True)
        self.update_asap_rbtn.setObjectName("update_asap_rbtn")
        self.gridlayout1.addWidget(self.update_asap_rbtn,0,0,1,1)
        self.gridlayout.addWidget(self.watch_motion_groupbox,1,0,1,1)

        self.md_engine_groupbox = QtWidgets.QGroupBox(SimSetupDialog)
        self.md_engine_groupbox.setObjectName("md_engine_groupbox")

        self.vboxlayout3 = QtWidgets.QVBoxLayout(self.md_engine_groupbox)
        self.vboxlayout3.setContentsMargins(4, 4, 4, 4)
        self.vboxlayout3.setSpacing(4)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.hboxlayout3 = QtWidgets.QHBoxLayout()
        self.hboxlayout3.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout3.setSpacing(4)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.simulation_engine_combobox = QtWidgets.QComboBox(self.md_engine_groupbox)
        self.simulation_engine_combobox.setObjectName("simulation_engine_combobox")
        self.hboxlayout3.addWidget(self.simulation_engine_combobox)

        spacerItem4 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem4)
        self.vboxlayout3.addLayout(self.hboxlayout3)

        self.electrostaticsForDnaDuringDynamics_checkBox = QtWidgets.QCheckBox(self.md_engine_groupbox)
        self.electrostaticsForDnaDuringDynamics_checkBox.setChecked(True)
        self.electrostaticsForDnaDuringDynamics_checkBox.setObjectName("electrostaticsForDnaDuringDynamics_checkBox")
        self.vboxlayout3.addWidget(self.electrostaticsForDnaDuringDynamics_checkBox)
        self.gridlayout.addWidget(self.md_engine_groupbox,2,0,1,1)

        self.retranslateUi(SimSetupDialog)
        self.cancel_btn.clicked.connect(SimSetupDialog.close)
        QtCore.QMetaObject.connectSlotsByName(SimSetupDialog)

    def retranslateUi(self, SimSetupDialog):
        SimSetupDialog.setWindowTitle(QtCore.QCoreApplication.translate("SimSetupDialog", "Run Dynamics", None))
        SimSetupDialog.setToolTip(QtCore.QCoreApplication.translate("SimSetupDialog", "Run Dynamics Setup Dialog", None))
        self.cancel_btn.setText(QtCore.QCoreApplication.translate("SimSetupDialog", "Cancel", None))
        self.run_sim_btn.setText(QtCore.QCoreApplication.translate("SimSetupDialog", "Run Simulation", None))
        self.parms_grpbox.setTitle(QtCore.QCoreApplication.translate("SimSetupDialog", "Simulation parameters", None))
        self.textLabel5.setText(QtCore.QCoreApplication.translate("SimSetupDialog", "Total frames:", None))
        self.textLabel2.setText(QtCore.QCoreApplication.translate("SimSetupDialog", "Steps per frame:", None))
        self.textLabel3.setText(QtCore.QCoreApplication.translate("SimSetupDialog", "Temperature:", None))
        self.totalFramesSpinBox.setToolTip(QtCore.QCoreApplication.translate("SimSetupDialog", "Total Frames value", None))
        self.totalFramesSpinBox.setSuffix(QtCore.QCoreApplication.translate("SimSetupDialog", " frames", None))
        self.stepsPerFrameDoubleSpinBox.setSuffix(QtCore.QCoreApplication.translate("SimSetupDialog", " femtoseconds", None))
        self.temperatureSpinBox.setToolTip(QtCore.QCoreApplication.translate("SimSetupDialog", "Temperature", None))
        self.temperatureSpinBox.setSuffix(QtCore.QCoreApplication.translate("SimSetupDialog", " K", None))
        self.potential_energy_checkbox.setText(QtCore.QCoreApplication.translate("SimSetupDialog", "Plot energy in tracefile", None))
        self.watch_motion_groupbox.setTitle(QtCore.QCoreApplication.translate("SimSetupDialog", "Watch motion in real time", None))
        self.update_every_rbtn.setToolTip(QtCore.QCoreApplication.translate("SimSetupDialog", "Specify how often to update the screen during the simulation.", None))
        self.update_every_rbtn.setText(QtCore.QCoreApplication.translate("SimSetupDialog", "Update every", None))
        self.update_number_spinbox.setToolTip(QtCore.QCoreApplication.translate("SimSetupDialog", "Specify how often to update the screen during the simulation.", None))
        self.update_units_combobox.setToolTip(QtCore.QCoreApplication.translate("SimSetupDialog", "Specify how often to update the screen during the simulation.", None))
        self.update_units_combobox.addItem(QtCore.QCoreApplication.translate("SimSetupDialog", "frames", None))
        self.update_units_combobox.addItem(QtCore.QCoreApplication.translate("SimSetupDialog", "seconds", None))
        self.update_units_combobox.addItem(QtCore.QCoreApplication.translate("SimSetupDialog", "minutes", None))
        self.update_units_combobox.addItem(QtCore.QCoreApplication.translate("SimSetupDialog", "hours", None))
        self.update_asap_rbtn.setToolTip(QtCore.QCoreApplication.translate("SimSetupDialog", "Update every 2 seconds, or faster if it doesn\'t slow simulation by more than 20%", None))
        self.update_asap_rbtn.setText(QtCore.QCoreApplication.translate("SimSetupDialog", "Update as fast as possible", None))
        self.md_engine_groupbox.setTitle(QtCore.QCoreApplication.translate("SimSetupDialog", "Molecular Dynamics Engine", None))
        self.simulation_engine_combobox.setToolTip(QtCore.QCoreApplication.translate("SimSetupDialog", "Choose the simulation engine with which to minimize energy.", None))
        self.simulation_engine_combobox.addItem(QtCore.QCoreApplication.translate("SimSetupDialog", "NanoDynamics-1 (Default)", None))
        self.simulation_engine_combobox.addItem(QtCore.QCoreApplication.translate("SimSetupDialog", "GROMACS", None))
        self.electrostaticsForDnaDuringDynamics_checkBox.setText(QtCore.QCoreApplication.translate("SimSetupDialog", "Electrostatics for DNA reduced model", None))

