# -*- coding: utf-8 -*-
"""
Created on Sun May  1 22:31:54 2016

@author: Xiaotao Wang
"""

"""
Problem 73:

Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order
of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
proper fractions for d ≤ 12,000?

"""
# Reference: Farey Sequence in WiKi:
# https://en.wikipedia.org/wiki/Farey_sequence
# The link gives an algorithm to generate the terms of F(n)
def gen_farey(n = 12000, a = 1, b = 3, c = 4000, d = 11999, end = 1/2):
    
    count = 0
    while c/d < end:
        count += 1
        k = (n + b) // d
        a, b, c, d = c, d, k*c - a, k*d - b
    
    return count

if __name__ == '__main__':
    res = gen_farey() # ~180ns
    