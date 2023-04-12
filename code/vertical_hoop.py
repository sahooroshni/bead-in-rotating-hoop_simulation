# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 19:17:19 2021

@author: roshn
"""

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint,ode 


#mass of bead 
m = 0.01 #kg

#angular velocity of rotating hoop 
w = 20 #rads-1

#radius of the rotating hoop 
R = 0.05 #m 

#gravitational constant 
g = 9.8 #ms-2

def bead_on_hoop(x,t,w,R):
    theta,z = x 
    thetadot = z 
    zdot = np.sin(theta)*((w**2)*np.cos(theta) - (g/R))
    return (thetadot, zdot)

#initial condition: theta(radian), thetadot(radian/s)
#x0 = [2*(np.pi/180),0]
x0 = [-np.arccos(g/(R*w**2))+0.005,0]

#time coordinate to solve the ODE for: from 0 to 60 seconds
t = np.linspace(0,60,6000)

#solving the ODE 
sol = odeint(bead_on_hoop,x0,t,args=(w,R))

# plot the angle as a function of time
fig= plt.figure(figsize=(12,4))
ax = plt.axes()
ax.plot(t, sol[:, 0]*(180/np.pi), 'g',label='$\\theta_o$ = {}'.format(x0[0]*(180/np.pi)))   #unpacking theta
ax.set_title('$\\theta$ (degree) vs time(s)',fontsize='20')
ax.set_xlabel("time (seconds)",fontsize='20')
ax.set_ylabel("$\\theta$ (degree)", fontsize = '20')
ax.legend(loc='upper right',fontsize = '20')

#3-D plotting 
from mpl_toolkits.mplot3d import Axes3D

theta = sol[:,0]        #in radian
phi = w*t                #wt in radian

X = R*np.cos(phi)*np.sin(theta)
Y = R*np.sin(phi)*np.sin(theta)
Z = -R*np.cos(theta)
fig= plt.figure(figsize=(12,4))
ax = plt.axes(projection ='3d')
p = ax.plot3D(X,Y,Z,c='b')
ax.set_title('Cartesian co-ordinate of bead on a vertical rotating hoop',fontsize='20')
ax.set_xlabel("x",fontsize='20')
ax.set_ylabel("y", fontsize = '20')
ax.set_zlabel("z", fontsize = '20')


