# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 12:07:17 2023

@author: becat
"""

import os, glob

mol_names = []

for file in glob.glob("./molecules/*"):
    mol_names.append(file)
    

for np in mol_names:
    molname = np[2:]
    dumpname = "dump/"+np[12:] + ".dump"
    outmolname = "molecules_therm/"+ np[12:] +".therm"
    logname = "./logs/log.equil." + np[12:]
    command = "lmp -v molname {} -v dumpname {} -v outmolname {} < in.thermalize > {}".format(molname, dumpname, outmolname, logname)
    os.system(command)
    print(np + " Equilibrated")