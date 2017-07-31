# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 12:01:19 2017

@author: XiaoTao Wang
"""

"""
Problem 120: Square remainders

Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2.

For example, if a = 7 and n = 3, then r = 42: 6^3 + 8^3 = 728 ≡ 42 mod 49. And
as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

For 3 ≤ a ≤ 1000, find ∑ rmax.
"""
# Expand the expresion for a few values of n,
# Then we can find a pattern:
# r = 2 for any even value of n
# r = 2na for any odd value of n

# Then the problem is reduced to: determine the value of n which maximizes r
# for any a.

# For 2na = a^2, n = a/2, that is, when n = a/2, the value of r is minimized.
# Then r must be maximized when n = (a-1)/2.

def solve(maxa):
    
    Sum = 0
    for a in range(3,maxa+1):
        Sum += 2*a*((a-1)//2)
    
    return Sum

if __name__ == '__main__':
    Sum = solve(1000) # ~ 128us