#!/usr/bin/env python
from math import sqrt, fmod
def multypliers(number):
    sqrtNum=int(sqrt(number))+1
    mp=[]
    for i in xrange(2,sqrtNum):
        while fmod(number,i)==0:
            mp.append(i)
            number=number/i
    return mp


def equation(a,b,c):
    D=b*b-4*a*c
    if D>=0:
        x1=(-b+sqrt(D))/2*a
        x2=(-b-sqrt(D))/2*a
        print 'x1  '+str(x1)
        print 'x2  '+str(x2)
    else:
        print 'no'
        
def simple(number):
    i=2
    maxnum=sqrt(number)+1
    while i<maxnum:
        if number%i==0:
            print 'ne prostoe'
            return
        i=i+1
    print 'prostoe'

def atm(number):
    a=[5000,1000,500,100,50,10,5,2,1]
    k=0
    b=0
    while k!=number:
        t=True
        while t:
            if k+a[b]<= number:
                print a[b]
                k=k+a[b]
                #print k
            else:
                b=b+1
                t=False
    
            

    
print multypliers(30)
equation(1,-5,6)
simple(25)
atm(286)
    
