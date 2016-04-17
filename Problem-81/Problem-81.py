# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:06:02 2016

@author: Xiaotao Wang
"""

"""
Problem 81:

In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is indicated in bold
red and is equal to 2427.

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80
by 80 matrix, from the top left to the bottom right by only moving right and
down.

"""
import copy

def readdata(filename):
    
    data = [list(map(int, line.rstrip().split(','))) for line in open(filename)]
    totalsum = sum(list(map(sum, data)))
    
    return data, totalsum

def dynamic(data, totalsum):
    
    paths = copy.deepcopy(data)
    mintotal = copy.deepcopy(data)
    
    paths[0][0] = (0, 0)
    for i in range(1, len(data)):
        mintotal[i][0] = mintotal[i-1][0] + data[i][0]
        paths[i][0] = (i-1, 0)
    for i in range(1, len(data[0])):
        mintotal[0][i] = mintotal[0][i-1] + data[0][i]
        paths[0][i] = (0, i-1)
    
    for i in range(1, len(data)):
        for j in range(1, len(data[i])):
            tmp = totalsum
            for k, t in zip([i-1,i], [j,j-1]):
                if mintotal[k][t] < tmp:
                    mintotal[i][j] = mintotal[k][t] + data[i][j]
                    paths[i][j] = (k, t)
                    tmp = mintotal[k][t]
    
    minimum = mintotal[-1][-1]
    idx = paths[-1][-1]
    
    path = [idx]
    while idx != (0, 0):
        idx = paths[idx[0]][idx[1]]
        path = [idx] + path
    
    return minimum, path

if __name__ == '__main__':
    
    data, totalsum = readdata('p081_matrix.txt')
    minimum, path = dynamic(data, totalsum)
