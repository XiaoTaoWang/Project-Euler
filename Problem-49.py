# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 18:24:47 2016

@author: wxt
"""

"""
Problem 49:

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

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
    
def checkPermutation(strnum1, strnum2):
    
    L1 = list(strnum1)
    L2 = list(strnum2)
    L1.sort()
    L2.sort()
    
    return L1 == L2

def findseq():
    
    primeSet = set(findallprimes(10000)) - set(findallprimes(1000))
    primeList = list(primeSet)
    primeList.sort()
    
    for i in xrange(len(primeList)-1):
        a = primeList[i]
        if a == 1487:
            continue
        for j in xrange(i+1, len(primeList)):
            b = primeList[j]
            delta = b - a
            c = b + delta
            if c in primeSet:
                if checkPermutation(str(a), str(b)) and checkPermutation(str(b), str(c)):
                    return a, b, c

if __name__ == '__main__':
    print findseq()
    