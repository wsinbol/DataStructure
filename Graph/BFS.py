'''
@Description: 广度优先搜索 Breadth First Search
@Date: 2020-05-30 17:09:50
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-06-20 23:01:52
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
            '5':['4'],
            '6':['6']
        }
        
def show(route, start, end):
    # 打印出来看下喽
    # print(route)
    if start != end:
        show(route, start, route[end])
    # 后序遍历了。。。
    print(end, end="->")

'''
visited 是用来记录已经被访问的顶点，用来避免顶点被重复访问。
如果顶点 a 被访问，那相应的 visited[a]会被设置为 true。

q 是一个队列，用来存储已经被访问、但相连的顶点还没有被访问的顶点:
因为广度优先搜索是逐层访问的，也就是说，我们只有把第 k 层的顶点都访问完成之后，才能访问第 k+1 层的顶点。当我们访问到第 k 层的顶点的时候，我们需要把第 k 层的顶点记录下来，稍后才能通过第 k 层的顶点来找第 k+1 层的顶点。所以，我们用这个队列来实现记录的功能。

route 用来记录搜索路径：
当我们从顶点 s 开始，广度优先搜索到顶点 t 后，route 数组中存储的就是搜索的路径。不过，这个路径是反向存储的。route[w]存储的是，顶点 w 是从哪个前驱顶点遍历过来的。比如，我们通过顶点 2 的邻接表访问到顶点 3，那 route[3]就等于 2。为了正向打印出路径，我们需要递归地来打印，你可以看下 show() 函数的实现方式。
'''

def BFS(start, end):
    q = queue.LinkedQueue() # 借助队列
    q.enqueue(start) # 将起点入队
    visited = set() # 避免重复访问
    step = 0 # 记录扩散的步数
    route = {}
    visited.add(start)
    g = Graph()
    
    while not q.is_empty():
        size = q.get_length() # 获得当前队列的长度

        # 将当前队列中的所有节点向四周扩散
        for i in range(size):
            cur = q.dequeue() # 队首元素出队
            
            if cur == end: # 找到目标元素
                show(route, start, end)
                return step # 返回步数
            
            # 遍历队首元素的邻接链表
            # 将 cur 的邻接节点加入队列
            for j in g.data[cur]:
                if j not in visited:
                    route[j] = cur
                    q.enqueue(j)
                    visited.add(j)
        # 更新步数   
        step += 1
        
 

# 按层遍历

def BFS_leval(start, end):
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
        
    print('the step is :', step)

if __name__ == '__main__':
    print('the min route:')
    r = BFS('1','6')
    print('\nthe min step:')
    print(r)
    exit()
    
    
# 知乎版，比上面的精简了许多，思路也不尽相同
# https://zhuanlan.zhihu.com/p/61628249

graph = {
    'a' : ['b', 'c'],
    'b' : ['a', 'c', 'd'],
    'c' : ['a','b', 'd','e'],
    'd' : ['b' , 'c', 'e', 'f'],
    'e' : ['c', 'd'],
    'f' : ['d']
}

# 借助 list 实现

def BFS(graph, s):
    queue = []
    queue.append(s)
    
    seen = set()
    seen.add(s)
    
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
        print(vertex)
        
BFS(graph, 'a')


    