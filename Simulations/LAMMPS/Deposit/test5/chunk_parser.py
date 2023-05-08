# -*- coding: utf-8 -*-
"""
Created on Sat May  6 21:55:43 2023

@author: becat
"""

def chunk_parse(fname, outname, N_step, N_freq):
    """
    

    Parameters
    ----------
    fname : STR
        Name of the output file with the ave/chunk data.
    outname : STR
        Path to the output files with prefix.
    N_step : INT
        Number of steps of the simulation.
    N_freq : INT
        Number of timestep between each calculation (defined in lammps input).
    
    Returns
    -------
    Indivdual files containing the chunk averaged values for each chunk calculation.

    """
    infile = open(fname, "r")
    

    N_calc = N_step / N_freq
    
    N_chunk = 8000
    
    
    for i in range(3):
        desc = infile.readline()
        
    for i in range(int(N_calc)):
        first_line = infile.readline()
        out_file = open(outname + "_" + str(i), "w")
        for j in range(N_chunk):
            ch = infile.readline()
            out_file.write(ch)
        print(first_line)

        
        

