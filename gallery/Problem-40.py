# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 13:45:28 2016

@author: Xiaotao Wang
"""

"""
Problem 40:

An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of
the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

"""
def solve(pos):
    
    i = 1
    maxdigit = max(pos)
    strnum = ''
    while True:
        strnum += str(i)
        if len(strnum) > maxdigit:
            break
        i += 1
    
    prod = 1
    for p in pos:
        prod *= int(strnum[p-1])
    
    return prod

if __name__ == '__main__':
    print(solve([1,10,100,1000,10000,100000,1000000]))
