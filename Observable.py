from PyQt5.QtCore import QObject, pyqtSignal

class Observable(QObject):

    valueChanged = pyqtSignal(object)

    def __init__(self, val):
        super().__init__()
        self._value = val

    def observe(self, slot):
        self.valueChanged.connect(slot)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newval):
        self._value = newval
        self.valueChanged.emit(self._value)