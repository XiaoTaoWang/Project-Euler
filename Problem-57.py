# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:11:37 2016

@author: Xiaotao Wang
"""

"""
Problem 57:

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?

"""

def count(maxexp = 1000):
    
    n = 3 # numerator
    d = 2 # denominator
    num = 0
    for c in range(maxexp):
        if len(str(n)) > len(str(d)):
            num += 1
        n = n + 2 * d
        d = n - d
    
    return num

if __name__ == '__main__':
    print(count())