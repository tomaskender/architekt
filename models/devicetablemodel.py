import pandas as pd
from models.tablemodel import TableModel
from PySide6.QtCore import Qt

class DeviceTableModel(TableModel):
    def __init__(self, data: pd.DataFrame = pd.DataFrame()):
        cols = ["Name"]
        super(DeviceTableModel, self).__init__(cols, data)

    def setData(self, index, value, role):
        # TODO: rename references for this device in variableTableModel
        old_value = self._data.iloc[index.row(),index.column()]
        return super(DeviceTableModel, self).setData(index, value, role)