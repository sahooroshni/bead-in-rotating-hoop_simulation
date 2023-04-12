# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:52:11 2021

@author: roshn
"""


import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint,ode 


#mass of bead 
m = 0.01 #kg

#angular velocity of rotating hoop 
w = 40 #rads-1

#radius of the rotating hoop 
R = 0.05 #m 

#gravitational constant 
g = 9.8 #ms-2

#angle that hoop makes with vertical 
alpha = 0.2  #radian 

def bead_on_tilted_hoop(x,t,w,R,a):
    theta,z = x 
    thetadot = z 
    zdot = np.sin(theta)*(((w**2)*np.cos(theta)) - (g*np.cos(alpha)/R)) + ((g*np.cos(theta)*np.sin(alpha))/R)
    return (thetadot, zdot)

#initial condition: theta(radian), thetadot(radian/s)

x0 = [1.1050528763418,0]
#x0 = [np.arccos(g*np.cos(alpha)/(R*w**2)),0]
#time coordinate to solve the ODE for: from 0 to 60 seconds
t = np.linspace(0,10,3000)

#solving the ODE 
sol = odeint(bead_on_tilted_hoop,x0,t,args=(w,R,alpha))
    

# plot the angle as a function of time 
fig= plt.figure(figsize=(12,4))
ax = plt.axes()
ax.plot(t, sol[:, 0]*(180/np.pi), 'g', label='$\\theta_o$ = {}\n $\\alpha$ = {} '.format(x0[0]*(180/np.pi),alpha*(180/np.pi)))   #unpacking theta
ax.set_title('$\\theta$ (degree) vs time(s)',fontsize='20')
ax.set_xlabel("time (seconds)",fontsize='20')
ax.set_ylabel('$\\theta$ (degree)', fontsize = '20')
ax.legend(loc='upper right',fontsize='20')
#ax.set_ylim(77.0,77.9)

#3-D plotting 
from mpl_toolkits.mplot3d import Axes3D
    
theta = sol[:,0]        #in radian
phi = w*t                #wt in radian

X = R*np.cos(phi)*np.sin(theta-alpha)
Y = R*np.sin(phi)*np.sin(theta-alpha) 
Z = -R*np.cos(theta-alpha)
fig= plt.figure(figsize=(12,4))
ax = plt.axes(projection ='3d')
p = ax.plot3D(X,Y,Z,c='magenta')
ax.set_title('Cartesian co-ordinate of bead on a tilted rotating hoop',fontsize='20')
ax.set_xlabel("x",fontsize='20')
ax.set_ylabel("y", fontsize = '20')
ax.set_zlabel("z", fontsize = '20')