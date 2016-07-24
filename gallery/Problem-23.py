# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 20:43:15 2016

@author: wxt
"""

"""
Problem 23:

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

"""
import numpy as np

def sumfactors(num):
    
    result = 1
    maxiter = int(np.sqrt(num))
    if maxiter ** 2 == num:
        result += maxiter
        maxiter -= 1
        
    for i in xrange(2, maxiter+1):
        if num % i == 0:
            result += (i + num / i)
    
    return result

def findabundant(minnum = 12, maxnum = 28123):
    
    abundant = []
    for num in xrange(minnum, maxnum):
        sumfac = sumfactors(num)
        if sumfac > num:
            abundant.append(num)
    
    return abundant

if __name__ == '__main__':
    
    mask = np.ones(28123, bool)
    abundant = findabundant()
    for i in xrange(len(abundant)):
        for j in xrange(i, len(abundant)):
            multi = abundant[i] + abundant[j]
            if multi <= mask.size:
                mask[multi-1] = 0
    
    total = np.arange(1, 28124)
    
    print total[mask].sum()