import numpy as np
import math
import os

import h5py
import Vehicle


scenario = "Base"
numRuns = 10
dt = .0005
endTime = 100
fileName = scenario + ".hdf5"
if os.path.exists(fileName):
    os.remove(fileName)
    
f = h5py.File(fileName, "a",
              driver="core", backing_store=True)

scenario = "/" + scenario
np.random.seed(0)
for j in range(0, numRuns):
    nodeName = scenario + "/" + str(j) + "/VehicleData"
    vehicle = Vehicle.Vehicle(dt, endTime)
    for i in range(0, vehicle.simLength-1):
        vehicle.update()

    if nodeName in f:
        f[nodeName].resize((f[nodeName].shape[0] 
                            + vehicle.eom.data.shape[0], f[nodeName].shape[1]))
        f[nodeName][-vehicle.eom.data.shape[0]:] = vehicle.eom.data
    else:
        f.create_dataset(nodeName, 
                         chunks=True, data=vehicle.eom.data, 
                         maxshape=(None, vehicle.eom.data.shape[1]))

f.close()
