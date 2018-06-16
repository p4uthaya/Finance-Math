# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:34:15 2018

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

# Q1

A = 180000
i = 0.065/12
p = 1137.72

B60  = A*(1+i)**(6*12) - p*s(6*12,i)
B360 = A*(1+i)**(30*12) - p*s(30*12,i)


print(B60)
print(B360)

# Q2

#a
R = 74000/a(300,0.045/12)
print(R)

#b
X = (74000 - 412*a(299,0.045/12))/(1+0.045/12)**-300
print(X)

#c
CB21 = 412*a(300-22,0.045/12)
OB22 = CB21
print(OB22)

I22 = (0.045/12)*OB22
print(I22)

CB22 = OB22 + I22 - 412
print(CB22)


#d 
A = 74000
i = 0.045/12
B108 = A*(1+i)**(9*12) - 412*s(9*12,i)

Rnew = B108/a(16*12,0.091/12)
print(Rnew)

#Q3

i12 = (1.042)**(1/12) - 1
R = 14000/s(4*12,i12)

print (i12*12,R)

#WA3

#q1
print('wa1 -------------------------------------------')
R = 2000000/s(15,0.07)

print(R)

i = 0.07

# test
R = 79589.25

CB4 = R*s(4,i)
OB4 = CB3 = R*s(3,i)
print(CB4)
print(OB4)
print(CB4 - OB4 - R)
print(OB4 * i)

ob9 = R*s(8,i)
Inc = ob9*i + R
print(Inc)

cb11 = R*s(11,i)
print(cb11)

print('q2 --------------------------------------------')

i = ((1+ 0.09/2)**(2/12) - 1)*12

print(i)

R = 255000/a(300,i/12)
print(R)

i = 0.0883575/12
R = 2111.35

Bal = 255000*(1+i)**42 - R * s(42,i)
print(Bal)
print(Bal*(1+i)**3)



print('test ------------------------------------------')

ob1 = 255000
in1 = ob1*i
pm1 = R
cb1 = ob1+in1-pm1
print('Row 1:',ob1,in1,pm1,cb1)


ob299 = 255000*(1+i)**298 - R*s(298,i)
print(ob299)
print(ob299*i)
print(ob299*(1+i) - pm1)
print((ob299*(1+i) - pm1)*i)


