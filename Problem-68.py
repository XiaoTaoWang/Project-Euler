# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 20:07:08 2016

@author: Xiaotao Wang
"""

"""
Problem 68: Magic 5-gon ring

https://projecteuler.net/problem=68

"""

import itertools

class FiveGonRing(object):
    
    def __init__(self, inner = [1,2,3,4,5], outer = [6,7,8,9,10]):
        # Intuitively, I set the inner ring to 1,2,3,4,5, and the outer ring
        # to 6,7,8,9,10
        totalsum = sum(inner) * 2 + sum(outer)
        assert totalsum % 5 == 0, 'No solution exists under given settings'
        
        outer.sort()
        self.inner = inner
        self.outer = outer
        self.linesum = totalsum // 5
        self._validSolution()
    
    def _validSolution(self):
        
        self.solutions = []
        for o in itertools.permutations(self.outer[1:]):
            outer = (self.outer[0],) + o
            for inner in itertools.permutations(self.inner):
                cur = []
                for idx in range(len(outer)):
                    tmp = [outer[idx], inner[idx], inner[(idx+1)%5]]
                    check = sum(tmp)==self.linesum
                    if check:
                        cur.append(tmp)
                if len(cur) == 5:
                    self.solutions.append(cur)
    
    def getBest(self):
        
        best = 0
        bestsolution = []
        for s in self.solutions:
            string = ''
            for line in s:
                string += ''.join(map(str, line))
            num = int(string)
            if num > best:
                best = num
                bestsolution = s
        
        return best, bestsolution

if __name__ == '__main__':
    
    fivegon = FiveGonRing() # ~8.03ms
    answer = fivegon.getBest()
                    