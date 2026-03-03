# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controlzJrhbq.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QDial, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QWidget)

class Ui_ControlWindow(object):
    def setupUi(self, ControlWindow):
        if not ControlWindow.objectName():
            ControlWindow.setObjectName(u"ControlWindow")
        ControlWindow.resize(371, 305)
        self.gridLayout = QGridLayout(ControlWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.rb_4ChMode = QRadioButton(ControlWindow)
        self.bg_mode = QButtonGroup(ControlWindow)
        self.bg_mode.setObjectName(u"bg_mode")
        self.bg_mode.addButton(self.rb_4ChMode)
        self.rb_4ChMode.setObjectName(u"rb_4ChMode")
        self.rb_4ChMode.setAutoExclusive(True)

        self.gridLayout.addWidget(self.rb_4ChMode, 2, 0, 1, 1)

        self.hs_x = QSlider(ControlWindow)
        self.hs_x.setObjectName(u"hs_x")
        self.hs_x.setEnabled(True)
        self.hs_x.setMinimum(-2730)
        self.hs_x.setMaximum(2730)
        self.hs_x.setTracking(True)
        self.hs_x.setOrientation(Qt.Orientation.Horizontal)
        self.hs_x.setTickPosition(QSlider.TickPosition.NoTicks)
        self.hs_x.setTickInterval(0)

        self.gridLayout.addWidget(self.hs_x, 0, 1, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(ControlWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_6)

        self.l_x = QLineEdit(ControlWindow)
        self.l_x.setObjectName(u"l_x")
        self.l_x.setMaximumSize(QSize(60, 20))
        self.l_x.setBaseSize(QSize(0, 0))
        self.l_x.setMaxLength(10)
        self.l_x.setFrame(True)
        self.l_x.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.l_x)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.pb_tx = QPushButton(ControlWindow)
        self.pb_tx.setObjectName(u"pb_tx")
        self.pb_tx.setCheckable(True)

        self.gridLayout.addWidget(self.pb_tx, 1, 0, 1, 1)

        self.rb_1ChMode = QRadioButton(ControlWindow)
        self.bg_mode.addButton(self.rb_1ChMode)
        self.rb_1ChMode.setObjectName(u"rb_1ChMode")

        self.gridLayout.addWidget(self.rb_1ChMode, 4, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(ControlWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.l_y = QLineEdit(ControlWindow)
        self.l_y.setObjectName(u"l_y")
        self.l_y.setMaximumSize(QSize(60, 20))
        self.l_y.setBaseSize(QSize(0, 0))
        self.l_y.setMaxLength(10)
        self.l_y.setFrame(True)
        self.l_y.setEchoMode(QLineEdit.EchoMode.Normal)
        self.l_y.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.l_y)


        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 1, 1, 2)

        self.vs_y = QSlider(ControlWindow)
        self.vs_y.setObjectName(u"vs_y")
        self.vs_y.setMinimum(-2730)
        self.vs_y.setMaximum(2730)
        self.vs_y.setOrientation(Qt.Orientation.Vertical)
        self.vs_y.setInvertedAppearance(False)
        self.vs_y.setInvertedControls(False)

        self.gridLayout.addWidget(self.vs_y, 1, 2, 3, 1)

        self.rb_2ChMode = QRadioButton(ControlWindow)
        self.bg_mode.addButton(self.rb_2ChMode)
        self.rb_2ChMode.setObjectName(u"rb_2ChMode")

        self.gridLayout.addWidget(self.rb_2ChMode, 3, 0, 1, 1)

        self.d_xy = QDial(ControlWindow)
        self.d_xy.setObjectName(u"d_xy")
        self.d_xy.setMinimum(-2730)
        self.d_xy.setMaximum(2730)
        self.d_xy.setValue(0)
        self.d_xy.setSliderPosition(0)
        self.d_xy.setOrientation(Qt.Orientation.Horizontal)
        self.d_xy.setInvertedControls(False)
        self.d_xy.setWrapping(True)
        self.d_xy.setNotchTarget(91.000000000000000)
        self.d_xy.setNotchesVisible(True)

        self.gridLayout.addWidget(self.d_xy, 1, 1, 3, 1)

        self.gridLayout.setColumnStretch(1, 1)

        self.retranslateUi(ControlWindow)

        QMetaObject.connectSlotsByName(ControlWindow)
    # setupUi

    def retranslateUi(self, ControlWindow):
        ControlWindow.setWindowTitle(QCoreApplication.translate("ControlWindow", u"Form", None))
        self.rb_4ChMode.setText(QCoreApplication.translate("ControlWindow", u"4 Ch", None))
        self.label_6.setText(QCoreApplication.translate("ControlWindow", u"X:", None))
        self.pb_tx.setText(QCoreApplication.translate("ControlWindow", u"TX", None))
        self.rb_1ChMode.setText(QCoreApplication.translate("ControlWindow", u"1 Ch", None))
        self.label_5.setText(QCoreApplication.translate("ControlWindow", u"Y:", None))
        self.rb_2ChMode.setText(QCoreApplication.translate("ControlWindow", u"2 Ch", None))
    # retranslateUi

