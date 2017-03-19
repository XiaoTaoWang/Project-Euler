# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 12:49:22 2017

@author: XiaoTao Wang
"""

"""
Problem 113: Non-bouncy numbers

Working from left-to-right if no digit is exceeded by the digit to its left it
is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a
"bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that
there are only 12951 numbers below one-million that are not bouncy and only
277032 non-bouncy numbers below 10^10.

How many numbers below a googol (10^100) are not bouncy?

"""
# Reference: http://mathschallenge.net/full/never_decreasing_digits

from math import factorial

def non_decreasing(n_digit=100):
    
    total = factorial(n_digit+9) / factorial(9) / factorial(n_digit) - 1
    
    return total

def non_increasing(n_digit=100):
    # a decreasing number can be obtained by reversing an increasing number
    # to consider possible tailing zeros of a decreasing number, I dissect
    # leading part of the coded binary strings into several cases:
    # 0, 10, 110, 1110, 11110, ...
    r = 8
    ori = n_digit + 8
    m = 1
    total = 0
    while ori >= 9:
        cur = factorial(ori) / factorial(r) / factorial(ori-r)
        total += (cur*m)
        m += 1
        ori -= 1
    
    return total

def doubles(n_digit=100):
    # Some numbers are counted tiwce:
    # 1, 11, 111, 1111, ...
    # 2, 22, 222, 2222, ...
    # 3, 33, 333, 3333, ...
    # ...
    return 9*n_digit

def not_bouncy(n_digit=100):
    
    total = non_increasing(n_digit) + non_decreasing(n_digit) - doubles(n_digit)
    
    return total

if __name__ == '__main__':
    total = not_bouncy(100) # ~833us