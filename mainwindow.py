#!python
from configparser import ConfigParser
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

from delegates.combobox import ComboboxDelegate
from delegates.multiselect import MultiSelectDelegate
from tablemodel import VariableTableModel
from ui.ui_form import Ui_MainWindow

CONFIG_FILE = 'config.ini'
config = ConfigParser()
config.read(CONFIG_FILE)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon("img/icon.png"))

        # Setup variable tab
        varTableView = self.ui.variableTableView
        varTableView.setModel(VariableTableModel())
        varTableView.setItemDelegateForColumn(
            1, ComboboxDelegate(config.get("types", "value").split(" "), varTableView)) # TODO dynamic lookup of column index
        varTableView.setItemDelegateForColumn(
            3, ComboboxDelegate(["Sync", "Async"], varTableView)) # TODO dynamic lookup of column index
        varTableView.setItemDelegateForColumn(
            5, ComboboxDelegate(config.get("types", "dev").split(" "), varTableView)) # TODO dynamic lookup of column index
        varTableView.setItemDelegateForColumn(
            6, MultiSelectDelegate(config.get("types", "dev").split(" "), varTableView)) # TODO dynamic lookup of column index

        # Setup device tab
        # TODO

        # Setup buttons
        self.ui.addRowButton.clicked.connect(lambda: self._insert_row())
        self.ui.removeRowButton.clicked.connect(lambda: self._remove_variables())
        self.ui.exportButton.clicked.connect(lambda: self._export())
        # self.ui.actionExport.triggered.connect(lambda: self._export())

    def _insert_row(self):
        index = self.ui.variableTableView.model().rowCount()
        self.ui.variableTableView.model().insertRow(index)
        self.ui.variableTableView.scrollToBottom()

    def _remove_variables(self):
        indices = self.ui.variableTableView.selectionModel().selectedRows() 
        for i in sorted(indices):
            self.ui.variableTableView.model().removeRow(i.row())

    def _export(self):
        data = self.ui.variableTableView.model()._data
        devices = data.groupby("Source Device")
        
        for name, data in devices:
            print(f"Ive found data for device {name}, list of entries is {len(data)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
