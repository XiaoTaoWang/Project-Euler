# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 20:00:15 2016

@author: Xiaotao Wang
"""

"""
Problem 78:

Let p(n) represent the number of different ways in which n coins can be separated
into piles. For example, five coins can be separated into piles in exactly seven
different ways, so p(5)=7.

OOOOO
OOOO O
OOO OO
OOO O O
OO OO O
OO O O O
O O O O O

Find the least value of n for which p(n) is divisible by one million.
"""
# I recalled problem 31, 76, and 77 again at the first sight.
# However, this problem is a much more difficult continuation compared with
# previous ones. It's intolerable to run that dynamic program again
# and again until finding the p(n) divisible by 1000000.

# Treat this problem more mathematically, the p(n) is the partition function
# in number theory.
# And refer to wiki, there's a marvelous recursive generating function for it.
def pentagonal():
    """
    Generalized pentagonal number generator.
    """
    idx = 2
    while True:
        size = idx // 2
        k = size*(-1)**idx
        gk = k*(3*k-1) // 2
        sign = (-1)**abs(k-1)
        yield gk, sign
        idx += 1
    
def worker():
    pcache = [1] # p(0) = 1
    divisor = 1000000
    remainder = 1
    n = 0
    while remainder != 0:
        n += 1
        cur = 0
        pen = pentagonal()
        for gk, sign in pen:
            if n - gk < 0:
                break
            cur += (sign*pcache[n-gk])
        pcache.append(cur)
        remainder = cur % divisor
    
    return n

if __name__ == '__main__':
    res = worker() # ~11.7s
        