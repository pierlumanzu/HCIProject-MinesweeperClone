# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ControlsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ControlsDialog(object):
    def setupUi(self, ControlsDialog):
        ControlsDialog.setObjectName("ControlsDialog")
        ControlsDialog.resize(400, 137)
        self.labelLeftClick = QtWidgets.QLabel(ControlsDialog)
        self.labelLeftClick.setGeometry(QtCore.QRect(40, 30, 321, 21))
        self.labelLeftClick.setObjectName("labelLeftClick")
        self.labelRigthClick = QtWidgets.QLabel(ControlsDialog)
        self.labelRigthClick.setGeometry(QtCore.QRect(40, 80, 321, 21))
        self.labelRigthClick.setObjectName("labelRigthClick")

        self.retranslateUi(ControlsDialog)
        QtCore.QMetaObject.connectSlotsByName(ControlsDialog)

    def retranslateUi(self, ControlsDialog):
        _translate = QtCore.QCoreApplication.translate
        ControlsDialog.setWindowTitle(_translate("ControlsDialog", "Controls"))
        self.labelLeftClick.setText(_translate("ControlsDialog", "Left-click an empty grid button to reveal it."))
        self.labelRigthClick.setText(_translate("ControlsDialog", "Right-click an empty grid button to check it."))

