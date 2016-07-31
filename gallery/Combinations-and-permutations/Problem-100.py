# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 15:31:17 2016

@author: Xiaotao Wang
"""

"""
Problem 100:

If a box contains twenty-one coloured discs, composed of fifteen blue discs and
six red discs, and two discs were taken at random, it can be seen that the
probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two
blue discs at random, is a box containing eighty-five blue discs and thirty-five
red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs
in total, determine the number of blue discs that the box would contain.

"""
# Simple analysis
# denote blue disc number as b, total disc number as n
# we have:
# (b / n) * ((b - 1) / (n - 1)) = 1 / 2
# so n^2 - 2b^2 - n + 2b = 0
# since n and b must be integer, this is a quadratic Diophantine Equation

# Referennce site:
# https://www.alpertron.com.ar/QUAD.HTM

# From the reference site, we have the recursive fomulas below:
# n(k+1) = 3 * n(k) + 4 * b(k) - 3
# b(k+1) = 2 * n(k) + 3 * b(k) - 2

def find(target):
    
    n, b = 21, 15
    while n < target:
        nextn = 3 * n + 4 * b - 3
        nextb = 2 * n + 3 * b - 2
        n, b = nextn, nextb
    
    return n, b

if __name__ == '__main__':
    n, b = find(10**12)