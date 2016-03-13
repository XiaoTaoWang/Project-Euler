# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 21:12:58 2016

@author: wxt
"""

"""
Problem 6:

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

"""
def diff(maxn):
    
    # Sum of squares
    sum_sq = maxn * (maxn + 1) * (2*maxn + 1) / 6
    
    # Square of sum
    sq_sum = (maxn * (maxn + 1)) ** 2 / 4
    
    return sq_sum - sum_sq

if __name__ == '__main__':
    
    print diff(100)
