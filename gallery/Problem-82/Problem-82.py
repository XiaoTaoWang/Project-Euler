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
# Given a n*n matirx, the complexity of this algorithm is O(n^3)
import copy
import numpy as np

def readdata(filename):
    
    data = [list(map(int, line.rstrip().split(','))) for line in open(filename)]
    
    return data

def dynamic(data):
    
    paths = copy.deepcopy(data)
    mintotal = np.r_[data]
    
    for i in range(1, len(data)):
        paths[i][0] = (i, 0)
    
    for stage in range(1, len(data[0])):
        tmpsum = []
        for i in range(len(data)):
            orisum = mintotal[i, stage-1] + mintotal[i, stage]
            p = (i, stage-1)
            for j in range(0, i):
                cursum = mintotal[j, stage-1] + mintotal[j:i+1, stage].sum()
                if cursum < orisum:
                    orisum = cursum
                    p = (i-1, stage)
            
            for j in range(i+1, len(data)):
                cursum = mintotal[j, stage-1] + mintotal[i:j+1, stage].sum()
                if cursum < orisum:
                    orisum = cursum
                    p = (i+1, stage)
                    
            tmpsum.append(orisum)
            paths[i][stage] = p
        
        mintotal[:,stage] = tmpsum
    
    minidx = mintotal[:,-1].argmin()
    minimum = mintotal[minidx, -1]
    
    pos = paths[minidx][-1]
    path = [pos]
    while pos[1] != 0:
        pos = paths[pos[0]][pos[1]]
        path = [pos] + path
    
    return minimum, path
    
if __name__ == '__main__':
    
    data = readdata('p082_matrix.txt')
    res = dynamic(data) # ~1.26s