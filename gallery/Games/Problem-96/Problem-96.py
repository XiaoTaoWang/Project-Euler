# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 21:55:26 2016

@author: Xiaotao Wang
"""

"""
Problem 96:

Su Doku (Japanese meaning number place) is the name given to a popular puzzle
concept. Its origin is unclear, but credit must be attributed to Leonhard Euler
who invented a similar, and much more difficult, puzzle idea called Latin Squares.
The objective of Su Doku puzzles, however, is to replace the blanks (or zeros)
in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of
the digits 1 to 9. Below is an example of a typical starting puzzle grid and
its solution grid.

...Omitted example...

A well constructed Su Doku puzzle has a unique solution and can be solved by
logic, although it may be necessary to employ "guess and test" methods in order
to eliminate options (there is much contested opinion over this). The complexity
of the search determines the difficulty of the puzzle; the example above is
considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt, contains fifty different Su Doku puzzles ranging
in difficulty, but all with unique solutions (the first puzzle in the file is
the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the
top left corner of each solution grid; for example, 483 is the 3-digit number
found in the top left corner of the solution grid above.

"""
import cPickle, time, copy
#------------------------------------------------------------------------------
# An implementation for Algorithm X using Python's built-in types

# To my knowledge, Algorithm X is first introduced by Donald Knuth in his paper
# "Dancing Links" to refer to "the most obvious trial-and-error approach" for
# finding all solutions to the exact cover problem. And in that well-known paper,
# Knuth proposed an efficient technique using doubly linked list for quickly
# removing and recovering 1s in the matrix representation of the exact cover
# problem. In this program, I re-implement the Algorithm X using Python's own
# types, above all, dict and set, which are also efficient for removing and
# adding elements, and more flexible compared with doubly linked list.

# Recursive function is used for backtracking naturally and concisely.
# Now ...
def exactcover(X, Y, solution = []):
    """
    Core worker for the exact cover problem solver.
    
    Parameters
    ----------
    X : dict
        Standard representation of the exact cover problem, with the key
        indicating the subset, and the value, which is stored as list, indicating
        elements contained in corresponding subset.
    Y : dict
        Inverse representation. The key indicates the element, and the vaule,
        stored as set, lists the subsets corresponding element is contained in.
    solution : list
        To find all solutions, this list is updated and yielded dynamically
        during the algorithm.
    """
    if not len(Y):
        yield sorted(solution)
    else:
        minc = None; numr = float('inf')
        for k in Y:
            if len(Y[k]) < numr:
                numr = len(Y[k])
                minc = k
        for r in Y[minc]:
            solution.append(r)
            cache = trim(X, Y, r)
            # The algorithm clones itself into subalgorithms
            for s in exactcover(X, Y, solution):
                yield s
            recover(X, Y, r, cache)
            solution.pop()

def trim(X, Y, r):
    
    cache = {} # Cache columns for recovering the last-stage problem
    for j in X[r]:
        for i in Y[j]:
            for k in X[i]:
                if k != j:
                    Y[k].remove(i) # mask rows
        cache[j] = Y.pop(j) # mask columns
    return cache

def recover(X, Y, r, cache):
    
    # To reverse the trim operation, we should add the column reversely
    # Since the rows in the last-removed column now don't cover columns
    # removed previously.
    for j in reversed(X[r]): # X remains intact
        Y[j] = cache.pop(j) # recover columns
        for i in Y[j]:
            for k in X[i]:
                if k != j:
                    Y[k].add(i) # recover rows

#------------------------------------------------------------------------------
# Translate Su Doku into the exact cover problem
# Reference: https://en.wikipedia.org/wiki/Exact_cover
standard, inverse = cPickle.load(open('constraints.db','rb'))

class sudoku(object):
    
    def __init__(self, ori, X = standard, Y = copy.deepcopy(inverse)):
        # Add additional constraints
        for i in range(len(ori)):
            for j in range(len(ori[i])):
                if ori[i][j] != '0':
                    trim(X, Y, (i,j,ori[i][j]))
        
        self.X = X
        self.Y = Y
        self.ori = ori
    
    def solve(self):
        start = time.time()
        self.solutions = set()
        X = self.X; Y = copy.deepcopy(self.Y)
        gensolution = exactcover(X, Y)
        for s in gensolution:
            self.solutions.add(tuple(s))
        self.elapse = time.time() - start
        self.solutions = list(self.solutions)
    
    def _report(self):
        
        print('Problem:\n')
        self.pretty_print(self.ori)
        print('Solved in %.4gs, found %d solution(s)\n' % (self.elapse,
              len(self.solutions)))
        if len(self.solutions):
            candi = self.solutions[0]
            solution = copy.deepcopy(self.ori)
            for r in candi:
                solution[r[0]][r[1]] = r[2]
            print('Solution view:\n')
            self.pretty_print(solution)
    
    def pretty_print(self, data):
        
        template = ['|','','','','|','','','','|','','','','|']
        mapidx = [1, 2, 3, 5, 6, 7, 9, 10, 11]
        string = '+-----------------------+\n'
        for i in range(len(data)):
            for j, idx in enumerate(mapidx):
                template[idx] = data[i][j]
            string += (' '.join(template)+'\n')
            if (i % 3 == 2) and (i != 8):
                string += '|-------+-------+-------|\n'
        string += '+-----------------------+\n'
        
        print(string)

#------------------------------------------------------------------------------
# Problem loading
def readdata(filename):
    
    problems = {}
    with open(filename) as source:
        for line in source:
            if line.startswith('G'):
                key = line.rstrip()
                problems[key] = []
            else:
                tmp = list(line.rstrip())
                if tmp:
                    problems[key].append(tmp)
    
    return problems
#------------------------------------------------------------------------------

if __name__ == '__main__':
    problems = readdata('p096_sudoku.txt')
    start = time.time()
    count = 0
    for p in problems:
        P = sudoku(problems[p], X = standard, Y = copy.deepcopy(inverse))
        P.solve()
        candi = P.solutions[0]
        solution = copy.deepcopy(P.ori)
        for r in candi:
            solution[r[0]][r[1]] = r[2]
        count += int(''.join(solution[0][:3]))
    elapse = time.time() - start
    print('Time elapse: %.4gs' % elapse) # ~1.03s
        
        