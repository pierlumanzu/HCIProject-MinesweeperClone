from PyQt5.QtWidgets import QDialog, QLabel

import sys
sys.path.append("UiDesigner/UiDesignerFilePython/")
from Ui_NewDialog import Ui_NewGame  #NewDialog View.

from NewDialogModel import NewDialogModel

class NewDialog(QDialog):#NewDialog Controller.

    def __init__(self, modelMinesweeper, isChangedAnythingObservable):

        super().__init__()

        self._model = NewDialogModel(modelMinesweeper, isChangedAnythingObservable)

        self._ui = Ui_NewGame()
        self._ui.setupUi(self)

        self._model.observeCreationNewModel(self.closingDialog)
        self._ui.newGameButton.clicked.connect(self.createNewGame)

    def createNewGame(self):

        if self._ui.beginnerButton.isChecked():
            #print("Beginner")
            self._model.W = int(self._ui.widthBeginner.text())
            self._model.H = int(self._ui.heightBeginner.text())
            self._model.mines = int(self._ui.minesBeginner.text())
            self._model.rankingType = 0
            self._model.isChangedAnythingObservable.value = True
        else:
            if self._ui.intermediateButton.isChecked():
                #print("Intermediate")
                self._model.W = int(self._ui.widthIntermediate.text())
                self._model.H = int(self._ui.heightIntermediate.text())
                self._model.mines = int(self._ui.minesIntermediate.text())
                self._model.rankingType = 1
                self._model.isChangedAnythingObservable.value = True
            else:
                if self._ui.expertButton.isChecked():
                    #print("Expert")
                    self._model.W = int(self._ui.widthExpert.text())
                    self._model.H = int(self._ui.heightExpert.text())
                    self._model.mines = int(self._ui.minesExpert.text())
                    self._model.rankingType = 2
                    self._model.isChangedAnythingObservable.value = True
                else:
                    if self._ui.customButton.isChecked():
                        #print("Custom")
                        self._model.W = self._ui.widthCustom.value()
                        self._model.H = self._ui.heightCustom.value()
                        if self._model.W * self._model.H <= self._ui.minesCustom.value():           #The mines number must always be less than the product between the width and the height of the grid.
                            self._ui.minesCustom.setValue(self._model.W * self._model.H - 1)
                        self._model.mines = self._ui.minesCustom.value()
                        self._model.rankingType = 3
                        self._model.isChangedAnythingObservable.value = True
                    else:
                        if self._ui.scrollAreaWidgetContents.layout().count() == 3:
                            self._ui.scrollAreaWidgetContents.layout().addWidget(QLabel("Choose one of the options."))
                            self._ui.scrollAreaWidgetContents.layout().itemAt(self._ui.scrollAreaWidgetContents.layout().count() - 1).widget().setStyleSheet("color:red; font-size:11pt;")

    def closingDialog(self):

        self._model.modelMinesweeper.W = self._model.W
        self._model.modelMinesweeper.H = self._model.H
        self._model.modelMinesweeper.mines = self._model.mines
        self._model.modelMinesweeper.rankingType = self._model.rankingType
        self.close()