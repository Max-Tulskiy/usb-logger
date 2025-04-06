# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.log_table = QTableWidget(self.centralwidget)
        self.log_table.setObjectName(u"log_table")
        self.log_table.setGeometry(QRect(15, 91, 761, 411))
        self.sort_button = QPushButton(self.centralwidget)
        self.sort_button.setObjectName(u"sort_button")
        self.sort_button.setGeometry(QRect(690, 30, 91, 31))
        self.sort_button.setStyleSheet(u"QPushButton {\n"
"border-radius: 5px;\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: white;               \n"
"    background-color: #1c5980;\n"
"}")
        self.filter_button = QPushButton(self.centralwidget)
        self.filter_button.setObjectName(u"filter_button")
        self.filter_button.setGeometry(QRect(490, 30, 81, 31))
        self.filter_button.setStyleSheet(u"QPushButton {\n"
"border-radius: 5px;\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: white;               \n"
"    background-color: #1c5980;\n"
"}")
        self.export_button = QPushButton(self.centralwidget)
        self.export_button.setObjectName(u"export_button")
        self.export_button.setGeometry(QRect(590, 30, 81, 31))
        self.export_button.setStyleSheet(u"QPushButton {\n"
"border-radius: 5px;\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: white;               \n"
"    background-color: #1c5980;\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 31, 17))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 40, 31, 17))
        self.end_date = QDateTimeEdit(self.centralwidget)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setGeometry(QRect(70, 40, 194, 26))
        self.end_date.setStyleSheet(u"")
        self.start_date = QDateTimeEdit(self.centralwidget)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setGeometry(QRect(70, 10, 194, 26))
        self.start_date.setStyleSheet(u"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sort_button.setText(QCoreApplication.translate("MainWindow", u"sort", None))
        self.filter_button.setText(QCoreApplication.translate("MainWindow", u"filter", None))
        self.export_button.setText(QCoreApplication.translate("MainWindow", u"exp2pdf", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"end", None))
    # retranslateUi

