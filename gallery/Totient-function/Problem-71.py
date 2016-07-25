# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 12:59:09 2016

@author: Xiaotao Wang
"""

"""
Problem 71:

Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order
of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending
order of size, find the numerator of the fraction immediately to the left of
3/7.

"""
# HCF -- Highest Common Factor
def euclidean(x, y):
    
    assert x > 0, y > 0
    
    if x < y:
        x, y = y, x
    
    mod = x % y
    while mod != 0:
        x, y = y, mod
        mod = x % y
    
    return y

def find_fraction(a, b, maxdenom = 1000000):
    
    r = 0
    s = 1
    lowerbound = 2
    q = maxdenom
    while q > lowerbound:
        # Given q, the largest p is ...
        p = (a * q - 1) // b # p/q < a/b --> pb <= aq - 1
        if p*s > q*r: # a better fraction? r/s < p/q
            s = q
            r = p
            # When we consider the distance between p/q and a/b
            # We can give the lower bound of q
            # a/b - p/q = (aq - bp)/bq >= 1/bq
            # p/q is better than r/s if:
            # (as - rb)/bs > 1/bq
            lowerbound = s / (a*s - b*r)
        q -= 1
    
    while euclidean(r, s) != 1:
        r /= euclidean(r, s)
        s /= euclidean(r, s)
    
    return r, s

if __name__ == '__main__':
    res = find_fraction(3, 7) # ~2.05us
