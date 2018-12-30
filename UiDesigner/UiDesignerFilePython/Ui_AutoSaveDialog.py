# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutoSaveDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AutoSaveDialog(object):
    def setupUi(self, AutoSaveDialog):
        AutoSaveDialog.setObjectName("AutoSaveDialog")
        AutoSaveDialog.resize(400, 102)
        self.buttonBox = QtWidgets.QDialogButtonBox(AutoSaveDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 60, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.labelAutoSave = QtWidgets.QLabel(AutoSaveDialog)
        self.labelAutoSave.setGeometry(QtCore.QRect(30, 20, 261, 31))
        self.labelAutoSave.setObjectName("labelAutoSave")

        self.retranslateUi(AutoSaveDialog)
        self.buttonBox.accepted.connect(AutoSaveDialog.accept)
        self.buttonBox.rejected.connect(AutoSaveDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AutoSaveDialog)

    def retranslateUi(self, AutoSaveDialog):
        _translate = QtCore.QCoreApplication.translate
        AutoSaveDialog.setWindowTitle(_translate("AutoSaveDialog", "Welcome back"))
        self.labelAutoSave.setText(_translate("AutoSaveDialog", "Do you want to pick up where you left off?"))

