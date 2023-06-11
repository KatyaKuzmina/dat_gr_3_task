"""
Task:
12.1. Funkciju salīdzināšana kā attēlu analīzes pamats
12.1a) Izstrādāt datorprogrammu, kas aprēķina un vizualizē divu krāsainu attēlu normalizētu korelāciju.

Author:
Katerina Kuzmina, kk20156

Date:
05.06.2023

Šajā uzdevumā tiek aprēķināta divu krāsainu attēlu normalizētu korelācija.
Un tiek vizualizēta jauns attēls, pamatojoties uz iegūto korelāciju.
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# calculating normalized correlation
def normalized_correlation(image1, image2):
    # calculating means for each color channel (rgb)
    mean1 = np.mean(image1, axis=(0, 1))
    mean2 = np.mean(image2, axis=(0, 1))

    # calculating deviations from the means
    dev1 = image1 - mean1
    dev2 = image2 - mean2

    # calculating numerator and denominator terms
    numerator = np.sum(dev1 * dev2, axis=(0, 1))  # axis - height and width dimensions of the image arrays
    denominator = np.sqrt(np.sum(dev1 ** 2, axis=(0, 1))) * np.sqrt(np.sum(dev2 ** 2, axis=(0, 1)))

    # calculating normalized correlation coefficients for each color channel
    corr = numerator / denominator
    return corr


# creating new image
def create_new_image(image1, image2, correlation):
    new_image = image1 * correlation + image2 * (1 - correlation)
    return new_image


image1 = Image.open('task12_1.jpg')
image1_mat = np.array(image1)  # making array from an image

image2 = Image.open('task12_2.jpg')
image2_mat = np.array(image2)  # making array from an image

correlation = normalized_correlation(image1_mat, image2_mat)
new_image = create_new_image(image1_mat, image2_mat, correlation)

# showing an image
plt.imshow(new_image.astype("uint8"))
plt.axis('off')
plt.show()
