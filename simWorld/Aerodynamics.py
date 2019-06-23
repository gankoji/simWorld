import numpy as np
import math
import AeroSurface

debugAero = False

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

class Aerodynamics:
    def __init__(self):
        self.Al = 1
        self.Ad = 1
        self.Lmax = 3
        self.Mmax = 3
        self.Nmax = 3
        self.rVmax = 1.475*150

        self.Surfaces = []
        self.Surfaces.append(AeroSurface.AeroSurface(1.0, 
                                                     np.eye(3), np.array([0.0, 0.25, 0.0])))
        self.Surfaces.append(AeroSurface.AeroSurface(1.0, 
                                                     np.eye(3), np.array([0.0,-0.25, 0.0])))
        self.Surfaces.append(AeroSurface.AeroSurface(0.5, 
                                                     np.eye(3), np.array([-0.75, 0.0, -0.1])))
        self.Surfaces.append(AeroSurface.AeroSurface(0.375, 
                                                     np.array([[1,0,0],
                                                               [0,0,1],
                                                               [0,-1,0]]), 
                                                     np.array([-0.75, 0.0, -0.25])))
        self.nSurfaces = 4

    def getForces(self, rho, Vb):
        Fsum = np.zeros((3,))
        f = np.zeros((3,self.nSurfaces))
        
        for i in range(0,self.nSurfaces):
            C = self.Surfaces[i].getRotToBody()
            Va = np.dot(C.transpose(),Vb)
            f[:,i] = self.Surfaces[i].getForces(rho,Va)
            Fsum += np.dot(C, f[:,i])

        return Fsum

    def getMoments(self, rho, Vb, deflect):
        V = np.linalg.norm(Vb)
        rVfrac = rho*V/self.rVmax

        L = rVfrac*(deflect[0]**3)*self.Lmax
        M = rVfrac*(deflect[1]**3)*self.Mmax
        N = rVfrac*(deflect[2]**3)*self.Nmax

        return np.array([L,M,N])
    
    def getLift(self, alpha):
        Cl = self.gain[0]*alpha + self.bias[0]
        Cl = biClamp(Cl, 0.45)
        return Cl

    def getDrag(self, alpha):
        Cd = self.gain[1]*math.fabs(alpha) + self.bias[1]
        Cd = clamp(Cd, 0.99)
        return Cd

    def getSlip(self, beta):
        Cs = self.gain[2]*math.fabs(beta) + self.bias[2]
        Cs = clamp(Cs, 0.99)
            
        return Cs
