#!/usr/bin/python
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
def isPrime(number):
	if number == 1:
		return False
	i = 2
	bPrime = True
	while i < number/2:
		if number % i == 0:
			bPrime = False
		i += 1	
	return bPrime

def multiplicity(number, factor):
	numMulti = 1
	while numMulti * factor < number / 2 + 1:
		if number % (numMulti + 1) * factor == 0:
			numMulti += 1
		else:
			break
	return numMulti
def factors(number):
	tmpNumber = number
	listOut = []
	factor = 3
	while factor < int(number / 2):
		if tmpNumber % factor == 0 :
			listOut.append(factor)
			#tmpNumber = tmpNumber / (factor * multiplicity(tmpNumber, factor) )
			tmpNumber = tmpNumber / factor
			if tmpNumber == 1:
				break
		factor += 2
	return listOut
	
number = 13195
number = 600851475143
originalNumber = number
listFactors = factors(number)
print listFactors[-1]

