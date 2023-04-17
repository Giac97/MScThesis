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

@dataclass
class nanoparticle:
    """
    Class used to store data about a nanoparticle, useful for analysis and also just to save the name automatically
    Note, as of right now can only be used with mono-element nanoparticles
    """
    def __init__(self, n_atoms: int, shape: str, element: str, fname: str = ""):
        self.n_atoms = n_atoms
        self.shape = shape
        self.element = element
        self.fname = element + str(n_atoms) + shape
        
        

def write_lammps_molecule(inname, fname):
    
    """
    Read an xyz file and produce a molecule file to be used in a LAMMPS simulation
    Parameters:
        inname (string): the "xyz" file name
        fname (string): the "molecule" file name
    Returns:
        f: The molecule file
    """
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

def get_element(fname):
    return fname[0:2]

def number_of_atoms(fname):
    """
    Given a filename returns the number of atoms, this requires a filename with the format ElNatoms_shape_otherdescription.xyz
    Where El: element, Natoms: number of atoms, shape: the shape of the nanoparticle
    """
    
    #isolate the part of the filename that contains the element and the number of atoms
    contains_number = fname.split("_")[0]
    
    n_str = ""
    for m in contains_number:
        if m.isdigit():
            n_str += m
    return int(n_str)

def get_shape(fname):
    return fname.split("_")[1].split(".")[0]

