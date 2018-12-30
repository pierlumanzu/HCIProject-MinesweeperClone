# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuccessSaveDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuccessSaveDialog(object):
    def setupUi(self, SuccessSaveDialog):
        SuccessSaveDialog.setObjectName("SuccessSaveDialog")
        SuccessSaveDialog.resize(400, 85)
        self.buttonBox = QtWidgets.QDialogButtonBox(SuccessSaveDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 50, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.labelSuccessSave = QtWidgets.QLabel(SuccessSaveDialog)
        self.labelSuccessSave.setGeometry(QtCore.QRect(30, 20, 161, 31))
        self.labelSuccessSave.setObjectName("labelSuccessSave")

        self.retranslateUi(SuccessSaveDialog)
        self.buttonBox.accepted.connect(SuccessSaveDialog.accept)
        self.buttonBox.rejected.connect(SuccessSaveDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SuccessSaveDialog)

    def retranslateUi(self, SuccessSaveDialog):
        _translate = QtCore.QCoreApplication.translate
        SuccessSaveDialog.setWindowTitle(_translate("SuccessSaveDialog", "Success"))
        self.labelSuccessSave.setText(_translate("SuccessSaveDialog", "Game Saved Successfully"))

