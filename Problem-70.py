# -*- coding: utf-8 -*-
"""
Created on Sun May  8 10:55:54 2016

@author: Xiaotao Wang
"""

"""
Problem 70:

Euler's Totient function, φ(n) [sometimes called the phi function], is used
to determine the number of positive numbers less than or equal to n which
are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all
less than nine and relatively prime to nine, φ(9)=6.

The number 1 is considered to be relatively prime to every positive number,
so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation
of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and
the ratio n/φ(n) produces a minimum.

"""
import numpy as np

def checkPermutation(strnum1, strnum2):
    
    L1 = list(strnum1)
    L2 = list(strnum2)
    L1.sort()
    L2.sort()
    
    return L1 == L2

def findallprimes(maxnum):
    
    Bool = np.ones(maxnum, dtype = bool)
    Bool[0] = 0
    maxiter = int(np.sqrt(maxnum))
    for i in range(2, maxiter+1):
        if Bool[i-1]:
            # Sieve of Eratosthenes
            Bool[np.arange(2*i-1, maxnum, i)] = False
    
    return np.where(Bool)[0] + 1

def iter_check(lower = 2000, upper = 5000, maximum = 10**7):
    """
    The details of this function depends on the analysis of the problem.
    
    Since we need to minimize the n/φ(n), the prime factors of n should be
    large and the number of them should be as small as possible.
    
    The simplest case, there is only one prime, and n == p, φ(n) = p - 1.
    Obviously, p - 1 cannot be a permutation of p.
    
    Then the case, two primes, and n == p1 * p2, φ(n) = (p1 - 1) * (p2 - 1).
    
    ...
    
    """
    
    primeList = findallprimes(upper)
    primeList = primeList[(primeList > lower) & (primeList < upper)]
    minimum = np.inf
    solution = 0
    for i in range(primeList.size-1):
        for j in range(i+1, primeList.size):
            p1 = primeList[i]
            p2 = primeList[j]
            n = p1 * p2
            if n > maximum:
                continue
            phi_n = (p1 - 1) * (p2 - 1)
            if checkPermutation(str(n), str(phi_n)):
                ratio = n / phi_n
                if ratio < minimum:
                    minimum = ratio
                    solution = n
    if minimum == np.inf:
        raise 'No soultion can be found in this case, try next case: three primes'
    
    return solution, minimum

if __name__ == '__main__':
    res = iter_check() # Takes about 168ms
    
    