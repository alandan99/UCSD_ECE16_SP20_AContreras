# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:33:42 2020

@author: alan2
"""

import numpy as np
import matplotlib.pyplot as plt


#data_array_from_file = np.genfromtxt('foo.csv', delimiter=',')
s = np.genfromtxt("Data_01_084.csv", delimiter=',')


#s = data_array_from_file[:,3] #get the z axis
# mean_s = np.mean(s)#take the mean of s with numpy
# s = s - mean_s # subtract off the mean

def moving_average(s, n_avg):
    ma = np.zeros(s.size)
    for i in np.arange(0, len(s)):
        ma[i] = np.mean(s[i:i+n_avg])
    return ma

#remove the moving average from the signal
def detrend(s,n_avg):
    ma = moving_average(s,n_avg)
    s = s- ma
    return  s # s minus the moving_average

def signal_diff(s):
    s_diff = np.diff(s) # calculate the gradient using np.diff
    s_diff = np.append(s_diff, 0) # np.diff returns one shorter, so need to add a 0
    return s_diff


def main():
    x = detrend(s, 100)
    y = moving_average(x, 5)
    z = signal_diff(y)
    
    #z = detrend(y, 2)
    plt.clf()
    print("detrend plot:")
    plt.plot(x)
    plt.show()
    print("smooth plot:")
    plt.clf()
    plt.plot(z)
    plt.show()
    # print("smooth mean move")
    # plt.clf()
    # plt.plot(z)
    # plt.show()
    # print("diff plot:")
    # plt.clf()
    # plt.plot(y)
    # plt.show()
    
main()

