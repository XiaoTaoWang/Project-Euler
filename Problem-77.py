# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 18:45:02 2016

@author: Xiaotao Wang
"""

"""
Problem 77:

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five
thousand different ways?

"""
# Recall problem 31 an 76 ...
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

def worker():
    
    pieces = findallprimes(100)
    num = 10
    waynum = 5
    while waynum <= 5000:
        num += 1
        counts = [0 for i in range(num+1)]
        counts[0] = 1
        for p in pieces:
            for med in xrange(p, num+1):
                counts[med] += counts[med-p]
        
        waynum = counts[-1]
    
    return num

if __name__ == '__main__':
    target = worker() # ~5.36ms