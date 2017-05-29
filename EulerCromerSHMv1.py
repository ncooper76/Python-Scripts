#This script tests Simple Harmonic Oscillator using the Euler Cromer method
#This will show that the Euler Cromer method is stable for SHM
#import numpy as np
import matplotlib.pyplot as plt
#from math import sin
#from math import cos
from math import pi


theta_i = 0  # this is the initial angluar coordinate of the SHM
theta = [theta_i] # stores the angular position
del_t = 0.01 # time step in seconds
t_i = 0# initial time coordinate
t = [t_i] # stores t for graphing
omega_i = 2*pi #initial angular speed in radians/second
omega = [omega_i] # stores the anular speed
i = 0 # list iteration
g = 9.81 # Earth Surface Gravity in m/s^2
l = 1 # length of osillator in meters
KE = [(0.5*l**2)*omega[i]**2]
PE = [(0.5*g*l)*theta[i]**2] #height is l*(1-cos) small angle approx
# for cosine is 1-theta**2/2

while(i < 2000):   # maps out the oscillation for 20 seconds
#The difference is that omega is appended first and theta uses
#the appended omega
    omega.append(omega[i] - (g/l)*theta[i]*del_t)
    theta.append(theta[i] + omega[i+1]*del_t)
    KE.append((0.5*l**2)*omega[i]**2)
    PE.append((0.5*g*l)*theta[i]**2)
    t.append(t[i] + del_t)
    i += 1

plt.scatter(t,theta) #Amplitude stays the same
plt.xlabel('time in s')
plt.ylabel('angle in rad')
plt.show()
plt.scatter(t,KE)
plt.scatter(t,PE)
plt.xlabel('time in s')
plt.ylabel('Energy in Joules') 
plt.show()
