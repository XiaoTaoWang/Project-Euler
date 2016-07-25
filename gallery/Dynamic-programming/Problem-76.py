# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 21:56:05 2016

@author: Xiaotao Wang
"""

"""
Problem 76:


It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two
positive integers?

"""
# Recall Problem 31 ...
# Use dynamic programming
def dynamic(total):
    
    pieces = list(range(1, total))
    counts = [0 for i in range(total+1)]
    counts[0] = 1
    for p in pieces:
        for med in range(p, total+1):
            counts[med] += counts[med-p]
    
    return counts[-1]

if __name__ == '__main__':
    res = dynamic(100) # ~520us