# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 10:36:05 2016

@author: wxt
"""

"""
Problem 34:

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their
digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""
# Similar to Problem 30, determining the upper bound is the key point of this
# problem.
# 6 * 9! = 2177280, 7 digits
# 7 * 9! = 2540160, 7 digits
# 8 * 9! = 2903040, 7 digits
import math

pool = []
for num in xrange(10, 2540161):
    strnum = str(num)
    check = 0
    for n in strnum:
        check += math.factorial(int(n))
    if check == num:
        pool.append(num)

print sum(pool)