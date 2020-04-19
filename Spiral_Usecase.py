# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 15:51:43 2019

@author: 780020
"""
from numpy import *
row=int(input("Enter Number of Rows = "))
column=int(input("Enter Number of Columns = "))
print(column,row)
val=[]
op=[]
TotalNos = row*column
for i in range(1,TotalNos+1):
    val.append(i)
print(val)
arr1=array(val)
arr2=arr1.reshape(row,column)
print(arr2)
startup=0
startdown=row-1
startright=column-1
startleft=0
while TotalNos>0:
    #print("TotalNos = ",TotalNos)
    if TotalNos>0:
        for i in range(startleft,startright+1):
            op.append(arr2[startup][i])
            TotalNos-=1
        startup+=1    
   # print("TotalNos = ",TotalNos)
    if TotalNos>0:
        for i in range(startup,startdown+1):
            op.append(arr2[i][startright])
            TotalNos-=1
        startright-=1
    if TotalNos>0:
        for i in range(startright,startleft-1,-1):
            op.append(arr2[startdown][i])
            TotalNos-=1
        startdown-=1
    #startup+=1
    if TotalNos>0:
        for i in range(startdown,startup-1,-1):
            op.append(arr2[i][startleft])
            TotalNos-=1
        startleft+=1
    #print("TotalNos",TotalNos)
    #TotalNos=0
#    print(TotalNos)
#    startleft+=1
#    startright-=1
#    startdown-=1
#    startup+=1
print(TotalNos)
print(op)