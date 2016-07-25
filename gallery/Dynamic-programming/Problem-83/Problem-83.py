# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 18:00:08 2016

@author: Xiaotao Wang
"""

"""
Problem 83:

In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by moving left, right, up, and down, is indicated in bold red
and is equal to 2297.

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by
80 matrix, from the top left to the bottom right by moving left, right, up,
and down.

"""
# This problem can be converted into a shortest path problem in Graph Theory.
# Here is my implementation for the well-known Dijkstra's algorithm
# The code runs in O((|E|+|V|)log|V|) by using a priority queue, where |E|
# indicates the number of edges, and |V| is the number of nodes.

import heapq, itertools, math

class PriorityQueue():
    
    REMOVED = '<removed-task>'
    
    def __init__(self):
        self.hq = []
        self.entry_finder = {}
        self.counter = itertools.count()
    
    def add_with_priority(self, task, priority):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.hq, entry)
    
    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED
    
    def extract_min(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.hq:
            priority, count, task = heapq.heappop(self.hq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task, priority
        raise KeyError('pop from an empty priority queue')
        
def readdata(filename):
    
    data = [list(map(int, line.rstrip().split(','))) for line in open(filename)]
    
    return data

def convertToAdjacency(data):
    
    adjacency = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            adjacency[(i,j)] = {}
            queue = [(i-1,j), (i,j-1), (i+1,j), (i,j+1)]
            for k, t in queue:
                if (0 <= k < len(data)) and (0 <= t < len(data[0])):
                    adjacency[(i,j)][(k,t)] = {'weight':data[k][t]}
    adjacency[(-1,-1)] = {(0,0):{'weight':data[0][0]}}
    
    return adjacency

def my_Dijkstra(data, source, target):
    
    dist = {}
    prev = {}
    Q = PriorityQueue()
    Q.add_with_priority(source, 0)
    
    adjacency = convertToAdjacency(data)
    
    while len(Q.hq):
        u, dist_u = Q.extract_min()
        dist[u] = dist_u
        if u == target:
            break
        
        for v in adjacency[u]:
            if not v in dist:
                dist[v] = float('inf')
            alt = dist[u] + adjacency[u][v]['weight']
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                Q.add_with_priority(v, alt)
    
    Path = []
    end = target
    while True:
        Path.append(end)
        if end == source:
            break
        end = prev[end]
        
    Path.reverse()
    
    return dist[target], path
    

if __name__ == '__main__':
    
    data = readdata('p083_matrix.txt')
    length, path = my_Dijkstra(data, (-1,-1), (79, 79)) # ~60ms
