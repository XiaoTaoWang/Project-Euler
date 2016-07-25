# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 20:02:04 2016

@author: wxt
"""

"""
Problem 92:

A number chain is created by continuously adding the square of the digits in a
number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1
or 89.

How many starting numbers below ten million will arrive at 89?

"""
def splitnum(n):
    
    digits = [int(i) for i in str(n) if i!='0']
    digits.sort()
    
    return tuple(digits)

def sumsuqare(digits):
    
    return sum(d**2 for d in digits)

def count(maxnum = 10000000):
    
    cache = {}
    stat = 0
    for n in xrange(1, maxnum+1):
        Next = splitnum(n)
        tmp = [Next]
        while True:
            if Next in cache:
                for d in tmp:
                    cache[d] = cache[Next]
                    
                if cache[Next] == 89:
                    stat += 1
                break
        
            check = sumsuqare(Next)
            if (check == 89) or (check == 1):
                for d in tmp:
                    cache[d] = check
                if check == 89:
                    stat += 1
                break
            
            Next = splitnum(check)
            tmp.append(Next)
    
    return stat, cache

if __name__ == '__main__':
    res = count(10000000) # ~56.9s
                
            