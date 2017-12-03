# Copyright 2006-2007 Nanorex, Inc.  See LICENSE file for details.
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Ticker(QObject):

    def __init__(self):
        QObject.__init__(self)
        self.timer = timer = QTimer(self)
        #timer.setSingleShot(True)
        self.timer.timeout.connect(self.hello)
        timer.start(1000)

    def hello(self):
        print('hi it works')
        return 4

x=Ticker()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.show()
    app.exec_()
