# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MinesweeperClone.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MinesweeperClone(object):
    def setupUi(self, MinesweeperClone):
        MinesweeperClone.setObjectName("MinesweeperClone")
        MinesweeperClone.resize(715, 501)
        self.centralwidget = QtWidgets.QWidget(MinesweeperClone)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidgetMinesweeperClone = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetMinesweeperClone.setObjectName("tabWidgetMinesweeperClone")
        self.tabGame = QtWidgets.QWidget()
        self.tabGame.setObjectName("tabGame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabGame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollAreaGame = QtWidgets.QScrollArea(self.tabGame)
        self.scrollAreaGame.setWidgetResizable(True)
        self.scrollAreaGame.setObjectName("scrollAreaGame")
        self.gameArea = QtWidgets.QWidget()
        self.gameArea.setGeometry(QtCore.QRect(0, 0, 673, 392))
        self.gameArea.setObjectName("gameArea")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gameArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.timersRefreshWidget = QtWidgets.QWidget(self.gameArea)
        self.timersRefreshWidget.setObjectName("timersRefreshWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.timersRefreshWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lcdMines = QtWidgets.QLCDNumber(self.timersRefreshWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdMines.sizePolicy().hasHeightForWidth())
        self.lcdMines.setSizePolicy(sizePolicy)
        self.lcdMines.setObjectName("lcdMines")
        self.horizontalLayout.addWidget(self.lcdMines)
        self.refreshButton = QtWidgets.QPushButton(self.timersRefreshWidget)
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout.addWidget(self.refreshButton)
        self.lcdTime = QtWidgets.QLCDNumber(self.timersRefreshWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdTime.sizePolicy().hasHeightForWidth())
        self.lcdTime.setSizePolicy(sizePolicy)
        self.lcdTime.setObjectName("lcdTime")
        self.horizontalLayout.addWidget(self.lcdTime)
        self.verticalLayout_3.addWidget(self.timersRefreshWidget)
        self.gridButtons = QtWidgets.QWidget(self.gameArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridButtons.sizePolicy().hasHeightForWidth())
        self.gridButtons.setSizePolicy(sizePolicy)
        self.gridButtons.setObjectName("gridButtons")
        self.gridLayout = QtWidgets.QGridLayout(self.gridButtons)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3.addWidget(self.gridButtons)
        self.scrollAreaGame.setWidget(self.gameArea)
        self.verticalLayout_2.addWidget(self.scrollAreaGame)
        self.tabWidgetMinesweeperClone.addTab(self.tabGame, "")
        self.tabRankings = QtWidgets.QWidget()
        self.tabRankings.setObjectName("tabRankings")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabRankings)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollAreaRankings = QtWidgets.QScrollArea(self.tabRankings)
        self.scrollAreaRankings.setWidgetResizable(True)
        self.scrollAreaRankings.setObjectName("scrollAreaRankings")
        self.rankingsArea = QtWidgets.QWidget()
        self.rankingsArea.setGeometry(QtCore.QRect(0, 0, 145, 137))
        self.rankingsArea.setObjectName("rankingsArea")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.rankingsArea)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidgetRankings = QtWidgets.QTabWidget(self.rankingsArea)
        self.tabWidgetRankings.setObjectName("tabWidgetRankings")
        self.tabBeginner = QtWidgets.QWidget()
        self.tabBeginner.setObjectName("tabBeginner")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabBeginner)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollAreaBeginnerRanking = QtWidgets.QScrollArea(self.tabBeginner)
        self.scrollAreaBeginnerRanking.setWidgetResizable(True)
        self.scrollAreaBeginnerRanking.setObjectName("scrollAreaBeginnerRanking")
        self.beginnerRankingArea = QtWidgets.QWidget()
        self.beginnerRankingArea.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.beginnerRankingArea.setObjectName("beginnerRankingArea")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.beginnerRankingArea)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scrollAreaBeginnerRanking.setWidget(self.beginnerRankingArea)
        self.verticalLayout_6.addWidget(self.scrollAreaBeginnerRanking)
        self.tabWidgetRankings.addTab(self.tabBeginner, "")
        self.tabIntermediate = QtWidgets.QWidget()
        self.tabIntermediate.setObjectName("tabIntermediate")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tabIntermediate)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollAreaIntermediateRanking = QtWidgets.QScrollArea(self.tabIntermediate)
        self.scrollAreaIntermediateRanking.setWidgetResizable(True)
        self.scrollAreaIntermediateRanking.setObjectName("scrollAreaIntermediateRanking")
        self.intermediateRankingArea = QtWidgets.QWidget()
        self.intermediateRankingArea.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.intermediateRankingArea.setObjectName("intermediateRankingArea")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.intermediateRankingArea)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.scrollAreaIntermediateRanking.setWidget(self.intermediateRankingArea)
        self.verticalLayout_7.addWidget(self.scrollAreaIntermediateRanking)
        self.tabWidgetRankings.addTab(self.tabIntermediate, "")
        self.tabExpert = QtWidgets.QWidget()
        self.tabExpert.setObjectName("tabExpert")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tabExpert)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.scrollAreaExpertRanking = QtWidgets.QScrollArea(self.tabExpert)
        self.scrollAreaExpertRanking.setWidgetResizable(True)
        self.scrollAreaExpertRanking.setObjectName("scrollAreaExpertRanking")
        self.expertRankingArea = QtWidgets.QWidget()
        self.expertRankingArea.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.expertRankingArea.setObjectName("expertRankingArea")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.expertRankingArea)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.scrollAreaExpertRanking.setWidget(self.expertRankingArea)
        self.verticalLayout_8.addWidget(self.scrollAreaExpertRanking)
        self.tabWidgetRankings.addTab(self.tabExpert, "")
        self.verticalLayout_5.addWidget(self.tabWidgetRankings)
        self.scrollAreaRankings.setWidget(self.rankingsArea)
        self.verticalLayout_4.addWidget(self.scrollAreaRankings)
        self.tabWidgetMinesweeperClone.addTab(self.tabRankings, "")
        self.verticalLayout.addWidget(self.tabWidgetMinesweeperClone)
        MinesweeperClone.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MinesweeperClone)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 20))
        self.menubar.setObjectName("menubar")
        self.menuGame = QtWidgets.QMenu(self.menubar)
        self.menuGame.setObjectName("menuGame")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.menuInformations = QtWidgets.QMenu(self.menubar)
        self.menuInformations.setObjectName("menuInformations")
        MinesweeperClone.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MinesweeperClone)
        self.statusbar.setObjectName("statusbar")
        MinesweeperClone.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MinesweeperClone)
        self.actionNew.setObjectName("actionNew")
        self.actionSaveAs = QtWidgets.QAction(MinesweeperClone)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionLoad = QtWidgets.QAction(MinesweeperClone)
        self.actionLoad.setObjectName("actionLoad")
        self.actionDelete = QtWidgets.QAction(MinesweeperClone)
        self.actionDelete.setObjectName("actionDelete")
        self.actionControls = QtWidgets.QAction(MinesweeperClone)
        self.actionControls.setObjectName("actionControls")
        self.menuGame.addAction(self.actionNew)
        self.menuActions.addAction(self.actionSaveAs)
        self.menuActions.addAction(self.actionLoad)
        self.menuActions.addAction(self.actionDelete)
        self.menuInformations.addAction(self.actionControls)
        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuInformations.menuAction())

        self.retranslateUi(MinesweeperClone)
        self.tabWidgetMinesweeperClone.setCurrentIndex(0)
        self.tabWidgetRankings.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MinesweeperClone)

    def retranslateUi(self, MinesweeperClone):
        _translate = QtCore.QCoreApplication.translate
        MinesweeperClone.setWindowTitle(_translate("MinesweeperClone", "MinesSweeper Clone"))
        self.refreshButton.setText(_translate("MinesweeperClone", "Refresh"))
        self.tabWidgetMinesweeperClone.setTabText(self.tabWidgetMinesweeperClone.indexOf(self.tabGame), _translate("MinesweeperClone", "Game"))
        self.tabWidgetRankings.setTabText(self.tabWidgetRankings.indexOf(self.tabBeginner), _translate("MinesweeperClone", "Beginner"))
        self.tabWidgetRankings.setTabText(self.tabWidgetRankings.indexOf(self.tabIntermediate), _translate("MinesweeperClone", "Intermediate"))
        self.tabWidgetRankings.setTabText(self.tabWidgetRankings.indexOf(self.tabExpert), _translate("MinesweeperClone", "Expert"))
        self.tabWidgetMinesweeperClone.setTabText(self.tabWidgetMinesweeperClone.indexOf(self.tabRankings), _translate("MinesweeperClone", "Rankings"))
        self.menuGame.setTitle(_translate("MinesweeperClone", "Game"))
        self.menuActions.setTitle(_translate("MinesweeperClone", "Actions"))
        self.menuInformations.setTitle(_translate("MinesweeperClone", "Informations"))
        self.actionNew.setText(_translate("MinesweeperClone", "New..."))
        self.actionSaveAs.setText(_translate("MinesweeperClone", "Save as..."))
        self.actionLoad.setText(_translate("MinesweeperClone", "Load..."))
        self.actionDelete.setText(_translate("MinesweeperClone", "Delete..."))
        self.actionControls.setText(_translate("MinesweeperClone", "Controls"))

