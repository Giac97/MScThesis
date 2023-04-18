# MScThesis
This repository contains the materials used for my MSc thesis project. 
## Structure
The folder structure is as follows:
- Dissertation: will contain the dissertation paper itself, both the LaTex sorce and the pdf, together with graphs, pictures and the bibliography
- Literature Review: contains the literature review with all the supporting media and bibliography
- Simulations: contains the LAMMPS input scripts, outputs, dumps and nanoparticles models, it will also contains all the necessary scripts used to analyze the output data

## Python scripts
A few python scripts are present in this repository, primarily used for analysis purposes but also to prepare inputs and run simulations. Below a brief description of each is given

### Convert xyz to molecule
The script write_molecule.py contains a simple function, called "write_lammps_molecule", which reads in a xyz file and produces a molecule file which can be read as a "molecule" by LAMMPS, the one present in ./Simulations/LAMMPS/Nanoparticles Equilibration also contains additional functions to run through all the xyz models in a folder in order to convert them all to molecule files. A very simple parser extract from the file names informations such as the element composing the nanoparticle (note, as of right now, it can only parse single element nanoparticles where the element symbol has two letters, such as Au, Cu, Fe... it won't be able, for example, to parse a bimetallic nanoparticle or a "single letter" element one).

### Running Thermalization
In the "./Simulations/LAMMPS/Nanoparticles Equilibration" folder another script is present, named "run_thermo.py" it goes through all the nanoparticles saved as molecule files in the "molecules" folder, and it runs a LAMMPS simulation at 300K for 25000 steps (25 ps) and it saves the "movie" of the simulation and a logfile. Both the movie and the logfile have unique names extraced from the nanoparticle's molecule filename

### Some analysis tools
A temporary python script has been added to "./Simulations/LAMMPS/Deposit/test" called "analysis_test.py", its purpose is right now simply to test the ovito package on python, right now it can calculate, given a snapshot of the deposited thin film, the filled volume and the filled fraction using the ConstructSurfaceMesh modifier.