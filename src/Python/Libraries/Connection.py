# -*- coding: utf-8 -*-
"""
Created on Wed May 13 09:46:29 2020

@author: alan2
"""

import serial
import numpy as np

class Connection:

  def __init__(self, serial_name, baud_rate):
    self.serial_name = serial_name
    self.baud_rate = baud_rate
    self.setup_connection()
    self.string_buffer = []
    self.data_array = np.array([0])

  def setup_connection(self):
    self.ser = serial.Serial(self.serial_name, self.baud_rate) # open Serial port using self.serial_name and self.baud_rate

  def close_connection(self):
    #close the Serial connection
    self.ser.close()

  def send_serial(self, message):
    # write message to Serial
    S = message + '\n'
    self.ser.write(S.encode('utf-8'))
    
  def start_streaming(self):
    # send 'Start Data\n' through Serial
    S = 'start data\n'
    self.ser.write(S.encode('utf-8'))

  def receive_data(self, input_char):
    # This should have the same functionality as parse_input from Lab 3, but use the class
    # attributes defined above instead of global variables like you used in Lab 3
    if(input_char == '\n'):
        data_string = ''.join(self.string_buffer)
        #sample_number = sample_number + 1
        np_buffer = np.fromstring(data_string, dtype=int, sep=',')
        
        if (self.data_array.size == 0):
            self.data_array = np_buffer
        else: 
            self.data_array = np.vstack((self.data_array, np_buffer))
        self.string_buffer =[]
    else:
        self.string_buffer.append(input_char)

  def read_serial(self):
    #read one byte at a time and call receive_data(input_char)
    c = self.ser.read(1).decode('utf-8')
    self.receive_data(c)
    
  def checkSerial(self):
    if (self.ser.in_waiting > 0):
        return True
    
    
  def end_streaming(self):
       # send 'Stop Data\n' through Serial
       S = 'stop data\n'
       self.ser.write(S.encode('utf-8'))

  def clear_data(self):
    # reset data_array to empty NumPy ndarray
    self.data_array = np.array([])

  def get_num_samples(self):
    # return the size of data_array
    return self.data_array.shape[0] 
    

  def calc_sampling_rate(self):
    # calculate the sampling rate
    global freq
    global mean1
    diff1 = np.diff(self.data_array, n=1, axis=0)
    mean1 = np.mean(diff1, axis=0)
    
    freq = 1000000/mean1[0]
    Y = str(freq)
    rate = Y[:12]
    return rate

# ser = Connection("COM3", 115200)
# ser.setup_connection()