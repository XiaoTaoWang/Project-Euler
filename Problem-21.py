# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 00:11:01 2016

@author: Xiaotao Wang
"""

"""
Problem 21:



Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""
import math
# Brute forcing
def sumfactors(num):
    
    result = 1
    maxiter = int(math.sqrt(num))
    if maxiter ** 2 == num:
        result += maxiter
        maxiter -= 1
        
    for i in range(2, maxiter+1):
        if num % i == 0:
            result += (i + num / i)
    
    return result

def brutefind(maxnum):
    
    pairs = []
    storage = set()
    for num in range(2, maxnum+1):
        if num in storage:
            continue
        sf = sumfactors(num)
        if num < sf <= maxnum:
            check = sumfactors(sf)
            if check == num:
                pairs.append((num, sf))
                storage.add(sf)
    
    return sum(map(sum, pairs))

if __name__ == '__main__':
    print(brutefind(10000))