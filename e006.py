#!/usr/bin/python
"""
The sum of the squares of the first ten natural numbers is,

"""
numMax = 100
sum = 0
sumSquares = 0
for x in range(1, numMax+1):
	sum += x
	sumSquares += x*x
print sum**2 - sumSquares
