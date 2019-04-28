import numpy as np
import math

class Propulsion:
    def __init__(self):
        self.Tmax = 500 # Newtons
        
    def getForces(self, rho, V, throttle):
        thrust = throttle*self.Tmax
        return np.array([thrust, 0, 0])

    def getMoments(self, rho, V, throttle):

        return np.zeros((3,))
