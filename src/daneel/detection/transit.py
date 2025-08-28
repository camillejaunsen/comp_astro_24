
# ana attempts the batman package quickstart
#10-25-24

import batman
import numpy as np
import matplotlib.pyplot as plt

# create a transitparams object to store the physical parameters describing the transit

#test planet: Kepler-549 Bb
# https://exoplanet.eu/catalog/kepler_549_bb--3626/
params = batman.TransitParams()
params.t0 = 0.                       #time of inferior conjunction
params.per = 42.9                    #orbital period
params.rp = 0.03                      #planet radius (in units of stellar radii)
params.a = 49.                       #semi-major axis (in units of stellar radii)
params.inc = 89.99                   #orbital inclination (in degrees)
params.ecc = 0.                      #eccentricity
params.w = 90.                       #longitude of periastron (in degrees)
params.u = [0.52, 0.15]                #limb darkening coefficients [u1, u2]
params.limb_dark = "quadratic"       #limb darkening model

# for circular orbits, batman uses the convention params.w = 90
# the units for params.t0 and params.per can be anything as long as they are consistent

# specify the times at which we wish to calculate the model
t = np.linspace(-0.05, 0.05, 100)

m = batman.TransitModel(params, t)    #initializes model
flux = m.light_curve(params)          #calculates light curve

plt.plot(t, flux)
plt.xlabel("Time from central transit")
plt.ylabel("Relative flux")
plt.show()
