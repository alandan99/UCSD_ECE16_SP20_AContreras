# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:39:50 2020

@author: alan2
"""

import sys
import serial
import time
from Libraries.Connection import Connection
from Libraries.Visualization import Visualization

adafruit = Connection("COM3" , 115200)




def main():
    try:
        adafruit.setup_connection()
    except():
        adafruit.close_connection
        adafruit.clear_data()
        sys.exit()
        
        
    adafruit.clear_data()
    adafruit.start_streaming()
    time.sleep(.01)
    
    try:
      while (adafruit.get_num_samples() < 100):
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
    my_plotter = Visualization(adafruit.data_array)
    my_plotter.plotAccel()
    
    adafruit.clear_data()
    adafruit.close_connection()
    
    sys.exit()
    
if __name__ == "__main__":
    main()