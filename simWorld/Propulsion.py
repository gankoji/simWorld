import numpy as np
import math

def clamp(val, lim):
    if val >= lim:
        val = lim
    elif val <= 0.0:
        val = 0.0
        
    return val

class Propulsion:
    def __init__(self):
        self.Tmax = 25 # Newtons
        self.Vmax = 50
        
    def getForces(self, rho, Vb, throttle):
        V = Vb[0]
        Vfrac = (V/self.Vmax)
        Vfrac = clamp(Vfrac, 1.0)
        thrust = throttle*self.Tmax*(1 - Vfrac)
        
        return np.array([thrust, 0, 0])

    def getMoments(self, rho, V, throttle):

        return np.zeros((3,))
