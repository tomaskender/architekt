import pandas as pd
from models.column import Column
from models.tablemodel import TableModel

class VariableTableModel(TableModel):
    def __init__(self, data: pd.DataFrame = pd.DataFrame()):
        cols = [
            Column.NAME.value,
            Column.TYPE.value,
            Column.DEFAULT_VALUE.value,
            Column.PUBLISHING.value,
            Column.RATE.value,
            Column.SRC_DEV.value,
            Column.DST_DEV.value
        ]
        super(VariableTableModel, self).__init__(cols, data)
