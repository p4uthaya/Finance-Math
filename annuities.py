# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 20:48:04 2018

@author: Prabha
"""

def a(n,i):
    return (1-(1+i)**(-n))/i

def s(n,i):
    return ((1+i)**(n)-1)/i

i = 0.036/12
n = 1*12
R = 125

print(a(n,i))

ans = R*a(n,i)*(1+i)
print(ans)

#------------------------------------------

i = 0.111/1
n = 15
R = 16000

print(a(n,i))

ans = R*a(n,i)*(1+i)**(-16)
print(ans)

#------------------------------------------

i = 0.075/12
n = 36
R = 740


ans = R*s(n,i)*(1+i)**(36+1)
print(ans)

#------------------------------------------

i = 0.075/12
n = 36
R = 740


ans = R*s(n,i)*(1+i)**(36+1)
print(ans)

#------------------------------------------

i= 0.054/4
n = 24
R = 190


ans = (3910-R*a(n,i))*(1+i)**(25)
print(ans)

#------------------------------------------

i= 0.089/4
n = 26
R = 470


ans = (9450-R*a(n,i))*(1+i)**(27)
print(ans)