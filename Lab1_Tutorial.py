# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:28:55 2020

@author: Alan Contreras
"""
import numpy as np
def func1():
    test_array = np.array([0,10,4,12])
    test_array1 = test_array - 20
    print(test_array1)
    print(test_array.shape)
    
def func2():
    test_2D_array = np.array([(0,10,4,12),(1,20,3,41)])
    print(test_2D_array)
    
def func3():
    zero_array = np.zeros((10,20))
    print(zero_array)
    

def func4():
    new_array = np.hstack((test_array, test_array))
    new_array = np.vstack((new_array, new_array, new_array, new_array))
    print(new_array)
    
def func5():
    arange_array1 = np.arange(-3, 16, 6)
    print(arange_array1)
    arange_array2 = np.arange(-7, -20,-2)
    print(arange_array2)
    
def func6():
    linspace_array = np.linspace(0, 100, num = 49)
    print(linspace_array)
    
def func7():
    e = np.array([(12,3,1,2),(0,0,1,2),(4,2,3,1)])
    print('created array e =\n',e,'\n')
    print(e[0])    #>>> [12 3 1 2]
    print(e[1,0])  #>>> 0
    print(e[:,1])  #>>> [3 0 2]
    print(e[2, :2])#>>> [4 2]
    print(e[2, 2:])#>>> [3 1]
    print(e[:,2])  #>>> [1 1 3]
    print(e[1,3])  #>>> 2
    
def func8():
    f = np.zeros((3,4),dtype=np.int32)
    #print(f)
    f[0]    = (12,3,1,2)
    f[1,0]  = 0
    f[:,1]  = (3,0,2)
    f[2,:2] = (4,2)
    f[2,2:] = (3,1)
    f[:,2]  = (1,1,3)
    f[1,3]  = (2)
    print(f)
    
def func9():
    data_str = '1,2,3,4'
    arr = np.fromstring(data_str, dtype=int, sep = ',')
    for x in range(0,99):
         arr1 = np.fromstring(data_str, dtype=int, sep = ',')
         arr = np.vstack((arr, arr1))
         x+=1
         
    print(arr)
    print(arr.shape)

     
func9()
#func8()
#func2()
#func3() 
#func4()
#func5()
#func6()
#func7()