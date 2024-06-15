from configparser import ConfigParser
from PySide6.QtWidgets import QApplication
import sys

from src.mainwindow import MainWindow

CONFIG_FILE = 'config.ini'

if __name__ == "__main__":

    config = ConfigParser()
    config.read(CONFIG_FILE)

    app = QApplication(sys.argv)
    widget = MainWindow(config)
    widget.show()
    sys.exit(app.exec())
