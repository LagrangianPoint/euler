#!/usr/bin/python
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
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

#target = 6
target = 10001
primeCount = 0
i = 2
while primeCount <= target :
	if isPrime(i):
		primeCount += 1
		if primeCount == target:
			break;
	if i < 3:
		i += 1
	else :
		i += 2
print "============="
print i
