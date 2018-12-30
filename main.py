from PyQt5.QtWidgets import QApplication

import sys

from MinesweeperClone import MinesweeperClone
from Observable import Observable

app = QApplication(sys.argv)
appIsAlive = Observable(True)            #This Observable is used to communicate to the background threads when the application is closed by the user.
window = MinesweeperClone(appIsAlive)
window.show()
app.exec_()
appIsAlive.value = False