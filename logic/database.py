import sqlite3
import os

# Константы
DB_FOLDER = "data"
DB_NAME = "cosmetics.db"
DB_PATH = os.path.join(DB_FOLDER, DB_NAME)


class DatabaseManager:
    """Класс для управления базой данных косметики."""

    def __init__(self):
        # Создаем папку для БД, если её нет
        if not os.path.exists(DB_FOLDER):
            os.makedirs(DB_FOLDER)
        
        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()
        self.create_tables()
        self.insert_initial_data()

    def create_tables(self):
        """Создает таблицы категорий и товаров (связь один-ко-многим)."""
        # Таблица категорий
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """)
        
        # Таблица товаров
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category_id INTEGER NOT NULL,
                price REAL NOT NULL,
                description TEXT,
                image_path TEXT,
                is_favorite INTEGER DEFAULT 0,
                FOREIGN KEY (category_id) REFERENCES categories (id)
            )
        """)
        self.connection.commit()

    def insert_initial_data(self):
        """Добавляет категории и тестовые товары, если БД пустая."""
        self.cursor.execute("SELECT COUNT(*) FROM categories")
        if self.cursor.fetchone()[0] == 0:
            # Запись (INSERT) - добавляем 3 категории (id: 1, 2, 3)
            categories = [
                ("Макияж",), 
                ("Уход за кожей",), 
                ("Парфюмерия",)
            ]
            self.cursor.executemany("INSERT INTO categories (name) VALUES (?)", categories)
            
            # Запись (INSERT) - добавляем 9 тестовых товаров 
            products = [
                # Макияж (category_id = 1)
                ("Помада матовая", 1, 1500.0, "Стойкая матовая помада для губ", None),
                ("Тушь для ресниц", 1, 1200.0, "Объемная тушь для выразительного взгляда", None),
                ("Тональный крем", 1, 2800.0, "Легкий тональный крем с эффектом сияния", None),
                
                # Уход за кожей (category_id = 2)
                ("Крем для лица", 2, 2500.0, "Увлажняющий крем с гиалуроновой кислотой", None),
                ("Сыворотка для лица", 2, 3200.0, "Витаминная сыворотка для сияния кожи", None),
                ("Пенка для умывания", 2, 800.0, "Очищающая пенка для всех типов кожи", None),
                
                # Парфюмерия (category_id = 3)
                ("Туалетная вода", 3, 4500.0, "Цветочный аромат с нотами ванили", None),
                ("Парфюмерный набор", 3, 6000.0, "Набор из трех мини-флаконов", None),
                ("Твердые духи", 3, 1800.0, "Удобный формат духов в стике", None),
            ]

            self.cursor.executemany("""
                INSERT INTO products (name, category_id, price, description, image_path) 
                VALUES (?, ?, ?, ?, ?)
            """, products)
            self.connection.commit()

    # ЧТЕНИЕ 
    
    def get_categories(self):
        """Возвращает список всех категорий."""
        self.cursor.execute("SELECT id, name FROM categories")
        return self.cursor.fetchall()

    def get_all_products(self):
        """Возвращает все товары с названием категории."""
        self.cursor.execute("""
            SELECT p.id, p.name, c.name, p.price, p.description, p.image_path, p.is_favorite
            FROM products p
            JOIN categories c ON p.category_id = c.id
        """)
        return self.cursor.fetchall()

    def get_products_by_category(self, category_id):
        """Возвращает товары только выбранной категории."""
        self.cursor.execute("""
            SELECT p.id, p.name, c.name, p.price, p.description, p.image_path, p.is_favorite
            FROM products p
            JOIN categories c ON p.category_id = c.id
            WHERE p.category_id = ?
        """, (category_id,))
        return self.cursor.fetchall()

    #  ЗАПИСЬ 
    
    def add_product(self, name, category_id, price, description, image_path):
        """Добавляет новый товар в базу."""
        self.cursor.execute("""
            INSERT INTO products (name, category_id, price, description, image_path)
            VALUES (?, ?, ?, ?, ?)
        """, (name, category_id, price, description, image_path))
        self.connection.commit()

    #  ИЗМЕНЕНИЕ 
    
    def update_product(self, product_id, name, category_id, price, description, image_path):
        """Обновляет данные существующего товара."""
        self.cursor.execute("""
            UPDATE products 
            SET name=?, category_id=?, price=?, description=?, image_path=?
            WHERE id=?
        """, (name, category_id, price, description, image_path, product_id))
        self.connection.commit()

    def toggle_favorite(self, product_id):
        """Переключает статус избранного (0 на 1 и наоборот)."""
        self.cursor.execute("""
            UPDATE products 
            SET is_favorite = CASE WHEN is_favorite = 1 THEN 0 ELSE 1 END
            WHERE id=?
        """, (product_id,))
        self.connection.commit()

    #  УДАЛЕНИЕ 
    
    def delete_product(self, product_id):
        """Удаляет товар из базы."""
        self.cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
        self.connection.commit()

    def close(self):
        """Закрывает соединение с БД."""
        self.connection.close()