import numpy as np
import math

def clamp(val, lim):
    if val >= lim:
        val = lim
    elif val <= 0.0:
        val = 0.0
        
    return val

class ElMotor:
    def __init__(self, C_m_b, r_m):
        self.Tmax = 25 # Newtons
        self.Vmax = 50
        self.C_m_b = C_m_b
        self.r_m = r_m
        
    def getForces(self, rho, Vb, throttle):
        V = Vb[0]
        Vfrac = (V/self.Vmax)
        Vfrac = clamp(Vfrac, 1.0)
        thrust = throttle*self.Tmax*(1 - Vfrac)
        
        return np.array([thrust, 0, 0])

    def getMoments(self, rho, Vb, throttle):
        thrust = np.linalg.norm(self.getForces(rho, Vb, throttle))
        momShape = np.array([0.0005, 0.0, -0.001])
        
        return thrust*momShape
    
    def getDispToBody(self):
        return self.r_m
    
    def getRotToBody(self):
        return self.C_m_b
