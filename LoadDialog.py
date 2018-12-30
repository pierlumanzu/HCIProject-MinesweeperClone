from PyQt5.QtWidgets import QDialog, QLabel, QRadioButton

import sys
sys.path.append("UiDesigner/UiDesignerFilePython/")
from Ui_LoadDialog import Ui_Load #LoadDialog View.

import os

from SaveAsLoadDeleteDialogModel import SaveAsLoadDeleteDialogModel

class LoadDialog(QDialog):#LoadDialog Controller.

    def __init__(self, gameToLoadObservable):

        super().__init__()

        self._model = SaveAsLoadDeleteDialogModel(gameToLoadObservable)

        self._ui = Ui_Load()
        self._ui.setupUi(self)

        fileList = os.listdir("DataSaved/SavedGames")
        for fileName in fileList:
            if fileName.lower().endswith(('.pkl')):
                fileName = fileName[0:len(fileName) - 4]
                self._model.setItemSavedGames(fileName)

        self.makeListSavedGames()
        self._ui.loadButton.clicked.connect(self.callingLoadOperation)

    def makeListSavedGames(self):

        if self._model.getLenSavedGames() == 0:
            self._ui.savedGamesArea.layout().addWidget(QLabel("No Games Saved."))
            self._ui.savedGamesArea.layout().itemAt(0).widget().setStyleSheet("font-size:11pt;")
        else:
            for i in range(self._model.getLenSavedGames()):
                self._ui.savedGamesArea.layout().addWidget(QRadioButton(self._model.getItemSavedGames(i)))

    def callingLoadOperation(self):
        if self._model.getLenSavedGames() == 0:
            if self._ui.scrollAreaWidgetContents.layout().count() == 3:                                             #"scrollAreaWidgetContents" is the dialog main area.
                self._ui.scrollAreaWidgetContents.layout().addWidget(QLabel("Select a game to load."))
                self._ui.scrollAreaWidgetContents.layout().itemAt(self._ui.scrollAreaWidgetContents.layout().count() - 1).widget().setStyleSheet("color:red; font-size:11pt;")
        else:
            for i in range(self._ui.savedGamesArea.layout().count()):
                if self._ui.savedGamesArea.layout().itemAt(i).widget().isChecked():
                    self._model.gameObservable.value = self._model.getItemSavedGames(i)
                    self.close()
            if self._ui.scrollAreaWidgetContents.layout().count() == 3:
                self._ui.scrollAreaWidgetContents.layout().addWidget(QLabel("Select a game to load."))
                self._ui.scrollAreaWidgetContents.layout().itemAt(self._ui.scrollAreaWidgetContents.layout().count() - 1).widget().setStyleSheet("color:red; font-size:11pt;")


