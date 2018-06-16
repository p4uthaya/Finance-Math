# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 12:10:10 2018

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


# Loans and Debts

# sinking funds 

n = 15
i = 0.07

R = 2000000/s(n,i)
R = 79589.25

print (R)


op2 = R*s(1,i)
print(op2)
op14 = R*s(13,i)
print(op14)


Cst = 60000
i = 0.075

a1 = 20000*s(3,i)
b1 = 10000*s(4,i)

c = 20000*a(3,i)
d = 10000*a(4,i)


NPV1 = -Cst + a1*(1+i)**-5 + b1*(1+i)**-9
NPV2 = -Cst + c*(1+i)**-2 + d*(1+i)**-5

print(NPV1)
print(NPV2)