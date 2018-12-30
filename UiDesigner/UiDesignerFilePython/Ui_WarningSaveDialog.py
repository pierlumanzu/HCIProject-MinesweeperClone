# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WarningSaveDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WarningSaveDialog(object):
    def setupUi(self, WarningSaveDialog):
        WarningSaveDialog.setObjectName("WarningSaveDialog")
        WarningSaveDialog.resize(400, 124)
        self.buttonBox = QtWidgets.QDialogButtonBox(WarningSaveDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 80, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.labelSameName = QtWidgets.QLabel(WarningSaveDialog)
        self.labelSameName.setGeometry(QtCore.QRect(20, 20, 321, 31))
        self.labelSameName.setObjectName("labelSameName")
        self.labelReplace = QtWidgets.QLabel(WarningSaveDialog)
        self.labelReplace.setGeometry(QtCore.QRect(20, 50, 201, 16))
        self.labelReplace.setObjectName("labelReplace")

        self.retranslateUi(WarningSaveDialog)
        self.buttonBox.accepted.connect(WarningSaveDialog.accept)
        self.buttonBox.rejected.connect(WarningSaveDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(WarningSaveDialog)

    def retranslateUi(self, WarningSaveDialog):
        _translate = QtCore.QCoreApplication.translate
        WarningSaveDialog.setWindowTitle(_translate("WarningSaveDialog", "Warning"))
        self.labelSameName.setText(_translate("WarningSaveDialog", "There is another game with the same name."))
        self.labelReplace.setText(_translate("WarningSaveDialog", "Do you want to replace it?"))

