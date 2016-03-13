# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 11:42:13 2016

@author: Xiaotao Wang
"""

"""
Problem 35:

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?

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

def circular(strnum):
    
    for i in range(1, len(strnum)):
        yield int(strnum[i:] + strnum[:i])

def cirPrimes(maxnum):
    
    primeList = set(findallprimes(maxnum))
    cirList = set()
    for num in primeList:
        strnum = str(num)
        tmpList = []
        if len(strnum) == 1:
            cirList.add(num)
            continue
        for i in strnum:
            if (int(i) % 2 == 0) or (i == '5'):
                break
        else:
            for c in circular(strnum):
                if c in primeList:
                    tmpList.append(c)
                else:
                    break
            else:
                tmpList.append(num)
                cirList.update(set(tmpList))
    
    return cirList

if __name__ == '__main__':
    L = cirPrimes(1000000)
        

