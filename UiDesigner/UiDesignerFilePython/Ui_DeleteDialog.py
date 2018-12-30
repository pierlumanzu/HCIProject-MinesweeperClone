# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Delete(object):
    def setupUi(self, Delete):
        Delete.setObjectName("Delete")
        Delete.resize(438, 349)
        self.verticalLayout = QtWidgets.QVBoxLayout(Delete)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollAreaDeleteDialog = QtWidgets.QScrollArea(Delete)
        self.scrollAreaDeleteDialog.setWidgetResizable(True)
        self.scrollAreaDeleteDialog.setObjectName("scrollAreaDeleteDialog")
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
        self.deleteButtonArea = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.deleteButtonArea.setObjectName("deleteButtonArea")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.deleteButtonArea)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.deleteButton = QtWidgets.QPushButton(self.deleteButtonArea)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_2.addWidget(self.deleteButton)
        self.verticalLayout_2.addWidget(self.deleteButtonArea)
        self.scrollAreaDeleteDialog.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollAreaDeleteDialog)

        self.retranslateUi(Delete)
        QtCore.QMetaObject.connectSlotsByName(Delete)

    def retranslateUi(self, Delete):
        _translate = QtCore.QCoreApplication.translate
        Delete.setWindowTitle(_translate("Delete", "Delete Game..."))
        self.labelSavedGames.setText(_translate("Delete", "Saved Games:"))
        self.deleteButton.setText(_translate("Delete", "Delete"))

