#!/usr/bin/python
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(number):
	strNumber = str(number);
	numLength = len(strNumber)
	i = 0
	bPalindrome = True
	while i <= numLength/2 :
		if strNumber[i] != strNumber[numLength-1-i]:
			bPalindrome = False;
			break;
		i += 1
	return bPalindrome
digits = 3
largest = 1
for A in range(10**(digits-1),10**(digits)):
	for B in range(10**(digits-1),10**(digits)):
		if isPalindrome(A*B):
			print (">>>> %s and %s are palindrome! --> %s ") %(A,B,A*B)
			if A*B > largest:
				largest =  A*B
print "Largest"
print largest
