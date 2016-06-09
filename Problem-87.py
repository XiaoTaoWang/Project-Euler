# -*- coding: utf-8 -*-
"""
Created on Tue May 31 13:06:24 2016

@author: Xiaotao Wang
"""

"""
Problem 87:

The smallest number expressible as the sum of a prime square, prime cube, and
prime fourth power is 28. In fact, there are exactly four numbers below fifty
that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime
square, prime cube, and prime fourth power?

"""
import numpy as np

def findallprimes(maxnum):
    
    Bool = np.ones(maxnum, dtype = bool)
    Bool[0] = 0
    maxiter = int(np.sqrt(maxnum))
    for i in xrange(2, maxiter+1):
        if Bool[i-1]:
            # Sieve of Eratosthenes
            Bool[np.arange(2*i-1, maxnum, i)] = False
    
    return np.where(Bool)[0] + 1

def bruteSearch():
    upperbound = 50000000
    primes = findallprimes(int(np.ceil(np.sqrt(upperbound))))
    results = set()
    for i in primes:
        for j in primes:
            for k in primes:
                tmpnum = i**2 + j**3 + k**4
                if tmpnum < upperbound:
                    results.add(tmpnum)
                else:
                    break
    
    return len(results)

if __name__ == '__main__':
    res = bruteSearch() # ~2.28s