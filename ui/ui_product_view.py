# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'product_view.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(939, 692)
        self.product_image_label = QLabel(Dialog)
        self.product_image_label.setObjectName(u"product_image_label")
        self.product_image_label.setGeometry(QRect(140, 109, 481, 481))
        self.product_image_label.setMinimumSize(QSize(300, 300))
        self.product_image_label.setFrameShape(QFrame.Shape.Box)
        self.product_name_label = QLabel(Dialog)
        self.product_name_label.setObjectName(u"product_name_label")
        self.product_name_label.setGeometry(QRect(140, 60, 341, 61))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.product_name_label.setFont(font)
        self.product_category_label = QLabel(Dialog)
        self.product_category_label.setObjectName(u"product_category_label")
        self.product_category_label.setGeometry(QRect(630, 340, 351, 61))
        font1 = QFont()
        font1.setPointSize(18)
        self.product_category_label.setFont(font1)
        self.product_category_label.setStyleSheet(u"")
        self.product_price_label = QLabel(Dialog)
        self.product_price_label.setObjectName(u"product_price_label")
        self.product_price_label.setGeometry(QRect(630, 380, 261, 61))
        self.product_price_label.setFont(font1)
        self.product_description_edit = QTextEdit(Dialog)
        self.product_description_edit.setObjectName(u"product_description_edit")
        self.product_description_edit.setGeometry(QRect(630, 450, 361, 141))
        self.product_description_edit.setReadOnly(True)
        self.favorite_button = QPushButton(Dialog)
        self.favorite_button.setObjectName(u"favorite_button")
        self.favorite_button.setGeometry(QRect(180, 600, 161, 51))
        self.close_button = QPushButton(Dialog)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(400, 600, 171, 51))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.product_image_label.setText("")
        self.product_name_label.setText("")
        self.product_category_label.setText("")
        self.product_price_label.setText("")
        self.favorite_button.setText(QCoreApplication.translate("Dialog", u"\u0412 \u0438\u0437\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.close_button.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

