# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:15:16 2016

@author: Xiaotao Wang
"""

"""
Problem 52:

It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.

"""
def checkPermutation(strnum1, strnum2):
    
    L1 = list(strnum1)
    L2 = list(strnum2)
    L1.sort()
    L2.sort()
    
    return L1 == L2

def search():
    
    start = 100
    while True:
        end = int(start * 10 / 6)
        for num in range(start, end+1):
            strnum = str(num)
            for idx in range(2, 7):
                checknum = num * idx
                checkstr = str(checknum)
                if not checkPermutation(strnum, checkstr):
                    break
            else:
                return num
        start *= 10

if __name__ == '__main__':
    print(search())