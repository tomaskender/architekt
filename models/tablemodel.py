from typing import List, Callable
import pandas as pd
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex

class TableModel(QAbstractTableModel):
    def __init__(
            self,
            cols: List[str],
            data: pd.DataFrame = None,
            defaults: dict = None,
    ):
        super(TableModel, self).__init__()
        self._cols = cols
        self._data = data if (data is not None and not data.empty) else pd.DataFrame(columns=cols)
        self._defaults = defaults if defaults is not None else {}
        self._onChange = None
        self._onRemove = None

    def columns(self):
        return self._cols

    @property
    def data_frame(self) -> pd.DataFrame:
        return self._data

    def headerData(self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole = None):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self._cols[section]
        else:
            return QAbstractTableModel.headerData(self, section, orientation, role)

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            old = self._data.iloc[index.row(), index.column()]
            self._data.iloc[index.row(), index.column()] = value
            if self._onChange:
                self._onChange(index, old, value)
            return super(TableModel, self).setData(index, value, role)

    def setOnChange(self, func: Callable[[QModelIndex, str, str], None]):
        self._onChange = func

    def setOnRemove(self, func: Callable[[QModelIndex, str], None]):
        self._onRemove = func

    def flags(self, _):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def data(self, index: QModelIndex, role: Qt.ItemDataRole):
        if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
            return self._data.iloc[index.row(), index.column()]

    def insertRow(self, row: int) -> bool:
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())

        new_row = {col: [self._defaults.get(col, '')] for col in self._cols}
        new_df = pd.DataFrame(new_row)

        df1 = self._data.iloc[:row]
        df2 = self._data.iloc[row:]
        self._data = pd.concat([df1, new_df, df2])
        self._data.reset_index(drop=True, inplace=True)

        self.endInsertRows()
        return True

    def removeRow(self, row: int) -> bool:
        self.beginRemoveRows(QModelIndex(), row, row)
        try:
            label = self._data.index[row]
            if self._onRemove:
                self._onRemove(self.index(row, 0), self._data.iloc[row, 0])
            self._data.drop(label, inplace=True)
            self._data.reset_index(drop=True, inplace=True)
            succ = True
        except (KeyError, IndexError):
            succ = False
        self.endRemoveRows()
        return succ

    def rowCount(self, _ = None):
        return len(self._data)

    def columnCount(self, _):
        return len(self._cols)
