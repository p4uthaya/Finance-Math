# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 18:16:48 2018

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

def Is2(n,i):
    return Ia(n,i)*(1+i)**n


R = 17900/a(28,0.045/4)
print (R)

X = (17900 - R*a(27,0.045/4))/((1+0.045/4)**(-28))

print (X)

####

T = 148000
i = 0.127/2

R = T/a(48,i)

B6 = T*(1+i)**6 - 9914*s(6,i)

print(R)
print(B6)

B12 = B6*(1+i)**6

print(B12)

Rn = B12/a(36,i)

print(Rn)

###take 2 

R = 11600/a(16,0.0525/4)
print (R)

X = (11600 - 809*a(15,0.0525/4))/((1+0.0525/4)**(-16))
print (X)


print ("q3")

T = 225000
i = 0.108/2

R = T/a(44,i)

B7 = T*(1+i)**7 - 13483*s(7,i)

print(R)
print(B7)

B11 = B7*(1+i)**4

print(B11)

Rn = B11/a(33,i)

print(Rn)
