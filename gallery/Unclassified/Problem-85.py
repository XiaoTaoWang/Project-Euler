# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 22:15:25 2016

@author: Xiaotao Wang
"""

"""
Problem 85:

By counting carefully it can be seen that a rectangular grid measuring 3 by
2 contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two million
rectangles, find the area of the grid with the nearest solution.
"""

def find_solution(X, Y, obj = 2000000):
    
    dis = obj
    solution = [0, 0]
    for i in range(1, X+1):
        for j in range(i, Y+1):
            tmpnum = i * j * (i + 1) * (j + 1) / 4
            assert tmpnum == int(tmpnum)
            tmpdis = abs(tmpnum - obj)
            if tmpdis < dis:
                dis = tmpdis
                solution = [i, j]
    
    return solution, dis

if __name__ == '__main__':
    res = find_solution(2000, 2000) # ~1.71s