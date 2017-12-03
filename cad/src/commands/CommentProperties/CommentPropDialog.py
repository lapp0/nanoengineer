# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'COmmentPropDialog.ui'
#
# Created: Thu Aug 07 18:04:11 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CommentPropDialog(object):
    def setupUi(self, CommentPropDialog):
        CommentPropDialog.setObjectName("CommentPropDialog")
        CommentPropDialog.resize(QtCore.QSize(QtCore.QRect(0,0,390,275).size()).expandedTo(CommentPropDialog.minimumSizeHint()))

        self.gridlayout = QtWidgets.QGridLayout(CommentPropDialog)

        # note: this change will be lost when this file is remade from the .ui file.
        # it's a short term workaround only. [bruce 080808]
        from utilities.GlobalPreferences import debug_pref_support_Qt_4point2

        # doesn't seem to work with qt 4.2?
        #if not debug_pref_support_Qt_4point2():
        #    self.gridlayout.setContentsMargins(0,0,0,2)

        self.gridlayout.setSpacing(2)
        self.gridlayout.setObjectName("gridlayout")

        self.comment_textedit = QtWidgets.QTextEdit(CommentPropDialog)
        self.comment_textedit.setObjectName("comment_textedit")
        self.gridlayout.addWidget(self.comment_textedit,0,0,1,1)

        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setSpacing(4)
        self.hboxlayout.setObjectName("hboxlayout")

        self.date_time_btn = QtWidgets.QPushButton(CommentPropDialog)
        self.date_time_btn.setObjectName("date_time_btn")
        self.hboxlayout.addWidget(self.date_time_btn)

        spacerItem = QtWidgets.QSpacerItem(81,25,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.cancel_btn = QtWidgets.QPushButton(CommentPropDialog)
        self.cancel_btn.setObjectName("cancel_btn")
        self.hboxlayout.addWidget(self.cancel_btn)

        self.ok__btn = QtWidgets.QPushButton(CommentPropDialog)
        self.ok__btn.setObjectName("ok__btn")
        self.hboxlayout.addWidget(self.ok__btn)

        spacerItem1 = QtWidgets.QSpacerItem(20,20,QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.gridlayout.addLayout(self.hboxlayout,1,0,1,1)

        self.retranslateUi(CommentPropDialog)
        self.cancel_btn.clicked.connect(CommentPropDialog.reject)
        self.ok__btn.clicked.connect(CommentPropDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(CommentPropDialog)

    def retranslateUi(self, CommentPropDialog):
        CommentPropDialog.setWindowTitle(QtCore.QCoreApplication.translate("CommentPropDialog", "Comment", None))
        self.date_time_btn.setText(QtCore.QCoreApplication.translate("CommentPropDialog", "Date/Time Stamp", None))
        self.cancel_btn.setText(QtCore.QCoreApplication.translate("CommentPropDialog", "Cancel", None))
        self.ok__btn.setText(QtCore.QCoreApplication.translate("CommentPropDialog", "OK", None))

