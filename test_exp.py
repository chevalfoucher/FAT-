# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:11:45 2015

@author: foucher
"""
import numpy as *
import numpy.random as rand
import numpy as np

T=1000
t=0.0
#Lambda=[[ 7.0, 5.0],[ 5.0,7.0]]
Lambda=ones
Occup=[[ 13, 9],[ 7,15]]




def update():
    global Occup    
    global t    
    t1=T
    I,J=0,0
    for i in range(0,2):
        for j in range(0,2):
            if Occup[i][j]!=0:
                if i==j:
                    t2=rand.exponential(Lambda[i][j])    
                else:
                    t2=rand.exponential(Lambda[i][j]/Occup[i][j])
                if t2<t1:
                    I,J=i,j
                    t1=t2
#    print t1
    if I==0 and J==0:
        Occup[0][0]=Occup[0][0]-1
        Occup[0][1]=Occup[0][1]+1
    if I==1 and J==1:
        Occup[1][1]=Occup[1][1]-1
        Occup[1][0]=Occup[1][0]+1
    if I==1 and J==0:
        Occup[1][0]=Occup[1][0]-1
        Occup[0][0]=Occup[0][0]+1
    if I==0 and J==1:
        Occup[0][1]=Occup[0][1]-1
        Occup[1][1]=Occup[1][1]+1
    t=t+t1

def print_status():
    #print "Time is : ", t   
    print(Occup)
    
print_status()
while t<=T:
    update()

print_status()