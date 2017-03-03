# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 12:53:48 2017

@author: Xiaotao Wang
"""

"""
Three distinct points are plotted at random on a Cartesian plane, for which
-1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ
does not.

Using p102_triangles.txt, a 27K text file containing the coordinates of one
thousand "random" triangles, find the number of triangles for which the interior
contains the origin.

NOTE: The first two examples in the file represent the triangles in the example
given above.

"""
# https://en.wikipedia.org/wiki/Triangle#Using_coordinates
# Given coordinates of three vertices of the triangle (A,B,C), it's easy to
# calculate its area: Area(ABC) = |(x(A)-x(C))(y(B)-y(A))-(x(A)-x(B))(y(c)-y(A))|/2
# Intuitively, if ABC contains O, the area of ABC must be equal to the sum
# of the area of ABO, AOC and BOC

def readdata(fil):
    
    triangles = []
    with open(fil, 'r') as source:
        for line in source:
            parse = line.rstrip().split(',')
            cur = []
            for i in range(0,6,2):
                cur.append((int(parse[i]),int(parse[i+1])))
            triangles.append(cur)
    
    return triangles

def area(A, B, C):
    
    S = 0.5 * abs((A[0]-C[0])*(B[1]-A[1]) - (A[0]-B[0])*(C[1]-A[1]))
    
    return S

def work(fil):
    
    triangles = readdata(fil)
    count = 0
    for A, B, C in triangles:
        total = area(A,B,C)
        part1 = area(A,B,(0,0))
        part2 = area(A,C,(0,0))
        part3 = area(B,C,(0,0))
        if (part1>0) and (part2>0) and (part3>0) and (part1+part2+part3==total):
            count += 1
    
    return count

if __name__ == '__main__':
    count = work('p102_triangles.txt') # ~5.56ms
            