# -*- coding: utf-8 -*-
"""
Created on Sun May  1 12:43:41 2016

@author: Xiaotao Wang
"""

"""
Problem 65:

The square root of 2 can be written as an infinite continued fraction.

The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates
that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for
square roots provide the best rational approximations. Let us consider the
convergents for √2.

Hence the sequence of the first ten convergents for √2 are:
1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:
2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.
"""

# There's a recursive formula about the numerator
# n(k) = c(k) * n(k-1) + n(k-2)

def Gen(num):
    
    yield 2
    
    idx = 1
    while True:
        idx += 1
        if idx % 3 == 0:
            k = idx // 3
            yield k * 2
        else:
            yield 1
        if idx == num:
            break


def num_of_digits(n = 100):
    
    n1 = 2
    n2 = 3
    
    g = Gen(n)
    for idx, c in enumerate(g):
        if idx >= 2:
            tmp = c * n2 + n1
            n1 = n2
            n2 = tmp
    
    return sum(map(int, str(n2)))

if __name__ == '__main__':
    res = num_of_digits()
    
    
