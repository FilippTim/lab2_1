import sys
from PyQt6.QtWidgets import QComboBox, QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class ImageWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Изображения")
        self.setGeometry(100, 100, 800, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)

        
        self.image_layout = QVBoxLayout()
        self.layout.addLayout(self.image_layout)

     
        self.image_label1 = QLabel()
        self.image_label2 = QLabel()
        self.label1_title = QLabel("До обработки:")
        self.label2_title = QLabel('После обработки')

       
        self.update_images1("stuff/images/white.jpg")
        #self.update_images2("stuff/images/white.jpg")

        
        self.image_layout.addWidget(self.label1_title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_layout.addWidget(self.image_label1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_layout.addWidget(self.label2_title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_layout.addWidget(self.image_label2, alignment=Qt.AlignmentFlag.AlignCenter)

       
        self.button_layout = QVBoxLayout()
        self.layout.addLayout(self.button_layout)
        self.update_button()

        self.show() 

    def update_images1(self, image_path1):
        
        pixmap1 = QPixmap(image_path1)

        
        scaled_pixmap1 = pixmap1.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)

        
        self.image_label1.setPixmap(scaled_pixmap1)
        
        self.update()
        
    def update_images2(self, image_path2):
        
        pixmap2 = QPixmap(image_path2)

        
        scaled_pixmap2 = pixmap2.scaled(200,200, Qt.AspectRatioMode.KeepAspectRatio)

        
        self.image_label2.setPixmap(scaled_pixmap2)
        
        self.update()
    def update_button(self):
        self.button1 = QPushButton("Выбрать изображение")
        self.button1.clicked.connect(self.on_button1_clicked)
        self.button_layout.addWidget(self.button1)

        self.combo_box = QComboBox()
        self.combo_box.addItem("Выевести один из цветовых каналов")
        self.combo_box.addItem("Опция 2")
        self.combo_box.addItem("Опция 3")
        self.combo_box.currentIndexChanged.connect(self.on_combo_box_changed)
        self.button_layout.addWidget(self.combo_box)

        self.button_down_img2 = QPushButton("Выбрать изображение 2")
        self.button_down_img2.clicked.connect(self.on_button_down_img2_clicked)
        self.button_layout.addWidget(self.button_down_img2)
        self.button_down_img2.hide()

        self.combo_box_rgb = QComboBox()
        self.combo_box_rgb.addItem("Red")
        self.combo_box_rgb.addItem("Green")
        self.combo_box_rgb.addItem("Blue")
        self.combo_box_rgb.currentIndexChanged.connect(self.on_combo_box_rgb_changed)
        self.button_layout.addWidget(self.combo_box_rgb)
        self.combo_box_rgb.hide()


        self.button_apply = QPushButton("Применить")
        self.button_apply.clicked.connect(self.on_button_apply_clicked)
        self.button_layout.addWidget(self.button_apply)





