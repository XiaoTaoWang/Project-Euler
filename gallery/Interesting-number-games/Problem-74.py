# -*- coding: utf-8 -*-
"""
Created on Sun May  8 17:41:48 2016

@author: Xiaotao Wang
"""

"""
Problem 74:

The number 145 is well known for the property that the sum of the factorial
of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of
numbers that link back to 169; it turns out that there are only three such
loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get
stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the
longest non-repeating chain with a starting number below one million is
sixty terms.

How many chains, with a starting number below one million, contain exactly
sixty non-repeating terms?

"""
import math

def facsum(num):
    strnum = str(num)
    Sum = 0
    for d in strnum:
        Sum += math.factorial(int(d))
    
    return Sum

def count_chains(chainLen = 60, maxnum = 10**6):
    
    cache = {}
    count = 0
    for start in range(2, maxnum):
        if start in cache:
            if cache[start] == 60:
                count += 1
                continue
        tmpdict = {}
        reverse = {}
        cur = start
        tick = 1
        while not cur in tmpdict:
            tmpdict[cur] = tick
            reverse[tick] = cur
            cur = facsum(cur)
            tick += 1
        for i in range(1, tmpdict[cur]+1):
            cache[reverse[i]] = tick - i
        if cache[start] == 60:
            count += 1
    
    return count

if __name__ == '__main__':
    count = count_chains() # ~1min 8s
    