from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QBoxLayout, QSizePolicy, QFrame
from PyQt5.QtCore import Qt

import sys
sys.path.append("UiDesigner/UiDesignerFilePython/")
from Ui_MinesweeperClone import Ui_MinesweeperClone  #MinesweeperClone View (all the views are created through Qt Designer).

import random
import time
import threading
import pickle
import os

from MinesweeperCloneModel import MinesweeperCloneModel
from Cell import ButtonModel, ButtonViewController
from NewDialog import NewDialog
from SaveAsDialog import SaveAsDialog
from LoadDialog import LoadDialog
from DeleteDialog import DeleteDialog
from Dialogs import SuccessSaveDialog, AutoSaveDialog, RecordDialog, ControlsDialog
from Observable import Observable

class MinesweeperClone(QMainWindow):#MinesweeperClone Controller.

    def __init__(self, appIsAliveObservable, W=None, H=None, mines=None, rankingType=None, buttons=None, parameters=None):    #This function is used both for the creation of a new game grid and for the loading of a saved one.

        super().__init__()

        #If a rankings-related file exists, this file is loaded. Else there are no rankings yet for the application.
        if os.path.exists("DataSaved/Rankings/Rankings.pkl"):
            with open("DataSaved/Rankings/Rankings.pkl", "rb") as input:
                rankings = pickle.load(input)
        else:
            rankings = None

        if W is None and H is None and mines is None and rankingType is None and buttons is None and parameters is None:
            #When the application is started, it try to find a file containing an autosave of the last played game.
            if os.path.exists("DataSaved/AutoSavedGames/AutoSave.pkl"):
                isAutoLoading = Observable(False)
                #If the file exixts, a dialog appears and the user has the possibility to choice between the loading of the last played game or the creation of a new game grid.
                dialog = AutoSaveDialog(isAutoLoading)
                dialog.exec_()
                if isAutoLoading.value:
                    with open("DataSaved/AutoSavedGames/AutoSave.pkl", "rb") as input:
                        vectorLoaded = pickle.load(input)

                    W = vectorLoaded[0][0]
                    H = vectorLoaded[0][1]
                    mines = vectorLoaded[0][2]
                    rankingType = vectorLoaded[0][3]
                    buttons = vectorLoaded[2]
                    parameters = vectorLoaded[1]

                else:
                    os.remove("DataSaved/AutoSavedGames/AutoSave.pkl")

        if W is None and H is None and mines is None and rankingType is None:
            #By default, the ranking type is the Intermediate type.
            self._model = MinesweeperCloneModel(appIsAliveObservable, 1, rankings=rankings)
        else:
            self._model = MinesweeperCloneModel(appIsAliveObservable, rankingType, W, H, mines, rankings=rankings)

        self._ui = Ui_MinesweeperClone()
        self._ui.setupUi(self)

        for i in range(3):
            self.makeRankings(i)
        self.makeGrid()
        self._model.observeCounterMinesUpdate(lambda counterMines: self._ui.lcdMines.display(counterMines))
        self._model.counterMines = self._model.mines
        self._ui.refreshButton.clicked.connect(self.refreshGrid)
        self._ui.actionNew.triggered.connect(self.openNewGameDialog)
        self._ui.actionSaveAs.triggered.connect(self.openSaveAsDialog)
        self._ui.actionLoad.triggered.connect(self.openLoadDialog)
        self._ui.actionDelete.triggered.connect(self.openDeleteDialog)
        self._ui.actionControls.triggered.connect(self.openControlsDialog)

        if buttons is not None:
            for i in range(len(buttons)):
                self._model.getItemModelsGridButtons(buttons[i][1] * self._model.W + buttons[i][0]).loadButton(buttons[i][2], buttons[i][3], buttons[i][4], buttons[i][5], buttons[i][6])

        if parameters is None:
            threadTimer = threading.Thread(target=self.timerUp, args=[0])
            threadTimer.start()
            self.setGeometry(0, 0, 1280, 720)
        else:
            self._model.counterMines = parameters[1]
            threadTimer = threading.Thread(target=self.timerUp, args=[parameters[0]])
            threadTimer.start()
            while self._ui.lcdTime.value() != parameters[0]:
                pass
            if not(parameters[2]) and not(parameters[3]):
                self._model.isBlocked = parameters[4]
            else:
                if parameters[2]:
                    self._ui.statusbar.setStyleSheet("color:green; font-size: 14pt;")
                    self._ui.statusbar.showMessage("You Win!")
                    self._model.isWin = True
                else:
                    self._ui.statusbar.setStyleSheet("color:red; font-size: 14pt;")
                    self._ui.statusbar.showMessage("You Loose!")
                    self._model.isLos = True
            self.setGeometry(parameters[5][0], parameters[5][1], parameters[5][2], parameters[5][3])
        threadAutoSave = threading.Thread(target=self.autosave)
        threadAutoSave.start()

    #MAKING FUNCTIONS: The functions aim is the creation of the rankings (makeRankings and makePositionRanking) and of the game grid (makeGrid).

    def makeRankings(self, typeRanking):

        if typeRanking == 0:
            for i in reversed(range(self._ui.beginnerRankingArea.layout().count())):
                self._ui.beginnerRankingArea.layout().itemAt(i).widget().setParent(None)
        if typeRanking == 1:
            for i in reversed(range(self._ui.intermediateRankingArea.layout().count())):
                self._ui.intermediateRankingArea.layout().itemAt(i).widget().setParent(None)
        if typeRanking == 2:
            for i in reversed(range(self._ui.expertRankingArea.layout().count())):
                self._ui.expertRankingArea.layout().itemAt(i).widget().setParent(None)

        if self._model.getLenRanking(typeRanking) == 0:
            if typeRanking == 0:
                self._ui.beginnerRankingArea.layout().addWidget(QLabel("No positions in this ranking yet."))
                self._ui.beginnerRankingArea.layout().itemAt(0).widget().setStyleSheet("font-size:11pt;")
            if typeRanking == 1:
                self._ui.intermediateRankingArea.layout().addWidget(QLabel("No positions in this ranking yet."))
                self._ui.intermediateRankingArea.layout().itemAt(0).widget().setStyleSheet("font-size:11pt;")
            if typeRanking == 2:
                self._ui.expertRankingArea.layout().addWidget(QLabel("No positions in this ranking yet."))
                self._ui.expertRankingArea.layout().itemAt(0).widget().setStyleSheet("font-size:11pt;")
        else:
            for i in range(self._model.getLenRanking(typeRanking)):
                self.makePositionRanking(typeRanking, i + 1, self._model.getItemRanking(typeRanking, i))

    def makePositionRanking(self, typeRanking, position, dataPlayer):

        widget = QWidget()
        layout = QBoxLayout(QBoxLayout.LeftToRight)

        labelPosition = QLabel(str(position))
        labelPosition.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labelPosition.setStyleSheet("font-size:15pt;")
        labelPosition.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))
        layout.addWidget(labelPosition)

        labelNamePlayer = QLabel(dataPlayer[0])
        labelNamePlayer.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labelNamePlayer.setStyleSheet("font-size:15pt;")
        labelNamePlayer.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed))
        layout.addWidget(labelNamePlayer)

        labelTime = QLabel(str(round(dataPlayer[1], 3)))
        labelTime.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labelTime.setStyleSheet("font-size:15pt;")
        labelTime.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed))
        layout.addWidget(labelTime)

        widget.setLayout(layout)

        lineSeparator = QFrame()
        lineSeparator.setFrameShape(QFrame.HLine)
        lineSeparator.setFrameShadow(QFrame.Sunken)

        if typeRanking == 0:
            self._ui.beginnerRankingArea.layout().addWidget(widget)
            self._ui.beginnerRankingArea.layout().addWidget(lineSeparator)
        if typeRanking == 1:
            self._ui.intermediateRankingArea.layout().addWidget(widget)
            self._ui.intermediateRankingArea.layout().addWidget(lineSeparator)
        if typeRanking == 2:
            self._ui.expertRankingArea.layout().addWidget(widget)
            self._ui.expertRankingArea.layout().addWidget(lineSeparator)

    def makeGrid(self, positionMines=None):

        if positionMines is None:
            positionMines = []
            i = self._model.mines
            while i > 0:
                positionMinesH = random.randint(0, self._model.H - 1)
                positionMinesW = random.randint(0, self._model.W - 1)

                if [positionMinesH, positionMinesW] not in positionMines:
                    positionMines.append([positionMinesH, positionMinesW])
                    i -= 1

        for i in range(self._model.H):
            for j in range(self._model.W):
                if [i, j] in positionMines:
                    self._model.setItemModelsGridButtons(ButtonModel(j, i, True))
                else:
                    self._model.setItemModelsGridButtons(ButtonModel(j, i, False))
                self._model.getItemModelsGridButtons(i * self._model.W + j).observeNeighbors(self.propagateToNeighbors)
                self._model.getItemModelsGridButtons(i * self._model.W + j).observeChecked(self.changeLcdMines)
                self._ui.gridButtons.layout().addWidget(ButtonViewController(self._model.getItemModelsGridButtons(i * self._model.W + j)), i, j)

    #GAME ENGINE
    def propagateToNeighbors(self, tuplePositionPoint):#When a button on the grid is clicked.

        self._model.isBlocked = True

        if self.checkLoose(tuplePositionPoint):

            self._ui.statusbar.setStyleSheet("color:red; font-size: 14pt;")
            self._ui.statusbar.showMessage("You Loose!")
            self._model.isPropagation = True

        else:
            #If the clicked button is not a mine, the program controls the neighbor buttons.
            listNeighbors = []
            listNeighbors.append([tuplePositionPoint[0], tuplePositionPoint[1]])

            while len(listNeighbors) != 0:
                [x, y] = listNeighbors[0]
                listNeighbors = listNeighbors[1:len(listNeighbors)]

                self._model.getItemModelsGridButtons(y * self._model.W + x).isActive = False    #These variables of all the controlled buttons are setted.
                self._model.getItemModelsGridButtons(y * self._model.W + x).isClicked = True

                countMines = 0

                for i in range(y - 1, y + 2):
                    for j in range(x - 1, x + 2):

                        if (j != x or i != y) and i >= 0 and i < self._model.H and j >= 0 and j < self._model.W:
                            if self._model.getItemModelsGridButtons(i * self._model.W + j).isMine:
                                countMines += 1

                #If a button has any mines in its neighborhood, it is not inserted in the list of the buttons to control.
                if countMines == 0:
                    self._model.getItemModelsGridButtons(y * self._model.W + x).value = ""
                    for i in range(y - 1, y + 2):
                        for j in range(x - 1, x + 2):

                            if (j != x or i != y) and i >= 0 and i < self._model.H and j >= 0 and j < self._model.W and not(self._model.getItemModelsGridButtons(i * self._model.W + j).isClicked) and not(self._model.getItemModelsGridButtons(i * self._model.W + j).isChecked) and [j, i] not in listNeighbors:
                                listNeighbors.append([j,i])
                else:
                    self._model.getItemModelsGridButtons(y * self._model.W + x).value = str(countMines)

            self.checkVictory()
            self._model.isPropagation = True
            self._model.isBlocked = False

    def checkLoose(self, tuplePositionPoint):#If the clicked button is a mine, the user looses and consequently all the mines are showed. The checked mines are characterized by a green background, the others by a red one.
        if self._model.getItemModelsGridButtons(tuplePositionPoint[1] * self._model.W + tuplePositionPoint[0]).isMine:

            self._model.isLos = True

            for i in range(self._model.getLenModelsGridButtons()):
                self._model.getItemModelsGridButtons(i).isActive = False
                if self._model.getItemModelsGridButtons(i).isMine:
                    self._model.getItemModelsGridButtons(i).isClicked = True
                    self._model.getItemModelsGridButtons(i).value = "M"

            return True
        else:
            return False

    def checkVictory(self):#If all the non clicked buttons are mines, the user wins the game and all the mines become checked.

        countRightPointsClicked = 0
        for i in range(self._model.getLenModelsGridButtons()):

            if not(self._model.getItemModelsGridButtons(i).isMine) and self._model.getItemModelsGridButtons(i).isClicked:
                countRightPointsClicked += 1

        if countRightPointsClicked == self._model.W * self._model.H - self._model.mines:

            self._model.isWin = True
            if self._ui.lcdTime.value() == 0:
                totalTime = 0
            else:
                if self._ui.lcdTime.value() == 99999:
                    totalTime = 99999
                else:
                    totalTime = self._ui.lcdTime.value() + (time.time() - self._model.gameTime)

            for i in range(self._model.getLenModelsGridButtons()):
                self._model.getItemModelsGridButtons(i).isActive = False
                if self._model.getItemModelsGridButtons(i).isMine:
                    self._model.getItemModelsGridButtons(i).isChecked = True
                    self._model.getItemModelsGridButtons(i).isClicked = True
            self._ui.statusbar.setStyleSheet("color:green; font-size: 14pt;")
            self._ui.statusbar.showMessage("You Win!")
            self._model.counterMines = 0

            #The maximum number of rankings positions are 20. So if the considered ranking are not already full, the user can insert his record; else if his game time is less than the last position one, the user does a new record; else the user does not have the possibility to insert his game time on the ranking.
            if self._model.rankingType != 3:
                if self._model.getLenRanking(self._model.rankingType) < 20 or totalTime < self._model.getMaxRanking(self._model.rankingType):
                    isRecord = Observable(False)
                    nameRecord = Observable(None)
                    # A dialog that gives the possibility to a user who does a new record to insert his name.
                    dialog = RecordDialog(totalTime, isRecord, nameRecord)
                    dialog.exec_()
                    #If there is a new record in the ranking, the rankings-related file is updated.
                    if isRecord.value:
                        self._model.setItemRanking(self._model.rankingType, [nameRecord.value, totalTime])
                        if os.path.exists("DataSaved/Rankings/Rankings.pkl"):
                            os.remove("DataSaved/Rankings/Rankings.pkl")
                        vectorToSave = [[], [], []]
                        for i in range(3):
                            for j in range(self._model.getLenRanking(i)):
                                vectorToSave[i].append(self._model.getItemRanking(i, j))
                        with open("DataSaved/Rankings/Rankings.pkl", "wb") as output:
                            pickle.dump(vectorToSave, output)
                        self.makeRankings(self._model.rankingType)

            return True
        else:
            return False

    def changeLcdMines(self, isChecked):#If a button is checked, the application must update the variable "counterMines" and consequently the mines-related LCD (lcdMines).
        self._model.isBlocked = False
        if isChecked:
            self._model.counterMines = self._model.counterMines - 1
        else:
            self._model.counterMines = self._model.counterMines + 1

    #NEW GAME DIALOG/FUNCTIONS

    def openNewGameDialog(self): #If the user wants to create a new grid, the application refreshes the grid and all the related widgets.

        isChangedAnything = Observable(False)
        blockedValue = self._model.isBlocked
        self._model.isBlocked = True
        self.setEnabled(False)
        self.setHidden(True)
        dialog = NewDialog(self._model, isChangedAnything)
        dialog.exec_()
        self.setEnabled(True)
        self.setHidden(False)
        if isChangedAnything.value:
            self.refreshGrid()
        else:
            self._model.isBlocked = blockedValue

    def refreshGrid(self):
        self._ui.refreshButton.setEnabled(False)
        self._ui.actionNew.setEnabled(False)
        self._ui.actionSaveAs.setEnabled(False)
        self._ui.actionLoad.setEnabled(False)
        self._ui.actionDelete.setEnabled(False)
        if os.path.exists("DataSaved/AutoSavedGames/AutoSave.pkl"):
            os.remove("DataSaved/AutoSavedGames/AutoSave.pkl")
        self._model.activeThread = False
        time.sleep(1.5)
        #This time sleep is needed because the background threads related to this current game must be closed before the game refreshing.
        self.close()
        window = MinesweeperClone(self._model.appIsAliveObservable, self._model.W, self._model.H, self._model.mines, self._model.rankingType)
        window.show()

    #SAVE/LOAD/DELETE DIALOG/FUNCTIONS

    def openSaveAsDialog(self):#The user can save a game with this dialog.
        blockedValue = self._model.isBlocked
        self._model.isBlocked = True
        gameToSave = Observable(None)
        self.setEnabled(False)
        self.setHidden(True)
        dialog = SaveAsDialog(gameToSave)
        dialog.exec_()
        if gameToSave.value is not None:
            self.saveGameAs("DataSaved/SavedGames/" + gameToSave.value + ".pkl", blockedValue)
            dialog = SuccessSaveDialog()
            dialog.exec_()
        self._model.isBlocked = blockedValue
        self.setEnabled(True)
        self.setHidden(False)

    def openLoadDialog(self):#The user can load a saved game with this dialog.
        blockedValue = self._model.isBlocked
        self._model.isBlocked = True
        gameToLoad = Observable(None)
        self.setEnabled(False)
        self.setHidden(True)
        dialog = LoadDialog(gameToLoad)
        dialog.exec_()
        self.setEnabled(True)
        self.setHidden(False)
        if gameToLoad.value is not None:
            self.loadGame("DataSaved/SavedGames/" + gameToLoad.value + ".pkl")
        self._model.isBlocked = blockedValue

    def openDeleteDialog(self):#The user can delete some saved games with this dialog.
        blockedValue = self._model.isBlocked
        self._model.isBlocked = True
        self.setEnabled(False)
        self.setHidden(True)
        dialog = DeleteDialog()
        dialog.exec_()
        self.setEnabled(True)
        self.setHidden(False)
        self._model.isBlocked = blockedValue

    def saveGameAs(self, fileGame, blockedValue):#Save function.
        if os.path.exists(fileGame):
            os.remove(fileGame)
        vectorToSave = []
        vectorToSave.append([self._model.W, self._model.H, self._model.mines, self._model.rankingType])
        vectorToSave.append([self._ui.lcdTime.value(), self._model.counterMines, self._model.isWin, self._model.isLos, blockedValue, [self._ui.centralwidget.x(), self._ui.centralwidget.y(), self._ui.centralwidget.width(), self._ui.centralwidget.height()]])
        vectorToSave.append([])
        for i in range(self._model.getLenModelsGridButtons()):
            button = self._model.getItemModelsGridButtons(i)
            vectorToSave[2].append([button.X, button.Y, button.isMine, button.value, button.isChecked, button.isClicked, button.isActive])

        with open(fileGame, "wb") as output:
            pickle.dump(vectorToSave, output)

    def loadGame(self, fileGame):#Load function.
        self._ui.refreshButton.setEnabled(False)
        self._ui.actionNew.setEnabled(False)
        self._ui.actionSaveAs.setEnabled(False)
        self._ui.actionLoad.setEnabled(False)
        self._ui.actionDelete.setEnabled(False)
        if os.path.exists("DataSaved/AutoSavedGames/AutoSave.pkl"):
            os.remove("DataSaved/AutoSavedGames/AutoSave.pkl")
        with open(fileGame, "rb") as input:
            vectorLoaded = pickle.load(input)
        self._model.activeThread = False
        time.sleep(1.5)
        # This time sleep is needed because the background threads related to this game session must be closed before the game loading.
        self.close()
        window = MinesweeperClone(self._model.appIsAliveObservable, vectorLoaded[0][0], vectorLoaded[0][1], vectorLoaded[0][2], vectorLoaded[0][3], vectorLoaded[2], vectorLoaded[1])
        window.show()

    #CONTROLS DIALOG

    def openControlsDialog(self):
        blockedValue = self._model.isBlocked
        self._model.isBlocked = True
        self.setEnabled(False)
        self.setHidden(True)
        dialog = ControlsDialog()
        dialog.exec_()
        self.setEnabled(True)
        self.setHidden(False)
        self._model.isBlocked = blockedValue

    #BACKGROUND THREADS: functions used as background threads.

    def timerUp(self, timeLcd):#This function is a seconds counter.
        while self._model.appIsAliveObservable.value and self._model.activeThread:
            time.sleep(1)
            if self._model.isBlocked:
                self._ui.lcdTime.display(timeLcd)
            else:
                if not(self._model.isWin) and not(self._model.isLos) and timeLcd < 99999:
                    self._ui.lcdTime.display(self._ui.lcdTime.value() + 1)
                    self._model.gameTime = time.time()
                    timeLcd = self._ui.lcdTime.value()

    def autosave(self):#This function does the autosave of the game when a grid button is clicked or every 5 seconds.
        countTime = 0
        while self._model.appIsAliveObservable.value and self._model.activeThread:
            time.sleep(1)
            if self._model.isPropagation:
                countTime = 0
                self.saveGameAs("DataSaved/AutoSavedGames/AutoSave.pkl", False)
                self._model.isPropagation = False
            else:
                if not(self._model.isBlocked):
                    countTime += 1
                    if countTime == 5:
                        countTime = 0
                        self.saveGameAs("DataSaved/AutoSavedGames/AutoSave.pkl", False)
