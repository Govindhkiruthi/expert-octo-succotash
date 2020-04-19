# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 18:26:31 2020

@author: 780020
"""

def fog(a,b):
    c=a+b
    print(__name__)
    print(c)
    return c

def arbitrary(*args):
    pass
    print("No of args = " , args[5])
 
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
#
def myfunc(n,m):
    print(n,' ', m)
    
    a = lambda a,b : a * b * n * m
    #print(a)
    return a


     
if __name__=='__main__':
    
    fog(10,6)
    arbitrary(1,2,3,4,5,6)
    my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
    mytripler = myfunc(3,22)
    #print(mytripler(11,10))
    print(a(2,25))
  
    
