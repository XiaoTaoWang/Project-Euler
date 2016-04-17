# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 14:47:59 2016

@author: Xiaotao Wang
"""

"""
Problem 62:

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.

"""
from collections import defaultdict

def numtokey(num):
    numlist = list(map(str, str(num)))
    numlist.sort()
    return int(''.join(numlist[::-1]))

def findcube(start):
    
    counter = defaultdict(int)
    D = {}
    while True:
        cube = start ** 3
        key = numtokey(cube)
        if not key in D:
            D[key] = start
        counter[key] += 1
        if counter[key] == 5:
            return key, D[key]
        
        start += 1

if __name__ == '__main__':
    res = findcube(345)
        