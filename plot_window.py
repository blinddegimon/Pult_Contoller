import numpy as np
from PySide6.QtWidgets import QFrame, QGridLayout, QWidget, QPushButton

from amp import CurveWidget
from plot import Plot

from pyqtgraph import PlotDataItem, mkPen


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
