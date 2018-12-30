from PyQt5.QtCore import QObject

class SaveAsLoadDeleteDialogModel(QObject):#SaveAs/Load/DeleteDialog Model.

    def __init__(self, gameObservable=None):

        super().__init__()

        if gameObservable is None:
            self._gameObservable = None                      #The DeleteDialog does not need this observable.
        else:
            self._gameObservable = gameObservable            #This observable is used in the SaveAsDialog/LoadDialog to communicate to the MinesweeperClone Controller what is the name of the game to save/load.

        self._savedGames = []

    @property
    def gameObservable(self):
        return self._gameObservable

    def setItemSavedGames(self, savedGames):
        self._savedGames.append(savedGames)

    def getItemSavedGames(self, item):
        return self._savedGames[item]

    def delItemSavedGames(self, item):
        del self._savedGames[item]

    def getLenSavedGames(self):
        return len(self._savedGames)