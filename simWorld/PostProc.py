import h5py
from pylab import *
import numpy as np

fileName = "Base.hdf5"

f = h5py.File(fileName, "r",
              driver="core", backing_store=True)

for x in f.keys():
    for run in f[x].keys():
        dset = f[x][run]['VehicleData']
        
        subplot(3,1,1)
        plot(dset[:,18], dset[:,0])
        
        subplot(3,1,2)
        plot(dset[:,18], dset[:,1])
        
        subplot(3,1,3)
        plot(dset[:,18], dset[:,2])
        
plt.show()
