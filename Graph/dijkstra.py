'''
@Description: dijkstra最短路径demo
@Date: 2019-12-21 20:31:12
@Author: Wong Symbol
@LastEditors  : Wong Symbol
@LastEditTime : 2019-12-21 21:09:11
'''
# -*- coding:utf-8 -*-

import numpy as np

mat = np.array([
    [0,3,2,0,0,0],
    [3,0,0,1,0,0],
    [2,0,0,0,0,0],
    [0,1,0,0,4,0],
    [0,0,0,4,0,3],
    [0,0,0,0,3,0]
])

# 记录已经访问过的节点下标
aptSet = set()
# 记录开始节点到其他节点的最短距离，列表下标与节点下标同
dist = [float('inf')] * len(mat)
print('start:')
print(dist)
print(aptSet)

inf = float('inf')
# 定义节点0为初始节点
aptSet.add(0)

dist = [0, 3, 2, inf, inf, inf]                                                                                                 

def updateDist(index):
    new = dist[index]

    if index not in aptSet:
        aptSet.add(index)
    for i in range(len(mat)):
        if mat[index][i] > 0 and i not in aptSet:
            dist[i] = mat[index][i] + new

while len(aptSet) < len(mat):
    min_value = float('inf')
    min_index = None

    for i in dist:
        if i < min_value and dist.index(i) not in aptSet:
            min_index = dist.index(i)
            min_value = i
    updateDist(min_index)
    
print('end:')
print(dist)
print(aptSet)    

'''
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
'''