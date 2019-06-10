# New 6 DoF Equations of Motion, using DCM integration instead of
# quaternion.

import numpy as np
import math

class eom:
    def __init__(self, dt, end_time, initialState):
        self.simLength = int(math.floor(end_time/dt) + 1)

        # initialState should be a single frame of the entire state of
        # the 6 DoF:

        # Position (Inertial)                               3 [0:3]
        # Velocity                                          3 [3:6]
        # Attitude (Body to Inertial)                       9 [12:21]
        # Angular Rates (Body wrt Inertial, in body)        3 [21:24]
        # Time (s)
        # Total Elements:                                   19
        self.dataFrameLength = 19
        self.data = np.zeros((self.simLength, self.dataFrameLength))
        self.derivatives = np.zeros((self.dataFrameLength,))
        self.time = np.linspace(0, end_time, self.simLength)

        # Defines for easy indexing
        self.pos = slice(0,3)
        self.vel = slice(3,6)
        self.dcm = slice(6,15)
        self.rat = slice(15,18)
        self.time = 18

        self.dataIndex = 0
        self.data[self.dataIndex, :] = initialState
        self.dt = dt
        self.prevTime = 0.0

    def velMag(self):
        vm = np.linalg.norm(self.data[self.dataIndex, self.vel])
        return vm
    
    def getInputs(self, forces, moments, mass, inertia):
        # Forces is a 1x3 vector (XYZ)
        # expected in body frame
        self.forces = forces

        # Moments is a 1x3 vector (XYZ)
        # expected in body frame
        self.moments = moments

        # Mass is a scalar (kg)
        self.mass = mass

        # Inertia is a 3x3
        # expected in body coordinates
        self.inertia = inertia

        # Integrate the state vector
        self.integrateStates()

    def getOutputs(self):
        return self.data[self.dataIndex, :]

    def integrateStates(self):
        nc = self.dataIndex
        state = self.data[nc, :]
        h = self.dt
        k1 = h*self.updateDerivatives(state)
        k2 = h*self.updateDerivatives(state + 0.5*k1)
        k3 = h*self.updateDerivatives(state + 0.5*k2)
        k4 = h*self.updateDerivatives(state + k3)
        nc = nc + 1
        self.data[nc, :] = state + 0.5*(k1 + 2.0*k2 + 2.0*k3 + k4)

        # Gram-Schmidt Orthonormalization of DCM
        currentDCM = np.resize(self.data[nc, self.dcm], (3,3))
        currentDCM = self.gsOrtho(currentDCM)
        self.data[nc, self.dcm] = np.resize(currentDCM, (9,))
        self.prevTime = self.prevTime + self.dt
        self.data[nc, self.time] = self.prevTime
        self.dataIndex += 1

    def updateDerivatives(self, state):
        currentDCM = np.resize(state[self.dcm],(3,3))
        derivatives = np.zeros((self.dataFrameLength,))

        # Translational State
        pos = state[self.pos]
        vel = state[self.vel]
        bacc = self.forces/self.mass
        iacc = np.dot(currentDCM, bacc)

        # Rotational State
        invertia = np.linalg.inv(self.inertia)
        rates = state[self.rat]
        temp1 = np.dot(self.inertia, rates)
        temp2 = np.cross(rates, temp1)
        temp3 = self.moments - temp2

        omegaSkew = self.skewSymmetric(rates)
        dcmDeriv = np.resize(np.dot(currentDCM, omegaSkew), (9,))

        derivatives[self.pos] = vel
        derivatives[self.vel] = iacc + self.gravModel(pos)
        derivatives[self.dcm] = dcmDeriv
        derivatives[self.rat] = np.dot(invertia, temp3)
        
        return derivatives
        
    def gsOrtho(self, dcm):
        for i in range(0,3):
            norm = np.linalg.norm(dcm[i,:])
            for j in range(0,3):
                dcm[i,j] = dcm[i,j]/norm

        return dcm

    def gravModel(self, pos):
        upos = pos/np.linalg.norm(pos)
        grav = -9.81*upos
        
        return grav

    def skewSymmetric(self, vec):
        p = vec[0]
        q = vec[1]
        r = vec[2]

        s = np.array([[0, -r, q],
                      [r,  0,-p],
                      [-q, p, 0]])
        
        return s
