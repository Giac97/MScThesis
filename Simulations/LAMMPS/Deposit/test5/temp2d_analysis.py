# -*- coding: utf-8 -*-
"""
Created on Thu May  4 07:56:30 2023

@author: becat
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
Chunk, Coord1, Coord2, Ncount, v_temp = np.loadtxt("tempsmall2d.profile", unpack=True)

temp = np.reshape(v_temp, (50,50))

plt.figure(figsize = (10, 10))
plt.imshow(temp, cmap = "hot", origin = "lower", rasterized = True)
plt.xlabel("Y")
plt.ylabel("X")


plt.colorbar(location = "right", shrink = 0.8, label = "T[K]")
plt.savefig("tempd.pdf" )