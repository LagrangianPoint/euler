#!/usr/bin/python
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
import sys

A, B, C = 1,2,3
#max = 1000
max = 1000
while A <= max:
	B = A + 1
	while B <= max:
		C = B + 1
		while C <= max:
			#print "========="
			#print ("| %d | %d | %d |")%(A,B,C)			
			if A**2 + B**2 == C**2:
				if A + B + C == 1000:
					print ("(%d)^2+(%d)^2=(%d)^2")%(A,B,C)
					print "Multiplication: "+ str(A*B*C)
					sys.exit(1)
					break
				C += 1
				continue
			else:
				C += 1
				continue
			break
		else :
			B += 1
			continue
		break
	else:
		A += 1
		continue
	break


