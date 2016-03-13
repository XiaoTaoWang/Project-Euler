# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 19:30:52 2016

@author: wxt
"""

"""
Problem 10:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
import numpy as np

def findallprimes(maxnum):
    
    ori = np.arange(1, maxnum+1)
    Bool = np.ones(maxnum, dtype = bool)
    Bool[0] = 0
    maxiter = int(np.sqrt(maxnum))
    for i in xrange(2, maxiter+1):
        if Bool[i-1]:
            # Sieve of Eratosthenes
            Bool[np.arange(2*i-1, maxnum, i)] = False
    
    return ori[Bool]

if __name__ == '__main__':
    primes = findallprimes(2000000)
    Sum = 0L
    for p in primes:
        Sum += p
    print Sum