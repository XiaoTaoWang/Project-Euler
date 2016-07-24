# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 20:46:56 2016

@author: wxt
"""

"""
Problem 14:

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

def gofrom(start):
    
    count = 1
    while start > 1:
        if start % 2 == 0:
            start /= 2
        else:
            start = 3 * start + 1
        count += 1
    
    return count

def longest(maxnum):
    
    if maxnum % 2 == 0:
        start = maxnum - 2
    else:
        start = maxnum - 1
        
    tmp = gofrom(start)
    for i in xrange(3, maxnum, 2):
        count = gofrom(i)
        if count > tmp:
            tmp = count
            start = i
    return start, tmp

if __name__ == '__main__':
    
    start, chain = longest(1000000)
    print 'If we start at {0}, we will get the longest chain {1}'.format(start, chain)