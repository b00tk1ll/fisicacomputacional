# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:48:29 2017

@author: UFVJM
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

def lorenz(x,y,z, s=10.0, f=28.0, b=2.667):
    x_dot = s*(y-x)
    y_dot = f*x-y-x*z
    z_dot = x*y -b*z
    return x_dot, y_dot, z_dot
num_steps = 10000
dt=0.01
xs= np.zeros((num_steps+1))
ys= np.zeros((num_steps+1))
zs= np.zeros((num_steps+1))
xs[0],ys[0],zs[0]=(0.0,1.0,1.05)
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i],ys[i], zs[i])
    xs[i+1] = xs[i]+(x_dot * dt)
    ys[i+1] = ys[i]+(y_dot * dt)
    zs[i+1] = zs[i]+(z_dot * dt)
fig=plt.figure()
ax = fig.gca(projection='3d')
ax.plot(xs, ys, zs)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('z Axis')
ax.set_title('Lorenz Atractor')
plt.show()