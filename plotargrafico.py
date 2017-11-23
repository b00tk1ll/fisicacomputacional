# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:07:12 2017

@author: UFVJM
"""
import matplotlib.pyplot as plt
import numpy as np

iteracao = 100

indice = np.linspace (0, iteracao-1, iteracao)

x = np.linspace (0, iteracao-1, iteracao)

plt.plot(indice, x, color = '#0a0a0a', linestyle='dashed', linewidth=1, markerfacecolor='#ff0a0a')
plt.grid()
plt.show()