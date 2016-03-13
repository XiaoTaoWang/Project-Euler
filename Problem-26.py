# -*- coding: utf-8 -*-
"""
Created on Tue Mar 08 09:20:01 2016

@author: wxt
"""

"""
Problem 26:

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.

"""

def findcycles(num):
    
    startpoint = 1
    remainder = {1:0}
    
    cyclen = 0
    for i in xrange(1, num):
        startpoint *= 10
        r = startpoint % num
        if r  == 0:
            continue
        if r in remainder:
            cyclen = i - remainder[r]
            break
        else:
            remainder[r] = i
    
    return cyclen

if __name__ == '__main__':
    
    maxlen = 0; res = 0
    for num in xrange(1000, 1, -1):
        if maxlen >= num:
            break
        cyclen = findcycles(num)
        if cyclen > maxlen:
            maxlen = cyclen
            res = num
    
    print res, maxlen
        