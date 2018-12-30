# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WarningDeleteDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WarningDeleteDialog(object):
    def setupUi(self, WarningDeleteDialog):
        WarningDeleteDialog.setObjectName("WarningDeleteDialog")
        WarningDeleteDialog.resize(400, 109)
        self.buttonBox = QtWidgets.QDialogButtonBox(WarningDeleteDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 60, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.labelWarningDelete = QtWidgets.QLabel(WarningDeleteDialog)
        self.labelWarningDelete.setGeometry(QtCore.QRect(30, 20, 221, 31))
        self.labelWarningDelete.setObjectName("labelWarningDelete")

        self.retranslateUi(WarningDeleteDialog)
        self.buttonBox.accepted.connect(WarningDeleteDialog.accept)
        self.buttonBox.rejected.connect(WarningDeleteDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(WarningDeleteDialog)

    def retranslateUi(self, WarningDeleteDialog):
        _translate = QtCore.QCoreApplication.translate
        WarningDeleteDialog.setWindowTitle(_translate("WarningDeleteDialog", "Warning"))
        self.labelWarningDelete.setText(_translate("WarningDeleteDialog", "Are you sure to delete?"))

