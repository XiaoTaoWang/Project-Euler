# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:26:54 2016

@author: Xiaotao Wang
"""

"""
Problem 42:

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t(10). If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?

"""
import string, math

def readdata(filename):
    
    with open(filename, 'r') as F:
        parse = F.readline().rstrip().split(',')
        data = [mem[1:-1] for mem in parse]
    
    return data

def triangleWord(data):
    
    letters = string.ascii_uppercase
    D = dict(zip(letters, range(1, len(letters)+1)))
    
    count = 0
    for word in data:
        value = 0
        for w in word:
            value += D[w]
        check = (math.sqrt(8*value + 1) - 1) / 2.
        if check == int(check):
            count += 1
    
    return count

if __name__ == '__main__':
    data = readdata('p042_words.txt')
    print(triangleWord(data))
    