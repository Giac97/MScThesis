#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 17:30:53 2022

@author: giacomobecatti
"""
import numpy as np
from ase.atoms import Atoms
from ase.io import read
import glob, os
from dataclasses import dataclass



'''
Read an xyz file and produce a molecule file to be used in a LAMMPS simulation
Parameters:
    inname (string): the "xyz" file name
    fname (string): the "molecule" file name
Returns:
    f: The molecule file
'''
def write_lammps_molecule(inname, fname):
    nano = read(inname)
    coords = []
    
    for i in range(nano.get_global_number_of_atoms()):
        coords.append(nano.get_positions()[i])
        
    with open(fname, "w") as f:
        f.write("#{} molecule\n\n".format(fname))
        
        f.write(str(nano.get_global_number_of_atoms())+ " atoms\n\n")
        f.write("Coords\n\n")
        for i in range(nano.get_global_number_of_atoms()):
            f.write("{} {} {} {}\n".format(i+1, coords[i][0], coords[i][1], coords[i][2]))
        f.write("\nTypes\n\n")
    
        for i in range(nano.get_global_number_of_atoms()):    
            f.write("{} 1\n".format(i+1))
        f.close()


xyz_names = []

os.chdir("./NPs XYZ Models/")
for file in glob.glob("*.xyz"):
    xyz_names.append(file)
