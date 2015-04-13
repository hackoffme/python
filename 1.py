#!/usr/bin/env python
import math
def multypliers(number):
	#maxmultypliers = int(math.sqrt(number))
	i=1
	a=[]
	while i<number-1:
		i=i+1
		a.append(True)
		#a[i]=1

	i=1.0
	
	while i<number:
		i=i+1
		if int(number/i)==number/i:
			t=2
			while t*i<number:
				a[int(t*i-2)] = False
				t=t+1
		else:
			a[int(i-2)]=False
	i=0
	while i<number-2:
		if a[i]:
			print i+2
		i=i+1
		
	return 

def equation(a,b,c):
	D=float()
	D=b*b-4*a*c
	if D>=0:
		x1=(-b+math.sqrt(D))/2*a
		x2=(-b-math.sqrt(D))/2*a
		print 'x1  '+str(x1)
		print 'x2  '+str(x2)
	else:
		print 'no'
		
def simple(number):
	i=2
	maxnum=math.sqrt(number)
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
	
			

	
multypliers(30)
equation(1,-5,6)
simple(17)
atm(555555)
	
