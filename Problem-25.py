# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 00:17:25 2016

@author: Xiaotao Wang
"""

"""
Problem 25:

What is the index of the first term in the Fibonacci sequence to contain
1000 digits?
"""

def fib():
    
    a = b = 1
    while True:
        yield a
        a, b = b, a+b

if __name__ == '__main__':
    F = fib()
    for i, num in enumerate(F):
        digits = str(num)
        if len(digits) == 1000:
            print(i+1)
            break