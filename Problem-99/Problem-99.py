# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 21:57:35 2016

@author: Xiaotao Wang
"""

"""
Problem 99:


Comparing two numbers written in index form like 2^11 and 3^7 is not
difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more
difficult, as both numbers contain over three million digits.

Using base_exp.txt, a 22K text file containing one thousand lines with a
base/exponent pair on each line, determine which line number has the greatest
numerical value.

NOTE: The first two lines in the file represent the numbers in the example
given above.

"""
import numpy as np

def find_largest(filename):
    
    lognum = []
    cache = []
    with open(filename, 'r') as F:
        for line in F:
            parse = line.rstrip().split(',')
            lognum.append(int(parse[1]) * np.log(int(parse[0])))
            cache.append(line)
    
    lognum = np.r_[lognum]
    maxidx = lognum.argmax()
    
    return maxidx, cache[maxidx]

if __name__ == '__main__':
    res = find_largest('p099_base_exp.txt')