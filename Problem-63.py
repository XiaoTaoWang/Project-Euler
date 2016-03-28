# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 19:36:34 2016

@author: wxt
"""

"""
Problem 63:

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

"""
import math

def search():
    
    upperbound = 10
    n = 1
    lowerbound = math.ceil(pow(10, (n-1.)/n))
    
    count = 0
    while lowerbound < upperbound:
        count += (upperbound - lowerbound)
        n += 1
        lowerbound = math.ceil(pow(10, (n-1.)/n))
    
    return count

if __name__ == '__main__':
    print search()