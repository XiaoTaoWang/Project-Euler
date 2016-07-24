# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 10:12:39 2016

@author: wxt
"""

"""
Problem 69:


Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime
to nine, φ(9)=6.

n 	Relatively Prime   φ(n) 	  n/φ(n)
2 	1                   1 	       2
3 	1,2                 2 	       1.5
4 	1,3                 2 	       2
5 	1,2,3,4 	          4 	       1.25
6 	1,5                 2 	       3
7 	1,2,3,4,5,6         6 	       1.1666...
8 	1,3,5,7 	          4 	       2
9 	1,2,4,5,7,8         6 	       1.5
10 	1,3,7,9 	          4 	       2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

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

def maxratio(n):
    
    primeList = findallprimes(int(np.ceil(np.sqrt(n))))
    
    iteratio = 0
    iter_n = 2
    for i in range(2, n+1):
        factors = set(trial_division(i, primeList))
        phi_n = i
        for f in factors:
            phi_n = phi_n * (f-1) / f
        tmp = i / phi_n
        if tmp > iteratio:
            iteratio = tmp
            iter_n = i
    
    return iter_n, iteratio

if __name__ == '__main__':
    res = maxratio(10)
    
    # The best method to solve this problem doesn't need a computer,
    # 2*3*5*7*11*13*17 <= 1000000 < 2*3*5*7*11*13*17*19
    # so the result of this problem is 2*3*5*7*11*13*17 = 510510 