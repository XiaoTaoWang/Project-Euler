# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 18:41:13 2016

@author: wxt
"""

"""
Problem 50:

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive
primes?

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

def mostConsecutive(maxnum):
    
    primeList = findallprimes(maxnum)
    primeSum = primeList.cumsum()
    primeSet = set(primeList)
    
    most = 0
    res = 0
    for i in xrange(primeSum.size):
        for j in xrange(i-most-1, 0, -1):
            diff = primeSum[i] - primeSum[j]
            if diff > maxnum:
                break
            if diff in primeSet:
                tmp = i - j
                if tmp > most:
                    most = tmp
                    res = primeSum[i] - primeSum[j]
    
    return most, res

if __name__ == '__main__':
    print mostConsecutive(1000000)