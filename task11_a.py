"""
Task:
11. Attēlu struktūras analīze
11.a) Izstrādāt datorprogrammu attēlu sliekšņošanai, sliekšņa vērtību nosakot pēc histogrammas.

Author:
Katerina Kuzmina, kk20156

Date:
08.06.2023

Šajā uzdevumā tiek aprēķināta attēla sliekšņošana,
sliekšņa vērtību nosakot pēc histogrammas.
Un tiek izmantota Otsa metode, kur attēla pikseļus
var iedalīt divās klasēs: pikseļi ar intensitāti zem sliekšņa
un pikseļi ar intensitāti virs sliekšņa..
"""

import cv2
import numpy as np


# getting histogram from an image
def find_histogram(image):
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    return histogram


# implementing of Otsu method to determine the best threshold value
def otsu_method(image):
    histogram = find_histogram(image)
    best_threshold = 0
    best_interclass_variance = 0

    for threshold in range(256):

        # sum of histogram values
        # [0, threshold] and [threshold + 1, end of histogram]
        class1_pixels = histogram[:threshold + 1].sum()
        class2_pixels = histogram[threshold + 1:].sum()

        # pixel intensity
        class1_intensity = np.arange(threshold + 1)
        class2_intensity = np.arange(threshold + 1, 256)

        # mean value
        if class1_pixels > 0:
            class1_mean = np.sum(class1_intensity * histogram[:threshold]) / (class1_pixels + 1e-8)
        else:
            class1_mean = 0

        if class2_pixels > 0:
            class2_mean = np.sum(class2_intensity * histogram[threshold:]) / (class2_pixels + 1e-8)
        else:
            class2_mean = 0

        # calculation of interclass variance
        interclass_variance = class1_pixels * class2_pixels * ((class1_mean - class2_mean) ** 2)

        # updating the best threshold value
        if interclass_variance > best_interclass_variance:
            best_interclass_variance = interclass_variance
            best_threshold = threshold

    return best_threshold


def get_new_image(image, threshold_value):

    # getting new image after applying threshold value
    tr_image = np.where(image > threshold_value, 255, 0).astype(np.uint8)

    return tr_image


image = cv2.imread("task11.jpg", 0)

# histogram = find_histogram(image)
threshold_value = otsu_method(image)
new_image = get_new_image(image, threshold_value)

cv2.imshow('', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
