# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:04:41 2016

@author: Xiaotao Wang
"""

"""
Problem 56:

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum?

"""

def maxDigitSum(maxa = 100, maxb = 100):
    
    maxsum = 0
    for a in range(2, 100):
        if a % 10 == 0:
            continue
        for b in range(2, 100):
            res = a ** b
            Sum = sum(map(int, str(res)))
            if Sum > maxsum:
                maxsum = Sum
    
    return maxsum

if __name__ == '__main__':
    print(maxDigitSum()) # ~383ms