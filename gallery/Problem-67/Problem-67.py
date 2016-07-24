# -*- coding: utf-8 -*-
"""
Created on Sat Mar 05 21:05:55 2016

@author: wxt
"""

"""
Problem 18 and 67:

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Write a general program to do this job.
"""
import copy

def readdata(filename):
    
    data = [map(int, line.rstrip().split()) for line in open(filename)]
    
    return data

def dynamic(data):
    
    paths = copy.deepcopy(data)
    maxtotal = copy.deepcopy(data)
    
    paths[0][0] = 0
    for i in xrange(1, len(data)):
        maxtotal[i][0] = maxtotal[i-1][0] + data[i][0]
        paths[i][0] = 0
        for j in xrange(1, len(data[i])-1):
            tmp = 0
            for k in xrange(j-1, j+1):
                if maxtotal[i-1][k] > tmp:
                    maxtotal[i][j] = maxtotal[i-1][k] + data[i][j]
                    paths[i][j] = k
                    tmp = maxtotal[i-1][k]
                    
        maxtotal[i][-1] = maxtotal[i-1][len(data[i])-2] + data[i][-1]
        paths[i][-1] = len(data[i]) - 2
    
    maximum = 0
    idx = 0
    for i in xrange(len(maxtotal[-1])):
        if maxtotal[-1][i] > maximum:
            maximum = maxtotal[-1][i]
            idx = i
    
    path = [idx]
    for i in range(1, len(paths))[::-1]:
        path = [paths[i][path[0]]] + path
    
    return maximum, path

if __name__ == '__main__':
    #data = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    data = readdata('p067_triangle.txt')
    res = dynamic(data)
    
        
        
