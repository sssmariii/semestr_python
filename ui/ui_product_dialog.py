# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'product_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(939, 692)
        self.name_label = QLabel(Dialog)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(210, 70, 131, 16))
        font = QFont()
        font.setPointSize(14)
        self.name_label.setFont(font)
        self.product_name_edit = QLineEdit(Dialog)
        self.product_name_edit.setObjectName(u"product_name_edit")
        self.product_name_edit.setGeometry(QRect(210, 90, 151, 31))
        self.category_label = QLabel(Dialog)
        self.category_label.setObjectName(u"category_label")
        self.category_label.setGeometry(QRect(430, 70, 91, 16))
        self.category_label.setFont(font)
        self.product_category_combo = QComboBox(Dialog)
        self.product_category_combo.setObjectName(u"product_category_combo")
        self.product_category_combo.setGeometry(QRect(420, 80, 141, 51))
        self.price_label = QLabel(Dialog)
        self.price_label.setObjectName(u"price_label")
        self.price_label.setGeometry(QRect(630, 70, 101, 16))
        self.price_label.setFont(font)
        self.product_price_spin = QDoubleSpinBox(Dialog)
        self.product_price_spin.setObjectName(u"product_price_spin")
        self.product_price_spin.setGeometry(QRect(630, 90, 101, 31))
        self.product_price_spin.setMaximum(100000.000000000000000)
        self.desc_label = QLabel(Dialog)
        self.desc_label.setObjectName(u"desc_label")
        self.desc_label.setGeometry(QRect(210, 150, 81, 16))
        self.desc_label.setFont(font)
        self.product_desc_edit = QTextEdit(Dialog)
        self.product_desc_edit.setObjectName(u"product_desc_edit")
        self.product_desc_edit.setGeometry(QRect(210, 180, 491, 101))
        self.select_image_button = QPushButton(Dialog)
        self.select_image_button.setObjectName(u"select_image_button")
        self.select_image_button.setGeometry(QRect(340, 290, 171, 51))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 430, 58, 16))
        self.image_preview_label = QLabel(Dialog)
        self.image_preview_label.setObjectName(u"image_preview_label")
        self.image_preview_label.setGeometry(QRect(210, 350, 481, 231))
        self.image_preview_label.setMinimumSize(QSize(150, 150))
        self.save_button = QPushButton(Dialog)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(289, 620, 131, 51))
        self.cancel_button = QPushButton(Dialog)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(510, 620, 121, 51))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.name_label.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430:", None))
        self.product_name_edit.setText("")
        self.category_label.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.price_label.setText(QCoreApplication.translate("Dialog", u"\u0426\u0435\u043d\u0430:", None))
        self.desc_label.setText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.select_image_button.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443:", None))
        self.label.setText("")
        self.image_preview_label.setText("")
        self.save_button.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

