import matplotlib.pyplot as plt

import numpy as np

import math 

def funcoesexterna (a,omega,iteracoes):
    
     for i in range(0,iteracoes): 
         a[i]=math.sin(omega*i)
         
         
iteracoes=100
omega1 =0.1
omega2 = 0.3
 
a = np.linspace(0,iteracoes-1,iteracoes)
indice = np.linspace(0,iteracoes-1,iteracoes)
b = np.linspace (0,iteracoes-1,iteracoes)
 
funcoesexterna(a,omega1,iteracoes)
funcoesexterna(b,omega2,iteracoes)
 
plt.figure(1)
 
plt.subplot(211)
 
plt.plot(indice,a,color='#00ffff',linewidth = 2)

plt.grid()
plt.xlabel('i')
plt.ylabel('y(i)')

plt.subplot(212)
plt.plot(indice,b,color ='#00ffff',linewidth = 2)

plt.grid ()

plt.xlabel('i')
plt.ylabel('y(i)')

plt.show()