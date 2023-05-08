# -*- coding: utf-8 -*-
"""
Created on Thu May  4 16:37:32 2023

@author: becat
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pyvox.models import Vox
from pyvox.writer import VoxWriter
import pyvista as pv

z_slice = 10

# for i in range(5):
#     Chunk, Coord1, Coord2, Coord3, Ncount, dens = np.loadtxt("./chunks/density/density_3d_{}.profile".format(i), unpack=True)
    
#     # points = np.zeros((len(Coord1), 3))
#     # for i in range(len(Coord1)):
#     #     points[i, 0] = Coord1[i]
#     #     points[i, 1] = Coord2[i]
#     #     points[i, 2] = Coord3[i]
#     # point_cloud = pv.PolyData(points)   
    
    
#     # points_not_zero = []
#     # dens_not_zero = []
#     # for i in range(len(points)):
#     #     if (dens[i] != 0):
#     #         points_not_zero.append(points[i])
#     #         dens_not_zero.append(dens[i])
#     # not_zero = np.zeros((len(points_not_zero), 3))
    
#     # for i in range(len(points_not_zero)):
#     #     not_zero[i, 0] = points_not_zero[i][0]
#     #     not_zero[i, 1] = points_not_zero[i][1]
#     #     not_zero[i, 2] = points_not_zero[i][2]
    
#     L = 20
#     dens3d = dens.reshape((L,L,L))
    
    
    
#     # voxdens = dens3d > 0.0001
    
#     # vox = Vox.from_dense(voxdens)
    
#     # VoxWriter('test.vox', vox).write()
    
#     for z in range(2, 13):
#         plt.imshow(dens3d[:,:,z], interpolation="none", origin = "lower",  extent=[0,122,0,122], vmin=0, vmax = 0.07, cmap = "Reds")
#         plt.colorbar()
#         plt.xlabel("X [nm]")
#         plt.ylabel("Y [nm]")
#         plt.title("Chunk average number {}, z = {}".format(i, z))
#         plt.savefig("./test_chunk/density/slice_{}_z{}.png".format(i,z), dpi = 300)
#         plt.close()


for i in range(5):
    Chunk, Coord1, Coord2, Coord3, Ncount, dens = np.loadtxt("./chunks/temp/temp_3d_{}.profile".format(i), unpack=True)
    
    # points = np.zeros((len(Coord1), 3))
    # for i in range(len(Coord1)):
    #     points[i, 0] = Coord1[i]
    #     points[i, 1] = Coord2[i]
    #     points[i, 2] = Coord3[i]
    # point_cloud = pv.PolyData(points)   
    
    
    # points_not_zero = []
    # dens_not_zero = []
    # for i in range(len(points)):
    #     if (dens[i] != 0):
    #         points_not_zero.append(points[i])
    #         dens_not_zero.append(dens[i])
    # not_zero = np.zeros((len(points_not_zero), 3))
    
    # for i in range(len(points_not_zero)):
    #     not_zero[i, 0] = points_not_zero[i][0]
    #     not_zero[i, 1] = points_not_zero[i][1]
    #     not_zero[i, 2] = points_not_zero[i][2]
    
    L = 20
    temp3d = dens.reshape((L,L,L))
    
    temp1d = np.zeros(20)

    for j in range(20):
        avg = np.mean(temp3d[j, :, 2:13])
        temp1d[j] = avg
    
    plt.figure(figsize = (10, 5), dpi = 300)
    plt.plot(temp1d)
    plt.ylim((100, 1000))
    plt.xlabel("X")
    plt.ylabel("T [K]")
    plt.title("1d Averaged temperature profile, calc = {}". format(i))
    plt.savefig("./test_chunk/temp1d/temp1d_{}.png".format(i))
    plt.close()
    
    # voxdens = dens3d > 0.0001
    
    # vox = Vox.from_dense(voxdens)
    
    # VoxWriter('test.vox', vox).write()
    for z in range(2, 13):
        plt.imshow(temp3d[:,:,z], interpolation="none", origin = "lower",  extent=[0,122,0,122], vmin=100, vmax = 900, cmap = "hot")
        plt.colorbar()
        plt.xlabel("X [nm]")
        plt.ylabel("Y [nm]")
        plt.title("Chunk average number {}, z = {}".format(i, z))
        plt.savefig("./test_chunk/temp/slice_{}_z{}.png".format(i,z), dpi = 300)
        plt.close()


# points = np.zeros((len(Coord1), 3))
# for i in range(len(Coord1)):
#     points[i, 0] = Coord1[i]
#     points[i, 1] = Coord2[i]
#     points[i, 2] = Coord3[i]


# temp_pt_not_zero = []
# temp_not_zero = []
# for i in range(len(points)):
#     if (temp[i] != 0):
#         temp_pt_not_zero.append(points[i])
#         temp_not_zero.append(temp[i])
# t_not_zero = np.zeros((len(temp_pt_not_zero ), 3))

# for i in range(len(temp_pt_not_zero )):
#     t_not_zero[i, 0] = temp_pt_not_zero[i][0]
#     t_not_zero[i, 1] = temp_pt_not_zero[i][1]
#     t_not_zero[i, 2] = temp_pt_not_zero[i][2]
# point_cloud = pv.PolyData(t_not_zero)   

# t_not_zero_lim = np.zeros(len(temp_not_zero))
# for i in range(len( t_not_zero_lim)):
#     if temp_not_zero[i] > 900:
#         t_not_zero_lim[i] = 900
#     elif temp_not_zero[i] < 200:
#         t_not_zero_lim[i] = 200
#     else:
#         t_not_zero_lim[i] = temp_not_zero[i]
        

# temp3d = temp.reshape((L,L,L))

# for i in range(L):
#     plt.imshow(temp3d[:,:,i], vmin = 100, vmax = 850 ,interpolation="none", cmap = "hot",origin = "lower",  extent=[0,122,0,122])
#     plt.xlabel("X [nm]")
#     plt.ylabel("Y [nm]")
#     plt.colorbar()
#     plt.title("Slice number {}".format(i))
#     plt.savefig("C:/Users/becat/Pictures/Chunks/temp_slice/twotemp/slice_{}.png".format(i), dpi = 300)
#     plt.close()