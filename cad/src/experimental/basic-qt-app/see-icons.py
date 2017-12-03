#!/usr/bin/python

# Copyright 2006-2007 Nanorex, Inc.  See LICENSE file for details.
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

# Hunt for the icons directory
icons = 'icons'
for i in range(3):
    import os
    if os.path.exists(icons + '/MainWindowUI_image1.png'):
        break
    icons = '../' + icons

iconlist = [x[:-1] for x in os.popen("/bin/ls " + icons + " | grep -v CVS").readlines()]

#iconlist = filter(lambda x: x.startswith("MainWindowUI"), iconlist)

iconlist.sort()

n = len(iconlist)
numRows = int((n ** 0.5) + 1)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #centralwidget = QScrollArea()
        #w = QWidget(self)
        #centralwidget.setWidget(w)
        #self.setCentralWidget(centralwidget)
        #self.layout = QGridLayout(w)

        centralwidget = QWidget(self)
        self.layout = QGridLayout(centralwidget)

        if False:
            scroller = QScrollArea()
            scroller.setWidget(centralwidget)
            scroller.show()
            scroller.setFocus()
            scroller.ensureVisible(640,480,10,10)
            centralwidget = scroller

        self.setCentralWidget(centralwidget)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        row, col = 0, 0
        for icon in iconlist:
            w = QWidget()
            lo = QVBoxLayout(w)
            lbl = QLabel(w)
            lbl.setPixmap(QPixmap(icons + '/' + icon))
            lo.addWidget(lbl)
            lbl = QLabel(w)
            lbl.setText(icon)
            lo.addWidget(lbl)
            self.layout.addWidget(w, row, col)
            col += 1
            if col == 5:
                row += 1
                col = 0

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    #mainWin = ScanList()
    mainWin.show()
    sys.exit(app.exec_())

