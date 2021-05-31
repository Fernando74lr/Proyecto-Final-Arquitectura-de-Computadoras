# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 223)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Downloads/cheems.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(38, 70, 83);")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 787, 92))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelTemperatura = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(30)
        self.labelTemperatura.setFont(font)
        self.labelTemperatura.setStyleSheet("color:white;")
        self.labelTemperatura.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTemperatura.setObjectName("labelTemperatura")
        self.gridLayout.addWidget(self.labelTemperatura, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("System")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;\n"
"background-color: rgb(231, 111, 81);\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.labelProximidad = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(30)
        self.labelProximidad.setFont(font)
        self.labelProximidad.setStyleSheet("color:white;\n"
"background-color: rgb(203, 203, 203);\n"
"border-radius: 20px;")
        self.labelProximidad.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProximidad.setObjectName("labelProximidad")
        self.gridLayout.addWidget(self.labelProximidad, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("System")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"background-color: rgb(233, 196, 106);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("System")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"background-color: rgb(244, 162, 97);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("System")
        font.setItalic(False)
        self.progressBar.setFont(font)
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    background-color: rgba(211, 211, 211, .5);\n"
"    color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.189732, y1:0.204, x2:0.907, y2:0.125, stop:0 rgba(223, 223, 111, 255), stop:1 rgba(218, 72, 109, 255));\n"
"}\n"
"")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 170, 785, 3))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 180, 781, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.labelRefresh = QtWidgets.QLabel(self.centralwidget)
        self.labelRefresh.setGeometry(QtCore.QRect(540, 120, 251, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(15)
        self.labelRefresh.setFont(font)
        self.labelRefresh.setStyleSheet("color:white;")
        self.labelRefresh.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRefresh.setObjectName("labelRefresh")
        self.labelFecha = QtWidgets.QLabel(self.centralwidget)
        self.labelFecha.setGeometry(QtCore.QRect(10, 120, 301, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.labelFecha.setFont(font)
        self.labelFecha.setStyleSheet("color:white;")
        self.labelFecha.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFecha.setObjectName("labelFecha")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Momnitoreo"))
        self.labelTemperatura.setText(_translate("MainWindow", "---"))
        self.label_3.setText(_translate("MainWindow", "  SENSOR DE HUMEDAD  "))
        self.labelProximidad.setText(_translate("MainWindow", "---"))
        self.label.setText(_translate("MainWindow", "  SENSOR DE ILUMINACION  "))
        self.label_2.setText(_translate("MainWindow", "  SENSOR DE TEMPERATURA  "))
        self.progressBar.setToolTip(_translate("MainWindow", "<html><head/><body><p>Esta es una prueba</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Creado por team uwu: Alan Suárez, Benjamín Gutierrez, Fernando López, Kaleb Antonio\n"
""))
        self.labelRefresh.setText(_translate("MainWindow", "Actualizado hace: -- s"))
        self.labelFecha.setText(_translate("MainWindow", "Fecha: --------------------"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

