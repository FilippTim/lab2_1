from PyQt6.QtWidgets import QComboBox, QSlider, QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
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
        self.image_label3 = QLabel()
        self.label1_title = QLabel('До обработки')
        self.label2_title = QLabel('После обработки')
        self.label3_title = QLabel('Второе изображение')

       
        #self.update_images1("stuff/images/white.jpg")
        #self.update_images2("stuff/images/white.jpg")

        
        self.image_layout.addWidget(self.label1_title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_layout.addWidget(self.image_label1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_layout.addWidget(self.label3_title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_layout.addWidget(self.image_label3, alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_layout.addWidget(self.label2_title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_layout.addWidget(self.image_label2, alignment=Qt.AlignmentFlag.AlignCenter)

        self.label1_title.hide()
        self.label2_title.hide()
        self.label3_title.hide()
       
        self.button_layout = QVBoxLayout()
        self.layout.addLayout(self.button_layout)
        self.update_button()

        self.show() 

    def update_images1(self, image_path1):
        self.label1_title.show()
        
        pixmap1 = QPixmap(image_path1)

        
        scaled_pixmap1 = pixmap1.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio)

        
        self.image_label1.setPixmap(scaled_pixmap1)
        
        self.update()
        
    def update_images2(self, image_path2):
        self.label2_title.show()
        
        pixmap2 = QPixmap(image_path2)

        
        scaled_pixmap2 = pixmap2.scaled(300,300, Qt.AspectRatioMode.KeepAspectRatio)

        
        self.image_label2.setPixmap(scaled_pixmap2)
        
        self.update()

    def update_images3(self, image_path3):
        self.label3_title.show()
        
        pixmap3 = QPixmap(image_path3)

        
        scaled_pixmap3 = pixmap3.scaled(300,300, Qt.AspectRatioMode.KeepAspectRatio)

        
        self.image_label3.setPixmap(scaled_pixmap3)
        
        self.update()
    
    def update_button(self):
        self.button1 = QPushButton("Выбрать изображение")
        self.button1.clicked.connect(self.on_button1_clicked)
        self.button_layout.addWidget(self.button1)

        self.combo_box = QComboBox()
        self.combo_box.addItem("Выевести один из цветовых каналов")
        self.combo_box.addItem("Вевести Ч/Б версию изображения")
        self.combo_box.addItem("Sepia фильтр")
        self.combo_box.addItem("Изменить яркость и контрастность")
        self.combo_box.addItem("Логические опреации")
        self.combo_box.addItem("Преобразование в формат HSV")
        self.combo_box.addItem("Медианное размытие")
        self.combo_box.addItem("Оконный фильтр")
        self.combo_box.addItem("Акварельный фильтр")
        self.combo_box.addItem("cartoon filter")

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

        self.combo_box_log = QComboBox()
        self.combo_box_log.addItem("дополнение")
        self.combo_box_log.addItem("пересечение")
        self.combo_box_log.addItem("исключение")
        self.combo_box_log.currentIndexChanged.connect(self.on_combo_box_log_changed)
        self.button_layout.addWidget(self.combo_box_log)
        self.combo_box_log.hide()


        self.button_apply = QPushButton("Применить")
        self.button_apply.clicked.connect(self.on_button_apply_clicked)
        self.button_layout.addWidget(self.button_apply)

        self.labelb_title = QLabel('Яркость')
        self.button_layout.addWidget(self.labelb_title)
        self.labelb_title.hide()

        self.labelb = QLabel('0', self)
        self.labelb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_layout.addWidget(self.labelb)
        self.labelb.hide()

        self.slider_brig = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_brig.setMinimum(-255)
        self.slider_brig.setMaximum(255)
        self.slider_brig.setValue(0)
        self.slider_brig.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_brig.setTickInterval(1)
        self.slider_brig.valueChanged.connect(self.onChanged_brig)
        self.button_layout.addWidget(self.slider_brig)
        self.slider_brig.hide()

        self.labelc_title = QLabel('Контрастность')
        self.button_layout.addWidget(self.labelc_title)
        self.labelc_title.hide()

        self.labelc = QLabel('0', self)
        self.labelc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_layout.addWidget(self.labelc)
        self.labelc.hide()

        self.slider_cont = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_cont.setMinimum(-127)
        self.slider_cont.setMaximum(127)
        self.slider_cont.setValue(0)
        self.slider_cont.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_cont.setTickInterval(1)
        self.slider_cont.valueChanged.connect(self.onChanged_cont)
        self.button_layout.addWidget(self.slider_cont)
        self.slider_cont.hide()

        self.labelh_title = QLabel('Оттенок')
        self.button_layout.addWidget(self.labelh_title)
        self.labelh_title.hide()

        self.labelh = QLabel('0', self)
        self.labelh.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_layout.addWidget(self.labelh)
        self.labelh.hide()

        self.slider_h = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_h.setMinimum(0)
        self.slider_h.setMaximum(179)
        self.slider_h.setValue(179//2)
        self.slider_h.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_h.setTickInterval(1)
        self.slider_h.valueChanged.connect(self.onChanged_h)
        self.button_layout.addWidget(self.slider_h)
        self.slider_h.hide()

        self.labels_title = QLabel('Нассыщеность')
        self.button_layout.addWidget(self.labels_title)
        self.labels_title.hide()

        self.labels = QLabel('0', self)
        self.labels.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_layout.addWidget(self.labels)
        self.labels.hide()

        self.slider_s = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_s.setMinimum(0)
        self.slider_s.setMaximum(255)
        self.slider_s.setValue(0)
        self.slider_s.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_s.setTickInterval(1)
        self.slider_s.valueChanged.connect(self.onChanged_s)
        self.button_layout.addWidget(self.slider_s)
        self.slider_s.hide()

        self.labelv_title = QLabel('Яркость')
        self.button_layout.addWidget(self.labelv_title)
        self.labelv_title.hide()

        self.labelv = QLabel('0', self)
        self.labelv.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_layout.addWidget(self.labelv)
        self.labelv.hide()

        self.slider_v = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_v.setMinimum(0)
        self.slider_v.setMaximum(255)
        self.slider_v.setValue(0)
        self.slider_v.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_v.setTickInterval(1)
        self.slider_v.valueChanged.connect(self.onChanged_v)
        self.button_layout.addWidget(self.slider_v)
        self.slider_v.hide()





