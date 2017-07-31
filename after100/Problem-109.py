# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 15:50:49 2017

@author: XiaoTao Wang
"""

"""
Problem 109: Darts

In the game of darts a player throws three darts at a target board which is
split into twenty equal sized sections numbered one to twenty.

... Omitted figure ...

The score of a dart is determined by the number of the region that the dart
lands in. A dart landing outside the red/green outer ring scores zero. The black
and cream regions inside this ring represent single scores. However, the
red/green outer ring and middle ring score double and treble scores respectively.

At the centre of the board are two concentric circles called the bull region,
or bulls-eye. The outer bull is worth 25 points and the inner bull is a double,
worth 50 points.

There are many variations of rules but in the most popular game the players will
begin with a score 301 or 501 and the first player to reduce their running total
to zero is a winner. However, it is normal to play a "doubles out" system, which
means that the player must land a double (including the double bulls-eye at the
centre of the board) on their final dart to win; any other dart that would
reduce their running total to one or lower means the score for that set of three
darts is "bust".

When a player is able to finish on their current score it is called a "checkout"
and the highest checkout is 170: T20 T20 D25 (two treble 20s and double bull).

There are exactly eleven distinct ways to checkout on a score of 6:
    
... Omitted table ...

Note that D1 D2 is considered different to D2 D1 as they finish on different
doubles. However, the combination S1 T1 D1 is considered the same as T1 S1 D1.

In addition we shall not include misses in considering combinations; for example,
D3 is the same as 0 D3 and 0 0 D3.

Incredibly there are 42336 distinct ways of checking out in total.

How many distinct ways can a player checkout with a score less than 100?
"""
# Recall the problem 31 ...
from collections import defaultdict

cases = {}
code = {1:'S', 2:'D', 3:'T'}
for i in range(1,21):
    for j in range(1,4):
        key = ''.join([code[j], str(i)])
        cases[key] = i*j
cases['S25'] = 25
cases['D25'] = 50
cases['S0'] = 0

def list_ways(total):
    
    ways = set()
    pool = defaultdict(set)
    for d1 in cases:
        for d2 in cases:
            for d3 in cases:
                check = cases[d1] + cases[d2] + cases[d3]
                if check != total:
                    continue
                tmp = tuple(d for d in (d1,d2,d3) if cases[d]>0)
                if not ('D' in tmp[-1]):
                    continue
                check = tuple(sorted(tmp[:-1]))
                if not check in pool[tmp[-1]]:
                    ways.add(tmp)
                    pool[tmp[-1]].add(check)
    return ways

def work():
    count = 0
    for total in range(2, 100):
        count += len(list_ways(total))
    return count

if __name__ == '__main__':
    count = work()