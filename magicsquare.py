# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 21:08:24 2024

@author: adars
"""

def magicsquare(n):
    
    magicsquare1 = [[0 for i in range(n)]for j in range(3)]
    for i in range(n):
        for j in range(n):
            magicsquare1[i][j]=0
    i=n//2
    j=n-1
    num=n*n
    count=1
    while(count<=num):
        if(i==-1 and j==n):
            j=n-2
            i=0
        else:
            if(j==n):
                j=0
            elif(i<0):
                i=n-1
        if magicsquare1[i][j] != 0:
             j=j-2
             i=i+1
             continue
            
        else:
             magicsquare1[i][j]=count
             count=count+1
        i=i-1
        j=j+1
        
    
    for i in range(n):
        for j in range(n):
            print(magicsquare1[i][j], end=" ")
        print()
        