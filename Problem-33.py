# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 09:55:13 2016

@author: wxt
"""

"""
Problem 33:

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.

"""
# Think this problem mathematically can dramatically reduce the search space
# Consider 4 possible forms of the original fraction:
# (10i + n) / (10i + d) = n / d
# (10n + i) / (10d + i) = n / d
# (10i + n) / (10d + i) = n / d
# (10n + i) / (10i + d) = n / d
# where n < d
# Analyze these combinations, and you will realize that only the last form is
# possible and n < d < i

def euclidean(x, y):
    
    assert x > 0, y > 0
    
    if x < y:
        x, y = y, x
    
    mod = x % y
    while mod != 0:
        x, y = y, mod
        mod = x % y
    
    return y
    
if __name__ == '__main__':
    p_numerator = 1
    p_denominator = 1
    
    for i in range(1, 10):
        for d in range(1, i):
            for n in range(1, d):
                if (10*n + i) * d == (10*i + d) * n:
                    p_numerator *= n
                    p_denominator *= d
    print p_denominator / euclidean(p_numerator, p_denominator)