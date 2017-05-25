#Calculates a baseball trajectory with air reistance and plots
import numpy as np
import matplotlib.pyplot as plt
from math import sin
from math import cos
from math import pi

x_ideal = []  #the no resistance x coordinates will be stored here
x_real = [] #the resistance x coords here
y_ideal = [] #the no resistance y coordinates will be stored here
y_real = [] #the resistance y coords here
delta_t = 0.00 #this is the time increment to be added to t
initial_angle = 0.00 #this is the angle that the projectile at launch
g = -9.81 #Earth's Surface Gravity in m*s^-2
alpha = 1.23 #air density in kg/m^3
C = 0.47 # drag coeffiencient of a sphere
area = 0.004185386813 #cross sectional area of a baseball in m^2
mass = 0.145 #mass of a baseball in kg


#Now to set up the initial conditions
x_ideal.append(float(input("How far above the ground in meters does the projectile start?")))
x_real.append(x_ideal[0])
y_ideal.append(float(input("What is your horizontal distance from the projectile in meters at the start?")))
delta_t  = float(input("How small of a time step, in fractions of a second, between data points? "))
y_real.append(y_ideal[0])
initial_speed = float(input("What is the initial speed of the projectile in m/s?"))
initial_angle  = float(input("What's your launch angle above the ground in degrees?"))
rad_angle = float(initial_angle)*pi/180

#First no air resistance
vi_x = initial_speed*cos(rad_angle)#the velocity in the x direction ideal loop
vr_x = initial_speed*cos(rad_angle) #the velocity in the x direction real loop
vi_y = initial_speed*sin(rad_angle)#the velocity in the y direction ideal loop
vr_y = initial_speed*sin(rad_angle)#the velocity in the y direction real loop
i = 0 #while iteration
while y_ideal[i] >= 0:
    x_ideal.append(x_ideal[i] + vi_x*delta_t)
    y_ideal.append(y_ideal[i] + vi_y*delta_t)
    vi_y = vi_y + g*delta_t
    i += 1
    #print("X:"+str(x_coordinates[i]) +"\n"+ "Y:"+str(y_coordinates[i]) + "\n")

#now with air resistance
# The drag force is 1/2*air density*drag coeffiecient*cross sectional area*speed^2
# vx*v is the same as v**2*cosine, dividing by mass gives acceleration
j = 0 #while iteration
while y_real[j] >= 0:
    vr = (vr_x**2 + vr_y**2)**0.5 # speed of the ball
    x_real.append(x_real[j] + vr_x*delta_t)
    vr_x = vr_x - 0.5*alpha*C*area*vr*vr_x*delta_t/mass
    y_real.append(y_real[j] +vr_y*delta_t)
    vr_y = vr_y + g*delta_t - 0.5*alpha*C*area*vr*vr_y*delta_t/mass
    j += 1
    #print("X:"+str(x_real[j]) +"\n"+ "Y:"+str(y_real[j]) + "\n")
plt.scatter(x_ideal,y_ideal)
plt.scatter(x_real,y_real)
plt.show()

