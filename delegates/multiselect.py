from PySide6 import QtCore, QtWidgets
from typing import List

class MultiSelectDelegate(QtWidgets.QItemDelegate):
    def __init__(self, values: List[str], parent=None):
        QtWidgets.QItemDelegate.__init__(self, parent)
        self._data = values
        self._selected = []

    def createEditor(self, parent, option, index):
        editor = QtWidgets.QListWidget(parent)
        editor.setSelectionMode(QtWidgets.QListWidget.SelectionMode.MultiSelection)
        editor.addItems(self._data)

        def selectionChanged():
            self._selected = editor.selectedItems()
        editor.itemSelectionChanged.connect(selectionChanged)

        return editor

    def setEditorData(self, editor, index):
        editor.setCurrentIndex(index)

    def setModelData(self, editor, model, index):
        model.setData(index, ", ".join(list(map(lambda x: x.text(), self._selected))), QtCore.Qt.EditRole)
