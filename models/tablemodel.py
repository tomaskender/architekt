from typing import List
import pandas as pd
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from typing import Callable

class TableModel(QAbstractTableModel):
    def __init__(
            self,
            cols: List[str],
            data: pd.DataFrame = pd.DataFrame(),
    ):
        super(TableModel, self).__init__()
        self._cols = cols
        self._data = data
        self._onChange = None
        self._onRemove = None

    def columns(self):
        return self._cols

    def headerData(self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole = None):
        if role == Qt.ItemDataRole.DisplayRole and orientation==Qt.Orientation.Horizontal:
            return self._cols[section]
        else:
            return QAbstractTableModel.headerData(self, section, orientation, role)

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            if self._onChange:
                self._onChange(index, self._data.iloc[index.row(),index.column()], value)

            self._data.iloc[index.row(),index.column()] = value
            return super(TableModel, self).setData(index, value, role)

    def setOnChange(self, func: Callable[[QModelIndex, str, str], None]):
        self._onChange = func

    def flags(self, _):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def data(self, index: QModelIndex, role: Qt.ItemDataRole):
        if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
            return self._data.iloc[index.row(), index.column()]

    def insertRow(self, row: int) -> bool:
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        
        empty_data = {col: [''] for col in self._cols}
        empty_df = pd.DataFrame(empty_data)

        # Slice the original DataFrame into two parts
        df1 = self._data.iloc[:row]
        df2 = self._data.iloc[row:]

        self._data = pd.concat([df1, empty_df, df2])
        self._data.reset_index(drop=True, inplace=True)

        self.endInsertRows()
        return True

    def removeRow(self, row: int) -> bool:
        self.beginRemoveRows(QModelIndex(), row, row)
        try:
            self._data.drop(row, inplace=True)
            succ = True
        except KeyError:
            succ = False
        self.endRemoveRows()
        return succ
    
    def setOnRemove(self, func: Callable[[QModelIndex, str], None]):
        self._onRemove = func

    def rowCount(self, _ = None):
        return len(self._data)

    def columnCount(self, _):
        return len(self._cols)