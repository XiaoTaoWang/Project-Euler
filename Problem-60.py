# -*- coding: utf-8 -*-
"""
Created on Sun May 22 22:40:59 2016

@author: Xiaotao Wang
"""

"""
Problem 60:

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of
these four primes, 792, represents the lowest sum for a set of four primes
with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.

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

# Miller-Rabin primality test
def get_witnesses(n):
    """
    Returns a tuple of definitive Miller-Rabin witnesses for n.
    
    References
    ----------
    .. [1] http://oeis.org/A014233
    .. [2] http://mathworld.wolfram.com/Rabin-MillerStrongPseudoprimeTest.html
    .. [3] http://primes.utm.edu/prove/prove2_3.html
    .. [4] http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    
    """
    assert (n > 2) and (n % 2 == 1)
    if n < 2047:
        # References: [1], [2], [4]
        witnesses = (2,)
    elif n < 1373653:  # ~1.3 million
        # References: [1], [2], [3], [4]
        witnesses = (2, 3)
    elif n < 9080191:  # ~9.0 million
        # References: [3], [4]
        witnesses = (31, 73)
    elif n < 25326001:  # ~25.3 million
        # References: [1], [2], [3], [4]
        witnesses = (2, 3, 5)
    elif n < 3215031751:  # ~3.2 billion
        # References: [1], [2], [3], [4]
        witnesses = (2, 3, 5, 7)
    elif n < 4759123141:  # ~4.7 billion
        # References: [3], [4]
        witnesses = (2, 7, 61)
    elif n < 2152302898747:  # ~2.1 trillion
        # References: [1], [2], [3], [4]
        witnesses = (2, 3, 5, 7, 11)
    elif n < 3474749660383:  # ~3.4 trillion
        # References: [1], [2], [3], [4]
        witnesses = (2, 3, 5, 7, 11, 13)
    elif n < 341550071728321:  # ~341.5 trillion
        # References: [1], [2], [3], [4]
        witnesses = (2, 3, 5, 7, 11, 13, 17)
    elif n < 3825123056546413051:  # ~3.8 million trillion
        # References: [1], [4]
        witnesses = (2, 3, 5, 7, 11, 13, 17, 19, 23)
    elif n <= 2**64:
        witnesses = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    else:
        witnesses = None
        
    return witnesses

def is_miller_rabin_prime(n):
    """
    Returns True for primes, False for non-primes and raises ValueError for
    unsure cases.
    """
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    witnesses = get_witnesses(n)
    if witnesses is None:
        msg = 'No definite Miller-Rabin test is available for %d' % n
        raise ValueError(msg)
    
    d, s = factorN(n-1)
    for w in witnesses:
        if is_composite(w, n, d, s):
            return False
    
    return True

def is_composite(witness, n, d, s):
    
    assert d*2**s == n-1
    
    if pow(witness, d, n) == 1:
        return False
    for i in range(s):
        if pow(witness, 2**i*d, n) == n-1:
            return False
    
    return True
  
def factorN(n):
    
    s = 0
    d = n
    while True:
        q, r = divmod(d, 2)
        if r == 1:
            break
        s += 1
        d = q
    
    assert d*2**s == n
    
    return d, s
#------------------------------------------------------------------------------
def mergeCheck(num1, num2):
    check1 = num1 + num2 * 10**int(np.ceil(np.log10(num1)))
    check2 = num2 + num1 * 10**int(np.ceil(np.log10(num2)))
    
    return is_miller_rabin_prime(check1) and is_miller_rabin_prime(check2)
    
def main(searchmax = 20000):
    primes = findallprimes(searchmax)
    Bool_matrix = np.zeros((primes.size, primes.size), dtype = np.bool)
    
    for i in xrange(primes.size-1):
        for j in xrange(i+1, primes.size):
            check = mergeCheck(int(primes[i]), int(primes[j]))
            Bool_matrix[i, j] = check
    
    candidates = []
    for i1 in xrange(primes.size-4):
        for i2 in xrange(i1+1, primes.size-3):
            if not Bool_matrix[i1, i2]:
                continue
            for i3 in xrange(i2+1, primes.size-2):
                if (not Bool_matrix[i1, i3]) or (not Bool_matrix[i2, i3]):
                    continue
                for i4 in xrange(i3+1, primes.size-1):
                    if not (Bool_matrix[i1, i4] and Bool_matrix[i2, i4] and Bool_matrix[i3, i4]):
                        continue
                    for i5 in xrange(i4+1, primes.size):
                        if Bool_matrix[i1, i5] and Bool_matrix[i2, i5] and Bool_matrix[i3, i5] and Bool_matrix[i4, i5]:
                            candidates.append([primes[i] for i in [i1, i2, i3, i4, i5]])
    
    assert len(candidates) > 0, 'No solution can be found, please expand the search space'
    
    minsum = sum(candidates[0])
    lowest_five = candidates[0]
    for candi in candidates[1:]:
        cursum = sum(candi)
        if cursum < minsum:
            minsum = cursum
            lowest_five = candi
    
    lowest_five.sort()
    
    return lowest_five

if __name__ == '__main__':
    result = main(searchmax=10000) # ~20s
    