# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 15:29:19 2018

@author: Prabha
"""

def a(n,i):
    return (1-(1+i)**(-n))/i

def s(n,i):
    return ((1+i)**(n)-1)/i

def Ia(n,i):
    return ((1+i)*a(n,i) - n*(1+i)**(-n))/i

def Is(n,i): 
    return (s(n+1,i)-(n+1))/(i)


i = 0.07/12
n = 31

AV = 424*s(n,i) + 126*Is(n,i)

print (AV)

AV = 550*s(n,i) + 126*Is(n-1,i)

print (AV)

# get the same shit 

i = 0.104/12
n = 41

AV = 330*s(n,i) + 123*Is(n-1,i)

print (AV)

print (500*a(15,0.13/2))
print (500*a(20,0.13/2)*(1+0.13/2)**5 - 500*a(5,0.13/2)*(1+0.13/2)**5)
print (500*s(3,0.13/2)*(1+0.13/2))

A = 1000*s(3,0.09)
B = A*(1+0.11)**4 + 1000*s(4,0.11)
C = 1000*s(3,0.08) + B*(1+0.08)**3

print (A,B,C)


i = s(300,0.08/12)
j = a(240,0.07/12)

r = (2500*j*(1+0.07/12))/(i*(1+0.08/12)**60)

print(r)
print (217878.92/s(300,0.08/12))
print(i,j)