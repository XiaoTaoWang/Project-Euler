# -*- coding: utf-8 -*-
"""
Created on Sun May  1 12:01:32 2016

@author: Xiaotao Wang
"""

"""
Problem 89:

For a number written in Roman numerals to be considered valid there are basic
rules which must be followed. Even though the rules allow some numbers to be
expressed in more than one way there is always a "best" way of writing a
particular number.

For example, it would appear that there are at least six ways of writing the
number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last
example is considered to be the most efficient, as it uses the least number
of numerals.

The 11K text file, contains one thousand numbers written in valid, but not
necessarily minimal, Roman numerals; see About... Roman Numerals for the
definitive rules for this problem.

Find the number of characters saved by writing each of these in their
minimal form.

Note: You can assume that all the Roman numerals in the file contain no
more than four consecutive identical units.

"""

roman_numeral_map = (('M', 1000),
                     ('CM', 900),
                     ('D', 500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L', 50),
                     ('XL', 40),
                     ('X', 10),
                     ('IX', 9),
                     ('V', 5),
                     ('IV', 4),
                     ('I', 1))

def roman_to_num(S):
    """
    *S* is a valid Roman numeral, not necessarily in the minimal form.
    """
    result = 0
    index = 0
    for numeral, unit in roman_numeral_map:
        while S[index:index+len(numeral)] == numeral:
            result += unit
            index += len(numeral)
    
    return result

def num_to_minimal_roman(integer):
    
    result = ''
    for numeral, unit in roman_numeral_map:
        while integer >= unit:
            result += numeral
            integer -= unit
    
    return result

def workcore(strings):
    
    saved = 0
    for roman in strings:
        n = roman_to_num(roman)
        diff = len(roman) - len(num_to_minimal_roman(n))
        saved += diff
    
    return saved

if __name__ == '__main__':
    
    strings = [line.rstrip() for line in open('p089_roman.txt')]
    saved = workcore(strings) # ~5.79ms