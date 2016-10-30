# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 13:00:44 2016

@author: Xiaotao Wang
"""

"""
Problem 90:

Each of the six faces on a cube has a different digit (0 to 9) written on it;
the same is done to a second cube. By placing the two cubes side-by-side in
different positions we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:

...Omitted image...

In fact, by carefully choosing the digits on both cubes it is possible to display
all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and
81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on
one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so
that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for
all nine square numbers to be displayed; otherwise it would be impossible to
obtain 09.

In determining a distinct arrangement we are interested in the digits on each
cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in
the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the
purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square
numbers to be displayed?
"""

import itertools

def validpair(seq1, seq2):
    ref = {(0,1):0, (0,4):0, (0,9):0, (1,6):0, (2,5):0,
           (3,6):0, (4,9):0, (6,4):0, (8,1):0}
    if 6 in seq1:
        seq1 += (9,)
    if 9 in seq1:
        seq1 += (6,)
    if 6 in seq2:
        seq2 += (9,)
    if 9 in seq2:
        seq2 += (6,)
    
    for s1 in seq1:
        for s2 in seq2:
            r1 = ref.get((s1,s2))
            if r1==0:
                ref[(s1,s2)] = 1
            r2 = ref.get((s2,s1))
            if r2==0:
                ref[(s2,s1)] = 1
    count = sum(ref.values())
    
    return count==len(ref)

def worker():
    pool = list(itertools.combinations(range(10),6))
    count = 0
    for i in range(len(pool)-1):
        for j in range(i+1,len(pool)):
            seq1 = pool[i]
            seq2 = pool[j]
            check = validpair(seq1, seq2)
            if check:
                count += 1
    return count

if __name__ == '__main__':
    count = worker()