# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 10:46:37 2023

@author: atran
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit

# We fit experimental data to our viral load equation

# We opened the HIVseries.csv file and coverted the data to float
hiv_data_location = os.path.abspath("C:\\Users\\atran\\OneDrive\\Desktop\\HIV_project_class\\HIVseries.csv")
hiv_data_string = np.genfromtxt(fname=hiv_data_location, delimiter=',', dtype='unicode')
hiv_data = hiv_data_string.astype(np.float)

# Define the array
time = hiv_data[:,0]
viral_load = hiv_data[:,1]

# Plot the data
plt.scatter(time, viral_load, label='Experimental Data')
plt.xlabel('Time (days)')
plt.ylabel('Viral load')
plt.legend()

# We try to fit the data to the model
def model(time_model, A, B, alpha, beta):
# V(t) = Aexp(-alpha*t) + Bexp(-beta*t)\
    viral_load_model = A*np.exp(-alpha*time_model) + B*np.exp(-beta*time_model)
    return viral_load_model

guess_parameters = (90000,70000,3,3)
parameters, covariance = curve_fit(model, time, viral_load, guess_parameters)
fit_A = parameters[0]
fit_B = parameters[1]
fit_alpha = parameters[2]
fit_beta = parameters[3]

# Plot the fitted curve on top of the data points
time_array = np.linspace(0, 7, 100)
fit_viral_load = model(time_array, fit_A, fit_B, fit_alpha, fit_beta)
plt.plot(time_array, fit_viral_load, '-', label='fit')
plt.legend()

# Standard error
SE = np.sqrt(np.diag(covariance))
SE_A = SE[0]
SE_B = SE[1]
SE_alpha = SE[2]
SE_beta = SE[3]