# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Nov  4 21:55:54 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(447, 439)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 171, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 40, 93, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.firstCard = QtGui.QLabel(self.centralwidget)
        self.firstCard.setGeometry(QtCore.QRect(30, 90, 141, 261))
        self.firstCard.setAutoFillBackground(False)
        self.firstCard.setObjectName(_fromUtf8("firstCard"))
        self.firstCard_2 = QtGui.QLabel(self.centralwidget)
        self.firstCard_2.setGeometry(QtCore.QRect(200, 90, 141, 261))
        self.firstCard_2.setAutoFillBackground(False)
        self.firstCard_2.setObjectName(_fromUtf8("firstCard_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 447, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHej_och_v_lkommen_till_B = QtGui.QMenu(self.menubar)
        self.menuHej_och_v_lkommen_till_B.setObjectName(_fromUtf8("menuHej_och_v_lkommen_till_B"))
        MainWindow.setMenuBar(self.menubar)
        self.actionAvsluta = QtGui.QAction(MainWindow)
        self.actionAvsluta.setObjectName(_fromUtf8("actionAvsluta"))
        self.menuHej_och_v_lkommen_till_B.addAction(self.actionAvsluta)
        self.menubar.addAction(self.menuHej_och_v_lkommen_till_B.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionAvsluta, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "B-game", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Hej och välkommen till B!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.firstCard.setText(QtGui.QApplication.translate("MainWindow", "FÖSSTA KOTTET", None, QtGui.QApplication.UnicodeUTF8))
        self.firstCard_2.setText(QtGui.QApplication.translate("MainWindow", "ANDRA KOTTET", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHej_och_v_lkommen_till_B.setTitle(QtGui.QApplication.translate("MainWindow", "Arkiv", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAvsluta.setText(QtGui.QApplication.translate("MainWindow", "Avsluta", None, QtGui.QApplication.UnicodeUTF8))

