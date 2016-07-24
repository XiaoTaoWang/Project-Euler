# -*- coding: utf-8 -*-
"""
Created on Mon May 30 12:43:10 2016

@author: Xiaotao Wang
"""

"""
Problem 80:

It is well known that if the square root of a natural number is not an integer,
then it is irrational. The decimal expansion of such square roots is infinite
without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of
the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums
of the first one hundred decimal digits for all the irrational square roots.

"""
import decimal

def working(maxnum=100):
    sums = []
    for i in range(1, maxnum+1):
        rootint = int(i ** 0.5)
        if rootint ** 2 != i:
            with decimal.localcontext() as c:
                c.prec = 102
                rootstr = str(decimal.Decimal(i) ** decimal.Decimal('0.5'))
                rootstr = rootstr.replace('.', '')
                tmpsum = 0
                for j in range(100):
                    tmpsum += int(rootstr[j])
                sums.append(tmpsum)
    
    return sum(sums)

if __name__ == '__main__':
    res = working() # ~43.9ms