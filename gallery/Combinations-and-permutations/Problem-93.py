# -*- coding: utf-8 -*-
from __future__ import division
import itertools
"""
Created on Sun Oct 30 13:51:10 2016

@author: Xiaotao Wang
"""

"""
Problem 93:

By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and
making use of the four arithmetic operations (+, −, *, /) and brackets/parentheses,
it is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different
target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can
be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set
of consecutive positive integers, 1 to n, can be obtained, giving your answer
as a string: abcd.

"""

def genpattern():
    
    ori = [(['%d','%s','%d','%s','%d','%s','%d'],(1,3,5)),
           (['%d','%s','(','%d','%s','%d',')','%s','%d'],(1,4,7)),
           (['%d','%s','%d','%s','(','%d','%s','%d',')'],(1,3,6)),
           (['%d','%s','(','%d','%s','%d','%s','%d',')'],(1,4,6)),
           (['(','%d','%s','%d',')','%s','(','%d','%s','%d',')'],(2,5,8))]
    patterns = []
    signs = ['+','-','*','/']
    for i in signs:
        for j in signs:
            for k in signs:
                for o in ori:
                    tmp, p = o
                    tmp[p[0]] = i
                    tmp[p[1]] = j
                    tmp[p[2]] = k
                    patterns.append(''.join(tmp))
    return patterns

def maxn(res):
    for i in range(1,len(res)+1):
        if not i in res:
            return i-1
    return len(res)

def worker():
    patterns = genpattern()
    digits = itertools.combinations(range(10),4)
    med = 0
    abcd = None
    targets = None
    for d in digits:
        res = set()
        perm = itertools.permutations(d)
        for p in perm:
            for pat in patterns:
                exp = pat % p
                try:
                    r = eval(exp)
                    if int(r)==r:
                        res.add(int(r))
                except:
                    pass
        n = maxn(res)
        if n > med:
            med = n
            abcd = d
            targets = res
    return sorted(abcd), med, targets

if __name__ == '__main__':
    abcd, n, t = worker() # ~22.2s