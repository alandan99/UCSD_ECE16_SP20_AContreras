# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:22:25 2020

@author: alan2
"""
import numpy as np
import matplotlib.pyplot as plt
 # Importing Data # 
data_set = "Data_10_078.csv"
s = np.genfromtxt(data_set, delimiter=',')

def calc_heart_rate(signal):
    
    signal = detrend(signal, 50) # filter the signal to remove baseline drifting
    signal = moving_average(signal, 5)# filter the signal to remove high frequency noise# 
    signal = normalize_signal(signal)# normalize the signal between 0 and 1
    der_signal = signal_diff(signal)# explore using the signal directly or potentially a gradient 
    
    plt.clf()
    plt.subplot(211)
    plt.plot(signal)
    plt.title(data_set)
    plt.subplot(212)
    plt.plot(der_signal)
    plt.show()
    th = der_signal > 0.07     #consider values above threshold
    th[1:][th[:-1] & th[1:]] = False    #find cases of first threshold crossing only 
    th = der_signal[th]     #use boolean th to get the amount of first threshold crossings
    beats = th.shape[0] #number of 
    
    bpm =  6*beats # calculate the beats (threshold crossings) per minute
    return bpm# return the calculated heart rate
    
def normalize_signal(signal):
    minvalue = np.amin(signal)# find the minimum of signal
    signal = signal - minvalue# subtract the minimum so the minimum of the signal is now zero

    maxval = np.amax(signal)# find the maximum of the new signal
    signal = signal / maxval# divide the signal by the maximum so the maximum becomes 1

    return signal # return the normalized signal
    
def moving_average(s, n_avg):
    ma = np.zeros(s.size)
    for i in np.arange(0, len(s)):
        ma[i] = np.mean(s[i:i+n_avg])
    return ma

def detrend(s,n_avg):
    ma = moving_average(s,n_avg)
    s = s- ma
    return  s # s minus the moving_average

def signal_diff(s):

    s_diff = np.diff(s) # calculate the gradient using np.diff
    s_diff = np.append(s_diff, 0) # np.diff returns one shorter, so need to add a 0
    return s_diff


def main():
    bpm = calc_heart_rate(s)
    print("HR in bpm: ",bpm )
    
main()