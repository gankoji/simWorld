import numpy as np
import math

pi = 3.1415926
r2d = 180.0/pi
d2r = pi/180.0

def EulD2Quat(eul):
    # Assumes angles are YPR
    # Builds the ZYX rotation
    
    eul = eul*d2r
    quat = Eul2Quat(eul)
    return quat

def Eul2Quat(eul):
    halfAngles = eul/2

    a = math.cos(halfAngles[2])
    b = math.cos(halfAngles[1])
    c = math.cos(halfAngles[0])

    d = math.sin(halfAngles[2])
    e = math.sin(halfAngles[1])
    f = math.sin(halfAngles[0])

    q = np.zeros((4,))

    q[0] = a*b*c + d*e*f
    q[1] = d*b*c - a*e*f
    q[2] = a*e*c + d*b*f
    q[3] = a*b*f - d*e*c

    q = q/np.linalg.norm(q)
    return q

def EulD2DCM(eul):
    eul = eul*d2r
    dcm = Eul2DCM(eul)
    return dcm

def Eul2DCM(eul):
    # Assumes eul is YPR
    # Builds the ZYX rotation
    dcm = np.dot(C_z(eul[0]),np.dot(C_y(eul[1]),C_x(eul[2])))
    return dcm

def Quat2Eul(q):
    # Returns the euler angles YPR
    # Assumes a ZYX quaternion
    phi   = math.atan2(2*(q[0]*q[1] + q[2]*q[3]), 1 - 2*(q[1]**2 + q[2]**2))
    theta = math.asin(2*(q[0]*q[2] - q[3]*q[1]))
    psi   = math.atan2(2*(q[0]*q[3] + q[1]*q[2]), 1 - 2*(q[2]**2 + q[3]**2))

    eul = np.array([psi, theta, phi])
    return eul

def DCM2Quat(dcm):
    q = np.zeros((4,))

    q[0] = 0.5*math.sqrt(dcm[0][0] + dcm[1][1] + dcm[2][2] + 1)
    q[1] = (dcm[1][2] - dcm[2][1])/(4*q[0])
    q[2] = (dcm[2][0] - dcm[0][2])/(4*q[0])
    q[3] = (dcm[0][1] - dcm[1][0])/(4*q[0])

    q = q/np.linalg.norm(q)
    return q

def Quat2DCM(q):
    # Convert a quaternion rotation operator to an equivalent
    # rotation matrix

    C = np.zeros((3,3))

    C[0,0] = q[0]**2 + q[1]**2 - q[2]**2 - q[3]**2
    C[0,1] = 2*(q[1]*q[2] - q[0]*q[3])
    C[0,2] = 2*(q[0]*q[2] + q[1]*q[3])

    C[1,0] = 2*(q[1]*q[2] + q[0]*q[3])
    C[1,1] = q[0]**2 - q[1]**2 + q[2]**2 - q[3]**2
    C[1,2] = 2*(q[2]*q[3] - q[0]*q[1])

    C[2,0] = 2*(q[1]*q[3] - q[0]*q[2])        
    C[2,1] = 2*(q[0]*q[1] + q[2]*q[3])
    C[2,2] = q[0]**2 - q[1]**2 - q[2]**2 + q[3]**2

    return C
    

## Lower level utilities used by the library

def C_x(theta):
    # Standard active-sense right handed rotation about the X axis

    ct = math.cos(theta)
    st = math.sin(theta)

    c = np.array([[1,  0,   0],
                  [0, ct, -st],
                  [0, st,  ct]])

    return c

def C_y(theta):
    # Standard active-sense right handed rotation about the Y axis

    ct = math.cos(theta)
    st = math.sin(theta)

    c = np.array([[ ct,   0,   st],
                  [  0,   1,    0],
                  [-st,   0,   ct]])

    return c

def C_z(theta):
    # Standard active-sense right handed rotation about the Z axis

    ct = math.cos(theta)
    st = math.sin(theta)

    c = np.array([[ct, -st,  0],
                  [st,  ct,  0],
                  [ 0,   0,  1]])

    return c

def quatMult(p,q):
    out = np.zeros((4,))
    r1 = p[0]
    r2 = q[0]
    v1 = p[1:4]
    v2 = q[1:4]
    
    scalar = r1*r2 - np.dot(v1,v2)
    vector = r1*v2 + r2*v1
    cross = np.cross(v1, v2)
    vector += cross

    out[0] = scalar
    out[1:4] = vector

    return out

def DCM2Eul(dcm):
    th = math.acos((dcm[0][0] + dcm[1][1] + dcm[2][2] - 1)/2.0)

    if (th - 3.1415926) <= .001:
        eul = np.array([0,0,0])
    else:
        a = 2*math.sin(th)

        phi = (dcm[2][1] - dcm[1][2])/a
        theta = (dcm[0][2] - dcm[2][0])/a
        psi = (dcm[1][0] - dcm[0][1])/a

        eul = np.array([psi, theta, phi])

    return eul

def DCM2AxisAngle(dcm):
    b = 0.5*(dcm[0][0] + dcm[1][1] + dcm[2][2] - 1)
    if b > 1.0:
        b = 1.0
    elif b < -1.0:
        b = -1.0

    theta = math.acos(b)

    if theta > 0.001:
        a = 2*math.sin(theta)
        
        e1 = (dcm[2][1] - dcm[1][2])/a
        e2 = (dcm[0][2] - dcm[2][0])/a
        e3 = (dcm[1][0] - dcm[0][1])/a

        beta = np.array([a, e1, e2, e3])
    else:
        beta = np.zeros((4,))

    return beta

def Quat2AxisAngle(q):
    qbar = q[1:4]
    e = qbar/np.linalg.norm(qbar)

    theta = 2*math.acos(q[0])

    beta = np.append([theta], e, axis=0)
    return beta
