# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 20:30:55 2016

@author: Xiaotao Wang
"""

import cPickle

def reverseRep(X):
    Y = {}
    for sub in X:
        for e in X[sub]:
            if e in Y:
                Y[e].add(sub)
            else:
                Y[e] = {sub}
    return Y

# Generate and serialize general Su Doku constraints
X = {} # Standard representation of the exact cover problem
for i in range(9):# row number
    for j in range(9): # column number
        for n in range(1, 10): # 1-9
            t = (i, j, str(n)) # possibilities
            rc = (i, j, None) # Row-Column constraint
            rn = (i, None, str(n)) # Row-Number constraint
            cn = (None, j, str(n)) # Column-Number constraint
            bn = (i//3, j//3, str(n)) # Box-Number constraint
            X[t] = [rc, rn, cn, bn]

Y = reverseRep(X)

cPickle.dump((X,Y), open('constraints.db','wb'), protocol = 2)
