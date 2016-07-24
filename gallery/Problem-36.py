# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 12:25:41 2016

@author: Xiaotao Wang
"""

"""
Problem-36:

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)

"""
def countPalindromes(maxnum):
    
    count = 0
    for num in range(maxnum):
        strnum = str(num)
        if strnum != strnum[::-1]:
            continue
        binnum = bin(num)[2:]
        if binnum[-1] == 0:
            continue
        if binnum == binnum[::-1]:
            count += num
    
    return count

if __name__ == '__main__':
    print(countPalindromes(1000000))
