# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np
from scipy.integrate import odeint

def lotka (y, t, alfa, beta, gamma, delta):
    x1, y1 = y
    dydt= [alfa*x1-beta*x1*y1, gamma*x1*y1-delta*y1]
    return dydt
alfa=2.0/.30
beta=2.0/3.0
gamma=1.0
delta=1.0
tfinal=10.0
x = np.zeros((2,1000))
index=np.linspace(0,tfinal-1,tfinal*10)
y0=[0.9,0.9]
x = odeint (lotka,y0,index,args=(alfa,beta,gamma,delta))
np.savetxt ("out.dat", x)