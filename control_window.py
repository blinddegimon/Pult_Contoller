from ui_control import Ui_ControlWindow
from PySide6.QtCore import Slot

from tools import *

class ControlWindow(Ui_ControlWindow):
    def __init__(self, parent = None, degree_widget = None):
        self.setupUi(parent)
        self.degree_flag = False

        self.x = 0
        self.y = 0

        self.x_disp = 0
        self.y_disp = 0

        self.l_y.setText(str(self.y))
        self.l_x.setText(str(self.x))

        self.vs_y.setValue(int(self.y))
        self.hs_x.setValue(int(self.x))

        degree_widget.toggled.connect(self.update_degree_flag)

        self.vs_y.valueChanged.connect(self.vs_y_update)
        self.hs_x.valueChanged.connect(self.hs_x_update)

        self.d_xy.valueChanged.connect(self.d_xy_update)


        self.rb_1ChMode.clicked.connect(self.mode_1ch)
        self.rb_2ChMode.clicked.connect(self.mode_2ch)
        self.rb_4ChMode.clicked.connect(self.mode_4ch)

        self.l_y.editingFinished.connect(self.update_y)
        self.l_x.editingFinished.connect(self.update_x)

    def update_label(self, label, value):
        converted = convert_degrees(int(value),self.degree_flag)
        label.setText(str(f'{converted: .2f}'))

        return converted

    @Slot()
    def vs_y_update(self):
        self.y_disp = self.update_label(self.l_y, self.vs_y.value())
        self.y = self.vs_y.value()

    @Slot()
    def hs_x_update(self):
       self.x_disp = self.update_label(self.l_x, self.hs_x.value())
       self.x = self.hs_x.value()

    @Slot()
    def update_y(self):
        self.y = self.l_y.text()
        self.y_disp = self.update_label(self.l_y, self.y)
        self.vs_y.setValue(int(self.y))

    @Slot()
    def update_x(self):
        self.x = self.l_x.text()
        self.x_disp = self.update_label(self.l_x, self.x)
        self.hs_x.setValue(int(self.x))

    @Slot()
    def d_xy_update(self, val):
        self.y = np.cos((val / 2730) * np.pi) * 2730
        self.x = np.sin((val/2730) * np.pi) * 2730

        self.y_disp = self.update_label(self.l_y, self.y)
        self.x_disp = self.update_label(self.l_x, self.x)

        self.vs_y.setValue(int(self.y))
        self.hs_x.setValue(int(self.x))

    @Slot()
    def update_degree_flag(self, val):
        self.degree_flag = val

        self.vs_y_update()
        self.hs_x_update()

    @Slot()
    def mode_4ch(self):
        self.vs_y.setEnabled(False)
        self.hs_x.setEnabled(False)

        self.d_xy.setEnabled(False)

    @Slot()
    def mode_2ch(self):
        self.vs_y.setEnabled(True)
        self.hs_x.setEnabled(True)

        self.d_xy.setEnabled(False)

    @Slot()
    def mode_1ch(self):
        self.vs_y.setEnabled(False)
        self.hs_x.setEnabled(False)

        self.d_xy.setEnabled(True)


    def update_mode(self):
        print(self.rb_4ChMode.isChecked())
        if self.rb_1ChMode.isChecked():
            self.mode_1ch()
        elif self.rb_2ChMode.isChecked():
            self.mode_2ch()
        elif self.rb_4ChMode.isChecked():
            self.mode_4ch()
        else:
            pass


