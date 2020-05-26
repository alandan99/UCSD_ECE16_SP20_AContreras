# -*- coding: utf-8 -*-
"""
Created on Mon May  4 23:09:15 2020

@author: alan2
"""
import pyowm
import serial
import time
import sys
from datetime import datetime

degree_sign = u"\N{DEGREE SIGN}"

owm = pyowm.OWM('419dfea146ebfaa6e2e41022bf1456ed')
w = owm.weather_at_place('San Diego,USA')

r = w.get_weather()
skys = r.get_status()
temp = r.get_temperature('celsius')
humi = str(r.get_humidity())
print(skys)
print(str(temp['temp']) + degree_sign + 'C')
print(humi + '%')

now = datetime.now().time()
print(now)



