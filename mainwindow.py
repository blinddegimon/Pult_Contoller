from ui_mainwindow import Ui_MainWindow

from PySide6.QtCore import Slot, QIODeviceBase, QTimer
from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton, QMessageBox, QVBoxLayout, QFrame, QSizePolicy
from PySide6.QtSerialPort import QSerialPort


import numpy as np
import array

from settingsdialog import SettingsDialog
from plot_window import PlotWindow
from amp import AMP, add_shift_buffer

BUFFER_SIZE = 2000

def description(s):
    return (f"Connected to {s.name} : {s.string_baud_rate}, "
            f"{s.string_data_bits}, {s.string_parity}, {s.string_stop_bits}, "
            f"{s.string_flow_control}")

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.pps = 0
        self.prev_pps = 0

        self.m_ui = Ui_MainWindow()
        self.m_settings = SettingsDialog(self)
        self.m_status = QLabel()
        self.m_pps = QLabel()
        self.m_serial = QSerialPort(self)
        self.m_ui.setupUi(self)


        self.m_ui.f_control.setFixedSize(250,250)

        self.m_plot = PlotWindow(self.m_ui.f_plot)



        self.ampx1 = AMP(parent=self.m_ui.f_plot, buffer_size=BUFFER_SIZE, amp_str="X1", color=(7,41,84))
        self.ampx2 = AMP(parent=self.m_ui.f_plot, buffer_size=BUFFER_SIZE, amp_str="X2", color=(224,43,51))
        self.ampy1 = AMP(parent=self.m_ui.f_plot, buffer_size=BUFFER_SIZE, amp_str="Y1", color=(240,197,113))
        self.ampy2 = AMP(parent=self.m_ui.f_plot, buffer_size=BUFFER_SIZE, amp_str="Y2", color=(89,168,155))

        self.m_plot.add_compose_curve(self.ampx1.curve)
        self.m_plot.add_compose_curve(self.ampx2.curve)
        self.m_plot.add_compose_curve(self.ampy1.curve)
        self.m_plot.add_compose_curve(self.ampy2.curve)





        self.m_ui.statusbar.addWidget(self.m_status)
        self.m_ui.statusbar.addWidget(self.m_pps)

        self.m_ui.actionConnect.triggered.connect(self.open_serial_port)
        self.m_ui.actionDisconnect.triggered.connect(self.close_serial_port)
        self.m_ui.actionConnect.setEnabled(True)
        self.m_ui.actionDisconnect.setEnabled(False)

        self.m_ui.actionConfigure.triggered.connect(self.m_settings.show)
        self.m_ui.actionClear.triggered.connect(self.clear_curves)

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
    def read_data(self):
        self.pps += 1
        buffer_temp = np.array(array.array('h', bytes(self.m_serial.readAll())))

        if not self.m_ui.actionPause.isChecked():
            self.ampx1.add_points(buffer_temp[1],buffer_temp[2], buffer_temp[3])
            self.ampx2.add_points(buffer_temp[1], buffer_temp[2], buffer_temp[3])
            self.ampy1.add_points(buffer_temp[1], buffer_temp[2], buffer_temp[3])
            self.ampy2.add_points(buffer_temp[1], buffer_temp[2], buffer_temp[3])




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