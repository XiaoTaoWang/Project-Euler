# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 18:30:10 2016

@author: wxt
"""

"""
Problem 37:

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each stage:
3797, 7, 97, and 7. Similarly we can work from right to left: 3797, 379, 37,
and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""
import math

def checkprime(num):
    
    if num == 1:
        return 0
    
    maxiter = int(math.sqrt(num))
    
    isprime = 1
    for i in xrange(2, maxiter + 1):
        if num % i == 0:
            isprime = 0
            break
    
    return isprime

def left_trunctable(num):
    
    numstring = str(num)
    label = 1
    for i in range(1, len(numstring)):
        cur = numstring[i:]
        if not checkprime(int(cur)):
            label = 0
            break
    
    return label
    
def findall():
    
    candidates = [2, 3, 5, 7]
    add = [1, 3, 7, 9]
    res = []
    
    while candidates:
        cur = candidates.pop(0)
        for i in add:
            new = cur * 10 + i
            if checkprime(new):
                candidates.append(new)
                if left_trunctable(new):
                    res.append(new)
    
    return res

if __name__ == '__main__':
    
    print sum(findall())
    
    
            