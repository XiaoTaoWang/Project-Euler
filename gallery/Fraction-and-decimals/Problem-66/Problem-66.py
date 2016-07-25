# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 16:09:02 2016

@author: Xiaotao Wang
"""

"""
Problem 66: Diophantine equation

Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is
square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is
obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest
value of x is obtained.

"""
# The nature of this problem is to find the fundamental solution of Pell's equation
# For nonsquare D, sqrt(D) is irrational, so when x/y approximately equals sqrt(D),
# x^2/y^2 approximately equals D，and solutions of x^2 – Dy^2 = 1 give the best
# rational approximations to sqrt(n).

# That links the solutions to continued fractions, which we have tackled in
# Problem 64.
import math

def gen_contiued_fraction(S):
    """
    A generator version.
    """
    a0 = int(math.sqrt(S))
    a = a0
    m = 0
    d = 1
    
    while True:
        m = d * a - m
        d = (S - m**2) // d
        a = int((a0 + m) / d)
        yield a

def solve(maxnum):
    
    maxx = 9
    maxidx = 5
    for D in xrange(maxidx+1, maxnum+1):
        a0 = int(math.sqrt(D))
        if a0**2 != D:
            n0 = 1
            d0 = 0
            n = a0
            d = 1
            cf = gen_contiued_fraction(D)
            while n**2 - D*d**2 != 1:
                a = cf.next()
                tmpn = n
                tmpd = d
                n = a*n + n0 # numerator: n(i) = a(i)*n(i-1) + n(i-2)
                d = a*d + d0 # denominator: d(i) = a(i)*d(i-1) + d(i-2)
                n0 = tmpn
                d0 = tmpd
            if n > maxx:
                maxx = n
                maxidx = D
    
    return maxidx, maxx

if __name__ == '__main__':
    res = solve(1000) # ~22.8ms