# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:31:35 2017

@author: UFVJM
"""

import matplotlib.pyplot as plt
import numpy as np

iteracao = 100
indice = np.linspace (0, iteracao-1, iteracao)
x = np.linspace (0, iteracao-1, iteracao)

plt.plot (indice, x, 'bo', indice, x**1.3, 'g^', indice, x**1.5, 'y1')
plt.grid(color = '#ffff00', linestyle = 'dashed', linewidth=1)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()