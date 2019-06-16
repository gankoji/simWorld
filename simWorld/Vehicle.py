import numpy as np
import math
import random

import NewEOM
import Aerodynamics
import Propulsion

debugVehicle = False

class Vehicle:

    def __init__(self, dt, end):
        initialDCM = np.resize(np.eye(3),(9,))
        initialState = np.zeros((19,))
        initialState[6:15] = initialDCM
        initialState[0:3] = np.array([100000,6300000,1000000])
        initialState[3:6] = np.array([15, 0, 0])
        
        self.eom = NewEOM.eom(dt, end, initialState)
        self.aero = Aerodynamics.Aerodynamics()
        self.prop = Propulsion.Propulsion()
        self.throttle = 0.25
        self.Vset = 15
        self.simLength = self.eom.simLength

    def update(self):
        rho = 1.475 #- 0.4*np.random.normal()
        V = self.eom.velMag()

        self.throttle = 3*(self.Vset - V)
        if self.throttle >= 1.0:
            self.throttle = 1.0
        elif self.throttle <= 0.0:
            self.throttle = 0.0
            
        #self.throttle = 0.0
        
        deflect = np.array([0, 0, 0])
        C_w_b = self.eom.getWindToBody()
        
        f_aero = self.aero.getForces(rho, V, C_w_b)

        f_prop = self.prop.getForces(rho, V, self.throttle)

        m_aero = self.aero.getMoments(rho, V, C_w_b, deflect)
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

    def getMassProps(self):
        return 1, np.eye(3)
