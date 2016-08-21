# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 19:33:43 2016

@author: Xiaotao Wang
"""

"""
Problem 88:

A natural number, N, that can be written as the sum and product of a given set
of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum
number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a
minimal product-sum number. The minimal product-sum numbers for sets of size,
k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30;
note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6,
8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

"""
# A little analysis:
# There are two insights under this problem:
# First, for any set of factors, we can add ones to make it a valid product-sum.
# Of course, whether is's minimal or not is another question.
# The second insights is about the bound determination,
# the lower bound of the minimal product-sum for k must be k, which consists of
# k ones which sum up to k exactly, the upper bound may be 2k, because we can
# always convert {2, k} to a valid product-sum by adding k-2 ones.

# To solve this problem, we need to design an algorithm to factorize number
# between 2 and 24000 one by one, and check if any factorization is the minimal
# product-sum for some k.

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

def factorize(num, primes, cache):
    
    if num in primes:
        cache[num] = {(num,)}
        return cache[num]
    ways = cache.get(num, set())
    if len(ways):
        return ways
    for i in xrange(2, int(np.sqrt(num))+1):
        q, r = divmod(num, i)
        if r == 0:
            part1 = factorize(i, primes, cache)
            part2 = factorize(q, primes, cache)
            for p1 in part1:
                for p2 in part2:
                    tmp = list(p1+p2)
                    tmp.sort()
                    ways.add(tuple(tmp))
    ways.add((num,))
    cache[num] = ways
    return ways

def worker(maxk):
    
    primes = set(findallprimes(2*maxk))
    cache = {}
    pairs = {}
    for num in xrange(4, 2*maxk+1):
        ways = factorize(num, primes, cache)
        for w in ways:
            if len(w) > 1:
                k = num - sum(w) + len(w)
                if k <= maxk:
                    pairs.setdefault(k, num)
    res = sum(set(pairs.values()))
    
    return res, pairs
        
if __name__ == '__main__':
    res, pairs = worker(12000) # ~2.76s
    