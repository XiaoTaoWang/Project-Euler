# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 18:04:13 2016

@author: wxt
"""

"""
Problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""
def findmultiples(maxnum, *args):
    
    factors = args
    res = 0
    for i in xrange(2, maxnum):
        for j in factors:
            if i % j == 0:
                res += i
                break
    
    return res

if __name__ == '__main__':
    print findmultiples(1000, 3, 5)