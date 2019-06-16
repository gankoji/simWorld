import numpy as np
import math

debugAero = False
class Aerodynamics:
    def __init__(self):
        self.Cl = 1
        self.Cd = 0.005
        self.Al = 1
        self.Ad = 1
        self.Lmax = 3
        self.Mmax = 3
        self.Nmax = 3
        self.rVmax = 1.475*150

    def getForces(self, rho, V, C_w_b):
      
        alpha = math.asin(-C_w_b[2,0])
        beta = math.asin(C_w_b[0,1])

        Cl = self.getLift(alpha)
        Cd = self.getDrag(alpha)
        Cs = self.getSlip(beta)
        lift = 0.5*rho*self.Al*Cl*(V**2)
        drag = 0.5*rho*self.Al*Cd*(V**2)
        slip = 0.5*rho*self.Al*Cs*(V**2)

        dragSign = -np.sign(C_w_b[0,0])
        slipSign = -np.sign(C_w_b[1,1])
        liftSign = np.sign(C_w_b[2,2])
        forces = np.array([drag*dragSign, slip*slipSign, lift*liftSign])
        
        if debugAero:
            print("Alpha: " + str(alpha))
            print("Beta: " + str(beta))
            print("V: " + str(V))
            print("rhoV2: " + str(rho*V**2))
            print("Aero Forces Mag: " + str(np.linalg.norm(forces)))
            
        return forces

    def getMoments(self, rho, V, C_w_b, deflect):
        V = V*C_w_b[0,0]
        rVfrac = rho*V/self.rVmax

        L = rVfrac*(deflect[0]**3)*self.Lmax
        M = rVfrac*(deflect[1]**3)*self.Mmax
        N = rVfrac*(deflect[2]**3)*self.Nmax

        return np.array([L,M,N])
    
    def getLift(self, alpha):
        Cl = 0.1*alpha + 0.15

        return Cl

    def getDrag(self, alpha):
        Cd = 0.05*math.fabs(alpha) + 0.01

        return Cd

    def getSlip(self, beta):
        Cs = 0.05*math.fabs(beta)

        return Cs
