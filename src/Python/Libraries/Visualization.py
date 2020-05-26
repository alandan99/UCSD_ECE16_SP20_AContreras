# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:53:45 2020

@author: alan2
"""


import matplotlib.pyplot as plt

class Visualization:
  def __init__(self, data_array=None):
    (self.time, self.accelX, self.accelY, self.accelZ, self.ppg) = ([], [], [], [], [])
    if data_array is not None:
      self.addData(data_array)

  def addData(self, data_array):
    self.time = data_array[:, 0]
    self.accelX = data_array[:, 1]
    self.accelY = data_array[:, 2]
    self.accelZ = data_array[:, 3]
    if data_array.shape[1] == 5:
        self.ppg = data_array[:, 4]

  def plotData(self):
    # plot the 3 axis accelerometer axes and the heart pulse signal into 4 subplots
    # Hint: you could call the below methods! And do not forget the time on the x-axis!
    self.plotAccel()
    self.plotHR()
    plt.show()

  def plotAccel(self):
    # plot the 3 axis accelerometer data
    t = (self.time)/1000000
    x = self.accelX
    y = self.accelY
    z = self.accelZ
    plt.clf()
    # figure, axes = plt.subplots(nrows=3, ncols=1)
    # axes[0,0].plot(t,x)
    # axes[0,0].ylabel("x_ampl")
    # axes[1,0].plot(t,y)
    # axes[1,0].ylabel("y_ampl")
    # axes[2,0].plot(t,z)
    # axes[2,0].ylabel("z_ampl")
    
    plt.subplot(411)
    plt.plot(t,x)
    plt.title("Accel Data")
    plt.ylabel("x amp")
    plt.subplot(412)
    plt.plot(t,y)
    plt.ylabel("y amp")
    plt.subplot(413)
    plt.plot(t,z)
    plt.xlabel("Time (us)")
    plt.ylabel("z amp")
    

    
    

  def plotHR(self):
    # plot the heartbeat pulse data (covered later on in this lab)
    hr = (self.ppg ) *-1
    plt.subplot(414)
    t = (self.time)/1000000
    plt.plot(t, hr)
    plt.ylabel("HR amplitude")
