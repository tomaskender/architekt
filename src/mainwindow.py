#!python
from configparser import ConfigParser
import pandas as pd
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QAbstractItemView, QMainWindow

from delegates.combobox import ComboboxDelegate
from delegates.multiselect import MultiSelectDelegate
from models.column import Column
from models.devicetablemodel import DeviceTableModel
from models.variabletablemodel import VariableTableModel
from ui.ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, config: ConfigParser, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon("img/icon.png"))
        self.ui.variableTableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        # Setup variable tab
        varTableModel = VariableTableModel(pd.DataFrame())
        varTableView = self.ui.variableTableView
        varTableView.setModel(varTableModel)
        varTableView.setItemDelegateForColumn(
            varTableModel.columns().index(Column.TYPE.value), ComboboxDelegate(config.get("types", "value").split(" "), varTableView))
        varTableView.setItemDelegateForColumn(
            varTableModel.columns().index(Column.PUBLISHING.value), ComboboxDelegate(["Sync", "Async"], varTableView))
        varTableView.setItemDelegateForColumn(
            varTableModel.columns().index(Column.SRC_DEV.value), ComboboxDelegate(config.get("types", "dev").split(" "), varTableView))
        varTableView.setItemDelegateForColumn(
            varTableModel.columns().index(Column.DST_DEV.value), MultiSelectDelegate(config.get("types", "dev").split(" "), varTableView))

        # Setup device tab
        devTableModel = DeviceTableModel(pd.DataFrame())
        devTableView = self.ui.deviceTableView
        devTableView.setModel(devTableModel)

        def updateDeviceInVariableTable(index, old, new):
            if index.column() == devTableModel.columns().index(Column.NAME.value) and old != "":
                model = varTableModel._data

                model.loc[model[Column.SRC_DEV.value] == old, Column.SRC_DEV.value] = new
                model[Column.DST_DEV] = model[Column.DST_DEV.value].str.split(", ") \
                    .apply(lambda devs: [dev if dev != old else new for dev in devs]).join(", ")
        devTableModel.setOnChange(updateDeviceInVariableTable)

        def removeDeviceFromVariableTable(index, value):
            updateDeviceInVariableTable(index, value, "")
        devTableModel.setOnRemove(removeDeviceFromVariableTable)

        # Setup buttons
        def insert_row():
            if self.ui.tabWidget.currentIndex() == 0:
                index = varTableModel.rowCount()
                varTableModel.insertRow(index)
                varTableView.scrollToBottom()
            else:
                index = devTableModel.rowCount()
                devTableModel.insertRow(index)
                devTableView.scrollToBottom()

        self.ui.addRowButton.clicked.connect(lambda: insert_row())

        def remove_row():
            if self.ui.tabWidget.currentIndex() == 0:
                indices = varTableView.selectionModel().selectedRows()
                for i in sorted(indices):
                    varTableModel.removeRow(i.row())
            else:
                indices = devTableView.selectionModel().selectedRows()
                for i in sorted(indices):
                    # delete currently selected device from variables
                    name = i.data()
                    varModel = varTableModel._data
                    # TODO move line below to model event
                    varModel.loc[varModel[Column.SRC_DEV.value] == name, Column.SRC_DEV.value] = ""
                    devTableModel.removeRow(i.row())
        self.ui.removeRowButton.clicked.connect(lambda: remove_row())

        def export():
            data = varTableModel._data
            devices = data.groupby(Column.SRC_DEV.value)

            for name, data in devices:
                print(f"Ive found data for device {name}, list of entries is {len(data)}")
        self.ui.exportButton.clicked.connect(lambda: export())
        # self.ui.actionExport.triggered.connect(lambda: self._export())
