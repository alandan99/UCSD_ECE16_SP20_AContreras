# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:09:21 2020

@author: alan2
"""

from Libraries.Connection import Connection
from Libraries.Visualization import Visualization
from Libraries.PPG import PPG
import sys
import numpy as np
import matplotlib.pyplot as plt
import time

class Wearable:
    def __init__(self, serial_name, baud_rate):
        self.connection = Connection(serial_name, baud_rate)# use the appropriate arguments)
        
    def collect_data(self, num_samples):
        
        #self.connection.setup_connection()
        self.connection.clear_data()
        self.connection.end_streaming()# 1. make sure data sending is stopped by ending streaming
        self.connection.start_streaming()# 2. start streaming data again
        # 3. collect num_samples as outlined here
        time.sleep(.01)
        x = self.connection.get_num_samples()
        while (self.connection.get_num_samples() < num_samples): # collect x samples
            try:
                  if self.connection.checkSerial():
                     self.connection.read_serial()
            except(Exception, KeyboardInterrupt):
                self.connection.end_streaming() # deal with exceptions in a meaningful way
                self.connection.close_connection()
                print("Exiting due to Keyboard Interrupt or Exception")
                sys.exit()
        time.sleep(.01)
        self.connection.end_streaming()# 4. end streaming
        time.sleep(.01)
    
    def run(self):
        global data_array
        self.collect_data(500)# number of samples to collect)
        self.connection.calc_sampling_rate()# calculate sampling rate
        data_array = self.connection.data_array
        np.savetxt("saved_dataArr.csv", data_array, delimiter=",")# save data
        arr_data_from_saved = np.genfromtxt("saved_dataArr.csv", delimiter=',')# read data
        myplotter = Visualization(arr_data_from_saved) # data received from Connection class)
        myplotter.plotData()
        
        heart_beat_array = arr_data_from_saved[:,4] * -1# store the HR data in PPGs signal attribute
        self.ppg = PPG(heart_beat_array)#ppg signal)
        bpm = self.ppg.calc_heart_rate()# calculate heart rate
        # heartbeat = 
        # plt.clf()# visualize filtered heartbeat
        # plt.plot(heartbeat)
        
        print("your heart rate is", bpm)#print(bpm)# print out heart rate on Python console
        plt.show()
        heartRate = str(bpm)
        self.connection.send_serial(heartRate)# return heart rate to Huzzah32 to display on OLED
        self.connection.close_connection()
        

def main():
    wearable = Wearable("COM4", 115200)
    wearable.run()

if __name__== "__main__":
    main()

