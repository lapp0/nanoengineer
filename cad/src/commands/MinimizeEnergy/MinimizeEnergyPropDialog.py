# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MinimizeEnergyPropDialog.ui'
#
# Created: Fri Jun 06 11:55:35 2008
#      by: PyQt4 UI code generator 4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MinimizeEnergyPropDialog(object):
    def setupUi(self, MinimizeEnergyPropDialog):
        MinimizeEnergyPropDialog.setObjectName("MinimizeEnergyPropDialog")
        MinimizeEnergyPropDialog.resize(QtCore.QSize(QtCore.QRect(0,0,300,500).size()).expandedTo(MinimizeEnergyPropDialog.minimumSizeHint()))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(3),QtWidgets.QSizePolicy.Policy(3))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MinimizeEnergyPropDialog.sizePolicy().hasHeightForWidth())
        MinimizeEnergyPropDialog.setSizePolicy(sizePolicy)
        MinimizeEnergyPropDialog.setMinimumSize(QtCore.QSize(300,500))

        self.gridlayout = QtWidgets.QGridLayout(MinimizeEnergyPropDialog)
        self.gridlayout.setContentsMargins(9, 9, 9, 9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        spacerItem = QtWidgets.QSpacerItem(221,21,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem,5,0,1,1)

        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.whatsthis_btn = QtWidgets.QToolButton(MinimizeEnergyPropDialog)
        self.whatsthis_btn.setObjectName("whatsthis_btn")
        self.hboxlayout.addWidget(self.whatsthis_btn)

        spacerItem1 = QtWidgets.QSpacerItem(41,23,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)

        self.cancel_btn = QtWidgets.QPushButton(MinimizeEnergyPropDialog)
        self.cancel_btn.setAutoDefault(False)
        self.cancel_btn.setObjectName("cancel_btn")
        self.hboxlayout.addWidget(self.cancel_btn)

        self.ok_btn = QtWidgets.QPushButton(MinimizeEnergyPropDialog)
        self.ok_btn.setAutoDefault(False)
        self.ok_btn.setObjectName("ok_btn")
        self.hboxlayout.addWidget(self.ok_btn)
        self.gridlayout.addLayout(self.hboxlayout,6,0,1,1)

        self.buttonGroup8_2 = QtWidgets.QGroupBox(MinimizeEnergyPropDialog)
        self.buttonGroup8_2.setObjectName("buttonGroup8_2")

        self.vboxlayout = QtWidgets.QVBoxLayout(self.buttonGroup8_2)
        self.vboxlayout.setContentsMargins(4, 4, 4, 4)
        self.vboxlayout.setSpacing(4)
        self.vboxlayout.setObjectName("vboxlayout")

        self.minimize_engine_combobox = QtWidgets.QComboBox(self.buttonGroup8_2)
        self.minimize_engine_combobox.setObjectName("minimize_engine_combobox")
        self.vboxlayout.addWidget(self.minimize_engine_combobox)
        self.gridlayout.addWidget(self.buttonGroup8_2,0,0,1,1)

        self.buttonGroup8 = QtWidgets.QGroupBox(MinimizeEnergyPropDialog)
        self.buttonGroup8.setObjectName("buttonGroup8")

        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.buttonGroup8)
        self.vboxlayout1.setContentsMargins(4, 4, 4, 4)
        self.vboxlayout1.setSpacing(2)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.minimize_all_rbtn = QtWidgets.QRadioButton(self.buttonGroup8)
        self.minimize_all_rbtn.setChecked(True)
        self.minimize_all_rbtn.setObjectName("minimize_all_rbtn")
        self.vboxlayout1.addWidget(self.minimize_all_rbtn)

        self.minimize_sel_rbtn = QtWidgets.QRadioButton(self.buttonGroup8)
        self.minimize_sel_rbtn.setObjectName("minimize_sel_rbtn")
        self.vboxlayout1.addWidget(self.minimize_sel_rbtn)

        self.electrostaticsForDnaDuringMinimize_checkBox = QtWidgets.QCheckBox(self.buttonGroup8)
        self.electrostaticsForDnaDuringMinimize_checkBox.setChecked(True)
        self.electrostaticsForDnaDuringMinimize_checkBox.setObjectName("electrostaticsForDnaDuringMinimize_checkBox")
        self.vboxlayout1.addWidget(self.electrostaticsForDnaDuringMinimize_checkBox)

        self.enableNeighborSearching_check_box = QtWidgets.QCheckBox(self.buttonGroup8)
        self.enableNeighborSearching_check_box.setChecked(True)
        self.enableNeighborSearching_check_box.setObjectName("enableNeighborSearching_check_box")
        self.vboxlayout1.addWidget(self.enableNeighborSearching_check_box)
        self.gridlayout.addWidget(self.buttonGroup8,1,0,1,1)

        self.watch_motion_groupbox = QtWidgets.QGroupBox(MinimizeEnergyPropDialog)
        self.watch_motion_groupbox.setCheckable(True)
        self.watch_motion_groupbox.setObjectName("watch_motion_groupbox")

        self.gridlayout1 = QtWidgets.QGridLayout(self.watch_motion_groupbox)
        self.gridlayout1.setContentsMargins(4, 4, 4, 4)
        self.gridlayout1.setSpacing(2)
        self.gridlayout1.setObjectName("gridlayout1")

        self.update_asap_rbtn = QtWidgets.QRadioButton(self.watch_motion_groupbox)
        self.update_asap_rbtn.setChecked(True)
        self.update_asap_rbtn.setObjectName("update_asap_rbtn")
        self.gridlayout1.addWidget(self.update_asap_rbtn,0,0,1,1)

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(2)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.update_every_rbtn = QtWidgets.QRadioButton(self.watch_motion_groupbox)
        self.update_every_rbtn.setObjectName("update_every_rbtn")
        self.hboxlayout1.addWidget(self.update_every_rbtn)

        self.update_number_spinbox = QtWidgets.QSpinBox(self.watch_motion_groupbox)
        self.update_number_spinbox.setMaximum(9999)
        self.update_number_spinbox.setMinimum(1)
        self.update_number_spinbox.setProperty("value",QtCore.QVariant(1))
        self.update_number_spinbox.setObjectName("update_number_spinbox")
        self.hboxlayout1.addWidget(self.update_number_spinbox)

        self.update_units_combobox = QtWidgets.QComboBox(self.watch_motion_groupbox)
        self.update_units_combobox.setObjectName("update_units_combobox")
        self.hboxlayout1.addWidget(self.update_units_combobox)

        spacerItem2 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem2)
        self.gridlayout1.addLayout(self.hboxlayout1,1,0,1,1)
        self.gridlayout.addWidget(self.watch_motion_groupbox,2,0,1,1)

        self.groupBox20 = QtWidgets.QGroupBox(MinimizeEnergyPropDialog)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(5),QtWidgets.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox20.sizePolicy().hasHeightForWidth())
        self.groupBox20.setSizePolicy(sizePolicy)
        self.groupBox20.setObjectName("groupBox20")

        self.hboxlayout2 = QtWidgets.QHBoxLayout(self.groupBox20)
        self.hboxlayout2.setContentsMargins(4, 4, 4, 4)
        self.hboxlayout2.setSpacing(4)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.vboxlayout2 = QtWidgets.QVBoxLayout()
        self.vboxlayout2.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout2.setSpacing(2)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.endrms_lbl = QtWidgets.QLabel(self.groupBox20)
        self.endrms_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.endrms_lbl.setObjectName("endrms_lbl")
        self.vboxlayout2.addWidget(self.endrms_lbl)

        self.endmax_lbl = QtWidgets.QLabel(self.groupBox20)
        self.endmax_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.endmax_lbl.setObjectName("endmax_lbl")
        self.vboxlayout2.addWidget(self.endmax_lbl)

        self.cutoverrms_lbl = QtWidgets.QLabel(self.groupBox20)
        self.cutoverrms_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cutoverrms_lbl.setObjectName("cutoverrms_lbl")
        self.vboxlayout2.addWidget(self.cutoverrms_lbl)

        self.cutovermax_lbl = QtWidgets.QLabel(self.groupBox20)
        self.cutovermax_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cutovermax_lbl.setObjectName("cutovermax_lbl")
        self.vboxlayout2.addWidget(self.cutovermax_lbl)
        self.hboxlayout2.addLayout(self.vboxlayout2)

        self.vboxlayout3 = QtWidgets.QVBoxLayout()
        self.vboxlayout3.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout3.setSpacing(2)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.endRmsDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox20)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(3),QtWidgets.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endRmsDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.endRmsDoubleSpinBox.setSizePolicy(sizePolicy)
        self.endRmsDoubleSpinBox.setDecimals(3)
        self.endRmsDoubleSpinBox.setMaximum(501.0)
        self.endRmsDoubleSpinBox.setProperty("value",QtCore.QVariant(1.0))
        self.endRmsDoubleSpinBox.setObjectName("endRmsDoubleSpinBox")
        self.vboxlayout3.addWidget(self.endRmsDoubleSpinBox)

        self.endMaxDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox20)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(3),QtWidgets.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endMaxDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.endMaxDoubleSpinBox.setSizePolicy(sizePolicy)
        self.endMaxDoubleSpinBox.setDecimals(2)
        self.endMaxDoubleSpinBox.setMaximum(2501.0)
        self.endMaxDoubleSpinBox.setProperty("value",QtCore.QVariant(0.0))
        self.endMaxDoubleSpinBox.setObjectName("endMaxDoubleSpinBox")
        self.vboxlayout3.addWidget(self.endMaxDoubleSpinBox)

        self.cutoverRmsDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox20)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(3),QtWidgets.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cutoverRmsDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.cutoverRmsDoubleSpinBox.setSizePolicy(sizePolicy)
        self.cutoverRmsDoubleSpinBox.setDecimals(2)
        self.cutoverRmsDoubleSpinBox.setMaximum(12500.0)
        self.cutoverRmsDoubleSpinBox.setProperty("value",QtCore.QVariant(0.0))
        self.cutoverRmsDoubleSpinBox.setObjectName("cutoverRmsDoubleSpinBox")
        self.vboxlayout3.addWidget(self.cutoverRmsDoubleSpinBox)

        self.cutoverMaxDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox20)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(3),QtWidgets.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cutoverMaxDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.cutoverMaxDoubleSpinBox.setSizePolicy(sizePolicy)
        self.cutoverMaxDoubleSpinBox.setDecimals(2)
        self.cutoverMaxDoubleSpinBox.setMaximum(60001.0)
        self.cutoverMaxDoubleSpinBox.setProperty("value",QtCore.QVariant(0.0))
        self.cutoverMaxDoubleSpinBox.setObjectName("cutoverMaxDoubleSpinBox")
        self.vboxlayout3.addWidget(self.cutoverMaxDoubleSpinBox)
        self.hboxlayout2.addLayout(self.vboxlayout3)

        spacerItem3 = QtWidgets.QSpacerItem(80,20,QtWidgets.QSizePolicy.MinimumExpanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem3)
        self.gridlayout.addWidget(self.groupBox20,3,0,1,1)

        self.hboxlayout3 = QtWidgets.QHBoxLayout()
        self.hboxlayout3.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        spacerItem4 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem4)

        self.restore_btn = QtWidgets.QPushButton(MinimizeEnergyPropDialog)
        self.restore_btn.setObjectName("restore_btn")
        self.hboxlayout3.addWidget(self.restore_btn)
        self.gridlayout.addLayout(self.hboxlayout3,4,0,1,1)

        self.retranslateUi(MinimizeEnergyPropDialog)
        QtCore.QMetaObject.connectSlotsByName(MinimizeEnergyPropDialog)

    def retranslateUi(self, MinimizeEnergyPropDialog):
        MinimizeEnergyPropDialog.setWindowTitle(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Minimize Energy", None))
        self.cancel_btn.setToolTip(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Cancel", None))
        self.cancel_btn.setText(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Cancel", None))
        self.ok_btn.setToolTip(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "OK", None))
        self.ok_btn.setText(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Minimize Energy", None))
        self.buttonGroup8_2.setTitle(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Minimize physics engine", None))
        self.minimize_engine_combobox.setToolTip(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Choose the simulation engine with which to minimize energy.", None))
        self.minimize_engine_combobox.addItem(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "NanoDynamics-1 (Default)", None))
        self.minimize_engine_combobox.addItem(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "GROMACS with ND1 Force Field", None))
        self.minimize_engine_combobox.addItem(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Background GROMACS with ND1 Force Field", None))
        self.buttonGroup8.setTitle(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Minimize Options", None))
        self.minimize_all_rbtn.setToolTip(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Perform energy minimization on all the atoms in the workspace", None))
        self.minimize_all_rbtn.setText(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Minimize all", None))
        self.minimize_sel_rbtn.setToolTip(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Perform energy minimization on only the atoms that have been selected", None))
        self.minimize_sel_rbtn.setText(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Minimize selection", None))
        self.electrostaticsForDnaDuringMinimize_checkBox.setText(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Electrostatics for DNA reduced model", None))
        self.enableNeighborSearching_check_box.setText(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Enable neighbor searching (slow but accurate)", None))
        self.watch_motion_groupbox.setTitle(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Watch motion in real time", None))
        self.update_asap_rbtn.setToolTip(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Update every 2 seconds, or faster if it doesn\'t slow adjustments by more than 20%", None))
        self.update_asap_rbtn.setText(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Update as fast as possible", None))
        self.update_every_rbtn.setToolTip(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Specify how often to update the screen during adjustments", None))
        self.update_every_rbtn.setText(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Update every", None))
        self.update_number_spinbox.setToolTip(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Specify how often to update the screen during adjustments", None))
        self.update_units_combobox.setToolTip(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Specify how often to update the screen during adjustments", None))
        self.update_units_combobox.addItem(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "frames", None))
        self.update_units_combobox.addItem(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "seconds", None))
        self.update_units_combobox.addItem(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "minutes", None))
        self.update_units_combobox.addItem(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "hours", None))
        self.groupBox20.setTitle(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Convergence criteria", None))
        self.endrms_lbl.setToolTip(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Target RMS force (pN)", None))
        self.endrms_lbl.setText(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "EndRMS:", None))
        self.endmax_lbl.setToolTip(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Target max force (pN)", None))
        self.endmax_lbl.setText(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "EndMax:", None))
        self.cutoverrms_lbl.setToolTip(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Cutover RMS force (pN)", None))
        self.cutoverrms_lbl.setText(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "CutoverRMS:", None))
        self.cutovermax_lbl.setToolTip(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Cutover max force (pN)", None))
        self.cutovermax_lbl.setText(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "CutoverMax:", None))
        self.endRmsDoubleSpinBox.setSuffix(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", " pN", None))
        self.endMaxDoubleSpinBox.setSuffix(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", " pN", None))
        self.cutoverRmsDoubleSpinBox.setSuffix(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", " pN", None))
        self.cutoverMaxDoubleSpinBox.setSuffix(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", " pN", None))
        self.restore_btn.setText(QtCore.QCoreApplication.translate("MinimizeEnergyPropDialog", "Restore Defaults", None))

