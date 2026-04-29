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
        types = config.get("types", "value").split(" ")
        devices = config.get("devices", "names").split(" ")
        var_defaults = {
            Column.TYPE.value: types[0],
            Column.PUBLISHING.value: "Sync",
            Column.RATE.value: "0",
            Column.SRC_DEV.value: devices[0],
        }
        varTableModel = VariableTableModel(defaults=var_defaults)
        varTableView = self.ui.variableTableView
        varTableView.setModel(varTableModel)
        varTableView.setItemDelegateForColumn(
            varTableModel.columns().index(Column.TYPE.value), ComboboxDelegate(types, varTableView))
        varTableView.setItemDelegateForColumn(
            varTableModel.columns().index(Column.PUBLISHING.value), ComboboxDelegate(["Sync", "Async"], varTableView))
        varTableView.setItemDelegateForColumn(
            varTableModel.columns().index(Column.SRC_DEV.value), ComboboxDelegate(devices, varTableView))
        varTableView.setItemDelegateForColumn(
            varTableModel.columns().index(Column.DST_DEV.value), MultiSelectDelegate(devices, varTableView))

        # Setup device tab
        devTableModel = DeviceTableModel(pd.DataFrame({Column.NAME.value: devices}))
        devTableView = self.ui.deviceTableView
        devTableView.setModel(devTableModel)

        def updateDeviceInVariableTable(index, old, new):
            if index.column() == devTableModel.columns().index(Column.NAME.value):
                if old == "" and new != "":
                    devices.append(new)
                elif old != "":
                    varTableModel.rename_device(old, new)
                    if old in devices:
                        devices[devices.index(old)] = new
        devTableModel.setOnChange(updateDeviceInVariableTable)

        def removeDeviceFromVariableTable(index, value):
            varTableModel.clear_device(value)
            if value in devices:
                devices.remove(value)
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
                    devTableModel.removeRow(i.row())
        self.ui.removeRowButton.clicked.connect(lambda: remove_row())

        def export():
            data = varTableModel.data_frame
            for name, group in data.groupby(Column.SRC_DEV.value):
                print(f"Ive found data for device {name}, list of entries is {len(group)}")
        self.ui.exportButton.clicked.connect(lambda: export())
        # self.ui.actionExport.triggered.connect(lambda: self._export())
