import numpy as np
import math

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
        self.gain = np.zeros((3,))
        self.bias = np.zeros((3,))
        
        self.gain[0] = 0.10 + 0.010*np.random.randn()
        self.gain[1] = 0.05 + 0.001*np.random.randn()
        self.gain[2] = 0.05 + 0.001*np.random.randn()
        
        self.bias[0] = 0.05 + 0.01*np.random.randn()
        self.bias[1] = 0.10 + 0.100*np.random.randn()
        self.bias[2] = 0.10 + 0.100*np.random.randn()

    def getForces(self, rho, Vb):
      
        V = np.linalg.norm(Vb)
        alpha = math.atan2(Vb[0],Vb[2])
        beta = math.atan2(Vb[0],Vb[1])

        Cl = self.getLift(alpha)
        Cd = self.getDrag(alpha)
        Cs = self.getSlip(beta)
        
        qA = 0.5*rho*self.Al*(V**2)
        lift = Cl*qA
        drag = Cd*qA
        slip = Cs*qA
        
        dragSign = -np.sign(Vb[0])
        slipSign = -np.sign(Vb[1])
        liftSign = -np.sign(Vb[2])
        forces = np.array([drag*dragSign, slip*slipSign, lift*liftSign])
        
        if debugAero:
            print("Alpha: " + str(alpha))
            print("Beta: " + str(beta))
            print("V: " + str(V))
            print("rhoV2: " + str(rho*V**2))
            print("Aero Forces Mag: " + str(np.linalg.norm(forces)))
            print("Ratio: " + str(np.linalg.norm(forces)/(rho*V**2)))
            
        return forces

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
