# -*- coding: utf-8 -*-
"""
Created on Sun May  1 13:32:05 2016

@author: Xiaotao Wang
"""

"""
Problem 64:

https://projecteuler.net/problem=64

"""
# Refer to wiki, there's a iterative algorithm for continued fraction
# expansions
import math

def gen_contiued_fraction(S):
    
    m0 = 0
    d0 = 1
    a0 = int(math.sqrt(S))
    
    if a0 ** 2 == S:
        return [[a0]]
    
    expansion = [[a0]]
    a = a0
    m = m0
    d = d0
    
    while a != 2*a0:
        m = d * a - m
        d = (S - m**2) // d
        a = int((a0 + m) / d)
        expansion.append(a)
    
    return expansion

def workcore(maxn = 10000):
    
    count = 0
    for i in range(1, maxn+1):
        exp = gen_contiued_fraction(i)
        if len(exp) > 1:
            period = len(exp[1:])
            if period % 2 == 1:
                count += 1
    
    return count

if __name__ == '__main__':
    count = workcore()