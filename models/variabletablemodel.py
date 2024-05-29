import pandas as pd
from models.tablemodel import TableModel

class VariableTableModel(TableModel):
    def __init__(self, data: pd.DataFrame = pd.DataFrame()):
        cols = ["Name", "Type", "Default Value", "Publishing", "Rate (ms)", "Source Device", "Destination Devices"]
        super(VariableTableModel, self).__init__(cols, data)
