from PySide6 import QtCore, QtWidgets
from typing import List

class MultiSelectDelegate(QtWidgets.QItemDelegate):
    def __init__(self, values: List[str], parent=None):
        QtWidgets.QItemDelegate.__init__(self, parent)
        self._data = values

    def createEditor(self, parent, option, index):
        editor = QtWidgets.QListWidget(parent)
        editor.setSelectionMode(QtWidgets.QListWidget.SelectionMode.MultiSelection)
        editor.addItems(self._data)
        return editor

    def setEditorData(self, editor, index):
        current = index.model().data(index, QtCore.Qt.EditRole) or ""
        selected = {v.strip() for v in current.split(",") if v.strip()}
        for i in range(editor.count()):
            item = editor.item(i)
            item.setSelected(item.text() in selected)

    def setModelData(self, editor, model, index):
        selected = [editor.item(i).text() for i in range(editor.count()) if editor.item(i).isSelected()]
        model.setData(index, ", ".join(selected), QtCore.Qt.EditRole)
