import numpy as np
import math

class Aerodynamics:
    def __init__(self):
        self.Cl = 1
        self.Cd = 1
        self.Al = 1
        self.Ad = 1
        self.Lmax = 3
        self.Mmax = 3
        self.Nmax = 3
        self.rVmax = 1.475*150

    def getForces(self, rho, V, C_w_b):
        C_b_w = np.transpose(C_w_b)
        alpha = math.atan2(C_b_w[0,2], C_b_w[0,0])
        beta = math.atan2(C_b_w[0,2], C_b_w[0,0])

        Cl = self.getLift(alpha)
        Cd = self.getDrag(alpha)
        Cs = self.getSlip(beta)
        lift = 0.5*rho*self.Al*Cl*(V**2)
        drag = 0.5*rho*self.Al*Cd*(V**2)
        drag = 0.0
        slip = 0.5*rho*self.Al*Cs*(V**2)

        forces = np.array([-drag, -lift, slip])
        return forces

    def getMoments(self, rho, V, C_w_b, deflect):
        V = V*C_w_b[0,0]
        rVfrac = rho*V/self.rVmax

        L = rVfrac*(deflect[0]**3)*self.Lmax
        M = rVfrac*(deflect[1]**3)*self.Mmax
        N = rVfrac*(deflect[2]**3)*self.Nmax

        return np.array([L,M,N])
    
    def getLift(self, alpha):
        Cl = 0.1*alpha

        return Cl

    def getDrag(self, alpha):
        Cd = 0.05*alpha + 0.2

        return Cd

    def getSlip(self, beta):
        Cs = 0.05*beta

        return Cs
