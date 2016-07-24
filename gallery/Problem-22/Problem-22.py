# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 20:24:16 2016

@author: wxt
"""

"""
Problem 22:

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""
import string

def readdata(filename):
    
    with open(filename, 'r') as F:
        parse = F.readline().rstrip().split(',')
        data = [mem[1:-1] for mem in parse]
    
    return data

def namescore(data):
    
    data.sort()
    
    letters = string.ascii_uppercase
    D = dict(zip(letters, range(1, len(letters)+1)))
    total = 0
    
    for i, name in enumerate(data):
        cur = (i + 1) * sum([D[j] for j in name])
        total += cur
    
    return total

if __name__ == '__main__':
    
    data = readdata('p022_names.txt')
    print namescore(data)
    