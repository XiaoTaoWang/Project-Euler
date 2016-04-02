# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 19:05:53 2016

@author: wxt
"""

"""
Problem 79:

A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278, they
may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file
so as to determine the shortest possible secret passcode of unknown length.

"""
# This problem could be solved by topological sorting
# Successful login attemts tell the dependencies between digits 

def toposort(dependencies):
    
    if len(dependencies)==0:
        return
    
    dependencies = dependencies.copy()
    
    for k, v in dependencies.items():
        v.discard(k) # Remove self dependencies
    
    # root nodes (they have no incoming edges)
    roots = reduce(set.union, dependencies.values()) - set(dependencies.keys())
    
    for r in roots:
        dependencies[r] = set()
    
    while True:
        cur = set(key for key, value in dependencies.items() if len(value)==0)
        if len(cur)==0:
            break
        
        yield cur
        
        dependencies = {key:value-cur for key, value in dependencies.items()
                        if not key in cur}
    
    if len(dependencies) != 0:
        # DAG -- Directed Acylic Graph
        raise ValueError('The input dependencies is not a DAG, cycles occurs among: {}'.format(
                         ', '.join(repr(x) for x in dependencies.items())))

def graph_from_login(login_file):
    
    data = set([login.rstrip() for login in open(login_file)])
    
    graph = {}
    for d in data:
        for i in range(1, len(d)):
            if not d[i] in graph:
                graph[d[i]] = set()
            graph[d[i]].update(d[i-1])
    
    return graph

if __name__ == '__main__':
    graph = graph_from_login('p079_keylog.txt')
    passcode = toposort(graph)