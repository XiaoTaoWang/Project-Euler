# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 23:42:42 2016

@author: Xiaotao Wang
"""

"""
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
import numpy as np

def solveMatrix(row, col):
    
    matrix = np.zeros((row+1, col+1), dtype = np.int64)
    matrix[:,0] = 1
    for i in range(1, col+1):
        for j in range(row+1):
            matrix[j, i] = matrix[:j+1, i-1].sum()
    
    return matrix[-1, -1]

if __name__ == '__main__':
    print(solveMatrix(20, 20))