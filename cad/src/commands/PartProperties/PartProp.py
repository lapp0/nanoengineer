# Copyright 2004-2007 Nanorex, Inc.  See LICENSE file for details.
"""
PartProp.py

$Id$
"""

from PyQt5.QtWidgets import QDialog
from commands.PartProperties.PartPropDialog import Ui_PartPropDialog

class PartProp(QDialog, Ui_PartPropDialog):
    def __init__(self, assy):
        QDialog.__init__(self)
        self.setupUi(self)
        self.okPushButton.clicked.connect(self.accept)
        self.cancelPushButton.clicked.connect(self.reject)

        self.nameLineEdit.setText(assy.name)

        self.mmpformatLabel.setText("MMP File Format: " + assy.mmpformat)

        # Get statistics of part and display them in the statView widget.
        from commands.GroupProperties.GroupProp import Statistics
        stats = Statistics(assy.tree)
        stats.display(self.statsView)

    def accept(self):
        QDialog.accept(self)

    def reject(self):
        QDialog.reject(self)
