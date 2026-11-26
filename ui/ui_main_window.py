# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(831, 600)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.search_line_edit = QLineEdit(self.centralwidget)
        self.search_line_edit.setObjectName(u"search_line_edit")
        self.search_line_edit.setGeometry(QRect(500, 80, 201, 21))
        self.category_combo_box = QComboBox(self.centralwidget)
        self.category_combo_box.setObjectName(u"category_combo_box")
        self.category_combo_box.setGeometry(QRect(170, 60, 211, 61))
        self.add_button = QPushButton(self.centralwidget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(110, 420, 151, 51))
        self.edit_button = QPushButton(self.centralwidget)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setGeometry(QRect(280, 420, 151, 51))
        self.delete_button = QPushButton(self.centralwidget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(630, 420, 171, 51))
        self.status_label = QLabel(self.centralwidget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(390, 490, 301, 41))
        font = QFont()
        font.setPointSize(13)
        self.status_label.setFont(font)
        self.favorite_button = QPushButton(self.centralwidget)
        self.favorite_button.setObjectName(u"favorite_button")
        self.favorite_button.setGeometry(QRect(450, 420, 161, 51))
        self.products_table_widget = QTableWidget(self.centralwidget)
        if (self.products_table_widget.columnCount() < 4):
            self.products_table_widget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.products_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.products_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.products_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.products_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.products_table_widget.setObjectName(u"products_table_widget")
        self.products_table_widget.setGeometry(QRect(110, 120, 691, 291))
        self.products_table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.products_table_widget.horizontalHeader().setDefaultSectionSize(170)
        self.products_table_widget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.products_table_widget.horizontalHeader().setStretchLastSection(True)
        self.products_table_widget.verticalHeader().setVisible(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(550, 50, 91, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 50, 81, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 831, 36))
        MainWindow.setMenuBar(self.menuBar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.edit_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
        self.favorite_button.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0438\u0437\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        ___qtablewidgetitem = self.products_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u2116", None))
        ___qtablewidgetitem1 = self.products_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0432\u0430\u0440", None))
        ___qtablewidgetitem2 = self.products_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        ___qtablewidgetitem3 = self.products_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

