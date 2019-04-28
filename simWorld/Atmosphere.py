import numpy as np
import math

FT2METERS = 0.3048      # mult. ft. to get meters (exact)
KELVIN2RANKINE = 1.8    # mult deg K to get deg R
PSF2NSM = 47.880258     # mult lb/sq.ft to get sq.m
SCF2KCM = 515.379       # mult slugs/cu.ft to get kg/cu.m
TZERO   = 288.15        # sea-level temperature, kelvins
PZERO   = 101325.0      # sea-level pressure, N/sq.m
RHOZERO = 1.225         # sea-level density, kg/cu.m
AZERO   = 340.294       # speed of sound at S.L.  m/sec
BETAVISC = 1.458E-6     # viscosity constant
SUTH    = 110.4         # Sutherland's constant, kelvins

class Atmosphere:
    def __init__(self):
        self.table = np.zeros((45, 7))
        for i in range(-1,44):
            altKm=2*i
            (sigma, delta, theta) = self.Atmosphere(altKm)

            temp=TZERO*theta
            pressure=PZERO*delta
            density=RHOZERO*sigma
            asound=AZERO*math.sqrt(theta)
            viscosity= self.MetricViscosity(theta)
            kinematicViscosity=viscosity/density
            viscosity = 1.0e6*viscosity

            self.table[i+1, 0] = altKm
            self.table[i+1, 1] = temp
            self.table[i+1, 2] = pressure
            self.table[i+1, 3] = density
            self.table[i+1, 4] = asound
            self.table[i+1, 5] = viscosity
            self.table[i+1, 6] = kinematicViscosity

    def Atmosphere(self, alt):
        """ Compute temperature, density, and pressure in standard
        atmosphere.  Correct to 86 km.  Only approximate thereafter.
        Input: alt geometric altitude, km.  Return: (sigma, delta,
        theta) sigma density/sea-level standard density delta
        pressure/sea-level standard pressure theta
        temperature/sea-level std. temperature """

        REARTH = 6369.0     # radius of the Earth (km)
        GMR = 34.163195
        NTAB = 8            # length of tables

        htab = [ 0.0,  11.0, 20.0, 32.0, 47.0,
                 51.0, 71.0, 84.852 ]
        ttab = [ 288.15, 216.65, 216.65, 228.65, 270.65,
                 270.65, 214.65, 186.946 ]
        ptab = [ 1.0, 2.2336110E-1, 5.4032950E-2, 8.5666784E-3,
                 1.0945601E-3,6.6063531E-4, 3.9046834E-5, 3.68501E-6 ]
        gtab = [ -6.5, 0.0, 1.0, 2.8, 0, -2.8, -2.0, 0.0 ]
        
        ## geometric to geopotential altitude
        h = alt*REARTH/(alt+REARTH)

        i=0; j=len(htab)-1
        while (j > i+1):
            k = (i+j)//2      # this is floor division in Python 3
            if h < htab[k]:
                j = k
            else:
                i = k
                
        tgrad = gtab[i]     # temp. gradient of local layer
        tbase = ttab[i]     # base  temp. of local layer
        deltah=h-htab[i]        # height above local base
        tlocal=tbase+tgrad*deltah   # local temperature
        theta = tlocal/ttab[0]  # temperature ratio

        if 0.0 == tgrad:
            delta=ptab[i]*math.exp(-GMR*deltah/tbase)
        else:
            delta=ptab[i]*math.pow(tbase/tlocal, GMR/tgrad)
            
        sigma = delta/theta
        return ( sigma, delta, theta )

    def MetricViscosity(self, theta):
        t=theta*TZERO
        return BETAVISC*math.sqrt(t*t*t)/(t+SUTH)

    def getRho(self, altKm):
        rho = np.interp(altKm, self.table[:,0], self.table[:, 3])
        return rho

