# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

# The equation is:
# V(t) = A exp(-alpha * t) + Bexp(-beta * t)
# t is time in days
# V is the viral load
time = np.linspace(0, 1, 101)
A = 10
B = 10
alpha = 0.1
beta = 0.1

# Calculate the viral load
viral_load = A * np.exp(-alpha * time) + B * np.exp(-beta * time)

# Plot viral load
Astring = 'A =' + str(A) + '\n'
Bstring = 'B =' + str(B) + '\n'
alphastring = 'alpha =' + str(alpha) + '\n'
betastring = 'beta =' + str(beta) + '\n'
sample = Astring + Bstring + alphastring + betastring
plt.plot(time, viral_load, label = sample)
plt.xlabel('Time (days)')
plt.ylabel('Viral load')
plt.legend()