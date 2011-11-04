#!/usr/bin/python
from PyQt4 import QtGui, QtCore

#OMG LOL
from mainwindow import Ui_MainWindow
import sys

class NewLabel(QtGui.QLabel):
    def __init__(self, parent):
        QtGui.QLabel.__init__(self, parent)

    def mouseReleaseEvent(self, event):
        print "clikcat"
        self.emit(QtCore.SIGNAL("clicked()"))


class ClientWindow(QtGui.QMainWindow):
    Image = 'kukeliku.png'
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.firstCard.setPixmap(QtGui.QPixmap(self.Image))

        self.ui.firstCard = NewLabel(self)
        self.ui.firstCard.move(0,0)
        QtCore.QObject.connect(self.ui.firstCard, QtCore.SIGNAL("clicked()"), self.fix)

    def fix(self):
        self.ui.label.setText('Suck it')
            
if __name__ == '__main__':
    a = QtGui.QApplication(sys.argv)
            
    w = ClientWindow()
    w.show()
    sys.exit(a.exec_())
