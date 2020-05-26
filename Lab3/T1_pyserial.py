# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:12:44 2020

@author: alan2
"""

import serial
import time
import sys
import pyowm
import numpy as np

dataCheck = True
full_string =[]

def setup_serial():
    serial_name = "COM3"
    ser = serial.Serial(serial_name, 115200)  # open serial port
    print(ser.name)         # check which port was really used
    return ser

def weather_data(data_string):
    owm = pyowm.OWM('419dfea146ebfaa6e2e41022bf1456ed')
    print(data_string)
    w = owm.weather_at_place(data_string)  
    r = w.get_weather()
    skys = r.get_status()
    t = r.get_temperature('celsius')
    temp = str(t['temp']) + 'C'
    humi = str(r.get_humidity())
    return ' '.join([skys, temp, humi])
    
    

def send_serial(ser):
    global sendReport 
    
    S = sendReport + '\n'      
    ser.write(S.encode('utf-8'))         # write a string

def send_serial1(ser):
    S = 'send location\n'
    ser.write(S.encode('utf-8'))  
    
def send_locRec(ser):
    global data_string
    
    S = data_string +'\n'
    ser.write(S.encode('utf-8'))
    

# def main():
#     send_serial(ser)
    
def main():
    global s
    global sendReport
    global data_string 
    
    ser = setup_serial()
    while True :
        try:
            send_serial1(ser) #request location
            readSerial4(ser)  #get location 
            send_locRec(ser)  #got location
            time.sleep(1)
            sendReport = weather_data(data_string) #get weather
            send_serial(ser) #send to serial
            time.sleep(1)
        except(KeyboardInterrupt):
            ser.close() #we'll use ctrl+c to stop the program
            print("Exiting program due to KeyboardInterrupt")
            sys.exit()
    
    
    ser.close()
    
     
# def readSerial2(ser):
#     n=0
#     while (n<30):
#        s = ser.read(1).decode('utf-8')     # read 1 byte and decode it
#        print(s)
#        n=n+1

# def readSerial3(ser):
#    n=0
#    full_string = []
#    while (n<30):
#      s = ser.read(1).decode('utf-8')     # read 1 byte and decode it
#      full_string.append(s)
#      n=n+1
#    print(full_string)

# def receive_sample(ser):
#     global string_buffer
#     global data_array
    
#     c = ser.read(1).decode('utf-8') # read a byte from Serial (remember to decode)
#     parse_input(c) # same function as in the offline code

def readSerial4(ser):
    global s
    global full_string
    global data_string
    global dataCheck
    
    while dataCheck:
       try:
         s = ser.read(1).decode('utf-8')  # read 1 byte and decode to utf-8
         if s == '\n':
             dataCheck = False
             data_string = ''.join(full_string)
             return data_string 
             
         else :
             full_string.append(s) #append buffer to full_string
             
         
       except(KeyboardInterrupt):
         ser.close() #we'll use ctrl+c to stop the program
         print("Exiting program due to KeyboardInterrupt")
         sys.exit()



if __name__== "__main__":
    main();
#    try:
#         ser = setup_serial()
#         while(True):
#             main()
#     except KeyboardInterrupt:
#             ser.close()




