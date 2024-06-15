import pandas as pd
from models.column import Column
from models.tablemodel import TableModel

class DeviceTableModel(TableModel):
    def __init__(self, data: pd.DataFrame):
        cols = [Column.NAME.value]
        super(DeviceTableModel, self).__init__(cols, data)
