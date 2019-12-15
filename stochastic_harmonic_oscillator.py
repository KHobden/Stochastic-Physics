#Stochastic Harmonic Oscillator
#Kieran Hobden
#15-Dec-'19

#We solve the 2nd order SDE modelling an oscillator with random forcing using integrating factors
#Now we plot the solution for the stochasted harmonic oscillator (i.e. no damping)

import numpy as np
import matplotlib.pyplot as plt

#Initialise variables
N = 1000
x_0 = 0.1; y_0 = 0.1
k = 0.1
rtk = np.sqrt(k) #Save square_root(k) for later use
h = 0.01

#Initialise position (x) and velocity (y) variables
x = np.zeros(N)
y = np.zeros(N)

#Initialise stochastic integrals
sine_sum = 0
cosine_sum = 0

#Compute solution
for t in np.arange(N):
    sine_sum += np.sin(rtk)*np.random.normal(0,1)
    cosine_sum += np.cos(rtk)*np.random.normal(0,1)
    x[t] = x_0*np.cos(rtk*t) + (y_0/rtk)*np.sin(rtk*t) + (h/rtk)*sine_sum
    y[t] = -x_0*rtk*np.sin(rtk*t) + y_0*np.cos(rtk*t) + h*cosine_sum

#Plot physical result and phase portrait    
plt.plot(np.arange(N),x)
plt.title("Stochastic Harmonic Oscillator - Position Against Time")
plt.xlabel("t")
plt.ylabel("x")
plt.show()

plt.plot(x,y)
plt.title("Stochastic Harmonic Oscillator - Phase Portrait")
plt.xlabel("x")
plt.ylabel("x'")
plt.show()
