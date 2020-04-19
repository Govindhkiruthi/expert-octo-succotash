import sys
import math
import time  
a=[]
Uniq=[]
c=0
e=0
a1=int(input("Enter the Number of values going to provide:"))

for i in range(0,a1):
     b1=input("Enter the values:")
     a.append(b1)
for i in a:
    if i not in Uniq:
        Uniq.append(i)
        
for i in Uniq:
     b=a.count(i)
     d=int(b/2)
     e=e+d
print(int(e))
