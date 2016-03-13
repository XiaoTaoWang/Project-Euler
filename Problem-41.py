# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:06:05 2016

@author: Xiaotao Wang
"""

"""
Problem 41:

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?

"""
# Here's is a trick to lower the upper bound
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

def isPandigital(num):
    
    digits = list(map(int, num))
    digits.sort()
    
    return digits == list(range(1, len(digits)+1))

def search(maxnum):
    
    primeList = findallprimes(maxnum)
    maxpan = 0
    for i in primeList:
        if isPandigital(str(i)):
            if i > maxpan:
                maxpan = i
    return maxpan

if __name__ == '__main__':
    print(search(7654321))
