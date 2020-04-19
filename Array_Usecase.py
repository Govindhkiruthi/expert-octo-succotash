# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 13:36:14 2019
@author: 780020
"""

from numpy import *
ArraySiz=int(input("Enter the array size"))
cell=int(input("Enter the cell Count"))
val=[]
dest = ArraySiz*ArraySiz
#cell=2
#print(dest)
for i in range(1, dest+1):
    CorM=str(input("Enter the attribute Value"))
    val.append(CorM)
arr4=array(val)
#arr2=arr1.flatten()
arr3=arr4.reshape(ArraySiz,ArraySiz)
print(arr3)
catches=0
for i in range(0,ArraySiz):
    rat=[]
    cat=[]
    for j in range(0,ArraySiz):
        if arr3[i][j]=='M':
            rat.append(j)
        else:
            cat.append(j)
    print(rat,cat)    
    for k in rat:
        print("k= ",k)
        for l in range(1,cell+1):
            print("L= ",l)
            if (k+l)<ArraySiz:
                if (k+l) in cat:
                    catches+=1
                    #print("Success")
                    cat.remove((k+l))
                    break
            elif (k-l)>=0:
                 if (k-l) in cat:
                    #print("SUCCESS")
                    catches+=1
                    cat.remove((k-l))
                    break
    rat.clear()
    cat.clear()                
print("catches = ",catches)           