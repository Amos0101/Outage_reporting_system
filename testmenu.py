# Form implementation generated from reading ui file 'testmenu.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 240)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionexit = QtGui.QAction(parent=MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionsave = QtGui.QAction(parent=MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionclose = QtGui.QAction(parent=MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.actionquite = QtGui.QAction(parent=MainWindow)
        self.actionquite.setObjectName("actionquite")
        self.menuFile.addAction(self.actionexit)
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addAction(self.actionclose)
        self.menuFile.addAction(self.actionquite)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionclose.setText(_translate("MainWindow", "close"))
        self.actionquite.setText(_translate("MainWindow", "quite"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())