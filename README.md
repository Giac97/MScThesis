# MScThesis
This repository contains the materials used for my MSc thesis project. 
## Structure
The folder structure is as follows:
- Dissertation: will contain the dissertation paper itself, both the LaTex sorce and the pdf, together with graphs, pictures and the bibliography
- Literature Review: contains the literature review with all the supporting media and bibliography
- Simulations: contains the LAMMPS input scripts, outputs, dumps and nanoparticles models, it will also contains all the necessary scripts used to analyze the output data

## Simulations
Currently the Simulations folder contains, within the LAMMPS subfolder, a few test folders, these are supposed to contain inputs made to test various approaches before using them for the final simulation.

### Test
The "test" folder contains an input file which deposits nanoparticles of different shapes and sizes in N different steps: for each steps M nanoparticles (M_1 of size and shape si_1 sh_1, M_2 of size and shape si_2 sh_2...) are inserted in a region above the substrate at random locations with an initial downward velocity, then the simulation run for enough steps until they are at "rest" on the substrate, then this process is repeated N times.

### Test 2
The "test2" folder contains instead an input file which simulates the deposition of M nanoparticles of different sizes and shapes in a single step, after deposition the simulation is run for N steps with a shorter timestep to equilibrate the system. A simple python script "analysis_test.py", briefly described below, run a time series analysis of the system using the ovito package to find the filled fraction.

### Test 3
The "test3" folder contains test to check the viability of using Lennnard-Jones potentials in place of the more costly many bodies EAM potential in simulating the deposit. The idea would be to use LJ just for the deposit process and swith to EAM for the equilibration and other simulations (eg thermal conductivity). Issues found are that using too big a timestep causes the system to "explode": particles move to the point that they are too close, with the result that at the following timestep particles are "shoot" at very high velocity in all directions. The improvement in computing time for timestep makes using Lennard-Jones 3 times more effective, however, the previously mentioned "particles explosion" forces the use of a timestep above 0.001 fs, where, with an EAM potential, despite it being three times slower, a timestep of 0.01 fs can be safely used, making it ultimately not only more precise but also effectively faster.

### Test 4
The "test4" fodler contains an input file used to start a simulation from the restart file generated at the end of the deposition phase in the "test" folder

### 
## Python scripts
A few python scripts are present in this repository, primarily used for analysis purposes but also to prepare inputs and run simulations. Below a brief description of each is given

### Convert xyz to molecule
The script write_molecule.py contains a simple function, called "write_lammps_molecule", which reads in a xyz file and produces a molecule file which can be read as a "molecule" by LAMMPS, the one present in ./Simulations/LAMMPS/Nanoparticles Equilibration also contains additional functions to run through all the xyz models in a folder in order to convert them all to molecule files. A very simple parser extract from the file names informations such as the element composing the nanoparticle (note, as of right now, it can only parse single element nanoparticles where the element symbol has two letters, such as Au, Cu, Fe... it won't be able, for example, to parse a bimetallic nanoparticle or a "single letter" element one).

### Running Thermalization
In the "./Simulations/LAMMPS/Nanoparticles Equilibration" folder another script is present, named "run_thermo.py" it goes through all the nanoparticles saved as molecule files in the "molecules" folder, and it runs a LAMMPS simulation at 300K for 25000 steps (25 ps) and it saves the "movie" of the simulation and a logfile. Both the movie and the logfile have unique names extraced from the nanoparticle's molecule filename

### Some analysis tools
A temporary python script has been added to "./Simulations/LAMMPS/Deposit/test" called "analysis_test.py", its purpose is right now simply to test the ovito package on python, right now it can calculate, given a snapshot of the deposited thin film, the filled volume and the filled fraction using the ConstructSurfaceMesh modifier.

