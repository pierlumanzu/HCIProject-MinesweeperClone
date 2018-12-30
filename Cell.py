from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt


class ButtonModel(QObject):#Button Model.

    adviseCoordinates = pyqtSignal(tuple)
    adviseClicked = pyqtSignal()
    adviseChecked = pyqtSignal(bool)
    valueChanged = pyqtSignal(str)

    def __init__(self, X, Y, isMines, **kwargs):
        super().__init__(**kwargs)
        self._X = X                                     #This variable indicates the position on the horizontal axis on the grid.
        self._Y = Y                                     #This variable indicates the position on the vertical axis on the grid.
        self._isMines = isMines                         #This variable indicates if the button is a mines.
        self._value = None                              #This variable indicates the button value.
        self._isClicked = False                         #This variable indicates if the button is clicked.
        self._isChecked = False                         #This variable indicates if the button is checked.
        self._isActive = True                           #This variable indicates if the button is active.

    def loadButton(self, isMines, value, isChecked, isClicked, isActive):    #This function leads to the possibility of loading some characteristics of a button. It is used in the cases when a user decides to load a game.
        self._isMines = isMines
        self.value = value
        self._isChecked = isChecked
        self._isClicked = isClicked
        self._isActive = isActive
        if isClicked:
            self.adviseClicked.emit()

    @property
    def X(self):
        return self._X

    @property
    def Y(self):
        return self._Y

    @property
    def isMines(self):
        return self._isMines

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newValue):
        self._value = newValue
        self.valueChanged.emit(newValue)

    @property
    def isClicked(self):
        return self._isClicked

    @isClicked.setter
    def isClicked(self, newIsClicked):
        self._isClicked = newIsClicked
        self.adviseClicked.emit()
        if self._isActive:
            self.adviseCoordinates.emit((self._X, self._Y))

    @property
    def isChecked(self):
        return self._isChecked

    @isChecked.setter
    def isChecked(self, newIsChecked):
        self._isChecked = newIsChecked
        if newIsChecked:
            self.value = "C"
        else:
            self.value = None
        if self._isActive:
            self.adviseChecked.emit(newIsChecked)

    @property
    def isActive(self):
        return self._isActive

    @isActive.setter
    def isActive(self, newIsActive):
        self._isActive = newIsActive

    def observeCell(self, slot):                    #This function allows to observe if a button value is changed.
        self.valueChanged.connect(slot)

    def observeNeighbors(self, slot):               #This function allows to observe if a propagation from a clicked button is requested.
        self.adviseCoordinates.connect(slot)

    def observeClicked(self, slot):                 #This function allows to observe if a button is clicked.
        self.adviseClicked.connect(slot)

    def observeChecked(self, slot):                 #This function allows to observe if a button is checked.
        self.adviseChecked.connect(slot)


class ButtonViewController(QPushButton):#Button View/Controller.

    def __init__(self, model, **kwargs):
        super().__init__(**kwargs)
        self._model = model                          #The model of the button.
        self.setText(self._model.value)
        self.setFixedSize(25,25)
        self._model.observeCell(lambda value:self.setText(value))
        self._model.observeClicked(self.setStyleSheetCell)

    def mousePressEvent(self, QMouseEvent):          #If the left button of the mouse is clicked, the button is clicked. If the rigth button is clicked, the button is checked.
        if QMouseEvent.button() == Qt.LeftButton and self._model.isActive and not(self._model.isChecked):
            self._model.isClicked = True
        elif QMouseEvent.button() == Qt.RightButton and self._model.isActive:
            if self._model.isChecked:
                self._model.isChecked = False
            else:
                self._model.isChecked = True

    def setStyleSheetCell(self):                     #If a button is clicked and it is a mines, the button background color becomes red. Else if it is not a mines, the background color becomes gray. The background color green is used to indicate if a button is a mines and is checked by the user.
        if self._model.isMines:
            if self._model.isChecked:
                self.setStyleSheet("background-color:green;")
            else:
                self.setStyleSheet("background-color:red;")
        else:
            self.setStyleSheet("background-color:gray;")
