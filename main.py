from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication, QLabel, QPushButton

#from amp import AMPWidget

from mainwindow import MainWindow

import pyqtgraph as pg

"""PySide6 Controller for AMP v0.1"""


if __name__ == "__main__":
    #pg.setConfigOptions(useOpenGL = True, antialias = True)
    a = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    #l = QLabel()
    #l.show()

    #amp = AMPWidget()
    #amp.show()

    #tb = QPushButton()
    #tb.setText("Hello world from QT button!")    #tb.setFixedSize(50,50)
    #tb.show()


    sys.exit(a.exec())