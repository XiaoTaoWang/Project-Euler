# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 19:12:44 2016

@author: wxt
"""

"""
Problem 4:

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
def bruteforce():
    
    largest = 0
    f1 = f2 = 0
    for i in xrange(100, 1000):
        for j in xrange(i, 1000):
            product = i * j
            string = str(product)
            if string == string[::-1]:
                if product > largest:
                    largest = product
                    f1 = i
                    f2 = j
                
    return largest, f1, f2

if __name__ == '__main__':
    
    res = bruteforce()
    print 'The largest palindrome is {0}, which is the product of {1} and {2}'.format(*res)
