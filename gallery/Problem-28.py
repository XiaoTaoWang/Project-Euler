# -*- coding: utf-8 -*-
"""
Created on Tue Mar 08 10:38:57 2016

@author: wxt
"""

"""
Problem 28:

Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?

"""
# Try to find the underlying rules and you will get the iterative formula:
# f(0) = 1 and f(n) = f(n-1) + 4*(2*n+1)^2 - 12*n
# So all we need is to calculate f(500) iteratively.

def spiral():
    
    ini = 1
    n = 0
    while True:
        if n == 0:
            yield ini
        else:
            cur = ini + 4*(2*n+1)**2 - 12*n
            yield cur
            ini = cur
        n += 1

if __name__ == '__main__':
    
    sumdiag = spiral()
    for count, s in enumerate(sumdiag):
        if count == 500:
            print s
            break