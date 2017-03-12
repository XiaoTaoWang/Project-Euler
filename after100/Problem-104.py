# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 12:12:36 2017

@author: XiaoTao Wang
"""

"""
Problem 104:

The Fibonacci sequence is defined by the recurrence relation:

    F(n) = F(n−1) + F(n−2), where F(1) = 1 and F(2) = 1.

It turns out that F(541), which contains 113 digits, is the first Fibonacci
number for which the last nine digits are 1-9 pandigital (contain all the digits
1 to 9, but not necessarily in order). And F(2749), which contains 575 digits,
is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that F(k) is the first Fibonacci number for which the first nine digits
AND the last nine digits are 1-9 pandigital, find k.

"""
# Brute force

import math

def isPandigital(num):
    
    digits = map(int, str(num))
    digits.sort()
    
    return digits == range(1, len(digits)+1)

def lastnine(N):
    
    return N % pow(10,9)

def firstnine(N):
    
    exp_n = int(math.log10(N)) - 8
    return N // pow(10,exp_n)

def fib():
    
    a = b = 1
    while True:
        yield a
        a, b = b, a+b

def work():
    
    F = fib()
    hit_i = 1
    for i, num in enumerate(F):
        if i < 2749:
            continue
        tail = lastnine(num)
        if not isPandigital(tail):
            continue
        head = firstnine(num)
        if isPandigital(head):
            hit_i = i+1
            break
    return hit_i

if __name__ == '__main__':
    
    k = work() # ~22.9s
