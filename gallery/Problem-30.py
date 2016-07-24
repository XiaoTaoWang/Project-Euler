# -*- coding: utf-8 -*-
"""
Created on Tue Mar 08 11:15:47 2016

@author: wxt
"""

"""
Problem 30:

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.

"""
# Determining the upper bound is the critical point of this problem.
# 5 * 9 ** 5 = 295245, 6 * 9 ** 5 = 354294

pool = []

for num in xrange(2, 355000):
    
    strnum = str(num)
    check = 0
    for n in strnum:
        check += int(n) ** 5
    if check == num:
        pool.append(num)

print sum(pool)
