# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 22:47:09 2016

@author: Xiaotao Wang
"""

"""
Problem 75: Singular integer right triangles

It turns out that 12 cm is the smallest length of wire that can be bent to form
an integer sided right angle triangle in exactly one way, but there are many
more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer
sided right angle triangle, and other lengths allow more than one solution to be
found; for example, using 120 cm it is possible to form exactly three different
integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000
can exactly one integer sided right angle triangle be formed?

"""
# Notice that we have tackled a similar problem before (Problem 9 and 39).

import math
from collections import defaultdict

def euclidean(x, y):
    
    assert x > 0, y > 0
    
    if x < y:
        x, y = y, x
    
    mod = x % y
    while mod != 0:
        x, y = y, mod
        mod = x % y
    
    return y

def search(maxinum):
    
    container = defaultdict(int)
    maxiter = int(math.sqrt(maxinum))
    for n in range(1, maxiter + 1):
        for m in range(n+1, maxiter + 1):
            mod = euclidean(m, n)
            if (mod == 1) and ((m - n) % 2 != 0): # conditions for primitive solutions
                k = 1
                while True:
                    # Use the Euclid's foluma to generate Pythagorean triplets
                    a = k * (m**2 - n**2)
                    b = 2 * m * n * k
                    c = k * (m**2 + n**2)
                    if a + b + c > maxinum:
                        break
                    else:
                        container[a+b+c] += 1
                    k += 1 # non primitive triplets?
    
    count = 0
    for Len in container:
        if container[Len]==1:
            count += 1
    
    return count


if __name__ == '__main__':
    count = search(1500000) # ~1.71s