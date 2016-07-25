# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:18:47 2016

@author: wxt
"""

"""
Problem 46:

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?

"""
import numpy as np

def findallprimes(maxnum):
    
    Bool = np.ones(maxnum, dtype = bool)
    Bool[0] = 0
    maxiter = int(np.sqrt(maxnum))
    for i in range(2, maxiter+1):
        if Bool[i-1]:
            # Sieve of Eratosthenes
            Bool[np.arange(2*i-1, maxnum, i)] = False
    
    return np.where(Bool)[0] + 1

def twiceSquare(num):
    
    query = np.sqrt(num/2.)
    
    return query == int(query)

def itercheck(maxnum = 10000):
    
    primeList = findallprimes(maxnum)
    primeSet = set(primeList)
    
    n = 35
    while True:
        assert n < maxnum, 'n is greater than the upper bound'
        if not n in primeSet:
            label = False
            for p in primeList:
                if p > n:
                    break
                if twiceSquare(n - p):
                    label = True
            if not label:
                return n
        n += 2

if __name__ == '__main__':
    
    print itercheck() # ~3.37s