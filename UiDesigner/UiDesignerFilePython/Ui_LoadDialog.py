# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoadDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Load(object):
    def setupUi(self, Load):
        Load.setObjectName("Load")
        Load.resize(438, 349)
        self.verticalLayout = QtWidgets.QVBoxLayout(Load)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollAreaLoadDialog = QtWidgets.QScrollArea(Load)
        self.scrollAreaLoadDialog.setWidgetResizable(True)
        self.scrollAreaLoadDialog.setObjectName("scrollAreaLoadDialog")
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
        self.loadButtonArea = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.loadButtonArea.setObjectName("loadButtonArea")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.loadButtonArea)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.loadButton = QtWidgets.QPushButton(self.loadButtonArea)
        self.loadButton.setObjectName("loadButton")
        self.horizontalLayout_2.addWidget(self.loadButton)
        self.verticalLayout_2.addWidget(self.loadButtonArea)
        self.scrollAreaLoadDialog.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollAreaLoadDialog)

        self.retranslateUi(Load)
        QtCore.QMetaObject.connectSlotsByName(Load)

    def retranslateUi(self, Load):
        _translate = QtCore.QCoreApplication.translate
        Load.setWindowTitle(_translate("Load", "Load Game..."))
        self.labelSavedGames.setText(_translate("Load", "Saved Games:"))
        self.loadButton.setText(_translate("Load", "Load"))

