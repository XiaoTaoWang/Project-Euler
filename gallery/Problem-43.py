# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:09:14 2016

@author: Xiaotao Wang
"""

"""
Problem 43:

The number, 1406357289, is a 0 to 9 pandigital number because it is made up
of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we
note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

"""
import itertools

def divisibleCheck(strnum):
    
    divisors = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        sub = int(strnum[i:i+3])
        if not (sub % divisors[i-1] == 0):
            return False
    
    return True

def sumPan():
    
    per = itertools.permutations('0123456789')
    Sum = 0
    for p in per:
        strnum = ''.join(p)
        if strnum[0] == '0':
            continue
        if strnum[5] != '5':
            continue
        if divisibleCheck(strnum):
            Sum += int(strnum)
    
    return Sum

if __name__ == '__main__':
    print(sumPan())
