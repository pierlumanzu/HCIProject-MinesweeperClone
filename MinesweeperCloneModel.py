from PyQt5.QtCore import QObject, pyqtSignal

class MinesweeperCloneModel(QObject):#MinesweeperClone Model.
    counterMinesUpdate = pyqtSignal(int)

    def __init__(self, appIsAliveObservable, rankingType, W=None, H=None, mines=None, rankings=None):
        super().__init__()

        self._appIsAliveObservable = appIsAliveObservable

        if W is None and H is None and mines is None:
            self._W = 16                                    #Grid Width.
            self._H = 16                                    #Grid Height.
            self._mines = 40                                #Number of mines on the grid.
        else:
            self._W = W
            self._H = H
            self._mines = mines
        self._counterMines = 0                              #A mines counter. It is used to manage the mine-related LCD.
        self._isWin = False                                 #This variable indicates when the game is won.
        self._isLos = False                                 #This variable indicates when the game is lost.
        self._isBlocked = True                              #This variable indicates when there is a game refreshing/loading or when the background threads must be stuck.
        self._isPropagation = False                         #This variable indicates when a grid button is clicked. In this case an autosave must be done.
        self._modelsGridButtons = []                        #A list of the grid buttons.
        self._rankingType = rankingType                     #The ranking type of the current game (Beginner, Intermediate, Expert or Custom).
        if rankings is None:
            self._rankings = [[], [], []]
        else:
            self._rankings = rankings
        self._gameTime = 0                                   #This variable is used to compute the game time of a winner user.
        self._activeThread = True                            #The background threads need this variable. Before game refreshing/loading, this variable is setted as False and consequently the background threads related to the current game must stop. After the game refreshing/loading, the background threads related to the new game session are created.

    @property
    def appIsAliveObservable(self):
        return self._appIsAliveObservable

    @property
    def W(self):
        return self._W

    @W.setter
    def W(self, newW):
        self._W = newW

    @property
    def H(self):
        return self._H

    @H.setter
    def H(self, newH):
        self._H = newH

    @property
    def mines(self):
        return self._mines

    @mines.setter
    def mines(self, newMines):
        self._mines = newMines

    @property
    def counterMines(self):
        return self._counterMines

    @counterMines.setter
    def counterMines(self, newCounterMines):
        self._counterMines = newCounterMines
        self.counterMinesUpdate.emit(newCounterMines)

    @property
    def isWin(self):
        return self._isWin

    @isWin.setter
    def isWin(self, newIsWin):
        self._isWin = newIsWin

    @property
    def isLos(self):
        return self._isLos

    @isLos.setter
    def isLos(self, newIsLos):
        self._isLos = newIsLos

    @property
    def isBlocked(self):
        return self._isBlocked

    @isBlocked.setter
    def isBlocked(self, newIsBlocked):
        self._isBlocked = newIsBlocked

    @property
    def isPropagation(self):
        return self._isPropagation

    @isPropagation.setter
    def isPropagation(self, newIsPropagation):
        self._isPropagation = newIsPropagation

    @property
    def rankingType(self):
        return self._rankingType

    @rankingType.setter
    def rankingType(self, newRankingType):
        self._rankingType = newRankingType

    @property
    def gameTime(self):
        return self._gameTime

    @gameTime.setter
    def gameTime(self, newGameTime):
        self._gameTime = newGameTime

    @property
    def activeThread(self):
        return self._activeThread

    @activeThread.setter
    def activeThread(self, newActiveThread):
        self._activeThread = newActiveThread

    #FUNCTIONS RELATED TO THE VECTOR OF GRID BUTTONS.

    def getItemModelsGridButtons(self, item):
        return self._modelsGridButtons[item]

    def setItemModelsGridButtons(self, cellModel):
        self._modelsGridButtons.append(cellModel)

    def getLenModelsGridButtons(self):
        return len(self._modelsGridButtons)

    #FUNCTIONS RELATED TO RANKINGS

    def setItemRanking(self, typeRanking, newPosition):                  #This function finds the position of a new record and stores it.
        if len(self._rankings[typeRanking]) != 0:
            for i in reversed(range(len(self._rankings[typeRanking]))):
                if newPosition[1] >= self._rankings[typeRanking][i][1]:
                    i += 1
                    break
            vectorTmp = self._rankings[typeRanking][i: len(self._rankings[typeRanking])]
            del self._rankings[typeRanking][i: len(self._rankings[typeRanking])]
            self._rankings[typeRanking].append(newPosition)
            for i in range(len(vectorTmp)):
                self._rankings[typeRanking].append(vectorTmp[i])
            if len(self._rankings[typeRanking]) > 20:
                del self._rankings[typeRanking][len(self._rankings[typeRanking]) - 1]
        else:
            self._rankings[typeRanking].append(newPosition)


    def getItemRanking(self, typeRanking, item):
        return self._rankings[typeRanking][item]

    def getLenRanking(self, typeRanking):
        return len(self._rankings[typeRanking])

    def getMaxRanking(self, typeRanking):
        return self._rankings[typeRanking][len(self._rankings[typeRanking]) - 1][1]

    #FUNCTIONS RELATED TO SIGNALS

    def observeCounterMinesUpdate(self, slot):          #This function allows to observe the modification of the value of "counterMines".
        self.counterMinesUpdate.connect(slot)


