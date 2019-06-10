import h5py
from pylab import *
import numpy as np

fileName = "Base.hdf5"

f = h5py.File(fileName, "r",
              driver="core", backing_store=True)

for x in f.keys():
    for run in f[x].keys():
        dset = f[x][run]['VehicleData']
        
        subplot(1,1,1)
        plot(dset[:,18], np.linalg.norm(dset[:,3:5], axis=1))
        
        # subplot(3,1,2)
        # plot(dset[:,18], dset[:,4])
        
        # subplot(3,1,3)
        # plot(dset[:,18], dset[:,5])
        
plt.show()
