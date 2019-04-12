import numpy as np
import math

import h5py
import NewEOM
from importlib import reload
reload(NewEOM)
# f = h5py.File("HelloWorld.hdf5", "a",
#               driver="core", backing_store=True)

# arr = np.ones((5,2))
# dset = f["test data set"]

# print(dset[...])
# f.close()

initialDCM = np.resize(np.eye(3),(9,))
initialState = np.zeros((18,))
initialState[6:15] = initialDCM
initialState[0:3] = np.array([63000000,0,0])
vehicle = NewEOM.eom(0.01, .02, initialState)
j = 0
for i in range(0, vehicle.simLength-1):
    vehicle.getInputs(np.array([1,1,1]),
                      np.array([0,0,0]),
                      10,
                      np.eye(3))

finalData = vehicle.getOutputs()
print(str(finalData[0:6]))
