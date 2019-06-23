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

class AeroSurface:
    def __init__(self):
        self.Al = 2
        self.Ad = 1
        
        self.aTable  = np.array([-180,-90,-60,-45,-30,-15,-10,-5,
                                 0,5,10,15,30,45,60,90,180])
        self.ClTable = np.array([   0.5,0.00,-0.01,-0.1,-.025,-0.95, -0.75, -0.6,
                                    0,0.5,0.75, 0.99,0.5,0.25,0.01,0.0, -0.5]) 
        self.CdTable = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 0.1, 0.05, 0.025,
                                 0.01, 0.025, 0.05, 0.1, 1.0, 1.0, 1.0, 1.0, 1.0])
        self.aTable = self.aTable*math.pi/180.0

    def getForces(self, rho, Vb):
      
        V = np.linalg.norm(Vb)
        alpha = math.atan2(Vb[2],Vb[0])
        beta = math.atan2(Vb[1],Vb[0])

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
            print("Vb: " + str(Vb))
            print("Forces: " + str(forces))
            print("rhoV2: " + str(rho*V**2))
            print("Aero Forces Mag: " + str(np.linalg.norm(forces)))
            print("Ratio: " + str(np.linalg.norm(forces)/(rho*V**2)))
            print("ForceDot: " + str(np.dot(Vb, forces)/V/np.linalg.norm(forces)))    
        return forces

    def getMoments(self, rho, Vb, deflect):
        V = np.linalg.norm(Vb)
        rVfrac = rho*V/120.0

        L = rVfrac*(deflect[0]**3)*1.0
        M = rVfrac*(deflect[1]**3)*1.0
        N = rVfrac*(deflect[2]**3)*1.0

        return np.array([L,M,N])
    
    def getLift(self, alpha):
        Cl = np.interp(alpha, self.aTable, self.ClTable)
        return Cl

    def getDrag(self, alpha):
        Cd = np.interp(alpha, self.aTable, self.CdTable)
        return Cd

    def getSlip(self, beta):
        Cs = np.interp(beta, self.aTable, self.CdTable)
        return Cs
