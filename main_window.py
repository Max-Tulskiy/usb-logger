import pytz
import sqlite3
from datetime import datetime
from ui.window import Ui_MainWindow
from report import create_pdf_report
from PySide6.QtCore import QTimer, QDateTime
from PySide6.QtWidgets import (
    QMainWindow, 
    QTableWidgetItem, 
    QHeaderView, 
    QFileDialog
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_data()

        self.sorting_active = False
        self.filtering_active = False
        self.last_event_count = self.get_event_count()

        utc_now = datetime.now(pytz.utc)
        moscow_now = utc_now.astimezone(pytz.timezone("Europe/Moscow"))
        date_time = QDateTime.fromString(moscow_now.strftime('%Y-%m-%d %H:%M:%S'), "yyyy-MM-dd HH:mm:ss")  

        self.ui.end_date.setDateTime(date_time)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.conditional_update)
        self.timer.start(2000)

        self.ui.sort_button.clicked.connect(self.sort_by_time)
        self.ui.filter_button.clicked.connect(self.filter_by_date_range)
        self.ui.export_button.clicked.connect(self.export_to_pdf)

    def get_event_count(self):
        conn = sqlite3.connect("usb_devices.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM usb_events")
        count = cursor.fetchone()[0]
        conn.close()
        return count

    def conditional_update(self):
        current_count = self.get_event_count()
        if not self.sorting_active and not self.filtering_active:
            if current_count > self.last_event_count:
                self.load_data()
                self.last_event_count = current_count

    def load_data(self, order_by="timestamp", start_time=None, end_time=None):
        conn = sqlite3.connect("usb_devices.db")
        cursor = conn.cursor()
        query = "SELECT id, device_id, action, timestamp FROM usb_events"
        params = []
       
        if start_time and end_time:
            query += " WHERE timestamp BETWEEN ? AND ?"
            params.extend([start_time, end_time])
        query += f" ORDER BY {order_by}"
        cursor.execute(query, params)
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

    def filter_by_date_range(self):
        self.filtering_active = True  

        start = self.ui.start_date.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        end = self.ui.end_date.dateTime().toString("yyyy-MM-dd HH:mm:ss")

        self.load_data(start_time=start, end_time=end)

    def export_to_pdf(self):
        conn = sqlite3.connect("usb_devices.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, device_id, action, timestamp FROM usb_events ORDER BY timestamp")
        data = cursor.fetchall()
        conn.close()

        path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "report.pdf", "PDF Files (*.pdf)")
        if path:
            create_pdf_report(data, path)