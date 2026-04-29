import pandas as pd
from models.column import Column
from models.tablemodel import TableModel

class VariableTableModel(TableModel):
    def __init__(self, data: pd.DataFrame = None, defaults: dict = None):
        cols = [
            Column.NAME.value,
            Column.TYPE.value,
            Column.DEFAULT_VALUE.value,
            Column.PUBLISHING.value,
            Column.RATE.value,
            Column.SRC_DEV.value,
            Column.DST_DEV.value
        ]
        super(VariableTableModel, self).__init__(cols, data, defaults)

    def rename_device(self, old: str, new: str):
        src, dst = Column.SRC_DEV.value, Column.DST_DEV.value
        self._data.loc[self._data[src] == old, src] = new
        def _rename(devs):
            renamed = [new if d == old else d for d in devs if d]
            return [d for d in renamed if d]
        self._data[dst] = self._data[dst].str.split(", ").apply(_rename).str.join(", ")

    def clear_device(self, name: str):
        self.rename_device(name, "")
