# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 12:43:58 2017

@author: XiaoTao Wang
"""

"""
Problem 107:

Remove redundant edges from original network whilst ensuring that the network
remains connected.

https://projecteuler.net/problem=107
"""
# The problem is somewhat a basic problem in Graph Theory called finding the
# minimum spanning tree
import networkx as nx

def dataToGraph(fil):
    
    edges = []
    i = 0
    with open(fil, 'r') as source:
        for line in source:
            parse = line.rstrip().split(',')
            for j, w in enumerate(parse):
                if w != '-':
                    edges.append((i, j, int(w)))
            i += 1
    
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    
    return G

def work(fil):
    
    G = dataToGraph(fil)
    ori = sum([G.get_edge_data(i,j)['weight'] for i,j in G.edges_iter()])
    MST = nx.minimum_spanning_tree(G)
    new = sum([G.get_edge_data(i,j)['weight'] for i,j in MST.edges_iter()])
    saved = ori - new
    
    return saved

if __name__ == '__main__':
    saved = work('p107_network.txt') # ~4.72ms
    
            