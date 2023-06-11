"""
Task:
9. Attēla līmeņu transformācijas, histogrammas operācijas
9b) Izstrādāt datorprogrammu, kas realizē histogrammas vienmērīgošanu.

Author:
Katerina Kuzmina, kk20156

Date:
31.05.2023

Šajā uzdevumā tiek izmantots pārvietojamā vidējā aprēķins.
Mēs aprēķinām histogrammu no attēla pelēkās skalas.
Histogrammā būs 256 kolonnas, jo pikseļu vērtību diapazons
pelēkā gammā no 0 līdz 255.
Loga lielums ir 10, lai nodrošinātu lielāku histogrammas vienmērīgošanu.
To var mainīt uz mazāku vērtību, ja nepieciešama skaidrāka informācija.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


def smooth(image, window_size):
    # computing the histogram
    histogram = cv2.calcHist([image], [0], None, [256], [0, 255])   # 256 - bins, [0] - grayscale
    histogram = histogram.flatten()

    # preparing array
    sm_histogram = np.zeros_like(histogram)
    half_window = window_size // 2

    # sliding window calculation
    # for each histogram element will calculate
    # the average value using the current element,
    # 5 on the left and 5 on the right (for window size = 10).
    # and save the average value of this window.
    for i in range(half_window, len(histogram) - half_window):
        window = histogram[i - half_window: i + half_window + 1]
        sm_histogram[i] = np.mean(window)

    return sm_histogram


image = cv2.imread('task9.jpg', 0)  # 0 - to read the image in grayscale

window_size = 10
smooth = smooth(image, window_size)

plt.figure(figsize=(8, 4))  # width and height of graphic window

plt.subplot(1, 2, 1)
plt.hist(image.flatten(), bins=256, color='black')
plt.title('Original histogram')

plt.subplot(1, 2, 2)
plt.plot(smooth, color='black')
plt.title('Smoothed histogram')

plt.tight_layout()  # to align charts
plt.show()
