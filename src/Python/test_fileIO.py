# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:36:16 2020

@author: alan2
"""

import numpy as np
import matplotlib.pyplot as plt

data_array = np.array([[10252533, 1806, 1823, 2255],
  [10262471, 1808, 1822, 2246],
  [10272472, 1804, 1823, 2241],
  [10282472, 1805, 1830, 2239],
  [10292477, 1806, 1821, 2235],
  [10302475, 1808, 1823, 2247],
  [10312480, 1808, 1829, 2239],
  [10322483, 1807, 1828, 2242],
  [10332484, 1809, 1825, 2246],
  [10342488, 1799, 1823, 2243],
  [10352490, 1802, 1817, 2243],
  [10362492, 1803, 1822, 2235],
  [10372495, 1808, 1827, 2243],
  [10382499, 1802, 1822, 2251],
  [10392500, 1800, 1830, 2241],
  [10402502, 1793, 1825, 2245],
  [10412504, 1808, 1826, 2246],
  [10422506, 1803, 1829, 2247],
  [10432509, 1799, 1823, 2253],
  [10442511, 1795, 1823, 2239],
  [10452514, 1808, 1830, 2246],
  [10462514, 1797, 1820, 2237],
  [10472519, 1801, 1823, 2246],
  [10482524, 1802, 1827, 2249],
  [10492526, 1799, 1827, 2251],
  [10502526, 1808, 1819, 2229],
  [10512527, 1796, 1824, 2256],
  [10522533, 1795, 1823, 2241],
  [10532535, 1810, 1825, 2250],
  [10542538, 1811, 1822, 2243],])

np.savetxt("foo.csv", data_array, delimiter=",")

data_array_from_file = np.genfromtxt('foo.csv', delimiter=',')

s = data_array_from_file[:,3] #get the z axis
# mean_s = np.mean(s)#take the mean of s with numpy
# s = s - mean_s # subtract off the mean

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


def main():
    x = detrend(s, 2)
    plt.clf()
    print("original plot:")
    plt.plot(s)
    plt.show()
    print("final plot")
    plt.clf()
    plt.plot(x)
    plt.show()
    
main()

