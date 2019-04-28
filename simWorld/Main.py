import numpy as np
import math

import h5py
import Vehicle


vehicle = Vehicle.Vehicle(0.01, 2)

for i in range(0, vehicle.simLength-1):
    vehicle.update()

f = h5py.File("ActualData.hdf5", "a",
              driver="core", backing_store=True)

f.create_dataset("Vehicle Data", data=vehicle.eom.data)
f.close()
