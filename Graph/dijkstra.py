# -*- coding:utf-8 -*-

'''
简易dijkstra
'''

import numpy as np

mat = np.array([
    [0,3,2,0,0,0],
    [3,0,0,1,0,0],
    [2,0,0,0,0,0],
    [0,1,0,0,4,0],
    [0,0,0,4,0,3],
    [0,0,0,0,3,0]
])

aptSet = set()
dist = [float('inf')] * len(mat)
inf = float('inf')
aptSet.add(0)
# dist[0] = 0
dist[0] = 0
dist = [0, 3, 2, inf, inf, inf]                                                                                                 

def updateDist(index):
    new = dist[index]

    if index not in aptSet:
        aptSet.add(index)
    for i in range(len(mat)):
        if mat[index][i] > 0 and i not in aptSet:
            dist[i] = mat[index][i] + new


# updateDist(0)
# print(dist)
# print(aptSet)

# updateDist 的参数是下标
updateDist(2)
print(dist)
print(aptSet)

updateDist(1)
print(dist)
print(aptSet)

updateDist(3)
print(dist)
print(aptSet)

updateDist(4)
print(dist)
print(aptSet)