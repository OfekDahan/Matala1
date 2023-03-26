# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 21:47:53 2023

@author: ofekd
"""

def my_func(x1,x2,x3):
    denominator= x1+x2+x3
    if denominator==0:
        print("Not a number – denominator equals zero")
    if isinstance(x1, float) and isinstance(x2, float) and isinstance(x3, float)==False : # check if all parameters are float
        print("Error: parameters should be float")
    if type(x1) != float or type(x2) != float or type(x3) != float :
        print("None")
    else:
        value= ((denominator*(x2+x3)*x3)/denominator)
        print(value)

my_func(1.5,2.6,4.8)
    
