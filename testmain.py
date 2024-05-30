import cv2
import sys
from testwindow import ImageWindow
import numpy as np
from PyQt6.QtWidgets import QApplication, QFileDialog, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout, QWidget

def adjust_brightness_contrast(image, brightness=0, contrast=0):
    """
    Регулирует яркость и контраст изображения.

    Параметры:
    image (numpy.ndarray): Исходное изображение.
    brightness (int): Значение яркости (-255 до 255). Отрицательные значения затемняют изображение, положительные осветляют.
    contrast (int): Значение контраста (-127 до 127). Отрицательные значения уменьшают контраст, положительные увеличивают.

    Возвращает:
    numpy.ndarray: Изображение с изменённой яркостью и контрастом.
    """
    # Проверка входных параметров
    if brightness < -255 or brightness > 255:
        raise ValueError("Значение яркости должно быть в диапазоне от -255 до 255.")
    if contrast < -127 or contrast > 127:
        raise ValueError("Значение контраста должно быть в диапазоне от -127 до 127.")

    # Применение изменения яркости
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness

        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow

        img_brightness = cv2.addWeighted(image, alpha_b, image, 0, gamma_b)
    else:
        img_brightness = image

    # Применение изменения контраста
    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)

        img_contrast = cv2.addWeighted(img_brightness, alpha_c, img_brightness, 0, gamma_c)
    else:
        img_contrast = img_brightness

    return img_contrast

# Пример использования
image = cv2.imread('stuff/images/banan.jpg')
adjusted_image = adjust_brightness_contrast(image, brightness=30, contrast=40)
cv2.imshow('Adjusted Image', adjusted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()