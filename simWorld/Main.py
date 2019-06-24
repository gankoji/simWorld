import numpy as np
import math
import os
import time
import threading
from multiprocessing import Process

import h5py
import Vehicle

useThreading = True
numRuns = 25
dt = .001
endTime = 10

#dataStore = [0]*numRuns
dataStore = []
def runSim(j):
    vehicle = Vehicle.Vehicle(dt, endTime)
    for i in range(0, vehicle.simLength-1):
        vehicle.update()
        
    dataStore.append(vehicle)
    # print("Thread " + str(j) + " complete")

start_time = time.time()
scenario = "Base"
fileName = scenario + ".hdf5"
if os.path.exists(fileName):
    os.remove(fileName)
    
f = h5py.File(fileName, "a",
              driver="core", backing_store=True)

scenario = "/" + scenario
np.random.seed(0)

if useThreading:
    threads = []
    for j in range(0, numRuns):
        threads.append(Process(target=runSim, args=(j,)))
        threads[j].start()

    for j in range(0, numRuns):
        threads[j].join()

else:
    for j in range(0, numRuns):
        runSim(j)
        
        
# print(dataStore)
# for j in range(0, numRuns):
#     nodeName = scenario + "/" + str(j) + "/VehicleData"
#     vehicle = dataStore[j]
#     print(vehicle)

    # if nodeName in f:
    #     f[nodeName].resize((f[nodeName].shape[0] 
    #                         + vehicle.eom.data.shape[0], f[nodeName].shape[1]))
    #     f[nodeName][-vehicle.eom.data.shape[0]:] = vehicle.eom.data
    # else:
    #     f.create_dataset(nodeName, 
    #                      chunks=True, data=vehicle.eom.data, 
    #                      maxshape=(None, vehicle.eom.data.shape[1]))

f.close()

print("--- %s seconds ---" %(time.time() - start_time))
