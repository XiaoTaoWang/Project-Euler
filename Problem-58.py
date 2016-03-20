# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 17:51:19 2016

@author: Xiaotao Wang
"""

"""
Problem 58:

Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square
spiral with side length 9 will be formed. If this process is continued,
what is the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?

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

def trial_division(n, primeList):
    
    if n < 2:
        return []
        
    prime_factors = []
    for p in primeList:
        if p*p > n: break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1:
        prime_factors.append(n)
    return prime_factors

def spiralPrimes(ratio = 0.1, maxfactor = 30000):
    
    primeList = findallprimes(maxfactor)
    
    n = 3
    count = 0
    while True:
        assert n < maxfactor, 'The primeList is limited, raise maxfactor'
        
        total = 2 * n - 1
        for num in [n**2-n+1, n**2-2*n+2, n**2-3*n+3]:
            primefactor = trial_division(num, primeList)
            if len(primefactor) == 1:
                count += 1
        
        R = count / total
        if R < ratio:
            return n
        
        n += 2

if __name__ == '__main__':
    print(spiralPrimes())