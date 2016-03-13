# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 21:19:07 2016

@author: wxt
"""

"""
Problem 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?

"""
import math

def checkprime(num):
    
    maxiter = int(math.sqrt(num))
    
    isprime = 1
    for i in xrange(2, maxiter + 1):
        if num % i == 0:
            isprime = 0
            break
    
    return isprime

def getprime(idx):
    
    count = 0
    num = 2
    while True:
        if checkprime(num):
            count += 1
            if count == idx:
                return num
        num += 1

if __name__ == '__main__':
    
    print getprime(10001)
