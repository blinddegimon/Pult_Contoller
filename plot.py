from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSizePolicy
from pyqtgraph import PlotWidget

import pyqtgraph as pg


BUFFER_SIZE = 2000

def to_b16t(i):
    r = bytearray()
    for e in i:
        r += e.to_bytes(2,'little',signed=True)
    return r

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

