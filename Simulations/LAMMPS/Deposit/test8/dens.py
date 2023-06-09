import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

Chunk, Coord1, Coord2, Coord3, Ncount, dens = np.loadtxt("ptm.profile", unpack = True)
L = 20
for i in range(len(dens)):
    dens[i] = round(dens[i])
dens3d = dens.reshape((L,L,L))
print(max(dens))
for z in range(20):
    plt.imshow(dens3d[:,z,:], interpolation="none", origin = "lower", cmap = "Set1")
    plt.colorbar()
    plt.xlabel("X [nm]")
    plt.ylabel("Y [nm]")
    plt.savefig("C:/Users/becat/Pictures/single/slice_z{}.png".format(z), dpi = 300)
    plt.close()

