#!/usr/bin/python
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
import math, sys
def isPrime(number):
	if number < 4:
		return True
	if number % 2 == 0 or number % 3 == 0:
		return False
	numMax = int(math.ceil(math.sqrt(number)))
	i = 2
	bPrime = True
	while i <= numMax :
		if number % i == 0 :
			return False
		i += 1
	return bPrime

target = 2000000
#target = 10
primeSum = 0
i = 2
while i <= target :
	if isPrime(i):
		#print i
		primeSum += i
	if i < 3:
		i += 1
	else :
		i += 2
print "============="
print primeSum
