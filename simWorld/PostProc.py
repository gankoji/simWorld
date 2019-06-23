import h5py
#from pylab import *
import matplotlib.pyplot as plt
import numpy as np

plotAlt = True
plotRm = True
plotRI = True

plotVm = True
plotVI = True
plotVB = True

plotAtt = True

fileName = "Base.hdf5"

f = h5py.File(fileName, "r",
              driver="core", backing_store=True)

if plotRm:
    ## Altitude
    fig, ax = plt.subplots()
    for x in f.keys():
        for run in f[x].keys():
            dset = f[x][run]['VehicleData']
            ax.plot(dset[:,18], (np.linalg.norm(dset[:,0:3], axis=1) - 6.371e6))
    plt.title('Spherical Altitude')
    plt.ylabel('Altitude (m)')
    plt.xlabel('Time (s)')

if plotRm:
    ## Position Magnitude
    fig, ax = plt.subplots()
    for x in f.keys():
        for run in f[x].keys():
            dset = f[x][run]['VehicleData']
            ax.plot(dset[:,18], np.linalg.norm(dset[:,0:3], axis=1))
    plt.title('Position Magnitude')
    plt.ylabel('Position (m)')
    plt.xlabel('Time (s)')

if plotRI:
    ## Inertial Positions
    fig = plt.figure()
    for x in f.keys():
        for run in f[x].keys():
            dset = f[x][run]['VehicleData']
            plt.subplot(311)
            plt.title('ECI Positions')
            plt.ylabel('Position (m)')
            plt.plot(dset[:,18], dset[:,0])

            plt.subplot(312)
            plt.ylabel('Position (m)')
            plt.plot(dset[:,18], dset[:,1])

            plt.subplot(313)
            plt.ylabel('Position (m)')
            plt.plot(dset[:,18], dset[:,2])
            plt.xlabel('Time (s)')

if plotVm:
    fig, ax = plt.subplots()
    for x in f.keys():
        for run in f[x].keys():
            dset = f[x][run]['VehicleData']
            ax.plot(dset[:,18], np.linalg.norm(dset[:,3:6], axis=1))
    plt.title('Velocity Magnitude')
    plt.ylabel('Velocity (m/s)')
    plt.xlabel('Time (s)')

if plotVI:
    ## Inertial Velocities
    fig = plt.figure()
    for x in f.keys():
        for run in f[x].keys():
            dset = f[x][run]['VehicleData']
            plt.subplot(311)
            plt.title('ECI Velocities')
            plt.ylabel('Velocity (m/s)')
            plt.plot(dset[:,18], dset[:,3])

            plt.subplot(312)
            plt.ylabel('Velocity (m/s)')
            plt.plot(dset[:,18], dset[:,4])

            plt.subplot(313)
            plt.ylabel('Velocity (m/s)')
            plt.plot(dset[:,18], dset[:,5])
            plt.xlabel('Time (s)')
        
if plotAtt:
    ## Inertial Attitude
    fig = plt.figure()
    for x in f.keys():
        for run in f[x].keys():
            dset = f[x][run]['VehicleData']
            plt.subplot(311)
            plt.title('Body to ECI DCM - Row 1')
            plt.ylabel('Matrix Element')
            plt.plot(dset[:,18], dset[:,6:9])

            plt.subplot(312)
            plt.ylabel('Matrix Element')
            plt.plot(dset[:,18], dset[:,9:12])

            plt.subplot(313)
            plt.ylabel('Matrix Element')
            plt.plot(dset[:,18], dset[:,12:15])
            plt.xlabel('Time (s)')
            
    ## Body Rates
    fig = plt.figure()
    for x in f.keys():
        for run in f[x].keys():
            dset = f[x][run]['VehicleData']
            plt.subplot(311)
            plt.title('Body Rates')
            plt.ylabel('rad/s')
            plt.plot(dset[:,18], dset[:,15])

            plt.subplot(312)
            plt.ylabel('rad/s')
            plt.plot(dset[:,18], dset[:,16])

            plt.subplot(313)
            plt.ylabel('rad/s')
            plt.plot(dset[:,18], dset[:,17])
            plt.xlabel('Time (s)')
plt.show()
