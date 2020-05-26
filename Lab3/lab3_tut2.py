# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:48:29 2020

@author: alan2
"""
import matplotlib.pyplot as plt
import numpy as np

# plt.clf() #clear any existing plot
# plt.plot([1,2,3,4],[1,4,9,16])
# plt.show()

# a = np.array([[1,2,3,4],[1,4,9,16]])
# plt.clf()
# plt.plot(a)
# plt.show()

# a = np.array([[1,2,3,4],[1,4,9,16]])
# x = a[0] #index from a to get [1,2,3,4]
# y = a[1] #index from a to get [1,4,9,16]
# plt.clf()
# plt.title("First plot!")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.plot(x,y)
# plt.show()

a = np.array([[1,2,3,4],[1,4,9,16]])
b = np.array([[1,2,3,4],[4,2,1,6]])

plt.clf()
plt.subplot(211)
ax =  a[0]
bx = b[0]
ay = a[1]
by = b[1]
plt.plot(ax,ay) #fill in ax and ay
plt.subplot(212)
plt.plot(bx,by) #fill in bx and by
plt.show()
