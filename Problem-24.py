# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 21:04:32 2016

@author: wxt
"""

"""
Problem 24:

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?

"""
import itertools

per = itertools.permutations('0123456789')

for count, mem in enumerate(per):
    if count == (999999):
        print mem
        break