import sys
import threading
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from process_usb_dev import monitor_usb, init_db

def main():
    init_db()
    usb_thread = threading.Thread(target=monitor_usb, daemon=True)
    usb_thread.start()
    
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.setFixedSize(800, 600)
    window.setWindowTitle("USB Logger")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
