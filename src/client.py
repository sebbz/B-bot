#!/usr/bin/python

#OMG LOL

from PyQt4 import QtGui
from mainwindow import Ui_MainWindow
import sys

class ClientWindow(QtGui.QMainWindow):
	def __init__(self, parent=None):
        	QtGui.QWidget.__init__(self, parent)
        	self.ui = Ui_MainWindow()
        	self.ui.setupUi(self)
#hej
def run():
	a = QtGui.QApplication(sys.argv)
		
	w = ClientWindow()
	w.show()
	
	sys.exit(a.exec_())

if __name__ == '__main__':
	run()
