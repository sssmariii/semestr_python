import sys
from PySide6.QtWidgets import QApplication
from logic.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Устанавливаем цвет для всех окон и красивые стили для кнопок
    app.setStyleSheet("""
        QMainWindow, QDialog { 
            background-color: #f3e5d8; 
        }
        
        /* Стиль для всех кнопок */
        QPushButton {
            background-color: #ffffff;      
            border: 1px solid #c2a68c;      
            border-radius: 6px;             
            padding: 6px 15px;              
            color: #4a3b32;                 
            font-weight: bold;              
        }
        
        /* Эффект при наведении мышки на кнопку */
        QPushButton:hover {
            background-color: #fdfbf7;      
            border: 1px solid #a67c52;      
        }
        
        /* Эффект при нажатии на кнопку */
        QPushButton:pressed {
            background-color: #eaddcf;      
        }
    """)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

    