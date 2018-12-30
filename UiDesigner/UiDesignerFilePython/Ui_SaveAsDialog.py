# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SaveAsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SaveAs(object):
    def setupUi(self, SaveAs):
        SaveAs.setObjectName("SaveAs")
        SaveAs.resize(438, 349)
        self.verticalLayout = QtWidgets.QVBoxLayout(SaveAs)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollAreaSaveAsDialog = QtWidgets.QScrollArea(SaveAs)
        self.scrollAreaSaveAsDialog.setWidgetResizable(True)
        self.scrollAreaSaveAsDialog.setObjectName("scrollAreaSaveAsDialog")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 418, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelSavedGames = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelSavedGames.setObjectName("labelSavedGames")
        self.verticalLayout_2.addWidget(self.labelSavedGames)
        self.scrollAreaSavedGames = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollAreaSavedGames.setWidgetResizable(True)
        self.scrollAreaSavedGames.setObjectName("scrollAreaSavedGames")
        self.savedGamesArea = QtWidgets.QWidget()
        self.savedGamesArea.setGeometry(QtCore.QRect(0, 0, 398, 241))
        self.savedGamesArea.setObjectName("savedGamesArea")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.savedGamesArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollAreaSavedGames.setWidget(self.savedGamesArea)
        self.verticalLayout_2.addWidget(self.scrollAreaSavedGames)
        self.saveButtonArea = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.saveButtonArea.setObjectName("saveButtonArea")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.saveButtonArea)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nameGame = QtWidgets.QLineEdit(self.saveButtonArea)
        self.nameGame.setObjectName("nameGame")
        self.horizontalLayout_2.addWidget(self.nameGame)
        self.saveButton = QtWidgets.QPushButton(self.saveButtonArea)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.verticalLayout_2.addWidget(self.saveButtonArea)
        self.scrollAreaSaveAsDialog.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollAreaSaveAsDialog)

        self.retranslateUi(SaveAs)
        QtCore.QMetaObject.connectSlotsByName(SaveAs)

    def retranslateUi(self, SaveAs):
        _translate = QtCore.QCoreApplication.translate
        SaveAs.setWindowTitle(_translate("SaveAs", "Save Game as..."))
        self.labelSavedGames.setText(_translate("SaveAs", "Saved Games:"))
        self.saveButton.setText(_translate("SaveAs", "Save"))

