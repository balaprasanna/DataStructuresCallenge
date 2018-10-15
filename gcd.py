"""
GCD for a,b
"""
from util import collectInputs



def EuclidGCD(a,b):

	if b == 0:
		return a

	aPrime = a % b
	return EuclidGCD(b, aPrime)

if __name__ == "__main__":
	a,b = collectInputs(2)
	print(EuclidGCD(a,b))