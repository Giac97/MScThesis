# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:37:23 2023

@author: becat
"""

from ovito.io import import_file, export_file
from ovito.modifiers import SpatialBinningModifier, ComputePropertyModifier, ConstructSurfaceModifier
import numpy as np
import matplotlib.pyplot as plt

pipeline = import_file("./snapshots/firstdep.xyz", columns=["Particle Type", "Position.X", "Position.Y", "Position.Z"])

pipeline.modifiers.append(ConstructSurfaceModifier(
    method = ConstructSurfaceModifier.Method.AlphaShape,
    radius = 2.9,
    identify_regions = True))


data = pipeline.compute()

print("Agregate quantities:")
print(f"Surface area: {data.attributes['ConstructSurfaceMesh.surface_area']}")
print(f"Solid volume: {data.attributes['ConstructSurfaceMesh.filled_volume']}")
print(f"Filled volume fraction: {data.attributes['ConstructSurfaceMesh.filled_fraction']}")

f_frac_firstdep = data.attributes['ConstructSurfaceMesh.filled_fraction']
empty_frac_firstdep = data.attributes['ConstructSurfaceMesh.empty_fraction']

pipeline3 = import_file("./snapshots/thirddep.xyz", columns=["Position.X", "Position.Y", "Position.Z"])

pipeline3.modifiers.append(ConstructSurfaceModifier(
    method = ConstructSurfaceModifier.Method.AlphaShape,
    radius = 2.9,
    identify_regions = True))


data3 = pipeline3.compute()

print("Agregate quantities:")
print(f"Surface area: {data3.attributes['ConstructSurfaceMesh.surface_area']}")
print(f"Solid volume: {data3.attributes['ConstructSurfaceMesh.filled_volume']}")
print(f"Filled volume fraction: {data3.attributes['ConstructSurfaceMesh.filled_fraction']}")

f_frac_thirddep = data3.attributes['ConstructSurfaceMesh.filled_fraction']
empty_frac_thirddep = data3.attributes['ConstructSurfaceMesh.empty_fraction']

pipeline4 = import_file("./snapshots/fourthdep.xyz", columns=["Position.X", "Position.Y", "Position.Z"])

pipeline4.modifiers.append(ConstructSurfaceModifier(
    method = ConstructSurfaceModifier.Method.AlphaShape,
    radius = 1.9,
    identify_regions = True))


data4 = pipeline4.compute()

print("Agregate quantities:")
print(f"Surface area: {data4.attributes['ConstructSurfaceMesh.surface_area']}")
print(f"Solid volume: {data4.attributes['ConstructSurfaceMesh.filled_volume']}")
print(f"Filled volume fraction: {data4.attributes['ConstructSurfaceMesh.filled_fraction']}")

f_frac_forthtdep = data4.attributes['ConstructSurfaceMesh.filled_fraction']
empty_frac_forthdep = data4.attributes['ConstructSurfaceMesh.empty_fraction']