'''
@Description: 图的表示 - 邻接列表法
@Date: 2019-12-21 22:07:09
@Author: Wong Symbol
@LastEditors  : Wong Symbol
@LastEditTime : 2019-12-21 22:35:03
'''
# -*- coding:utf-8 -*-

class AdjNode:
    def __init__(self, data):
        self.node = data
        self._next = None

class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [None] * self.size

    def add_edge(self, src, dest):
        node = AdjNode(dest)
        node._next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node._next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self): 
        for i in range(self.size): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.node), end="") 
                temp = temp._next
            print(" \n") 

graph = Graph(5)
graph.add_edge(0, 1) 
graph.add_edge(0, 4)
graph.print_graph()
