# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 10:06:51 2016

@author: wxt
"""

"""
Problem 17:

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.

"""
# It's much more like a arithmetic problem
# 0 - 9
ones = sum([3, 3, 5, 4, 4, 3, 5, 5, 4])

# 10 - 19
teens = sum([3, 6, 6, 8, 8, 7, 7, 9, 8, 8])

# 20 - 99
tens = 10 * sum([6, 6, 5, 5, 5, 7, 6, 6]) + 8 * ones

# so, 1 - 99
tmp = ones + teens + tens

# 100 - 999
hundreds = ones * 100 + tmp * 9 + 7 * 9 + 10 * 9 * 99

# 1000
thousand = 11

print tmp + hundreds + thousand