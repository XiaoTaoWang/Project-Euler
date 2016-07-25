# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 13:07:31 2016

@author: Xiaotao Wang
"""

"""
Problem 38:

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?

"""
def isPandigital(num):
    
    digits = list(map(int, num))
    digits.sort()
    
    return digits == list(range(1, len(digits)+1))
    
def largest():
    
    tmp = 0
    for i in range(9123, 9877):
        strnum = str(i) + str(i*2)
        if isPandigital(strnum):
            num = int(strnum)
            if num > tmp:
                tmp = num
    
    return tmp

if __name__ == '__main__':
    print(largest()) # ~5.47ms