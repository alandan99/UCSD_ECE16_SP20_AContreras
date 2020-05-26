# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:39:33 2020

@author: alan2
"""


import numpy as np
import sys
import serial
import time
import matplotlib.pyplot as plt
from Libraries.Connection import Connection
from Libraries.Visualization import Visualization

adafruit = Connection("COM4" , 115200) #BT PORT

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
    # try:
    #     adafruit.setup_connection()
    # except():
    #     adafruit.close_connection
    #     adafruit.clear_data()
    #     sys.exit()
        
        
    adafruit.clear_data()
    adafruit.start_streaming()
    time.sleep(.01)
    
    try:
      while (adafruit.get_num_samples() < 500):
        try:
            if adafruit.checkSerial():
              adafruit.read_serial()
              
        except(KeyboardInterrupt):
            adafruit.end_streaming()
            #adafruit.clear_data()
            adafruit.close_connection()
            print("Exiting due to Keyboard Interrupt")
            sys.exit()
    except: 
      print(adafruit.get_num_samples())
      adafruit.end_streaming()
      adafruit.close_connection()
      sys.exit()
      
    adafruit.end_streaming()
    time.sleep(.01)
    message = adafruit.calc_sampling_rate()
    adafruit.send_serial(message)
    time.sleep(.01)
    #myplotter = Visualization(adafruit.data_array)
    data_array = adafruit.data_array
    np.savetxt("data_array.csv", data_array, delimiter=",")
    data_array_saved = np.genfromtxt("data_array.csv", delimiter=',')
    time.sleep(.01)
    #s = data_array_saved[:, 4]
    # x = detrend(s, 3)
    # plt.plot(x)
    # plt.show()
    myplotter = Visualization(data_array_saved)
    
    
    myplotter.plotData()
    
    
    adafruit.clear_data()
    adafruit.close_connection()
    
    sys.exit()
    
if __name__ == "__main__":
    main()





#np.savetxt("data_array.csv", data_array, delimiter=",")
#data_array_saved = np.genfromtxt('foo.csv', delimiter=',')
