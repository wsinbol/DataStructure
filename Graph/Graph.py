'''
@Description: 图的表示 - 邻接链表法
@Date: 2019-12-21 22:07:09
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-06-22 15:01:39
'''
# -*- coding:utf-8 -*-

class AdjNode:
    def __init__(self, data):
        self.node = data
        self._next = None

class GraphLinkedList:
    def __init__(self, size):
        self.size = size
        self.graph = [None] * self.size

    def add_edge(self, src, dest):
        # 总是在头部插入
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
            
class GraphList():
    def __init__(self, num_vertices):
        self._num_vertices = num_vertices
        self._adjacency = [[] for _ in range(num_vertices)]

    def add_edge(self,src,dst):
        self._adjacency[src].append(dst)
        self._adjacency[dst].append(src)
        
    def show(self):
        print(self._adjacency)
            
if __name__ == '__main__':
    '''
    graph = GraphLinkedList(5)
    graph.add_edge(0, 1) 
    graph.add_edge(0, 4)
    graph.print_graph()
    '''
    g = GraphList(8)
    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.show()
