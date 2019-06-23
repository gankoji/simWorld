import numpy as np
import math
import random

import NewEOM
import Aerodynamics
import AeroSurface
import Propulsion

debugVehicle = False

def biClamp(val, lim):
    if val >= lim:
        val = lim
    elif val <= -lim:
        val = -lim
        
    return val

def clamp(val, lim):
    if val >= lim:
        val = lim
    elif val <= 0.0:
        val = 0.0
        
    return val

class Vehicle:

    def __init__(self, dt, end):
        initialDCM = np.resize(np.eye(3),(9,))
        initialState = np.zeros((19,))
        initialState[6:15] = initialDCM
        initialState[0:3] = np.array([100000,6300000,1000000]) + 1e3*np.random.randn(3)
        initialState[3:6] = np.array([15, 0, 0]) + 10.0*np.random.randn(3)
        
        self.eom = NewEOM.eom(dt, end, initialState)
        #self.aero = Aerodynamics.Aerodynamics()
        self.aero = AeroSurface.AeroSurface()
        self.prop = Propulsion.Propulsion()
        self.throttle = 0.25
        self.Vset = 15
        self.simLength = self.eom.simLength

    def update(self):
        rho = 1.475 #- 0.4*np.random.normal()
        V = self.eom.velMag()

        C_w_b = self.eom.getWindToBody()
        
        C_b_i = self.eom.data[self.eom.dataIndex, self.eom.dcm]
        C_i_b = np.resize(C_b_i,(3,3)).transpose()
        Vb = np.dot(C_i_b, self.eom.data[self.eom.dataIndex, self.eom.vel])
        
        self.autothrottle(Vb)
        self.autopilot(Vb)
        
        f_aero = self.aero.getForces(rho, Vb)
        f_prop = self.prop.getForces(rho, Vb, self.throttle)

        m_aero = self.aero.getMoments(rho, Vb, self.deflect)
        m_prop = self.prop.getMoments(rho, V, self.throttle)

        f_total = f_aero + f_prop
        m_total = m_aero + m_prop

        m, J = self.getMassProps()

        self.eom.getInputs(f_total, m_total, m, J)
        self.eom.getOutputs()
        
        if debugVehicle:
            print("Aero Forces (Body): " 
                  + str(f_aero))
            print("Total Forces (Body): "
                  + str(f_total))

    def autothrottle(self, Vb):
        V = np.linalg.norm(Vb)
        self.throttle = 1.0*(self.Vset - V)
        clamp(self.throttle, 1.0)

        #self.throttle = 0.0
        
    def autopilot(self, Vb):
        V = np.linalg.norm(Vb)
        alpha = math.atan2(Vb[0],Vb[2])
        beta = math.atan2(Vb[0],Vb[1])
        
        self.deflect = np.array([0.0, 0.0, 0.0])
        
        self.deflect[1] = -0.05*alpha
        self.deflect[2] = -0.05*beta
        
    def getMassProps(self):
        return 10, np.eye(3)
