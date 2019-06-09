import numpy as np
import math

import h5py
import Vehicle


vehicle = Vehicle.Vehicle(0.01, 2)

for i in range(0, vehicle.simLength-1):
    vehicle.update()

f = h5py.File("ActualData.hdf5", "a",
              driver="core", backing_store=True)

nodeName = "Vehicle Data"
if nodeName in f:
    f[nodeName].resize(f[nodeName].shape[0] 
                       + len(vehicle.eom.data))
    f[nodeName][-vehicle.eom.data.shape[0]:] = vehicle.eom.data
else:
    f.create_dataset(nodeName, 
                     chunks=True, data=vehicle.eom.data)
f.close()
