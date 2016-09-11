# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 14:37:43 2016

@author: Xiaotao Wang
"""

"""
Problem 98:

By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively,
we form a square number: 1296 = 36^2. What is remarkable is that, by using the
same digital substitutions, the anagram, RACE, also forms a square number:
9216 = 96^2. We shall call CARE (and RACE) a square anagram word pair and specify
further that leading zeroes are not permitted, neither may a different letter
have the same digital value as another letter.

Using words.txt, a 16K text file containing nearly two-thousand common English
words, find all the square anagram word pairs (a palindromic word is NOT
considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.

"""
from string import maketrans

def readwords(filename):
    
    D = {}
    with open(filename,'r') as source:
        words = source.readline().rstrip().split(',')
        for w in words:
            w = w.strip('"')
            Len = len(w)
            if Len <= 1:
                continue # a palindromic word is not considered
            if not Len in D:
                D[Len] = [w]
            else:
                D[Len].append(w)
    return D

def buildpairs(words):
    
    pairs = {}
    for key in words:
        source = words[key]
        tmp = []
        for i in xrange(len(source)-1):
            for j in xrange(i+1,len(source)):
                w1 = source[i]
                w2 = source[j]
                if sorted(w1)==sorted(w2):
                    tmp.append((w1,w2))
        if len(tmp):
            pairs[key] = tmp
    
    return pairs

def buildsquares(maxnum):
    
    sm = 4
    D = {}
    while True:
        sqs = str(sm ** 2)
        Len = len(sqs)
        if Len > maxnum:
            break
        if not Len in D:
            D[Len] = {sqs}
        else:
            D[Len].add(sqs)
        sm += 1
    return D

def match(word, square):
    
    if len(set(word)) != len(set(square)):
        return False
    tmp = {}
    for i, l in enumerate(word):
        if l in tmp:
            if tmp[l] != square[i]:
                return False
        else:
            tmp[l] = square[i]
    
    return True

def search(pairs, squares):
    
    hits = set()
    for Len in pairs:
        candis = pairs[Len]
        spaces = squares[Len]
        for w1, w2 in candis:
            for sqs in spaces:
                numsqs = int(sqs)
                if numsqs in hits:
                    continue
                check = match(w1, sqs)
                if not check:
                    continue
                table = maketrans(w1, sqs)
                trans = w2.translate(table)
                if trans in spaces:
                    hits.add(numsqs)
                    hits.add(int(trans))
    
    return max(hits)

def worker():
    
    words = readwords('p098_words.txt')
    pairs = buildpairs(words)
    squares = buildsquares(max(pairs))
    res = search(pairs, squares)
    
    return res

if __name__ == '__main__':
    res = worker() # ~531ms