# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(332, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 450, 131, 71))
        self.pushButton.setObjectName("pushButton")
        self.name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.name.setGeometry(QtCore.QRect(80, 90, 221, 31))
        self.name.setObjectName("name")
        self.roasting = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.roasting.setGeometry(QtCore.QRect(80, 150, 221, 31))
        self.roasting.setObjectName("roasting")
        self.gog = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.gog.setGeometry(QtCore.QRect(10, 220, 221, 31))
        self.gog.setObjectName("gog")
        self.description = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.description.setGeometry(QtCore.QRect(80, 270, 221, 31))
        self.description.setObjectName("description")
        self.valume = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.valume.setGeometry(QtCore.QRect(80, 389, 221, 31))
        self.valume.setObjectName("valume")
        self.prise = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.prise.setGeometry(QtCore.QRect(80, 330, 221, 31))
        self.prise.setObjectName("prise")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 90, 61, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 61, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 111, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 270, 51, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 330, 41, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 390, 41, 31))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "сохранить"))
        self.label.setText(_translate("MainWindow", "название"))
        self.label_2.setText(_translate("MainWindow", "прожарка"))
        self.label_3.setText(_translate("MainWindow", "молотый или зерна"))
        self.label_4.setText(_translate("MainWindow", "описание"))
        self.label_5.setText(_translate("MainWindow", "цена"))
        self.label_6.setText(_translate("MainWindow", "объём"))