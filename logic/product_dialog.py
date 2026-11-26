import os
import shutil
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from ui.ui_product_dialog import Ui_Dialog
from logic.database import DatabaseManager


class ProductDialog(QDialog):
    """Диалоговое окно для добавления и редактирования товара."""

    def __init__(self, db: DatabaseManager, product_id=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # Устанавливаем заголовок окна по умолчанию
        self.setWindowTitle("Добавить товар")
        
        self.db = db
        self.product_id = product_id  
        self.selected_image_path = None  

        # Заполняем категории
        self.load_categories()

        # Подключаем кнопки
        self.ui.select_image_button.clicked.connect(self.select_image)
        self.ui.save_button.clicked.connect(self.save_product)
        self.ui.cancel_button.clicked.connect(self.reject)

        # Если передан ID, значит это редактирование
        if self.product_id is not None:
            self.setWindowTitle("Редактировать товар")
            self.load_product_data()

    def load_categories(self):
        """Загружает категории в выпадающий список."""
        categories = self.db.get_categories()
        for cat_id, cat_name in categories:
            self.ui.product_category_combo.addItem(cat_name, cat_id)

    def load_product_data(self):
        """Заполняет форму данными существующего товара."""
        products = self.db.get_all_products()
        for prod in products:
            if prod[0] == self.product_id:
                self.ui.product_name_edit.setText(prod[1])
                self.ui.product_price_spin.setValue(prod[3])
                self.ui.product_desc_edit.setText(prod[4] or "")
                
                # Устанавливаем категорию
                cat_name = prod[2]
                index = self.ui.product_category_combo.findText(cat_name)
                if index >= 0:
                    self.ui.product_category_combo.setCurrentIndex(index)
                
                # Устанавливаем картинку, если есть
                if prod[5]:
                    self.selected_image_path = prod[5]
                    self.show_image_preview(prod[5])
                break

    def select_image(self):
        """Открывает стандартный диалог выбора файла и копирует картинку в проект."""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выбрать картинку", "", "Images (*.png *.jpg *.jpeg)"
        )
        if file_path:
            # Создаем папку assets/images, если её нет
            images_dir = os.path.join("assets", "images")
            if not os.path.exists(images_dir):
                os.makedirs(images_dir)
            
            # Копируем файл в нашу папку, чтобы картинка не потерялась
            filename = os.path.basename(file_path)
            new_path = os.path.join(images_dir, filename)
            shutil.copy(file_path, new_path)
            
            # Сохраняем относительный путь для базы
            self.selected_image_path = new_path
            self.show_image_preview(new_path)


    def show_image_preview(self, image_path):
        """Отображает картинку в QLabel, заполняя всё пространство."""
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            self.ui.image_preview_label.setPixmap(pixmap.scaled(
                self.ui.image_preview_label.size(), 
                Qt.AspectRatioMode.IgnoreAspectRatio, 
                Qt.TransformationMode.SmoothTransformation
            ))

    def save_product(self):
        """Сохраняет товар в базу."""
        # Получаем данные из полей
        name = self.ui.product_name_edit.text().strip()
        category_id = self.ui.product_category_combo.currentData()
        price = self.ui.product_price_spin.value()
        description = self.ui.product_desc_edit.toPlainText().strip()

        # Валидация 
        if not name:
            QMessageBox.warning(self, "Ошибка", "Введите название товара!")
            return
        if category_id is None:
            QMessageBox.warning(self, "Ошибка", "Выберите категорию!")
            return

        # Записываем в базу
        if self.product_id is None:
            # Добавление нового
            self.db.add_product(name, category_id, price, description, self.selected_image_path)
        else:
            # Обновление существующего
            self.db.update_product(self.product_id, name, category_id, price, description, self.selected_image_path)

        self.accept() 