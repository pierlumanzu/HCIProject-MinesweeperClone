from PyQt5.QtCore import QObject, pyqtSignal

class NewDialogModel(QObject):#NewDialog Model.
    adviseCreationNewModel = pyqtSignal()

    def __init__(self, modelMinesweeper, isChangedAnythingObservable):

        super().__init__()

        self._modelMinesweeper = modelMinesweeper                           #Model of the MinesweeperClone. It is used to modify the variables "W", "H", "mines" and "rankingType" of the MinesweeperClone Model.
        self._isChangedAnythingObservable = isChangedAnythingObservable     #This Observable is used to advise the MinesweeperClone controller if a user decides to create a new game or not.

        self._W = None                                                      #The width of the new game.
        self._H = None                                                      #The height of the new game.
        self._mines = None                                                  #The mines of the new game.
        self._rankingType = None                                            #The ranking type of the new game.

    @property
    def modelMinesweeper(self):
        return self._modelMinesweeper

    @property
    def W(self):
        return self._W

    @W.setter
    def W(self, newW):
        self._W = newW
        if self._H is not None and self._mines is not None and self._rankingType is not None:
            self.adviseCreationNewModel.emit()

    @property
    def H(self):
        return self._H

    @H.setter
    def H(self, newH):
        self._H = newH
        if self._W is not None and self._mines is not None and self._rankingType is not None:
            self.adviseCreationNewModel.emit()

    @property
    def mines(self):
        return self._mines

    @mines.setter
    def mines(self, newMines):
        self._mines = newMines
        if self._W is not None and self._H is not None and self._rankingType is not None:
            self.adviseCreationNewModel.emit()

    @property
    def rankingType(self):
        return self._rankingType

    @rankingType.setter
    def rankingType(self, newRankingType):
        self._rankingType = newRankingType
        if self._W is not None and self._H is not None and self._mines is not None:
            self.adviseCreationNewModel.emit()

    @property
    def isChangedAnythingObservable(self):
        return self._isChangedAnythingObservable

    def observeCreationNewModel(self, slot):           #This function allows to observe if all the variables of the new game are setted.
        self.adviseCreationNewModel.connect(slot)