# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ampconfwidgetrOMAXC.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

class Ui_AmpConfWidget(object):
    def setupUi(self, AmpConfWidget):
        if not AmpConfWidget.objectName():
            AmpConfWidget.setObjectName(u"AmpConfWidget")
        AmpConfWidget.resize(317, 259)
        self.verticalLayout = QVBoxLayout(AmpConfWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(AmpConfWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(170, 170))
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.hs_pos = QSlider(self.frame)
        self.hs_pos.setObjectName(u"hs_pos")
        self.hs_pos.setMinimum(-2730)
        self.hs_pos.setMaximum(2730)
        self.hs_pos.setOrientation(Qt.Orientation.Horizontal)
        self.hs_pos.setInvertedAppearance(False)

        self.gridLayout.addWidget(self.hs_pos, 6, 0, 1, 2)

        self.pb_en = QPushButton(self.frame)
        self.pb_en.setObjectName(u"pb_en")
        self.pb_en.setCheckable(True)

        self.gridLayout.addWidget(self.pb_en, 4, 0, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)

        self.l_amp = QLabel(self.frame)
        self.l_amp.setObjectName(u"l_amp")
        self.l_amp.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.l_amp.setFont(font)
        self.l_amp.setFrameShape(QFrame.Shape.Box)
        self.l_amp.setLineWidth(1)
        self.l_amp.setTextFormat(Qt.TextFormat.AutoText)
        self.l_amp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.l_amp.setWordWrap(False)

        self.gridLayout.addWidget(self.l_amp, 3, 0, 1, 2)

        self.l_pos = QLineEdit(self.frame)
        self.l_pos.setObjectName(u"l_pos")

        self.gridLayout.addWidget(self.l_pos, 5, 1, 1, 1)

        self.pb_arrSt = QPushButton(self.frame)
        self.pb_arrSt.setObjectName(u"pb_arrSt")

        self.gridLayout.addWidget(self.pb_arrSt, 7, 0, 1, 2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(AmpConfWidget)

        QMetaObject.connectSlotsByName(AmpConfWidget)
    # setupUi

    def retranslateUi(self, AmpConfWidget):
        AmpConfWidget.setWindowTitle(QCoreApplication.translate("AmpConfWidget", u"Form", None))
        self.pb_en.setText(QCoreApplication.translate("AmpConfWidget", u"EN", None))
        self.label.setText(QCoreApplication.translate("AmpConfWidget", u"Position:", None))
        self.l_amp.setText(QCoreApplication.translate("AmpConfWidget", u"TextLabel", None))
        self.pb_arrSt.setText("")
    # retranslateUi

