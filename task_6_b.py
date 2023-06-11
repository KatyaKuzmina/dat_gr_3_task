"""
Task:
6. Ceļā uz vizuālo reālismu
6b) Izstrādāt datorprogrammu, kas sadala parametriski uzdotu virsmu trijstūros un rezultātu attēlo uz ekrāna.
Trijstūru izmēru rēķināt tā, lai uz ekrāna to izmērs būtu aptuveni vienāds.
Demonstrēt metodes darbību uz trīs dažādām virsmām.

Author:
Katerina Kuzmina, kk20156

Date:
16.05.2023

Šajā uzdevumā tiek izveidots algoritms, kas sadala parametriski uzdotu virsmu trijstūros.
Šajā uzdevumā ir trīs virsmas. Katru virsmu jāparbauda atsevišķi.
Jāatkomentē vienu no daļam (surface number <surface_number>)
"""

import matplotlib.pyplot as plt
import numpy as np


def triangle(surfaces):
    for surface in surfaces:

        triangles = []

        # uncomment each surface individually to see the result
        # surface number 1
        u = np.linspace(-1, 1, 20)
        v = np.linspace(-1, 1, 10)
        u, v = np.meshgrid(u, v)
        a = 1
        x = a * u
        y = a * v
        z = u + v

        # surface number 2
        # u = np.linspace(0, 2 * np.pi, 20)
        # v = np.linspace(0, 1, 10)
        # u, v = np.meshgrid(u, v)
        # a = 1
        # x = a * np.cos(u)
        # y = a * np.sin(u)
        # z = v

        # surface number 3
        # u = np.linspace(0, 2 * np.pi, 20)
        # v = np.linspace(0, np.pi, 10)
        # u, v = np.meshgrid(u, v)
        # a = 1
        # x = a * np.sin(v) * np.cos(u)
        # y = a * np.sin(v) * np.sin(u)
        # z = a * np.cos(v)

        # creating triangles are adding their vertex coordinates to the array
        # two neighboring triangles are created each loop
        print(x)
        for i in range(len(x) - 1):
            for j in range(len(x[i]) - 1):
                triangles.append([(x[i, j], y[i, j], z[i, j]),
                                  (x[i, j + 1], y[i, j + 1], z[i, j + 1]),
                                  (x[i + 1, j], y[i + 1, j], z[i + 1, j])
                                  ])

                triangles.append([(x[i + 1, j], y[i + 1, j], z[i + 1, j]),
                                  (x[i, j + 1], y[i, j + 1], z[i, j + 1]),
                                  (x[i + 1, j + 1], y[i + 1, j + 1], z[i + 1, j + 1])
                                  ])

        # drawing and displaying triangles
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for triangle in triangles:
            x1 = [triangle[0][0], triangle[1][0], triangle[2][0], triangle[0][0]]
            y1 = [triangle[0][1], triangle[1][1], triangle[2][1], triangle[0][1]]
            z1 = [triangle[0][2], triangle[1][2], triangle[2][2], triangle[0][2]]
            ax.plot(x1, y1, z1, color='black')

        plt.show()


surface = [
    {}  # Pievienojiet citus parametrus, ja nepieciešams
]

triangle(surface)
