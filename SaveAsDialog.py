from PyQt5.QtWidgets import QDialog, QLabel

import sys
sys.path.append("UiDesigner/UiDesignerFilePython/")
from Ui_SaveAsDialog import Ui_SaveAs #SaveAsDialog View.

import os

from SaveAsLoadDeleteDialogModel import SaveAsLoadDeleteDialogModel
from Dialogs import WarningSaveDialog
from Observable import Observable

class SaveAsDialog(QDialog):#SaveAsDialog Controller.

    def __init__(self, gameToSaveObservable):

        super().__init__()

        self._model = SaveAsLoadDeleteDialogModel(gameToSaveObservable)

        self._ui = Ui_SaveAs()
        self._ui.setupUi(self)

        fileList = os.listdir("DataSaved/SavedGames")
        for fileName in fileList:
            if fileName.lower().endswith(('.pkl')):
                fileName = fileName[0:len(fileName) - 4]
                self._model.setItemSavedGames(fileName)

        self.makeListSavedGames()
        self._ui.saveButton.clicked.connect(self.callingSaveOperation)

    def makeListSavedGames(self):

        if self._model.getLenSavedGames() == 0:
            self._ui.savedGamesArea.layout().addWidget(QLabel("No Games Saved."))
            self._ui.savedGamesArea.layout().itemAt(0).widget().setStyleSheet("font-size:11pt;")
        else:
            for i in range(self._model.getLenSavedGames()):
                self._ui.savedGamesArea.layout().addWidget(QLabel(self._model.getItemSavedGames(i)))

    def callingSaveOperation(self):
        if len(self._ui.nameGame.text()) == 0:
            if self._ui.scrollAreaWidgetContents.layout().count() == 3:                                                 #"scrollAreaWidgetContents" is the dialog main area.
                self._ui.scrollAreaWidgetContents.layout().addWidget(QLabel("Insert a game name."))
                self._ui.scrollAreaWidgetContents.layout().itemAt(self._ui.scrollAreaWidgetContents.layout().count() - 1).widget().setStyleSheet("color:red; font-size:11pt;")
            else:
                self._ui.scrollAreaWidgetContents.layout().itemAt(self._ui.scrollAreaWidgetContents.layout().count() - 1).widget().setText("Insert a game name.")
        else:
            if not(self._ui.nameGame.text().isalnum()):
                if self._ui.scrollAreaWidgetContents.layout().count() == 3:
                    self._ui.scrollAreaWidgetContents.layout().addWidget(QLabel("Insert a name without character special or spaces."))
                    self._ui.scrollAreaWidgetContents.layout().itemAt(self._ui.scrollAreaWidgetContents.layout().count() - 1).widget().setStyleSheet("color:red; font-size:11pt;")
                else:
                    self._ui.scrollAreaWidgetContents.layout().itemAt(self._ui.scrollAreaWidgetContents.layout().count() - 1).widget().setText("Insert a name without character special or spaces.")
            else:
                if self._ui.scrollAreaWidgetContents.layout().count() == 4:
                    self._ui.scrollAreaWidgetContents.layout().itemAt(self._ui.scrollAreaWidgetContents.layout().count() - 1).widget().setParent(None)
                count = 0
                for i in range(self._model.getLenSavedGames()):
                    if self._ui.nameGame.text() == self._model.getItemSavedGames(i):
                        isReplacing = Observable(False)
                        #If the user inserts a same name of another saved game, a dialog appears: he can replace this saved game or change the typed name.
                        dialog = WarningSaveDialog(isReplacing)
                        dialog.exec_()
                        if isReplacing.value:
                            self._model.gameObservable.value = self._ui.nameGame.text()
                            self.close()
                        break
                    else:
                        count += 1
                if count == self._model.getLenSavedGames():
                    self._model.gameObservable.value = self._ui.nameGame.text()
                    self.close()


