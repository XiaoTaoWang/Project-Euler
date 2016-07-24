# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 19:32:40 2016

@author: wxt
"""

"""
Problem 5:

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

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

def exprime(maxnum):
    
    res = 1
    primes = findallprimes(maxnum)
    table = {p:0 for p in primes}
    for num in xrange(2, maxnum + 1):
        for p in primes:
            tmp = num
            count = 0
            while tmp % p == 0:
               count += 1
               tmp /= p
            if count > table[p]:
                table[p] = count
    for p in table:
        res *= p**table[p]
    
    return res

if __name__ == '__main__':
    print exprime(20)
        
