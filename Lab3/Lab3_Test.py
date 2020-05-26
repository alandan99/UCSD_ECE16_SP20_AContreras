# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:58:26 2020

@author: alan2
"""
import matplotlib.pyplot as plt
import numpy as np

incoming_stream = b'1',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'2',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'3',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'4',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'5',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'6',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'7',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'8',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'9',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'1',b'0',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n'

string_buffer = []
data_array = np.array([])
sample_num = 0
x = 0 

def parse_input( input_char ):   
    global sample_num
    global string_buffer
    global data_array
    if( input_char == '\n' ):
        # data_string will contain the cumulative buffer of newline
        # (‘\n’) separated lines data (See Hint (2) below for help)
        data_string = ''.join(string_buffer)# join with the contents of string_buffer
        sample_num += 1
        print(data_string)
        np_buffer = np.fromstring(data_string, sep=',')# convert CSV string_buffer to a 1x4 ndarray
        if (data_array.size == 0): # data_array is empty ):
            data_array = np_buffer
        else:
            data_array = np.vstack((data_array, np_buffer))# vstack np_buffer to data_array
        string_buffer = [] # reset string_buffer to []
    else:
        string_buffer.append(input_char)# append the input_char to string_buffer

def calc_sampling_rate(data_array):
    global x
    x = np.diff(data_array, n=1, axis=0)
    x = np.mean(x, axis= 0)
    return x[0]

def plot_data(data_array):
    plt.clf()
    plt.subplot(311)
    time = (data_array[:,0])/1000000
    x =  data_array[:,1]
    y = data_array[:,2]
    z = data_array[:,3]
    plt.plot(time, x) #fill in ax and ay
    plt.subplot(312)
    plt.plot(time,y) #fill in bx and by
    plt.subplot(313)
    plt.plot(time,z)
    plt.show()
    

def main():
    for incoming_byte in incoming_stream:
        # this line takes the place of reading the byte from Serial
        c = incoming_byte.decode('utf-8')
        parse_input(c)
    calc_sampling_rate(data_array)
    plot_data(data_array)
    
    

if __name__== "__main__":    
    main()
