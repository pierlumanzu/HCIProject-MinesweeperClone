from PyQt5.QtWidgets import QDialog, QLabel, QCheckBox

import sys
sys.path.append("UiDesigner/UiDesignerFilePython/")
from Ui_DeleteDialog import Ui_Delete #DeleteDialog View.

import os

from SaveAsLoadDeleteDialogModel import SaveAsLoadDeleteDialogModel
from Dialogs import WarningDeleteDialog
from Observable import Observable

class DeleteDialog(QDialog):#DeleteDialog Controller.

    def __init__(self):

        super().__init__()

        self._model = SaveAsLoadDeleteDialogModel()

        self._ui = Ui_Delete()
        self._ui.setupUi(self)

        fileList = os.listdir("DataSaved/SavedGames")
        for fileName in fileList:
            if fileName.lower().endswith(('.pkl')):
                fileName = fileName[0:len(fileName) - 4]
                self._model.setItemSavedGames(fileName)

        self.makeListSavedGames()
        self._ui.deleteButton.clicked.connect(self.callingDeleteOperation)

    def makeListSavedGames(self):

        if self._model.getLenSavedGames() == 0:
            self._ui.savedGamesArea.layout().addWidget(QLabel("No Games Saved."))
            self._ui.savedGamesArea.layout().itemAt(0).widget().setStyleSheet("font-size:11pt;")
        else:
            for i in range(self._model.getLenSavedGames()):
                self._ui.savedGamesArea.layout().addWidget(QCheckBox(self._model.getItemSavedGames(i)))

    def callingDeleteOperation(self):
        if self._model.getLenSavedGames() == 0:
            if self._ui.scrollAreaWidgetContents.layout().count() == 3:                                                 #"scrollAreaWidgetContents" is the dialog main area.
                self._ui.scrollAreaWidgetContents.layout().addWidget(QLabel("Select at least one game to delete."))
                self._ui.scrollAreaWidgetContents.layout().itemAt(self._ui.scrollAreaWidgetContents.layout().count() - 1).widget().setStyleSheet("color:red; font-size:11pt;")
        else:
            countGameChecked = 0
            for i in reversed(range(self._ui.savedGamesArea.layout().count())):
                if self._ui.savedGamesArea.layout().itemAt(i).widget().isChecked():
                    if self._ui.scrollAreaWidgetContents.layout().count() == 4:
                        self._ui.scrollAreaWidgetContents.layout().itemAt(self._ui.scrollAreaWidgetContents.layout().count() - 1).widget().setParent(None)
                    countGameChecked += 1
                    if countGameChecked == 1:
                        isDelete = Observable(False)
                        # A dialog that asks to the user if he wants the imminent elimination of some selected games.
                        dialog = WarningDeleteDialog(isDelete)
                        dialog.exec_()
                        if not(isDelete.value):
                            break
                    self.deleteGame(self._model.getItemSavedGames(i))
                    self._model.delItemSavedGames(i)
                    self._ui.savedGamesArea.layout().itemAt(i).widget().setParent(None)
            if self._ui.scrollAreaWidgetContents.layout().count() == 3 and countGameChecked == 0:
                self._ui.scrollAreaWidgetContents.layout().addWidget(QLabel("Select at least one game to delete."))
                self._ui.scrollAreaWidgetContents.layout().itemAt(self._ui.scrollAreaWidgetContents.layout().count() - 1).widget().setStyleSheet("color:red; font-size:11pt;")
            if self._model.getLenSavedGames() == 0:
                self._ui.savedGamesArea.layout().addWidget(QLabel("No Games Saved."))
                self._ui.savedGamesArea.layout().itemAt(0).widget().setStyleSheet("font-size:11pt;")

    def deleteGame(self, gameToDelete):
        os.remove("DataSaved/SavedGames/" + gameToDelete + ".pkl")

