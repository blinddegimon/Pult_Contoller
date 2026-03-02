# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowEPiSdP.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLayout,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(811, 588)
        self.actionDisconnect = QAction(MainWindow)
        self.actionDisconnect.setObjectName(u"actionDisconnect")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemLogOut))
        self.actionDisconnect.setIcon(icon)
        self.actionConnect = QAction(MainWindow)
        self.actionConnect.setObjectName(u"actionConnect")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaylistShuffle))
        self.actionConnect.setIcon(icon1)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionConfigure = QAction(MainWindow)
        self.actionConfigure.setObjectName(u"actionConfigure")
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.actionClear.setIcon(icon2)
        self.actionClear.setMenuRole(QAction.MenuRole.NoRole)
        self.actionPause = QAction(MainWindow)
        self.actionPause.setObjectName(u"actionPause")
        self.actionPause.setCheckable(True)
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause))
        self.actionPause.setIcon(icon3)
        self.actionPause.setMenuRole(QAction.MenuRole.NoRole)
        self.actionStop = QAction(MainWindow)
        self.actionStop.setObjectName(u"actionStop")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop))
        self.actionStop.setIcon(icon4)
        self.actionStop.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.f_control = QFrame(self.centralwidget)
        self.f_control.setObjectName(u"f_control")
        self.f_control.setMinimumSize(QSize(0, 150))
        self.f_control.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_control.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.f_control, 1, 0, 1, 1)

        self.f_AMPConf = QFrame(self.centralwidget)
        self.f_AMPConf.setObjectName(u"f_AMPConf")
        self.f_AMPConf.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_AMPConf.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.f_AMPConf, 1, 1, 1, 1)

        self.f_plot = QFrame(self.centralwidget)
        self.f_plot.setObjectName(u"f_plot")
        self.f_plot.setMinimumSize(QSize(500, 300))
        self.f_plot.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_plot.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.f_plot, 0, 0, 1, 2)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 811, 33))
        self.menuCalls = QMenu(self.menubar)
        self.menuCalls.setObjectName(u"menuCalls")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuCalls.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menuCalls.addAction(self.actionConnect)
        self.menuCalls.addAction(self.actionDisconnect)
        self.menuTools.addAction(self.actionConfigure)
        self.toolBar.addAction(self.actionConnect)
        self.toolBar.addAction(self.actionDisconnect)
        self.toolBar.addAction(self.actionClear)
        self.toolBar.addAction(self.actionPause)
        self.toolBar.addAction(self.actionStop)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDisconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.actionConnect.setText(QCoreApplication.translate("MainWindow", u"Conncect", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionConfigure.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionClear.setText(QCoreApplication.translate("MainWindow", u"clear", None))
#if QT_CONFIG(tooltip)
        self.actionClear.setToolTip(QCoreApplication.translate("MainWindow", u"Clear plot ", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionClear.setShortcut(QCoreApplication.translate("MainWindow", u"C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPause.setText(QCoreApplication.translate("MainWindow", u"pause", None))
#if QT_CONFIG(tooltip)
        self.actionPause.setToolTip(QCoreApplication.translate("MainWindow", u"Pause plotting", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionPause.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.actionStop.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
#if QT_CONFIG(tooltip)
        self.actionStop.setToolTip(QCoreApplication.translate("MainWindow", u"Disable of drivers", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionStop.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.menuCalls.setTitle(QCoreApplication.translate("MainWindow", u"Calls", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

