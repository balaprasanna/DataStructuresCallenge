"""
git remote add origin https://github.com/balaprasanna/DataStructuresCallenge.git
git push -u origin master

GCD for a,b
"""
from util import collectInputs

best = 0
a,b = collectInputs(2)

def EuclidGCD(a,b):

	if b == 0:
		return a

	aPrime = a % b
	return EuclidGCD(b, aPrime)

print(EuclidGCD(a,b))	