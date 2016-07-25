# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 19:01:56 2016

@author: Xiaotao Wang
"""

"""
Problem 91:

https://projecteuler.net/problem=91

"""
# The counting process can be conducted in a symmetrical way
# We can classify those right angle triangles into two cases:
# In the special case, the right angle is just on the axis. (3*Xmax*Ymax in total)
# In the regular case, the right angle lies in the first quadrant

def euclidean(x, y):
    
    assert x > 0, y > 0
    
    if x < y:
        x, y = y, x
    
    mod = x % y
    while mod != 0:
        x, y = y, mod
        mod = x % y
    
    return y

def count(xmax, ymax):
    
    # The special case
    special = 3 * xmax * ymax
    
    # The regular case
    # Count symmetrically
    regular = 0
    for x1 in xrange(1, xmax+1):
        for y1 in xrange(1, ymax+1):
            gcd = euclidean(x1, y1)
            dx = x1 / gcd
            dy = y1 / gcd
            x2 = x1 + dy; y2 = y1 - dx
            while (x2 <= xmax) and (y2 >= 0):
                regular += 1
                x2 += dy
                y2 -= dx
    
    regular *= 2
    
    return special+regular

if __name__ == '__main__':
    res = count(50, 50) # ~1.66ms