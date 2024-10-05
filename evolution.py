# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 22:37:29 2024

@author: adars
"""
def evolve(x):
    ind=random.randint(0,( len(x)-1))
    p=random.randint(1,100)
    if(p==1):
        if(x[ind]=='0'):
            x[ind]='1'
        else:
            x[ind]='0'
    print(x)        
    
import random
with open("dna.txt") as file1:
    print(file1.read())
    file1.seek(0)
    x=file1.read()
    x=list(x)
file1.close
for i in range (0,1000):
    evolve(x)

    