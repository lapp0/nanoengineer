"""
FetchPDBDialog.py
Qt Dialog for fetching pdb files from the interweb

@author: Urmi
@version: $Id$
@copyright:2008 Nanorex, Inc. See LICENSE file for details.
"""

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QDialog, QLineEdit, QPushButton, QLabel, QApplication


class FetchPDBDialog(QDialog):
    editingFinished = pyqtSignal()

    def __init__(self, parent = None):
        self.parentWidget = parent
        super(FetchPDBDialog, self).__init__(parent)
        self.text = ''
        self.setWindowTitle("Fetch PDB")

        layout = QVBoxLayout()

        idLayout = QHBoxLayout()
        self.label = QLabel("Enter PDB ID:")
        self.lineEdit = QLineEdit()
        #self.lineEdit.setMaxLength(8) # Check with Piotr about this.
        idLayout.addWidget(self.label)
        idLayout.addWidget(self.lineEdit)

        self.okButton = QPushButton("&OK")
        self.cancelButton = QPushButton("Cancel")
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.okButton)
        buttonLayout.addWidget(self.cancelButton)

        layout.addLayout(idLayout)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

        self.lineEdit.returnPressed.connect(self.getProteinCode)
        self.okButton.clicked.connect(self.getProteinCode)
        self.cancelButton.clicked.connect(self.reject)
        self.show()
        return

    def getProteinCode(self):
        self.parentWidget.setPDBCode(str(self.lineEdit.text()))
        self.close()
        self.editingFinished.emit()
        return
