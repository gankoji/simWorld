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
                                                     np.eye(3), np.array([-0.5, 0.0, -0.1])))
        self.Surfaces.append(AeroSurface.AeroSurface(0.375, 
                                                     np.array([[1,0,0],
                                                               [0,0,1],
                                                               [0,-1,0]]), 
                                                     np.array([-0.5, 0.0, -0.25])))
        self.nSurfaces = 4

    def getForces(self, rho, Vb, wb):
        Fsum = np.zeros((3,))
        f = np.zeros((3,self.nSurfaces))
        
        for i in range(0,self.nSurfaces):
            C = self.Surfaces[i].getRotToBody()
            r = self.Surfaces[i].getDispToBody()
            Va = np.dot(C.transpose(),(Vb+ np.cross(r,wb)))
            f[:,i] = self.Surfaces[i].getForces(rho,Va)
            Fsum += np.dot(C, f[:,i])

        return Fsum

    def getMoments(self, rho, Vb, wb, deflect):
        Msum = np.zeros((3,))
        r = np.zeros((3,self.nSurfaces))
        R = np.zeros((3,3,self.nSurfaces))
        f = np.zeros((3,self.nSurfaces))
        m = np.zeros((3,self.nSurfaces))
        
        for i in range(0,self.nSurfaces):
            r[:,i] = self.Surfaces[i].getDispToBody()
            R[:,:,i] = self.Surfaces[i].getRotToBody()
            Va = np.dot(R[:,:,i].transpose(),(Vb + np.cross(r[:,i],wb)))
            f[:,i] = self.Surfaces[i].getForces(rho,Va)
            m[:,i] = self.Surfaces[i].getMoments(rho,Va,deflect)
            
            Msum += np.dot(R[:,:,i],m[:,i])
            Msum += np.cross(r[:,i],np.dot(R[:,:,i],f[:,i]))
            
        V = np.linalg.norm(Vb)
        rVfrac = rho*V/self.rVmax

        for i in range(0,3):
            Msum[i] += rVfrac*(deflect[i]**3)*self.Lmax

        return Msum
