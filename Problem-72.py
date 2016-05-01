# -*- coding: utf-8 -*-
"""
Created on Sun May  1 21:33:35 2016

@author: Xiaotao Wang
"""

"""
Problem 72:

Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order
of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions
for d ≤ 1,000,000?

"""
# The key point to solve this problem is to find the relationship between
# this problem and the well-known Euler's totient function
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

def num_elements(maxn = 1000000):
    
    primeList = findallprimes(int(np.ceil(np.sqrt(maxn))))
    
    count = 0
    for i in range(2, maxn+1):
        factors = set(trial_division(i, primeList))
        phi_n = i
        for f in factors:
            phi_n = phi_n * (f-1) / f
            
        count += phi_n
    
    return count
#-------------------------------------------------------------------------
# The clever solution
# Some talent people modified Sieve of Eratosthenes Algorithm to solve
# this problem
def clever_count(maxn = 1000000):
    
    phi = np.arange(2, maxn+1, dtype = np.int64)
    for i in range(2, maxn+1):
        if phi[i-2] == i:
            for j in range(i, maxn+1, i):
                phi[j-2] = phi[j-2] * (i - 1) / i
    
    return phi.sum()

if __name__ == '__main__':
    #count = num_elements()
    count = clever_count()