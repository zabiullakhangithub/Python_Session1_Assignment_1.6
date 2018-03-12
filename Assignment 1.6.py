# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:45:47 2018

@author: zabiulla.khan


Create the below pattern using nested for loop in Python.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
    
"""
#Initialize n to repeat the char n times
n=5

 # Append * in n rows n times
x=''
for i in range(0,n,1):  
    x = x + ' * '
    print(x)
    
 # remove * from n-1 rows, n-1 times
for i in range(0, n-1):
    for j in range(n-1, i, -1):
        print(" * ",end="")
    print()
    