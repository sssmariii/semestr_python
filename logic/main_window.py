import sys
import os
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QMenu
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QFont

# Импортируем сгенерированный интерфейс и базу данных
from ui.ui_main_window import Ui_MainWindow
from logic.database import DatabaseManager

# Импортируем формы 
from logic.product_dialog import ProductDialog
from logic.product_view import ProductView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Подключаем базу данных
        self.db = DatabaseManager()
        
        # Загружаем данные в интерфейс при старте
        self.load_categories()
        self.load_products()
        
        # Подключаем кнопки к функциям (обработчики событий)
        self.ui.add_button.clicked.connect(self.on_add_clicked)
        self.ui.delete_button.clicked.connect(self.on_delete_clicked)
        self.ui.favorite_button.clicked.connect(self.on_favorite_clicked)
        self.ui.edit_button.clicked.connect(self.on_edit_clicked)
        self.ui.category_combo_box.currentIndexChanged.connect(self.on_category_changed)
        
        # Подключаем поиск (по таблице)
        self.ui.search_line_edit.textChanged.connect(self.on_search_changed)

        # Обработка двойного клика по ТАБЛИЦЕ
        self.ui.products_table_widget.doubleClicked.connect(self.on_item_double_clicked)

        # Обработка клавиши Delete
        self.ui.products_table_widget.installEventFilter(self)

        # Обработка правого клика мыши
        self.ui.products_table_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.products_table_widget.customContextMenuRequested.connect(self.show_context_menu)

    def eventFilter(self, source, event):
        """Перехватывает нажатия клавиш, когда фокус на таблице."""
        if source == self.ui.products_table_widget and event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Delete:
                self.on_delete_clicked()
                return True
        return super().eventFilter(source, event)

    def show_context_menu(self, pos):
        """Обработка нажатия правой кнопки мыши по таблице."""
        index = self.ui.products_table_widget.indexAt(pos)
        if index.isValid():
            menu = QMenu()
            menu.addAction("В избранное", self.on_favorite_clicked)
            menu.addAction("Удалить", self.on_delete_clicked)
            menu.exec(self.ui.products_table_widget.mapToGlobal(pos))

    def load_categories(self):
        """Заполняет выпадающий список категориями из БД."""
        self.ui.category_combo_box.clear()
        self.ui.category_combo_box.addItem("Все категории", 0)
        
        categories = self.db.get_categories()
        for cat_id, cat_name in categories:
            self.ui.category_combo_box.addItem(cat_name, cat_id)

    def load_products(self, category_id=0):
        """Загружает товары в таблицу и выводит статистику."""
        self.ui.products_table_widget.setRowCount(0) # Очищаем таблицу
        
        if category_id == 0:
            products = self.db.get_all_products()
        else:
            products = self.db.get_products_by_category(category_id)

        # Растягиваем последний столбец (Цена) на всё оставшееся место
        self.ui.products_table_widget.horizontalHeader().setStretchLastSection(True)
        
        # Настраиваем ширину колонок
        self.ui.products_table_widget.setColumnWidth(0, 40)  # №
        self.ui.products_table_widget.setColumnWidth(1, 250) # Товар
        self.ui.products_table_widget.setColumnWidth(2, 200) # Категория
        self.ui.products_table_widget.setColumnWidth(3, 150) # Цена
            
        for row, prod in enumerate(products):
            prod_id, name, cat_name, price, desc, img, is_fav = prod
            
            self.ui.products_table_widget.insertRow(row)
            
            prefix = "⭐ " if is_fav == 1 else ""
            
            # Создаем ячейки
            item_num = QTableWidgetItem(str(row + 1))
            item_name = QTableWidgetItem(prefix + name)
            item_name.setData(Qt.ItemDataRole.UserRole, prod_id) # Скрытый ID
            item_cat = QTableWidgetItem(cat_name)
            item_price = QTableWidgetItem(f"{price} руб.")
            
            # Шрифт
            font = QFont()
            font.setPointSize(13)
            item_num.setFont(font)
            item_name.setFont(font)
            item_cat.setFont(font)
            item_price.setFont(font)
            
            # Запрещаем редактировать вручную
            item_num.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
            item_name.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
            item_cat.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
            item_price.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
            
            # Вставляем
            self.ui.products_table_widget.setItem(row, 0, item_num)
            self.ui.products_table_widget.setItem(row, 1, item_name)
            self.ui.products_table_widget.setItem(row, 2, item_cat)
            self.ui.products_table_widget.setItem(row, 3, item_price)

        #  СТАТИСТИКА 
        total = self.ui.products_table_widget.rowCount()
        self.ui.status_label.setText(f"Всего товаров: {total}")

    def on_search_changed(self, text):
        """Фильтрует таблицу по введенному тексту."""
        search_text = text.strip().lower()
        
        for i in range(self.ui.products_table_widget.rowCount()):
            item = self.ui.products_table_widget.item(i, 1) # Ищем по столбцу "Товар"
            if item:
                if not search_text or search_text in item.text().lower():
                    self.ui.products_table_widget.setRowHidden(i, False)
                else:
                    self.ui.products_table_widget.setRowHidden(i, True)

    def on_category_changed(self, index):
        """Срабатывает при смене категории в фильтре."""
        cat_id = self.ui.category_combo_box.itemData(index)
        self.load_products(cat_id)

    def on_add_clicked(self):
        """Открывает диалог добавления товара."""
        dialog = ProductDialog(self.db, parent=self)
        if dialog.exec():
            self.load_products()
            self.ui.status_label.setText("Товар успешно добавлен")

    def on_edit_clicked(self):
        """Открывает диалог редактирования выбранного товара."""
        current_row = self.ui.products_table_widget.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите товар для редактирования!")
            return
        
        prod_id = self.ui.products_table_widget.item(current_row, 1).data(Qt.ItemDataRole.UserRole)
        dialog = ProductDialog(self.db, product_id=prod_id, parent=self)
        if dialog.exec():
            self.load_products()
            self.ui.status_label.setText("Товар обновлен")

    def on_delete_clicked(self):
        """Кнопка Удалить."""
        current_row = self.ui.products_table_widget.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Ошибка", "Сначала выберите товар из списка!")
            return
            
        prod_id = self.ui.products_table_widget.item(current_row, 1).data(Qt.ItemDataRole.UserRole)
        name = self.ui.products_table_widget.item(current_row, 1).text()
        
        reply = QMessageBox.question(
            self, "Удаление", f"Удалить товар '{name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            # --- УДАЛЕНИЕ КАРТИНКИ С ДИСКА ---
            all_products = self.db.get_all_products()
            for prod in all_products:
                if prod[0] == prod_id:
                    img_path = prod[5]
                    if img_path and os.path.exists(img_path):
                        try:
                            os.remove(img_path)
                        except Exception as e:
                            print(f"Не удалось удалить файл: {e}")
                    break
            
            
            self.db.delete_product(prod_id)
            self.load_products()
            self.ui.status_label.setText("Товар удален")

    def on_favorite_clicked(self):
        """Кнопка В избранное."""
        current_row = self.ui.products_table_widget.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите товар!")
            return
            
        prod_id = self.ui.products_table_widget.item(current_row, 1).data(Qt.ItemDataRole.UserRole)
        self.db.toggle_favorite(prod_id)
        
        self.on_category_changed(self.ui.category_combo_box.currentIndex())
        self.ui.status_label.setText("Статус избранного изменен")

    def on_item_double_clicked(self, index):
        """Открывает карточку товара при двойном клике."""
        row = index.row()
        prod_id = self.ui.products_table_widget.item(row, 1).data(Qt.ItemDataRole.UserRole)
        
        all_products = self.db.get_all_products()
        product_data = None
        for prod in all_products:
            if prod[0] == prod_id:
                product_data = prod
                break
        
        if product_data:
            view_dialog = ProductView(self.db, product_data, parent=self)
            view_dialog.exec()
            self.on_category_changed(self.ui.category_combo_box.currentIndex())