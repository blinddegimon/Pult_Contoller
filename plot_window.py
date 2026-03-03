from PySide6.QtWidgets import QFrame, QGridLayout, QWidget, QPushButton
from PySide6.QtCore import Qt


import pyqtgraph as pg
from pyqtgraph import PlotDataItem, mkPen, PlotWidget

from tools import *

class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMouseMode(pg.ViewBox.RectMode)

    def mouseClickEvent(self, ev):
        if ev.button() == Qt.MouseButton.MiddleButton:
            self.show_custom_menu(ev)
            ev.accept()
        elif ev.button() == Qt.MouseButton.RightButton:
            self.enableAutoRange()
            ev.accept()
        else:
            super().mouseClickEvent(ev)

    def show_custom_menu(self, ev):
        menu = self.getMenu(ev)  # default pyqtgraph menu
        menu.popup(ev.screenPos().toPoint())

class Plot(PlotWidget):

    def __init__(self, parent=None):
        super().__init__(parent, background=(250,250,250), viewBox = CustomViewBox())

        #self.showGrid(x=True, y=True, alpha=0.3)

        self.getAxis('bottom').setStyle(maxTickLevel = 0)
        self.getAxis('left').setStyle(maxTickLevel = 0)

        self.getViewBox().setLimits(xMin = 0, xMax = BUFFER_SIZE)


        self.color_list = ((7,41,84), (224,43,51), (240,197,113), (89,168,155), (166,89,169), (0,250,0))


        self.setRange(xRange=[0, BUFFER_SIZE])
        self.showGrid(x=True, y=True)

class PlotWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QGridLayout(parent)

        self.m_plot = Plot(parent=parent)

        self.compose_curve_list = []

        self.layout.addWidget(self.m_plot, 0, 1, 0, -1)


    def init_curves(self, curves):
        for c in curves:
            self.m_plot.addItem(c)

    def add_compose_curve(self, compose_curve):
        self.compose_curve_list.append(compose_curve)
        self.init_curves(compose_curve.curve_list)
        self.layout.addWidget(compose_curve, len(self.compose_curve_list)-1, 0)
