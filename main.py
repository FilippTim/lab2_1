import cv2
import sys
from window import ImageWindow
import numpy as np
from PyQt6.QtWidgets import QApplication, QFileDialog, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout, QWidget

save_process_path='stuff/saved/save_proc.jpg'
class Mywindow(ImageWindow):
    def __init__(self):
        super().__init__()
        self.selected_operation=0
        self.selected_color=0
        self.logic_operation=0
        self.initial_path=''
        self.initial_path2=''
        self.brightness=0
        self.contrast=0
        self.hue=0
        self.saturation=0
        self.value=0
        self.kernel = np.array([
                                [1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]
                                ])/9

    def on_button1_clicked(self):
        self.download_img()
    def on_button_apply_clicked(self):
        try:
            if self.selected_operation==0:
                self.select_color_channel()
            elif self.selected_operation==1:
                self.bgr2gray()
            elif self.selected_operation==2:
                self.sepia()
            elif self.selected_operation==3:
                 self.brightness_contrast()
            elif self.selected_operation==4:
                self.logic()
            elif self.selected_operation==5:
                self.bgr2hvs()
            elif self.selected_operation==6:
                self.median()
            elif self.selected_operation==7:
                self.window_filter()
            elif self.selected_operation==8:
                self.watercolour()
            elif self.selected_operation==9:
                self.cartoon_filter()
            else:
                raise ValueError("Недопустимое значение выбранной операции.") 
        except Exception as e:
            print("Ошибка при выборе оперции", e)
            return None
        
    def on_button_down_img2_clicked(self):
        try:
            self.initial_path2, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Изображения (*.png *.jpg *.jpeg)")
            if not self.initial_path2:
                raise FileNotFoundError("Путь к изображению не был выбран.")
            self.update_images3(self.initial_path2)
        except Exception as e:
            print("Ошибка при загрузке изображения", e)
            return None

    def on_combo_box_changed(self, index):
            self.selected_operation=index
            #кнопка выбора второй картинки
            if self.selected_operation == 4:
                self.button_down_img2.show()
                self.combo_box_log.show()
            else:
                self.button_down_img2.hide()
                self.combo_box_log.hide()
            #список цветовых каналов
            if self.selected_operation == 0:
                self.combo_box_rgb.show()
            else:
                self.combo_box_rgb.hide()
            if self.selected_operation == 3:
                self.labelb_title.show()
                self.labelb.show()
                self.slider_brig.show()
                self.labelc_title.show()
                self.labelc.show()
                self.slider_cont.show()
            else:
                self.labelb_title.hide()
                self.labelb.hide()
                self.slider_brig.hide()
                self.labelc_title.hide()
                self.labelc.hide()
                self.slider_cont.hide()
            if self.selected_operation==5:
                self.labelh_title.show()
                self.labelh.show()
                self.slider_h.show()
                self.labels_title.show()
                self.labels.show()
                self.slider_s.show()
                self.labelv_title.show()
                self.labelv.show()
                self.slider_v.show()
            else:
                self.labelh_title.hide()
                self.labelh.hide()
                self.slider_h.hide()
                self.labels_title.hide()
                self.labels.hide()
                self.slider_s.hide()
                self.labelv_title.hide()
                self.labelv.hide()
                self.slider_v.hide()
            #if self.selected_operation == 8:
                #self.button_down_img2.show()
                # self.labelb_title.show()
                # self.labelb.show()
                # self.slider_brig.show()
                # self.labelc_title.show()
                # self.labelc.show()
                # self.slider_cont.show()
            #else:
                #self.button_down_img2.hide()
                #self.labelb_title.hide()
                #self.slider_brig.hide()
                #self.labelc_title.hide()
                #self.labelc.hide()
                #self.slider_cont.hide()
    def on_combo_box_rgb_changed(self, index):
            self.selected_color=index
    def on_combo_box_log_changed(self, index):
            self.logic_operation=index
    
    def onChanged_brig(self, value):
        self.brightness=value
        self.labelb.setText(str(value))
    def onChanged_cont(self, value):
        self.contrast=value
        self.labelc.setText(str(value))
    def onChanged_h(self, value):
        self.hue=value
        self.labelh.setText(str(value))
    def onChanged_s(self, value):
        self.saturation=value
        self.labels.setText(str(value))
    def onChanged_v(self, value):
        self.value=value
        self.labelv.setText(str(value))

    
    def download_img(self):
        try:
            self.initial_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Изображения (*.png *.jpg *.jpeg)")
            if not self.initial_path:
                raise FileNotFoundError("Путь к изображению не был выбран.")
            self.update_images1(self.initial_path)
        except Exception as e:
            print("Ошибка при загрузке изображения", e)
            return None
        
    def loadcv2(self, ini):
        try:
            if not ini:
                raise FileNotFoundError("Путь к изображению не был выбран.")
            img = cv2.imread(ini)
            return img
        except Exception as e:
            print("Ошибка при выполнении операции: ", e)
            return None
    def saved_and_print_process(self, img):
        cv2.imwrite(save_process_path, img)
        self.update_images2(save_process_path)


    def select_color_channel(self):
        img = self.loadcv2(self.initial_path)
        b,g,r = cv2.split(img)
        if self.selected_color ==0:
            self.saved_and_print_process(r)
        elif self.selected_color == 1:
            self.saved_and_print_process(g)
        elif self.selected_color == 2:
            self.saved_and_print_process(b)
        
    def bgr2gray(self):
            img = self.loadcv2(self.initial_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            self.saved_and_print_process(img)
        
    def sepia(self):
        img = self.loadcv2(self.initial_path)
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        img = cv2.transform(img, kernel)
        self.saved_and_print_process(img)
    
    def brightness_contrast(self):
        try:
            if self.brightness < -255 or self.brightness > 255:
                raise ValueError("Значение яркости должно быть в диапазоне от -255 до 255.")
            if self.contrast < -127 or self.contrast > 127:
                raise ValueError("Значение контраста должно быть в диапазоне от -127 до 127.")
            
            img = self.loadcv2(self.initial_path)

            if self.brightness != 0:
                if self.brightness > 0:
                    shadow = self.brightness
                    highlight = 255
                else:
                    shadow = 0
                    highlight = 255 + self.brightness

                alpha_b = (highlight - shadow) / 255
                gamma_b = shadow

                img_brightness = cv2.addWeighted(img, alpha_b, img, 0, gamma_b)
            else:
                img_brightness = img

            if self.contrast != 0:
                f = 131 * (self.contrast + 127) / (127 * (131 - self.contrast))
                alpha_c = f
                gamma_c = 127 * (1 - f)

                img_contrast = cv2.addWeighted(img_brightness, alpha_c, img_brightness, 0, gamma_c)
            else:
                img_contrast = img_brightness

            self.saved_and_print_process(img_contrast)
            return img_contrast         
        except Exception as e:
            print("Ошибка при выполнении операции: ", e)
            return None



    
    def logic(self):
        try:
            if self.logic_operation < 0 or self.logic_operation > 2:
                raise ValueError("Ошибка в выборе логической операции")
            img1=self.loadcv2(self.initial_path)
            img2=self.loadcv2(self.initial_path2)
            if img1.shape != img2.shape:
                img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
            if self.logic_operation == 0:
                result_image = cv2.bitwise_and(img1, img2)
            elif self.logic_operation == 1:
                result_image = cv2.bitwise_or(img1, img2)
            elif self.logic_operation == 2:
                result_image = cv2.bitwise_xor(img1, img2)
            self.saved_and_print_process(result_image)
        except Exception as e:
            print("Ошибка при выполнении операции: ", e)
            return None
    def bgr2hvs(self):
        try:
            if self.hue < 0 or self.hue > 179:
                raise ValueError("Значение оттенка должно быть в диапазоне от 0 до 179.")
            if self.saturation < 0 or self.saturation > 255:
                    raise ValueError("Значение нассыщености должно быть в диапазоне от 0 до 255.")
            if self.value < 0 or self.value > 255:
                    raise ValueError("Значение яркости должно быть в диапазоне от 0 до 255.")
            img=self.loadcv2(self.initial_path)
            hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            hsv_image[:, :, 0] = (hsv_image[:, :, 0] + self.hue) % 180
            hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] + self.saturation, 0, 255)
            hsv_image[:, :, 2] = np.clip(hsv_image[:, :, 2] + self.value, 0, 255)
            transformed_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
            self.saved_and_print_process(transformed_image)
        except Exception as e:
            print("Ошибка при выполнении операции bgr2hvs: ", e)
            return None
    def median(self):
        img=self.loadcv2(self.initial_path)
        img = cv2.medianBlur(img, 9)
        self.saved_and_print_process(img)
    def window_filter(self):
        img=self.loadcv2(self.initial_path)
        filtered_image = cv2.filter2D(img, -1, self.kernel)
        self.saved_and_print_process(filtered_image)
    def watercolour(self):
        image1=self.loadcv2(self.initial_path)
        image2=self.loadcv2(self.initial_path2)
        blend=0.5
        adjusted_image = self.brightness_contrast()
        blended_image = cv2.addWeighted(adjusted_image, blend, image2, 1 - blend, 0)
        self.saved_and_print_process(blended_image)
    def cartoon_filter(self):
        img = self.loadcv2(self.initial_path)
        tmp_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        tmp_img = cv2.medianBlur(tmp_img, 5)
        edges = cv2.adaptiveThreshold(tmp_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 13)
        img = cv2.bitwise_and(cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR), img)
        self.saved_and_print_process(img)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mywindow()
    sys.exit(app.exec())
