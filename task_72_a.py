"""
Task:
7.2. Krāsu reprodukcijas principi, krāsu koordinātas
7.2a) Izstrādāt datorprogrammu, kas sintezē attēlu, kurš satur maksimāli reālistisku
krāsu spektra attainojumu, piemēram, varavīksni vai gaismas laušanu stikla prizmā.

Author:
Katerina Kuzmina, kk20156

Date:
25.05.2023

Šajā uzdevumā tiek izveidots attēls, kurš satur varavīksni.
Tiek izmantota interpolācija,lai aprēķināt krāsu vērtības katram pikselim.
Kas nodrošina vienmērīgu pāreju no vienas krāsas uz citu.
"""

import numpy as np
import cv2


def rainbow(colors):
    # size of the window; channels = 3 - rgb
    width = 600
    height = 300
    channels = 3

    image = np.zeros((height, width, channels), dtype=np.uint8)

    colors_count = len(colors)
    rainbow_piece = width / (colors_count - 1)

    for i in range(colors_count - 1):
        color_start = colors[i]
        color_end = colors[i + 1]

        # passing through each pixel in a rainbow piece
        for x in range(int(rainbow_piece * i), int(rainbow_piece * (i + 1))):
            transition = (x - rainbow_piece * i) / rainbow_piece  # to know where to start switching to another color

            # RGB values for every column of pixels of window
            r = int(color_start[0] + (color_end[0] - color_start[0]) * transition)
            g = int(color_start[1] + (color_end[1] - color_start[1]) * transition)
            b = int(color_start[2] + (color_end[2] - color_start[2]) * transition)

            # assign color values to pixels in the image
            image[:, x, 0] = b
            image[:, x, 1] = g
            image[:, x, 2] = r

    return image


# rainbow colors (approximate values)
colors = [
    (255, 0, 0),  # red
    (255, 165, 0),  # orange
    (222, 255, 0),  # yellow
    (111, 255, 26),  # green
    (0, 205, 255),  # light_blue
    (0, 85, 255),  # blue
    (171, 0, 255)  # violet
]

rainbow_img = rainbow(colors)

cv2.imshow("Rainbow", rainbow_img)  # displays an image
cv2.waitKey(0)  # waiting for keyboard event
cv2.destroyAllWindows()  # closes all open windows after key was pressed
