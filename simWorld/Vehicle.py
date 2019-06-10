import numpy as np
import math
import random

import NewEOM
import Aerodynamics
import Propulsion

class Vehicle:

    def __init__(self, dt, end):
        initialDCM = np.resize(np.eye(3),(9,))
        initialState = np.zeros((19,))
        initialState[6:15] = initialDCM
        initialState[0:3] = np.array([6300000,100000,1000000])
        initialState[3:6] = np.array([50, 1, 0])
        
        self.eom = NewEOM.eom(dt, end, initialState)
        self.aero = Aerodynamics.Aerodynamics()
        self.prop = Propulsion.Propulsion()

        self.simLength = self.eom.simLength

    def update(self):
        rho = 1.475 - 0.4*np.random.normal()
        V = self.eom.velMag()
        throttle = 0
        deflect = np.array([0, 0, 0])
        C_w_b = np.eye(3)
        
        f_aero = self.aero.getForces(rho, V, C_w_b)
        f_prop = self.prop.getForces(rho, V, throttle)

        m_aero = self.aero.getMoments(rho, V, C_w_b, deflect)
        m_prop = self.prop.getMoments(rho, V, throttle)

        f_total = f_aero + f_prop
        m_total = m_aero + m_prop

        m, J = self.getMassProps()

        self.eom.getInputs(f_total, m_total, m, J)
        self.eom.getOutputs()

    def getMassProps(self):
        return 1, np.eye(3)
