'''
@Description: 广度优先搜索 Breadth First Search
@Date: 2020-05-30 17:09:50
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-05-31 11:40:59
'''

'''
BFS 问题的本质就是在 图 中找到从 起点start 到 终点end 的最短路径
按层遍历也是 BFS 实现的
'''

import sys
sys.path.append("C:\\Users\\symbol_woo\\Desktop\\DataStructure")

import Queue.LinkedQueue as queue

class Graph():
    def __init__(self):
        # 以字典的结构模拟 邻接表 结构
        self.data = {
            '1':['3','2'],
            '2':['1','3','4'],
            '3':['1','4'],
            '4':['3','2','5','6'],
            '5':[],
            '6':[]
        }


def BFS(start, end):
    q = queue.LinkedQueue() # 借助队列
    q.enqueue(start) # 将起点入队
    visited = set() # 避免重复访问
    step = 0 # 记录扩散的步数
    visited.add(start)
    g = Graph()
    
    while not q.is_empty():
        size = q.get_length() # 获得当前队列的长度

        # 将当前队列中的所有节点向四周扩散
        for i in range(size):
            cur = q.dequeue() # 队首元素出队
            
            if cur == end: # 找到目标元素
                return step # 返回步数
            
            # 遍历队首元素的邻接链表
            # 将 cur 的邻接节点加入队列
            for j in g.data[cur]:
                if j not in visited:
                    q.enqueue(j)
                    visited.add(j)
        # 更新步数   
        step += 1
        
 

# 按层遍历

def BFS(start, end):
    q = queue.LinkedQueue() # 借助队列
    q.enqueue(start) # 将起点入队
    visited = set() # 避免重复访问
    step = 0 # 记录扩散的步数
    visited.add(start)
    g = Graph()
    
    while not q.is_empty():
        size = q.get_length() # 获得当前队列的长度

        # 将当前队列中的所有节点向四周扩散
        for i in range(size):
            cur = q.dequeue() # 队首元素出队
            
            print(cur)
            
            # 遍历队首元素的邻接链表
            # 将 cur 的邻接节点加入队列
            for j in g.data[cur]:
                if j not in visited:
                    q.enqueue(j)
                    visited.add(j)
        # 更新步数   
        step += 1

if __name__ == '__main__':
    r = BFS('1','6')
    print(r)
    