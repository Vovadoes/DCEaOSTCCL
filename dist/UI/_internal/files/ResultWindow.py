# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'files/ResultWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 145)
        Form.setMinimumSize(QtCore.QSize(650, 145))
        Form.setMaximumSize(QtCore.QSize(650, 145))
        Form.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_34 = QtWidgets.QLabel(Form)
        self.label_34.setMinimumSize(QtCore.QSize(20, 0))
        self.label_34.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.gridLayout_17.addWidget(self.label_34, 0, 2, 1, 1)
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_9.setEnabled(False)
        self.doubleSpinBox_9.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox_9.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox_9.setFont(font)
        self.doubleSpinBox_9.setStyleSheet("color: black; background-color: white;")
        self.doubleSpinBox_9.setDecimals(4)
        self.doubleSpinBox_9.setMinimum(-999999999.0)
        self.doubleSpinBox_9.setMaximum(999999999.0)
        self.doubleSpinBox_9.setSingleStep(0.001)
        self.doubleSpinBox_9.setProperty("value", 0.0)
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.gridLayout_17.addWidget(self.doubleSpinBox_9, 0, 3, 1, 1)
        self.label_36 = QtWidgets.QLabel(Form)
        self.label_36.setMinimumSize(QtCore.QSize(100, 0))
        self.label_36.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.gridLayout_17.addWidget(self.label_36, 0, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(Form)
        self.label_35.setMinimumSize(QtCore.QSize(60, 0))
        self.label_35.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_35.setFont(font)
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.gridLayout_17.addWidget(self.label_35, 0, 4, 1, 1)
        self.label_37 = QtWidgets.QLabel(Form)
        self.label_37.setMinimumSize(QtCore.QSize(35, 0))
        self.label_37.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.gridLayout_17.addWidget(self.label_37, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_17, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Определение кардинальных элементов и оптической силы толстой выпукло-вогнутой линзы"))
        self.label_34.setText(_translate("Form", "="))
        self.label_36.setText(_translate("Form", "<html><head/><body><p>Оптическая сила линзы:</p></body></html>"))
        self.label_37.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Ф</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "Значения кардинальных точек"))
        self.pushButton.setText(_translate("Form", "ОК"))
