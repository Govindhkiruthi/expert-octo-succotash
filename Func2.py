# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 11:43:54 2020

@author: 780020
"""

from Func1 import fog

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))