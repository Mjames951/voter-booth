# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'voting_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 646)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.votebutton_john = QtWidgets.QPushButton(self.centralwidget)
        self.votebutton_john.setEnabled(False)
        self.votebutton_john.setGeometry(QtCore.QRect(160, 340, 93, 28))
        self.votebutton_john.setObjectName("votebutton_john")
        self.votebutton_jane = QtWidgets.QPushButton(self.centralwidget)
        self.votebutton_jane.setEnabled(False)
        self.votebutton_jane.setGeometry(QtCore.QRect(460, 340, 93, 28))
        self.votebutton_jane.setObjectName("votebutton_jane")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setEnabled(False)
        self.heading.setGeometry(QtCore.QRect(290, 250, 251, 16))
        self.heading.setObjectName("heading")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 50, 201, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 100, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(320, 430, 205, 16))
        self.description.setObjectName("description")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.votebutton_john.setText(_translate("MainWindow", "JOHN"))
        self.votebutton_jane.setText(_translate("MainWindow", "JANE"))
        self.heading.setText(_translate("MainWindow", "VOTE FOR SOMEONE"))
        self.label.setText(_translate("MainWindow", "DO YOOU WANT TO VOTE?"))
        self.pushButton.setText(_translate("MainWindow", "YES!"))
        self.description.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
