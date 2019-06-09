import h5py
import matplotlib.pyplot as plt
import numpy as np

fileName = "Base.hdf5"

f = h5py.File(fileName, "r",
              driver="core", backing_store=True)

fig, ax = plt.subplots()

for x in f.keys():
    for run in f[x].keys():
        dset = f[x][run]['VehicleData']
        ax.plot(dset[:,18], dset[:,0])
        
plt.show()
