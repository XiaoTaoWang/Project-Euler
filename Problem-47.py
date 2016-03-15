# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:21:20 2016

@author: wxt
"""

"""
Problem 47:

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?

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
    
def primeFactors(num, primeList):
    
    count = 0
    n = num
    p = primeList[0]
    tick = 0
    while (p * p <= n) and (n > 1) and (tick < primeList.size):
        p = primeList[tick]
        tick += 1
        if n % p == 0:
            count += 1
            n /= p
            while n % p == 0:
                n /= p
    
    if n > 1:
        count += 1
    
    return count

def findFours(start = 647, maxnum = 1000000):
    
    primeList = findallprimes(int(np.sqrt(maxnum)))
    
    n = start
    while n <= maxnum:
        count = primeFactors(n, primeList)
        if count == 4:
            label = True
            s = n
            for n in range(s+1, s+4):
                count = primeFactors(n, primeList)
                if count != 4:
                    label = False
                    break
            if label:
                return s
        n += 1

if __name__ == '__main__':
    print findFours()