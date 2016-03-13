# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 18:36:14 2016

@author: wxt
"""

"""
Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

"""
import math

def maxprimefactor(num):
    
    maxiter = int(math.sqrt(num))
    largest = 0
    for i in xrange(2, maxiter + 1):
        if num % i == 0:
            f1 = i
            f2 = num / i
            for f in [f1, f2]:
                prime = 1 # 0 -- is prime
                for p in xrange(2, int(math.sqrt(f)) + 1):
                    if f % p == 0:
                        prime = 0
                        break
                if prime and (f > largest):
                    largest = f
    
    return largest

def alterScheme(num):
    
    largest = 0
    factor = 2
    iternum = num
    while factor ** 2 <= iternum:
        while iternum % factor == 0:
            iternum /= factor
            largest = factor
        factor += 1
    
    if iternum > largest:
        largest = iternum
    
    return largest

if __name__ == '__main__':

    print maxprimefactor(600851475143)
    print alterScheme(600851475143)
