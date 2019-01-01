from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QObject

import sys
sys.path.append("UiDesigner/UiDesignerFilePython/")
from Ui_WarningSaveDialog import Ui_WarningSaveDialog               #WarningSaveDialog View.
from Ui_SuccessSaveDialog import Ui_SuccessSaveDialog               #SuccesSaveDialog View.
from Ui_AutoSaveDialog import Ui_AutoSaveDialog                     #AutoSaveDialog View.
from Ui_WarningDeleteDialog import Ui_WarningDeleteDialog           #WarningDeleteDialog View.
from Ui_RecordDialog import Ui_RecordDialog                         #RecordDialog View.
from Ui_ControlsDialog import Ui_ControlsDialog                     #ControlsDialog View.

class DialogModel(QObject):#Dialogs Model.

    def __init__(self, lineEditObservable=None, buttonBoxObservable=None):

        super().__init__()

        if lineEditObservable is None:
            self._lineEditObservable = None
        else:
            self._lineEditObservable = lineEditObservable             #Only the RecordDialog needs this observable. This latter one is used if a user must insert a text on the dialog.

        if buttonBoxObservable is None:
            self._buttonBoxObservable = None                          #The SuccessSaveDialog and the ControlsDialog do not need this observable.
        else:
            self._buttonBoxObservable = buttonBoxObservable           #This Observable is used to communicate if the user accepts the request of a dialog or not.

    @property
    def lineEditObservable(self):
        return self._lineEditObservable

    @property
    def buttonBoxObservable(self):
        return self._buttonBoxObservable

class WarningSaveDialog(QDialog):#WarningSaveDialog Controller.

    def __init__(self, isReplacingObservable):

        super().__init__()

        self._model = DialogModel(buttonBoxObservable=isReplacingObservable)

        self._ui = Ui_WarningSaveDialog()
        self._ui.setupUi(self)

        self._ui.buttonBox.accepted.connect(self.acceptReplacing)
        self._ui.buttonBox.rejected.connect(self.rejectReplacing)

    def acceptReplacing(self):
        self._model.buttonBoxObservable.value = True

    def rejectReplacing(self):
        self._model.buttonBoxObservable.value = False

class SuccessSaveDialog(QDialog):#SuccessSaveDialog Controller.

    def __init__(self):

        super().__init__()

        self._model = DialogModel()

        self._ui = Ui_SuccessSaveDialog()
        self._ui.setupUi(self)

class ControlsDialog(QDialog):#ControlsDialog Controller.

    def __init__(self):

        super().__init__()

        self._model = DialogModel()

        self._ui = Ui_ControlsDialog()
        self._ui.setupUi(self)

class AutoSaveDialog(QDialog):#AutoSaveDialog Controller.

    def __init__(self, isAutoLoadingObservable):

        super().__init__()

        self._model = DialogModel(buttonBoxObservable=isAutoLoadingObservable)

        self._ui = Ui_AutoSaveDialog()
        self._ui.setupUi(self)

        self._ui.buttonBox.accepted.connect(self.acceptAutoLoading)
        self._ui.buttonBox.rejected.connect(self.rejectAutoLoading)

    def acceptAutoLoading(self):
        self._model.buttonBoxObservable.value = True

    def rejectAutoLoading(self):
        self._model.buttonBoxObservable.value = False

class WarningDeleteDialog(QDialog):#WarningDeleteDialog Controller.

    def __init__(self, isDeleteObservable):

        super().__init__()

        self._model = DialogModel(buttonBoxObservable=isDeleteObservable)

        self._ui = Ui_WarningDeleteDialog()
        self._ui.setupUi(self)

        self._ui.buttonBox.accepted.connect(self.acceptDelete)
        self._ui.buttonBox.rejected.connect(self.rejectDelete)

    def acceptDelete(self):
        self._model.buttonBoxObservable.value = True

    def rejectDelete(self):
        self._model.buttonBoxObservable.value = False

class RecordDialog(QDialog):#RecordDialog Controller.

    def __init__(self, time, isRecordObservable, nameRecordObservable):

        super().__init__()

        self._model = DialogModel(nameRecordObservable, isRecordObservable)

        self._ui = Ui_RecordDialog()
        self._ui.setupUi(self)

        self._ui.labelTimeRecord.setText("Time:" + str(time))

        self._ui.buttonBox.accepted.connect(self.acceptRecord)
        self._ui.buttonBox.rejected.connect(self.rejectRecord)

    def acceptRecord(self):
        if len(self._ui.nameRecord.text()) != 0:
            self._model.buttonBoxObservable.value = True
            self._model.lineEditObservable.value = self._ui.nameRecord.text().replace(" ", "")
        else:
            self._model.buttonBoxObservable.value = True
            self._model.lineEditObservable.value = "unknown"

    def rejectRecord(self):
        self._model.buttonBoxObservable.value = False