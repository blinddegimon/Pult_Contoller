from ui_mainwindow import Ui_MainWindow
from control_window import ControlWindow


from PySide6.QtCore import Slot, QIODeviceBase, QTimer, QByteArray
from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton, QMessageBox, QVBoxLayout, QFrame, QSizePolicy, \
    QHBoxLayout, QLineEdit, QCheckBox, QRadioButton, QComboBox, QSpinBox, QSlider, QDial, QGroupBox
from PySide6.QtSerialPort import QSerialPort

from tools import *
import numpy as np
import array
import json


from settingsdialog import SettingsDialog
from plot_window import PlotWindow
from amp import AMP, AmpConfWidget

#QLineEdit, QCheckBox, QComboBox, QRadioButton, QSlider, QSpinBox, QDial
class AppConfig:
    def __init__(self, parent_name = ''):
        self.widgets = {}
        self.widget_dict = {}
        self.file_name = parent_name + '_config_widgets.json'


    def add_widget(self, widget, parent = None):
        if parent is not None:
            widget_group_name =  parent.objectName()
        else:
            widget_group_name = 'def'


        if widget_group_name not in self.widgets:
            self.widgets[widget_group_name] = {}
            self.widget_dict[widget_group_name] = {}

        self.widgets[widget_group_name][widget.objectName()] = widget



    def save_widgets(self):
        print(self.widgets)
        print(self.widget_dict)
        for parent, configs in self.widgets.items():
            for name, widget in configs.items():
                match = self.match_widget(widget)
                self.widget_dict[parent][match[0]] = match[1]

        with open(self.file_name, 'w', encoding='utf-8') as f:
            json.dump(self.widget_dict, f, ensure_ascii=False, indent=4)

    def load_widgets(self):
        load = False
        try:
            with open(self.file_name, 'r+', encoding='utf-8') as f:
                temp = json.load(f)
                if not len(temp) == 0:
                    load = True
                    self.widget_dict = temp
        except:
            pass

        if load:
            for parent, config in self.widget_dict.items():
                for name, value in config.items():
                    self.write_widget(self.widgets[parent][name], value)

    @staticmethod
    def match_widget(widget):
        key = ""
        value = ""
        key = widget.objectName()
        match widget:
            case QLineEdit():
                value = widget.text()
                #print("QLineEdit")
            case QCheckBox() | QRadioButton() | QPushButton():
                value = widget.isChecked()
                #print("QCheckBox")
            case QComboBox():
                value = widget.currentIndex()
                #print("QComboBox")
            case QSpinBox() | QSlider() | QDial():
                value = widget.value()
            case _:
                print("something went wrong")

        return key, value

    @staticmethod
    def write_widget(widget, value):

        match widget:
            case QLineEdit():
                widget.setText(value)
                #print("QLineEdit: ", value)
            case QCheckBox() | QRadioButton() | QPushButton():
                widget.setChecked(value)
                #print("QCheckBox")
            case QComboBox():
                widget.setCurrentIndex(value)
                #print("QComboBox")
            case QSpinBox() | QSlider() | QDial():
                widget.setValue(value)
            case _:
                print("bad Qwidget: " + str(widget))

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.pps = 0
        self.prev_pps = 0

        self.tx_buffer = [0 for _ in range(64)]

        self.m_ui = Ui_MainWindow()
        self.m_settings = SettingsDialog(self)
        self.m_status = QLabel()
        self.m_pps = QLabel()
        self.m_serial = QSerialPort(self)
        self.m_ui.setupUi(self)
        self.m_plot = PlotWindow(self.m_ui.f_plot)



        self.ampx1 = AMP(parent=self.m_ui.f_plot, parent2=self.m_ui.f_ampConf, buffer_size=BUFFER_SIZE, amp_str="X1", color=(7,41,84))
        self.ampx2 = AMP(parent=self.m_ui.f_plot, parent2=self.m_ui.f_ampConf, buffer_size=BUFFER_SIZE, amp_str="X2", color=(224,43,51))
        self.ampy1 = AMP(parent=self.m_ui.f_plot, parent2=self.m_ui.f_ampConf, buffer_size=BUFFER_SIZE, amp_str="Y1", color=(240,197,113))
        self.ampy2 = AMP(parent=self.m_ui.f_plot, parent2=self.m_ui.f_ampConf, buffer_size=BUFFER_SIZE, amp_str="Y2", color=(89,168,155))

        self.m_plot.add_compose_curve(self.ampx1.curve)
        self.m_plot.add_compose_curve(self.ampx2.curve)
        self.m_plot.add_compose_curve(self.ampy1.curve)
        self.m_plot.add_compose_curve(self.ampy2.curve)

        self.m_control = ControlWindow(self.m_ui.f_control, self.m_ui.actionDEG)


        self.m_ui.f_control.setFixedSize(250, 250)

        self.amp_conf_layout = QHBoxLayout(self.m_ui.f_ampConf)
        self.ampx1.amp_conf.setup()
        self.amp_conf_layout.addWidget(self.ampx1.amp_conf)
        self.ampx2.amp_conf.setup()
        self.amp_conf_layout.addWidget(self.ampx2.amp_conf)
        self.ampy1.amp_conf.setup()
        self.amp_conf_layout.addWidget(self.ampy1.amp_conf)
        self.ampy2.amp_conf.setup()
        self.amp_conf_layout.addWidget(self.ampy2.amp_conf)


        self.m_ui.statusbar.addWidget(self.m_status)
        self.m_ui.statusbar.addWidget(self.m_pps)


        self.app_config = AppConfig(parent_name="app_config")

        self.app_config.add_widget(self.m_control.rb_1ChMode, self.m_ui.f_control)
        self.app_config.add_widget(self.m_control.rb_2ChMode, self.m_ui.f_control)
        self.app_config.add_widget(self.m_control.rb_4ChMode, self.m_ui.f_control)
        self.app_config.add_widget(self.m_control.vs_y, self.m_ui.f_control)
        self.app_config.add_widget(self.m_control.hs_x, self.m_ui.f_control)


        self.app_config.add_widget(self.ampx1.amp_conf.conf_ui.pb_en, self.ampx1.amp_conf)
        self.app_config.add_widget(self.ampx1.amp_conf.conf_ui.l_pos, self.ampx1.amp_conf)
        self.app_config.add_widget(self.ampx1.amp_conf.conf_ui.hs_pos, self.ampx1.amp_conf)

        self.app_config.add_widget(self.ampx2.amp_conf.conf_ui.pb_en, self.ampx2.amp_conf)
        self.app_config.add_widget(self.ampx2.amp_conf.conf_ui.l_pos, self.ampx2.amp_conf)
        self.app_config.add_widget(self.ampx2.amp_conf.conf_ui.hs_pos, self.ampx2.amp_conf)

        self.app_config.add_widget(self.ampy1.amp_conf.conf_ui.pb_en, self.ampy1.amp_conf)
        self.app_config.add_widget(self.ampy1.amp_conf.conf_ui.l_pos, self.ampy1.amp_conf)
        self.app_config.add_widget(self.ampy1.amp_conf.conf_ui.hs_pos, self.ampy1.amp_conf)

        self.app_config.add_widget(self.ampy2.amp_conf.conf_ui.pb_en, self.ampy2.amp_conf)
        self.app_config.add_widget(self.ampy2.amp_conf.conf_ui.l_pos, self.ampy2.amp_conf)
        self.app_config.add_widget(self.ampy2.amp_conf.conf_ui.hs_pos, self.ampy2.amp_conf)


        self.app_config.load_widgets()
        self.m_control.update_mode()

        #Frame Config connections
        self.tx_timer = QTimer()
        self.tx_timer.setInterval(200)
        self.tx_timer.timeout.connect(self.update_tx_timer)
        self.m_control.pb_tx.clicked.connect(self.start_stop_tx_timer)


        self.m_ui.actionConnect.triggered.connect(self.open_serial_port)
        self.m_ui.actionDisconnect.triggered.connect(self.close_serial_port)
        self.m_ui.actionConnect.setEnabled(True)
        self.m_ui.actionDisconnect.setEnabled(False)

        self.m_ui.actionConfigure.triggered.connect(self.m_settings.show)
        self.m_ui.actionClear.triggered.connect(self.clear_curves)
        self.m_ui.actionDEG.triggered.connect(self.update_degree_flag)

        self.m_serial.errorOccurred.connect(self.handle_error)
        self.m_serial.readyRead.connect(self.read_data)

        self.pps_timer = QTimer()
        self.pps_timer.start(500)
        self.pps_timer.timeout.connect(self.update_pps_timer)

        self.plot_timer = QTimer()
        self.plot_timer.start(16)
        self.plot_timer.timeout.connect(self.update_plot_timer)

    @Slot()
    def update_pps_timer(self):
        self.m_pps.setText(str(self.pps*2)+"sps")
        self.prev_pps = self.pps
        self.pps = 0

    @Slot()
    def update_plot_timer(self):
        self.ampx1.update_curves()
        self.ampx2.update_curves()
        self.ampy1.update_curves()
        self.ampy2.update_curves()

    @Slot()
    def start_stop_tx_timer(self, btn):
        if btn:
            self.tx_timer.start()
        else:
            self.tx_timer.stop()

    @Slot()
    def update_tx_timer(self):
        self.send_data()

    @Slot()
    def update_degree_flag(self, action):
        pass
        #_degree_flag = action

        #self.vs_y_update()
        #self.hs_x_update()



    @Slot()
    def read_data(self):
        self.pps += 1
        buffer_temp = np.array(array.array('h', bytes(self.m_serial.readAll())))

        buffer_temp[2] = convert_degrees(buffer_temp[2])



        if not self.m_ui.actionPause.isChecked():
            self.ampx1.add_points(buffer_temp[1],float(self.m_control.x_disp), buffer_temp[3])
            self.ampx2.add_points(buffer_temp[1], -float(self.m_control.x_disp), buffer_temp[3])
            self.ampy1.add_points(buffer_temp[1], float(self.m_control.y_disp), buffer_temp[3])
            self.ampy2.add_points(buffer_temp[1], -float(self.m_control.y_disp), buffer_temp[3])

    def send_data(self):
        self.tx_buffer[0] = 0x7a7a
        self.tx_buffer[1] = int(self.m_control.vs_y.value())




        print(self.tx_buffer)

        buffer = QByteArray(to_b16t(self.tx_buffer))
        self.m_serial.write(buffer)


    @Slot()
    def clear_curves(self):
        self.ampx1.clear_buffers()
        self.ampx2.clear_buffers()
        self.ampy1.clear_buffers()
        self.ampy2.clear_buffers()

        self.ampx1.update_curves()
        self.ampx2.update_curves()
        self.ampy1.update_curves()
        self.ampy2.update_curves()



    @Slot()
    def open_serial_port(self):
        s = self.m_settings.settings()
        self.m_serial.setPortName(s.name)
        self.m_serial.setBaudRate(s.baud_rate)
        self.m_serial.setDataBits(s.data_bits)
        self.m_serial.setParity(s.parity)
        self.m_serial.setStopBits(s.stop_bits)
        self.m_serial.setFlowControl(s.flow_control)
        self.m_serial.setReadBufferSize(12)
        if self.m_serial.open(QIODeviceBase.OpenModeFlag.ReadWrite):
            #self.m_console.setEnabled(True)
            #self.m_console.set_local_echo_enabled(s.local_echo_enabled)
            self.m_ui.actionConnect.setEnabled(False)
            self.m_ui.actionDisconnect.setEnabled(True)
            self.m_ui.actionConfigure.setEnabled(False)
            self.show_status_message(description(s))
        else:
            QMessageBox.critical(self, "Error", self.m_serial.errorString())
            self.show_status_message("Open error")


    @Slot()
    def close_serial_port(self):
        if self.m_serial.isOpen():
            self.m_serial.close()
        self.m_ui.actionConnect.setEnabled(True)
        self.m_ui.actionDisconnect.setEnabled(False)
        self.m_ui.actionConfigure.setEnabled(True)
        self.show_status_message("Disconnected")

    @Slot(str)
    def show_status_message(self, message):
        self.m_status.setText(message)

    @Slot(QSerialPort.SerialPortError)
    def handle_error(self, error):
        if error == QSerialPort.SerialPortError.ResourceError:
            QMessageBox.critical(self, "Critical Error",
                                 self.m_serial.errorString())
            self.close_serial_port()

    def closeEvent(self, event):
        self.app_config.save_widgets()

