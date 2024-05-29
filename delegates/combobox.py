from PySide6 import QtCore, QtWidgets
from typing import List

class ComboboxDelegate(QtWidgets.QItemDelegate):
    def __init__(self, values: List[str], parent=None):
        QtWidgets.QItemDelegate.__init__(self, parent)
        self._data = values

    def createEditor(self, parent, option, index):
        # model_value = index.model().data(index, QtCore.Qt.DisplayRole)

        editor = QtWidgets.QComboBox(parent)
        editor.addItems(self._data)

        return editor

    def setEditorData(self, editor, index):

        model_value = index.model().data(index, QtCore.Qt.EditRole)

        current_index = editor.findText(model_value)
        if current_index > 0:
            editor.setCurrentIndex(current_index)

    def setModelData(self, editor, model, index):
        editor_value = editor.currentText()
        model.setData(index, editor_value, QtCore.Qt.EditRole)
