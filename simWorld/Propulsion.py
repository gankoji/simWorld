import numpy as np
import math
import ElMotor

unitTest = False

def clamp(val, lim):
    if val >= lim:
        val = lim
    elif val <= 0.0:
        val = 0.0
        
    return val

class Propulsion:
    def __init__(self):
        self.Motors = []
        self.Motors.append(ElMotor.ElMotor(np.eye(3), np.array([0.0, 0.25, 0.0])))
        self.Motors.append(ElMotor.ElMotor(np.eye(3), np.array([0.0,-0.25, 0.0])))
        self.nMotors = 2
        
    def getForces(self, rho, Vb, throttle):
        Fsum = np.zeros((3,))
        f = np.zeros((3,self.nMotors))
        
        for i in range(0,self.nMotors):
            f[:,i] = self.Motors[i].getForces(rho,Vb,throttle)
            Fsum += np.dot(self.Motors[i].getRotToBody(), f[:,i])

        return Fsum

    def getMoments(self, rho, Vb, throttle):
        Msum = np.zeros((3,))
        r = np.zeros((3,self.nMotors))
        R = np.zeros((3,3,self.nMotors))
        f = np.zeros((3,self.nMotors))
        m = np.zeros((3,self.nMotors))
        
        for i in range(0,self.nMotors):
            r[:,i] = self.Motors[i].getDispToBody()
            R[:,:,i] = self.Motors[i].getRotToBody()
            f[:,i] = self.Motors[i].getForces(rho,Vb,throttle)
            m[:,i] = self.Motors[i].getMoments(rho,Vb,throttle)
            
            Msum += np.dot(R[:,:,i],m[:,i])
            Msum += np.cross(r[:,i],np.dot(R[:,:,i],f[:,i]))
            
        return Msum

if unitTest:
    prop = Propulsion()
    print(prop.getForces(1.45, np.array([10,0,0]),1.0))    
    print(prop.getMoments(1.45, np.array([10,0,0]),1.0))
