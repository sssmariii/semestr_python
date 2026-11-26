import os
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from ui.ui_product_view import Ui_Dialog
from logic.database import DatabaseManager


class ProductView(QDialog):
    """Окно просмотра карточки товара."""

    def __init__(self, db: DatabaseManager, product_data: tuple, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.db = db
        # product_data = (id, name, category_name, price, description, image_path, is_favorite)
        self.product_id = product_data[0]
        
        # Заполняем данные
        self.ui.product_name_label.setText(product_data[1])
        self.ui.product_category_label.setText(f"Категория: {product_data[2]}")
        self.ui.product_price_label.setText(f"Цена: {product_data[3]} руб.")
        
        # Описание 
        desc = product_data[4] if product_data[4] else ""
        self.ui.product_description_edit.setText(desc)
        
        # Загружаем картинку
        image_path = product_data[5]
        self.load_image(image_path)
        
        # Подключаем кнопки
        self.ui.close_button.clicked.connect(self.close)
        self.ui.favorite_button.clicked.connect(self.toggle_favorite)

        # Меняем текст кнопки избранного в зависимости от статуса
        if product_data[6] == 1:
            self.ui.favorite_button.setText("Убрать из избранного")
        else:
            self.ui.favorite_button.setText("В избранное")

    def load_image(self, image_path):
        """Загружает картинку в QLabel, заполняя всё пространство."""
        if image_path and os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            # IgnoreAspectRatio растягивает картинку на весь QLabel
            self.ui.product_image_label.setPixmap(pixmap.scaled(
                self.ui.product_image_label.size(),
                Qt.AspectRatioMode.IgnoreAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))
        else:
            # Если картинки нет, просто очищаем Label 
            self.ui.product_image_label.clear()

    def toggle_favorite(self):
        """Переключает статус избранного прямо из карточки."""
        self.db.toggle_favorite(self.product_id)
        
        # Меняем текст на кнопке, чтобы пользователь видел результат
        if self.ui.favorite_button.text() == "В избранное":
            self.ui.favorite_button.setText("Убрать из избранного")
        else:
            self.ui.favorite_button.setText("В избранное")