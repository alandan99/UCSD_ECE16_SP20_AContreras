# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:50:15 2020

@author: alan2
"""
import serial
import time
import sys
import numpy as np
import matplotlib.pyplot as plt

#These two variables are global
string_buffer = []
data_array = np.array([])
sample_number = 0
x = []

def setup_serial():
    serial_name = "COM4"
    ser = serial.Serial(serial_name, 115200)  # open serial port
    print(ser.name)         # check which port was really used
    return ser

def parse_input( input_char ):   
    global string_buffer
    global data_array
    global sample_number
    
    if( input_char == '\n' ):
        # data_string will contain the cumulative buffer of newline
        # (‘\n’) separated lines data (See Hint (2) below for help)
        data_string = ''.join(string_buffer)# join with the contents of string_buffer
        sample_number += 1
        #print(data_string)
        np_buffer = np.fromstring(data_string, dtype=int, sep=',')# convert CSV string_buffer to a 1x4 ndarray
        if (data_array.size == 0): # data_array is empty ):
            data_array = np_buffer
            #data_array = np.vstack((data_array, np_buffer))
        else:
            data_array = np.vstack((data_array, np_buffer))# vstack np_buffer to data_array
        string_buffer = [] # reset string_buffer to []
    else:
        string_buffer.append(input_char)# append the input_char to string_buffer


def receive_sample(ser):
    global string_buffer
    global data_array
    
    c = ser.read(1).decode('utf-8') # read a byte from Serial (remember to decode)
    parse_input(c) # same function as in the offline code

def send_start(ser):
    S = 'start data\n'         
    ser.write(S.encode('utf-8'))         # write a string

def send_stop(ser):
     S = 'stop data\n'         
     ser.write(S.encode('utf-8'))         # write a string

# Send start data
def receive_data(ser):
    global sample_number
    global data_array
    while sample_number < 100 :    
    #while True:
       try:
           receive_sample(ser)
           
       except(KeyboardInterrupt):
           send_stop(ser)# Send stop data
           ser.close() #we'll use ctrl+c to stop the program
           print("Exiting program due to KeyboardInterrupt")
           sys.exit()
    return data_array           
# Send stop data

def calc_sampling_rate(data_array):
    global x
    x = np.diff(data_array, n=1, axis=0)
    x = np.mean(x, axis= 0)
    return x[0]

def plot_data(data_array):
    plt.clf()
    plt.subplot(311)
    t = (data_array[:,0])/1000000
    x =  data_array[:,1]
    y = data_array[:,2]
    z = data_array[:,3]
    plt.plot(t, x) #fill in ax and ay
    plt.subplot(312)
    plt.plot(t,y) #fill in bx and by
    plt.subplot(313)
    plt.plot(t,z)
    plt.show()

def main():
    global data_array
    
    ser = setup_serial()
    send_start(ser)
    data_array = receive_data(ser)
    print(data_array)
    print("Sampling Rate in us is: ")
    print(calc_sampling_rate(data_array))
    plot_data(data_array)
    send_stop(ser)
    ser.close()

if __name__== "__main__":    
    main()
