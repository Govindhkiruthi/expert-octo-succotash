# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:18:04 2020

@author: 780020
"""

import sys

x,y=input("Enter any two numbers: ").split()
#y=int(input("Enter any  number"))

op=0
if x>y:
    a=y
elif x==y:
    a=y
else:
    a=x
    int(a)
for i in range(1,a+1):
    if x%i==0 and y%i==0:
        op+=1
print(x,y)
print(op)