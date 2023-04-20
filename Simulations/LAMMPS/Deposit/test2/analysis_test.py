# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:37:23 2023

@author: becat
"""

from ovito.io import import_file, export_file
from ovito.modifiers import TimeSeriesModifier, ComputePropertyModifier, ConstructSurfaceModifier
from ovito.modifiers import PolyhedralTemplateMatchingModifier, GrainSegmentationModifier
import numpy as np
import matplotlib.pyplot as plt
from ovito.vis import Viewport, OSPRayRenderer
from ovito.qt_compat import QtGui

from ovito.data import SimulationCell, DataCollection
import numpy

def shrink_modify(frame: int, data: DataCollection):

    # There's nothing we can do if there are no input particles. 
    if not data.particles or data.particles.count == 0: return

    # Compute min/max range of particle coordinates.
    coords_min = numpy.amin(data.particles.positions, axis=0)
    coords_max = numpy.amax(data.particles.positions, axis=0)

    # Build the new 3x4 cell matrix:
    #   (x_max-x_min  0            0            x_min)
    #   (0            y_max-y_min  0            y_min)
    #   (0            0            z_max-z_min  z_min)
    matrix = numpy.empty((3,4))
    matrix[:,:3] = numpy.diag(coords_max - coords_min)
    matrix[:, 3] = coords_min

    # Assign the cell matrix - or create whole new SimulationCell object in 
    # the DataCollection if there isn't one already.
    data.create_cell(matrix, (False, False, False))


pipeline = import_file("./dump/dump.equil.nps")

pipeline.modifiers.append(shrink_modify)

# pipeline.modifiers.append(ConstructSurfaceModifier(radius = 2.9, identify_regions = True))
# pipeline.modifiers.append(TimeSeriesModifier(operate_on = 'ConstructSurfaceMesh.void_volume'))
# # pipeline.modifiers.append(PolyhedralTemplateMatchingModifier(output_orientation=True))
# # pipeline.modifiers.append(GrainSegmentationModifier())
# # pipeline.modifiers.append(TimeSeriesModifier(operate_on = 'GrainSegmentation.grain_count'))
# data = pipeline.compute()
# series = data.tables['time-series']

thick = []

for i in range(pipeline.source.num_frames):
    data = pipeline.compute(i)
    th = max(data.particles['Position'][:,2]) - min(data.particles['Position'][:,2])
    thick.append(th)

plt.figure(figsize=(10,6), dpi = 300)
plt.plot(thick)
plt.xlabel("Timestep")
plt.ylabel("Thickness [Angstrom]")
plt.grid()
plt.xticks(np.arange(0, pipeline.source.num_frames+10, 10))
# plt.plot(series.x[:],series.y[:])
