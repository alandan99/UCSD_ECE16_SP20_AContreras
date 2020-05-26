# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:09:07 2020

@author: alan2
"""
import matplotlib.pyplot as plt
import numpy as np

  #Importing Data # 
# data_set = "Data_04_078.csv"
# s = np.genfromtxt(data_set, delimiter=',')

class PPG:
    
    def __init__(self, signal): # set the signal attribute in the constructor
        self.signal = signal

    def moving_average(self, n_avg): # compute moving average of the signal
        s = self.signal
        ma = np.zeros(s.size)
        for i in np.arange(0, len(s)):
            ma[i] = np.mean(s[i:i+n_avg])
        return ma

    def detrend(self, n_avg): # detrend the signal
        s = self.signal
        ma = self.moving_average(n_avg)
        s = s - ma
        self.signal = s
        return  self.signal # s minus the moving_average

    def normalize_signal(self): # normalize the signal
        s = self.signal
        minvalue = np.amin(s)# find the minimum of signal
        s = s - minvalue# subtract the minimum so the minimum of the signal is now zero
        maxval = np.amax(s)# find the maximum of the new signal
        s = s / maxval# divide the signal by the maximum so the maximum becomes 1
        self.signal = s
        return self.signal
        
    def signal_diff(self): # compute the approximate gradient
        s = self.signal
        s_diff = np.diff(s) # calculate the gradient using np.diff
        s_diff = np.append(s_diff, 0) # np.diff returns one shorter, so need to add a 0
        return s_diff

    def calc_heart_rate(self): # calculate the heart rate
        
        self.detrend(50) # filter the signal to remove baseline drifting
        self.signal = self.moving_average(5)# filter the signal to remove high frequency noise# 
        signal = self.normalize_signal()# normalize the signal between 0 and 1
        plt.clf()
        plt.plot(signal)
       
        der_signal = self.signal_diff()# explore using the signal directly or potentially a gra
        th = der_signal > 0.07     #consider values above threshold
        th[1:][th[:-1] & th[1:]] = False    #find cases of first threshold crossing only 
        th = der_signal[th]     #use boolean th to get the amount of first threshold crossings
        beats = th.shape[0] #number of beats
    
        bpm =  6*beats # calculate the beats (threshold crossings) per minute
        return bpm# return the calculated heart rate
    
# def main():
#     signal = PPG(s)
#     hr = signal.calc_heart_rate()
#     print("heart rate: ",hr)
#     plt.show()
    
# main()
