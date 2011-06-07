#!/usr/bin/python
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import sys

maxNum = 20
#maxNum = 10
numDivideCount = 0
i = 1
smallest = 1
while numDivideCount < maxNum:
	numDivideCount = 0
	for j in range(1,maxNum+1):
		if i % j == 0:
			numDivideCount += 1
		else:
			continue
	if numDivideCount == maxNum:
		smallest = i
		break
	i+=1
print "Smallest = " + str(smallest)
