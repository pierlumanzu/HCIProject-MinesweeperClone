# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecordDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RecordDialog(object):
    def setupUi(self, RecordDialog):
        RecordDialog.setObjectName("RecordDialog")
        RecordDialog.resize(400, 192)
        self.buttonBox = QtWidgets.QDialogButtonBox(RecordDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.labelNewRecord = QtWidgets.QLabel(RecordDialog)
        self.labelNewRecord.setGeometry(QtCore.QRect(40, 10, 331, 16))
        self.labelNewRecord.setObjectName("labelNewRecord")
        self.nameRecord = QtWidgets.QLineEdit(RecordDialog)
        self.nameRecord.setGeometry(QtCore.QRect(40, 110, 331, 23))
        self.nameRecord.setMaxLength(30)
        self.nameRecord.setObjectName("nameRecord")
        self.labelNameRecord = QtWidgets.QLabel(RecordDialog)
        self.labelNameRecord.setGeometry(QtCore.QRect(40, 60, 321, 16))
        self.labelNameRecord.setObjectName("labelNameRecord")
        self.labelTimeRecord = QtWidgets.QLabel(RecordDialog)
        self.labelTimeRecord.setGeometry(QtCore.QRect(40, 20, 59, 41))
        self.labelTimeRecord.setObjectName("labelTimeRecord")
        self.labelWarningEmptySpaces = QtWidgets.QLabel(RecordDialog)
        self.labelWarningEmptySpaces.setGeometry(QtCore.QRect(40, 80, 241, 21))
        self.labelWarningEmptySpaces.setObjectName("labelWarningEmptySpaces")

        self.retranslateUi(RecordDialog)
        self.buttonBox.accepted.connect(RecordDialog.accept)
        self.buttonBox.rejected.connect(RecordDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RecordDialog)

    def retranslateUi(self, RecordDialog):
        _translate = QtCore.QCoreApplication.translate
        RecordDialog.setWindowTitle(_translate("RecordDialog", "A new record"))
        self.labelNewRecord.setText(_translate("RecordDialog", "Wow! A new record in this type of board."))
        self.labelNameRecord.setText(_translate("RecordDialog", "Insert your name in the ranking:"))
        self.labelTimeRecord.setText(_translate("RecordDialog", "TextLabel"))
        self.labelWarningEmptySpaces.setText(_translate("RecordDialog", "(All empty spaces will be deleted)"))

