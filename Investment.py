# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 23:05:19 2018

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

NPV = -40000 + 6000*a(4,0.077) + 2000*(1+0.077)**-5 + 2000*(1+0.077)**-6 + 2000*(1+0.077)**-7
print(NPV)

NPV = -40000 +6000*a(4,0.077) +2000*a(3,0.077)*(1+0.077)**-4
print(NPV)

def DivYld(i,p,s):
    return (i*p)/s

print(DivYld(3.90,2,78.50))

print(2.30/(0.12/4))




#A11

r1 = (38456/40000)**(1/3) - 1
r2 = (48673.20/(38456 + 140*48.07))**(1/5) - 1
r3 = (49555.80/(48673.20 - 130*51.78))**(1/2) - 1


r = ( (1+r1)**3 * (1+r2)**5 * (1+r3)**2 )**(1/10) - 1

print('Assignment 11')
print(r1)
print(r2)
print(r3)
print(r)