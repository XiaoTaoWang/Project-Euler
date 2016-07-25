# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:34:39 2016

@author: Xiaotao Wang
"""

"""
Problem 53:

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr = n! / (r!(n−r)!)

where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are
greater than one-million?

"""

import math

def count(min_n = 23, max_n = 100, mincom = 1000000):
    
    num = 0
    for n in range(min_n, max_n+1):
        for r in range(1, n//2+1):
            com = math.factorial(n) / (math.factorial(r) * math.factorial(n-r))
            if com > mincom:
                if n == 2 * r:
                    num += 1
                else:
                    num += 2
    
    return num

if __name__ == '__main__':
    print(count()) # ~22.2ms