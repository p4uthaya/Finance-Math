# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 11:41:47 2018

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



#Assignment 8 ____________________________________

#Q1
print('Q1 ---------------------------------------------------------')

PV = (1000*0.065/2)*a(9*2,0.061/2) + 1000*(1 + 0.061/2)**(-9*2)
print(PV)

print('Q2 ---------------------------------------------------------')

AI = (1000*0.063/2) * (58/181)
print (AI)

print('Q3 ---------------------------------------------------------')

P0 = (1000*0.088/2)*a(43,0.044/2) + 1000*(1 + 0.044/2)**-43

FP = P0*(1 + 0.044/2)**(63/181)

AI = (1000*0.088/2)*(63/181)


print(FP)
print(FP - AI)


print('Written Assignment 4 -----------------------------------------------')
print('Question 1')
F = 1000         # Face value
r = 0.065/2      # coupon rate (has to be the paying bond interest )
i = 0.07/2       # yield rate
n = 20*2         # total number of periods
C = F*r          # coupon amount 

P = C*a(n,i) + 1000*(1+i)**-n

print('Price of Bond at the start is $',P)

n = 30             # number of periods left over (40 - 10)
i = 0.05/2         # new YTM rate

P = C*a(n,i) + 1000*(1+i)**-n
print('Sale Price of Bond after 5 years is $',P)

print('Question 2')
F = 1000
r = 0.06/2
n = 7*2
P = 1000*(92/100)

totalInt = F*r*n + (F - P)
print('Total interest earned:',totalInt)

avgInt = totalInt/7
print('average interest:',avgInt)

avgInv = (F + P)/2
print('average investment:',avgInv)

i = avgInt/avgInv
print ('ytm:',i)

print('Question 3')
 
F = 1000
r = 0.05/2
i = 0.06/2
n = 10*2
C = F*r

P = C*a(n,i) + 1000*(1+i)**-n
print(P)

C = 25
n = 6
i = 0.075

P = C*a(n,i) + 1000*(1+i)**-n
print(P)









