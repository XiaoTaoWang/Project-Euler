# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:01:45 2016

@author: 27763
"""

"""
Problem 94:

It is easily proved that no equilateral triangle exists with integral length
sides and integral area. However, the almost equilateral triangle 5-5-6 has an
area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two
sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with
integral side lengths and area and whose perimeters do not exceed one billion
(1,000,000,000).

"""
# Recall problem 9, 39, 75 and 86
import math

def euclidean(x, y):
    
    assert x > 0, y > 0
    
    if x < y:
        x, y = y, x
    
    mod = x % y
    while mod != 0:
        x, y = y, mod
        mod = x % y
    
    return y

def worker(maxperi):
    
    # a + b + c = 2km(m+n)
    # so, m < sqrt((a+b+c)/2)
    maxiter = int(math.sqrt(maxperi/2.))
    res = 0
    for n in range(1, maxiter + 1):
        for m in range(n+1, maxiter + 1):
            mod = euclidean(m, n)
            if (mod == 1) and ((m - n) % 2 != 0): # conditions for primitive solutions
                # Use the Euclid's foluma to generate Pythagorean triplets
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                if a + b + c > maxperi:
                    pass
                else:
                    if abs(2*a-c)==1:
                        res += (2*c+2*a)
                    if abs(2*b-c)==1:
                        res += (2*c+2*b)
    return res

if __name__ == '__main__':
    res = worker(1000000000) # ~ 4min 24s
                    