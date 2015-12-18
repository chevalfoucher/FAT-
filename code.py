# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 16:27:18 2015

@author: foucher
"""
import numpy as np

#Parameters
Lambda=3*np.ones((5, 5))

State=3*np.ones((5,5),dtype=int)+10*np.identity(5,dtype=int)

Routing=0.25*np.ones((5,5))-0.25*np.identity(5)

#T horizon temporel
T=100

t=0
def print_status():
    #print "Time is : ", t   
    print("Time is :"+str(t))    
    print(State)

 
State[0][0]=0
print_status() 
def update():
    global t    
    Trans=np.zeros((5,5))
    for i in range(0,5):
        for j in range(0,5):
            if i==j:
                if State[i][i]==0:Trans[i][i]=0
                else:Trans[i][i]=Lambda[i][i]
            else:Trans[i][j]=State[i][j]*Lambda[i][j]

    #print Lambda
    #print State
    #print Trans
    L=np.sum(Trans)
    t1=np.random.exponential(1/L)
    t=t+t1
    if t<T:
        list_proba=np.ones(25)/25
        list_state=np.zeros(25)
        #print (list_proba)
        for i in range(0,5):
            for j in range(0,5):
                list_proba[i*5+j]=(Trans[i][j]/L)
                list_state[i*5+j]=(i*5+j)
        r=int(np.random.choice(a=list_state,p=list_proba))
        I=r/5
        J=r%5
        if I!=J:
            State[I][J]=State[I][J]-1
            State[J][J]=State[J][J]+1 
            print ("bike going from "+str(I)+" to "+ str(J)+" arrived")
        else:
            J1=np.random.choice([0,1,2,3,4],p=Routing[I][:])
            State[I][J]=State[I][J]-1
            State[I][J1]=State[I][J1]+1
            print ("Client arrives in station "+str(I)+" ,he goes to station "+str(J1))
        #print_status()
    else:print("We arrived at final time")


while t<T:
    update()

