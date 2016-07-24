# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 13:28:50 2016

@author: Xiaotao Wang
"""

"""
Problem 39:

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

"""
# Recall problem 9
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

def tripletNum(condition):
    
    count = 0
    maxiter = int(math.sqrt(condition))
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
                    if a + b + c > condition:
                        break
                    if a + b + c == condition:
                        count += 1
                    k += 1 # non primitive triplets?
    
    return count

if __name__ == '__main__':
    Sum = 0
    maxnum = 0
    for i in range(12, 1001):
        count = tripletNum(i)
        if count > maxnum:
            maxnum = count
            Sum = i