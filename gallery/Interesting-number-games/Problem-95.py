# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 17:17:41 2016

@author: Xiaotao Wang
"""

"""
Problem 95:

The proper divisors of a number are all the divisors excluding the number itself.
For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of
these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the
proper divisors of 284 is 220, forming a chain of two numbers. For this reason,
220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we
form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding
one million.

"""

# Recall problem 21
# Instead of brute forcing, I conceive of a slightly more efficient algorithm
# for calculating sum of proper divisors of large number by using Prime
# Fractorization.

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

# Prime Fractorization
def sumbyprimes(num, primelist):
    
    n = num
    result = 1
    p = primelist[0]
    count = 0
    while (p * p <= n) and (n > 1) and (count < primelist.size):
        p = primelist[count]
        count += 1
        if n % p == 0:
            j = p * p
            n /= p
            while n % p == 0:
                j *= p
                n /= p
            result *= ((j - 1) / (p - 1))
            
    if n > 1:
        result *= (n + 1)
    
    return result - num

def nextmem(num, primeList, cache):
    
    if num in cache:
        return cache[num]
    else:
        cache[num] = sumbyprimes(num, primeList)
        return cache[num]

def reconstruct(num, cache):
    
    chain = [num]
    while True:
        nextnum = cache[num]
        chain.append(nextnum)
        if nextnum == chain[0]:
            return chain
        else:
            num = nextnum

def search(maxnum):
    
    primelist = findallprimes(int(np.sqrt(maxnum)))
    cache = {}
    maxcount = 5
    smallest = 12496
    for num in xrange(2, maxnum+1):
        count = 1
        nested = set([num])
        nextnum = nextmem(num, primelist, cache)
        while nextnum != num:
            if (nextnum == 1) or (nextnum in nested) or (nextnum > maxnum):
                count = 0
                break
            nested.add(nextnum)
            nextnum = nextmem(nextnum, primelist, cache)
            count += 1
        if count > maxcount:
            maxcount = count
            smallest = num
    
    chain = reconstruct(smallest, cache)
    
    return smallest, maxcount,chain

if __name__ == '__main__':
    res = search(1000000) # ~36.4s