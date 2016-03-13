# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 08:56:01 2016

@author: wxt
"""

"""
Problem 32:

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.

"""

def isPandigital(num):
    
    digits = map(int, num)
    digits.sort()
    
    return digits == range(1, len(digits)+1)

def concatenate(*args):
    
    num = ''.join(map(str, args))
    
    return num

def findall():
    
    L = set()
    for i in xrange(1, 100):
        if i < 10:
            multiplier = xrange(1000, 10000)
        else:
            multiplier = xrange(100, 1000)
        for j in multiplier:
            p = i * j
            num = concatenate(i, j, p)
            if isPandigital(num):
                L.add(p)
    
    return sum(list(L))

if __name__ == '__main__':
    
    print findall()
    