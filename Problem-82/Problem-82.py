# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:09:44 2016

@author: Xiaotao Wang
"""

"""
Problem 82:

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in
the left column and finishing in any cell in the right column, and only
moving up, down, and right, is indicated in red and bold; the sum is equal
to 994.

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80
by 80 matrix, from the left column to the right column.
"""
import copy

def readdata(filename):
    
    data = [list(map(int, line.rstrip().split(','))) for line in open(filename)]
    totalsum = sum(list(map(sum, data)))
    
    return data, totalsum

def dynamic(data, totalsum):
    
    paths = copy.deepcopy(data)
    mintotal = copy.deepcopy(data)
    
    for i in range(1, len(data)):
        paths[i][0] = (i, 0)
    
    for i in range(len(data)):
        for j in range(1, len(data[i])):
            tmp = totalsum
            if i == 0:
                coords = zip([i,i+1], [j-1,j])
            elif i == (len(data)-1):
                coords = zip([i,i-1], [j-1,j])
            else:
                coords = zip([i,i-1,i+1], [j-1,j,j])
            for k, t in coords:
                if mintotal[k][t] < tmp:
                    mintotal[i][j] = mintotal[k][t] + data[i][j]
                    paths[i][j] = (k, t)
                    tmp = mintotal[k][t]
    
    minimum = totalsum
    for i in range(len(data)):
        if mintotal[i][-1] < minimum:
            minimum = mintotal[i][-1]
            idx = paths[i][-1]
    '''
    path = [idx]
    while idx[1] != 0:
        idx = paths[idx[0]][idx[1]]
        path = [idx] + path
    '''
    return mintotal, paths, minimum, idx
    
if __name__ == '__main__':
    
    data, totalsum = readdata('p082_matrix.txt')
    res = dynamic(data, totalsum)