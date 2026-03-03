from os import name

from PySide6.QtCore import QRect, Qt, Slot
from PySide6.QtWidgets import QGridLayout, QPushButton, QLabel, QWidget, QButtonGroup, QFrame

from pyqtgraph import PlotDataItem, mkPen

from ui_ampconfwidget import Ui_AmpConfWidget

from tools import *

class AmpConfWidget(QWidget):
    def __init__(self, parent=None, amp_name ="XY"):
        super().__init__(parent)
        self.conf_ui = Ui_AmpConfWidget()
        self.name = amp_name
        self.setObjectName("AmpConfWidget_"+amp_name)

        self.pos = 0
        self.degree_flag = False


    def setup(self, degree_widget = None):
        self.conf_ui.setupUi(self)
        self.conf_ui.frame.setMaximumWidth(200)
        self.conf_ui.l_amp.setText("AMP " + self.name)

        self.conf_ui.hs_pos.valueChanged.connect(self.pos_slider_update)
        self.conf_ui.l_pos.editingFinished.connect(self.pos_line_update)

        degree_widget.toggled.connect(self.update_degree_flag)

    @Slot()
    def pos_slider_update(self):
        self.pos = self.conf_ui.hs_pos.value()
        self.update_label(self.conf_ui.l_pos, self.pos)


    @Slot()
    def pos_line_update(self):
        self.pos = int(float(self.conf_ui.l_pos.text()))
        self.update_label(self.conf_ui.l_pos, self.pos)
        self.conf_ui.hs_pos.setValue(self.pos)

    @Slot()
    def update_degree_flag(self, val):
        self.degree_flag = val
        self.update_label(self.conf_ui.l_pos, self.pos)


    def update_label(self, label, value):
        converted = convert_degrees(int(float(value)),self.degree_flag)
        label.setText(str(f'{converted: .2f}'))

        return converted

class CurveWidget(QFrame):

    def __init__(self, parent=None, amp_str : str = "X1" , color = (224,43,51), buffer_size = 0):
        super().__init__(parent=parent)
        self.buffer_size = buffer_size


        self.setFrameShape(QFrame.Shape.Box)
        self.setFrameShadow(QFrame.Shadow.Plain)


        self.layout = QGridLayout(self)
        self.setMaximumHeight(120)

        self.l_amp = QLabel(self)
        self.l_amp.setText("AMP " + amp_str)
        self.l_amp.setFrameShape(QFrame.Shape.Box)
        self.l_amp.setMaximumHeight(20)

        self.pb_pos = QPushButton(self)
        self.pb_pos.setText("Pos")
        self.pb_pos.setCheckable(True)
        self.pb_pos.setFixedSize(40, 30)

        self.pb_spos = QPushButton(self)
        self.pb_spos.setText("SPos")
        self.pb_spos.setCheckable(True)
        self.pb_spos.setFixedSize(40, 30)

        self.pb_current = QPushButton(self)
        self.pb_current.setText("Cur")
        self.pb_current.setCheckable(True)
        self.pb_current.setFixedSize(40, 30)

        self.bg_buttons = QButtonGroup(parent)
        self.bg_buttons.setExclusive(False)
        self.bg_buttons.addButton(self.pb_pos, 0)
        self.bg_buttons.addButton(self.pb_spos, 1)
        self.bg_buttons.addButton(self.pb_current, 2)
        self.bg_buttons.idClicked.connect(self.update_curves)

        self.layout.addWidget(self.l_amp, 0, 0, 1, -1, alignment = Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.pb_pos, 1 ,0)
        self.layout.addWidget(self.pb_spos, 1, 1)
        self.layout.addWidget(self.pb_current, 1, 2)

        self.curve_pos = PlotDataItem(pen = mkPen(color, width=1))
        self.curve_spos = PlotDataItem(pen = mkPen(color, width=1))
        self.curve_current = PlotDataItem(pen = mkPen(color, width=1))

        self.curve_list = (self.curve_pos, self.curve_spos, self.curve_current)

    @Slot()
    def update_curves(self, btn_id):
        if not self.bg_buttons.button(btn_id).isChecked():
            self.curve_list[btn_id].setData(np.zeros(self.buffer_size))

    def update_pos_curve(self, buffer, clear=False):
        if self.pb_pos.isChecked() or clear:
            self.curve_pos.setData(buffer)

    def update_spos_curve(self, buffer, clear=False):
        if self.pb_spos.isChecked() or clear:
            self.curve_spos.setData(buffer)

    def update_current_curve(self, buffer, clear=False):
        if self.pb_current.isChecked() or clear:
            self.curve_current.setData(buffer)


class AMP:
    def __init__(self, parent=None, buffer_size = 64, amp_str : str = "X1", color = (224,43,51), parent2 = None):
        self.pos = 0
        self.current = 0

        self.en = 0
        self.spos = 0
        self.rot_mode = 0

        self.buffer_size = buffer_size

        self.buffer_pos = np.zeros(self.buffer_size)
        self.buffer_spos = np.zeros(self.buffer_size)
        self.buffer_current  = np.zeros(self.buffer_size)

        self.curve = CurveWidget(parent=parent, amp_str = amp_str, color = color, buffer_size=self.buffer_size)

        self.amp_conf = AmpConfWidget(parent2, amp_name=amp_str)

    def add_points(self, pos=0, spos=0, current=0):
        self.pos = pos
        self.current = current
        self.spos = spos

        self.buffer_pos = add_shift_buffer(self.buffer_pos, pos)
        self.buffer_spos = add_shift_buffer(self.buffer_spos, spos)
        self.buffer_current = add_shift_buffer(self.buffer_current, current)

    def clear_buffers(self):
        self.buffer_pos = np.zeros(self.buffer_size)
        self.buffer_spos = np.zeros(self.buffer_size)
        self.buffer_current = np.zeros(self.buffer_size)

    def update_curves(self):
        self.curve.update_pos_curve(self.buffer_pos)
        self.curve.update_spos_curve(self.buffer_spos)
        self.curve.update_current_curve(self.buffer_current)




