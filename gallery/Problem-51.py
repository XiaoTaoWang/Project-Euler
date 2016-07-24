# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:14:21 2016

@author: wxt
"""

"""
Problem 51:

By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime
with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.

"""
import itertools
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

def genMod(digitnum = 5):
    
    pool = range(digitnum)
    # The repeating part must be 3 or multiple of 3
    # The repeating part cannot include the last digit
    tset = set(range(digitnum-1))
    repeats = itertools.combinations(range(digitnum-1), 3)
    for r in repeats:
        rset = set(r)
        oset = tset - rset
        for i in r:
            pool[i] = '{0}'
        odigits = itertools.permutations('0123456789', len(oset))
        for o in odigits:
            idx = 0
            for i in oset:
                pool[i] = o[idx]
                idx += 1
            for last in ['1','3','7','9']:
                pool[-1] = last
                if pool[0] != '0':
                    yield ''.join(pool)

def findpatterns(digitnum = 5):
    
    primeSet = set(findallprimes(10**(digitnum))) - set(findallprimes(10**(digitnum-1)))
    Mods = genMod(digitnum)
    Res = []
    for m in Mods:
        for i in range(3): # The repeating digit of the smallest prime must be 0, 1, or 2
            numstr = m.format(i)
            if i == 0:
                if numstr.startswith('0'):
                    continue
            num = int(numstr)
            if num in primeSet:
                tmp = num
                break
        else:
            continue
        
        count = 1
        for j in range(i+1, 10):
            if count + 10 - j < 8:
                break
            if count == 8:
                break
            numstr = m.format(j)
            if int(numstr) in primeSet:
                count += 1
        
        if count == 8:
            Res.append(tmp)
    
    return Res

if __name__ == '__main__':
    print findpatterns(6)