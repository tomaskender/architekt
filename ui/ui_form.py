# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLayout,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(847, 647)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.topTabWithActionsHorizontalLayout = QHBoxLayout()
        self.topTabWithActionsHorizontalLayout.setObjectName(u"topTabWithActionsHorizontalLayout")
        self.topTabWithActionsHorizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.variableTab = QWidget()
        self.variableTab.setObjectName(u"variableTab")
        self.horizontalLayout_3 = QHBoxLayout(self.variableTab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.variableTableView = QTableView(self.variableTab)
        self.variableTableView.setObjectName(u"variableTableView")

        self.horizontalLayout_3.addWidget(self.variableTableView)

        self.tabWidget.addTab(self.variableTab, "")
        self.deviceTab = QWidget()
        self.deviceTab.setObjectName(u"deviceTab")
        sizePolicy.setHeightForWidth(self.deviceTab.sizePolicy().hasHeightForWidth())
        self.deviceTab.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.deviceTab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.deviceTableView = QTableView(self.deviceTab)
        self.deviceTableView.setObjectName(u"deviceTableView")

        self.horizontalLayout_2.addWidget(self.deviceTableView)

        self.tabWidget.addTab(self.deviceTab, "")

        self.topTabWithActionsHorizontalLayout.addWidget(self.tabWidget)

        self.sideActionVerticalLayout = QVBoxLayout()
        self.sideActionVerticalLayout.setObjectName(u"sideActionVerticalLayout")
        self.sideActionVerticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.sideActionVerticalLayout.setContentsMargins(0, -1, 0, -1)
        self.topSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.sideActionVerticalLayout.addItem(self.topSpacer)

        self.addRowButton = QPushButton(self.centralwidget)
        self.addRowButton.setObjectName(u"addRowButton")
        self.addRowButton.setAutoFillBackground(False)

        self.sideActionVerticalLayout.addWidget(self.addRowButton)

        self.removeRowButton = QPushButton(self.centralwidget)
        self.removeRowButton.setObjectName(u"removeRowButton")
        self.removeRowButton.setAutoFillBackground(False)

        self.sideActionVerticalLayout.addWidget(self.removeRowButton)

        self.bottomSpacer = QSpacerItem(10, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sideActionVerticalLayout.addItem(self.bottomSpacer)


        self.topTabWithActionsHorizontalLayout.addLayout(self.sideActionVerticalLayout)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.topTabWithActionsHorizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.topTabWithActionsHorizontalLayout)

        self.bottomActionButtonsHorizontalLayout = QHBoxLayout()
        self.bottomActionButtonsHorizontalLayout.setObjectName(u"bottomActionButtonsHorizontalLayout")
        self.bottomActionButtonsHorizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.leftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.bottomActionButtonsHorizontalLayout.addItem(self.leftSpacer)

        self.exportButton = QPushButton(self.centralwidget)
        self.exportButton.setObjectName(u"exportButton")

        self.bottomActionButtonsHorizontalLayout.addWidget(self.exportButton)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setAutoFillBackground(False)

        self.bottomActionButtonsHorizontalLayout.addWidget(self.saveButton)

        self.rightSpacer = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.bottomActionButtonsHorizontalLayout.addItem(self.rightSpacer)


        self.verticalLayout_3.addLayout(self.bottomActionButtonsHorizontalLayout)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 847, 37))
        self.menuArchitekt = QMenu(self.menubar)
        self.menuArchitekt.setObjectName(u"menuArchitekt")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuHelp_2 = QMenu(self.menubar)
        self.menuHelp_2.setObjectName(u"menuHelp_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchitekt.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuHelp_2.menuAction())
        self.menuArchitekt.addAction(self.actionOpen)
        self.menuArchitekt.addAction(self.actionSave)
        self.menuArchitekt.addAction(self.actionSave_as)
        self.menuArchitekt.addSeparator()
        self.menuArchitekt.addAction(self.actionImport)
        self.menuArchitekt.addAction(self.actionExport)
        self.menuArchitekt.addSeparator()
        self.menuArchitekt.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionUndo)
        self.menuHelp.addAction(self.actionRedo)
        self.menuHelp_2.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Architekt", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as...", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.variableTab), QCoreApplication.translate("MainWindow", u"Variables", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.deviceTab), QCoreApplication.translate("MainWindow", u"Devices", None))
#if QT_CONFIG(tooltip)
        self.addRowButton.setToolTip(QCoreApplication.translate("MainWindow", u"Add new variable to table", None))
#endif // QT_CONFIG(tooltip)
        self.addRowButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(tooltip)
        self.removeRowButton.setToolTip(QCoreApplication.translate("MainWindow", u"Remove currently selected variable", None))
#endif // QT_CONFIG(tooltip)
        self.removeRowButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuArchitekt.setTitle(QCoreApplication.translate("MainWindow", u"Project", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuHelp_2.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

