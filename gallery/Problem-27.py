# -*- coding: utf-8 -*-
"""
Created on Tue Mar 08 10:05:56 2016

@author: wxt
"""

"""
Problem 27:

Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n^2 − 79n + 1601 was discovered, which produces 80 primes
for the consecutive values n = 0 to 79. The product of the coefficients, −79 and
1601, is −126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with
n = 0.

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

def findquad(maxa = 1000, maxb = 1000):
    
    ref = set(findallprimes(100000))
    maxlen = resa = resb= 0
    for a in xrange(-maxa+1, maxa):
        for b in xrange(-maxb+1, maxb):
            if (not b in ref) or (not 1 + a + b in ref):
                continue
            i = 2
            while i**2 + a*i + b in ref:
                i += 1
            if i > maxlen:
                maxlen = i
                resa = a
                resb = b
    
    return resa, resb, maxlen

if __name__ == '__main__':
    print findquad()
    
    