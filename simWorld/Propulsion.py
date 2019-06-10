import numpy as np
import math

class Propulsion:
    def __init__(self):
        self.Tmax = 25 # Newtons
        self.Vmax = 150
    def getForces(self, rho, V, throttle):
        thrust = throttle*self.Tmax
        if V > self.Vmax:
            thrust = 0.0

        return np.array([thrust, 0, 0])

    def getMoments(self, rho, V, throttle):

        return np.zeros((3,))
