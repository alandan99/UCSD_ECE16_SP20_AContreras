# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:53:30 2020

@author: alan2
"""
import numpy as np

data_array = np.genfromtxt("data_array.csv", delimiter=',')
heart_beat_array = data_array[:,4] * -1
np.savetxt("Data_05_078.csv", heart_beat_array, delimiter=",")