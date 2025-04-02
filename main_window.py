import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PySide6.QtCore import QTimer
from ui.window import Ui_MainWindow
from process_usb_dev import init_db

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        init_db()
        self.load_data()
        self.ui.sort_button.clicked.connect(self.sort_by_time)

        self.sorting_active = False
        self.last_event_count = self.get_event_count()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.conditional_update)
        self.timer.start(2000)

    def get_event_count(self):
        conn = sqlite3.connect("usb_devices.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM usb_events")
        count = cursor.fetchone()[0]
        conn.close()
        return count

    def conditional_update(self):
        current_count = self.get_event_count()
        if not self.sorting_active or current_count > self.last_event_count:
            self.load_data()
            self.last_event_count = current_count

    def load_data(self, order_by="timestamp"):
        conn = sqlite3.connect("usb_devices.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, device_id, action, timestamp FROM usb_events ORDER BY {order_by}")
        rows = cursor.fetchall()
        conn.close()

        self.ui.log_table.setRowCount(len(rows))
        self.ui.log_table.setColumnCount(4)
        self.ui.log_table.setHorizontalHeaderLabels(["ID", "Device ID", "Action", "Timestamp"])

        for row_idx, row in enumerate(rows):
            for col_idx, item in enumerate(row):
                self.ui.log_table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))

        header = self.ui.log_table.horizontalHeader()
        
        for column in range(self.ui.log_table.columnCount()):
            header.setSectionResizeMode(column, QHeaderView.Stretch)

    def sort_by_time(self):
        self.sorting_active = True
        self.load_data(order_by="timestamp DESC")
