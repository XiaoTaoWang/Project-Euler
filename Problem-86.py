# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 08:45:07 2016

@author: Xiaotao Wang
"""

"""
Problem 86:

A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a
fly, F, sits in the opposite corner. By travelling on the surfaces of the room
the shortest "straight line" distance from S to F is 10 and the path is shown
on the diagram.

...Omitted diagram...

However, there are up to three "shortest" path candidates for any given cuboid
and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations,
with integer dimensions, up to a maximum size of M by M by M, for which the
shortest route has integer length when M = 100. This is the least value of M
for which the number of solutions first exceeds two thousand; the number of
solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one
million.
"""
# It can be proved for cuboid with x<=y<=z, s = sqrt(z^2+(x+y)^2) is the
# shortest route. So it's quite straightforward if you have a way to generate
# all Pythagorean triplets.
# Recall problem 9, 39 and 75
import math

def euclidean(x, y):
    
    assert x > 0, y > 0
    
    if x < y:
        x, y = y, x
    
    mod = x % y
    while mod != 0:
        x, y = y, mod
        mod = x % y
    
    return y

def integerSolution(M):
    
    maxperi = (3+math.sqrt(5))*M
    maxiter = int(math.sqrt(maxperi))
    count = 0
    for n in xrange(1, maxiter + 1):
        for m in xrange(n+1, maxiter + 1):
            mod = euclidean(m, n)
            # conditions for primitive solutions
            if (mod == 1) and ((m - n) % 2 != 0):
                k = 1
                while True:
                    # Use the Euclid's foluma to generate Pythagorean triplets
                    a = k * (m**2 - n**2)
                    b = 2 * m * n * k
                    if min(a, b) > M:
                        break
                    tmpcount = 0
                    if a <= M:
                        for i in xrange(b//2, 0, -1):
                            if a >= b-i:
                                tmpcount += 1
                            else:
                                break
                    if b <= M:
                        for i in xrange(a//2, 0, -1):
                            if b >= a-i:
                                tmpcount += 1
                            else:
                                break
                    count += tmpcount
                    k += 1 # non primitive triplets?
    
    return count

def binarysearch(minM, maxM, target = 1e6):
    
    while maxM-minM > 1:
        tmpM = (minM + maxM) // 2
        count = integerSolution(tmpM)
        if count > target:
            maxM = tmpM
        else:
            minM = tmpM
    
    return maxM

if __name__ == '__main__':
    M = binarysearch(100, 2000) # ~680ms