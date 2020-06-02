'''
@Description: DFS
@Date: 2020-05-31 11:45:50
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-06-02 11:30:09
'''

'''
DFS 
'''

class Graph():
    def __init__(self):
        # 以字典的结构模拟 邻接表 结构
        self.data = {
            'a' : ['b', 'c'],
            'b' : ['a', 'c', 'd'],
            'c' : ['a','b', 'd','e'],
            'd' : ['b' , 'c', 'e', 'f'],
            'e' : ['c', 'd'],
            'f' : ['d']
        }

track = []
g = Graph()
visited = set()
res = []

def backtrack(track, choices):
    res.extend(track)
    
    for item in choices:
        if item not in visited:
            print('select num is :', item)
            track.append(item)
            visited.add(item)
            backtrack(track, g.data[item])
            track.remove(item)


backtrack(track, g.data['a'])
print(set(res))

# 知乎版本

# 递归版

def DFS(graph, s, queue=[]):
    queue.append(s)
    for i in graph[s]:
        if i not in queue:
            DFS(graph, i, queue)
    return queue

# 非递归版 借助 list 结构

def DFS(graph, s):
    # 借助 list 来实现
    stack = []
    stack.append(s)

    visited = set()
    visited.add(s)
    
    while len(stack) > 0:
        vertex = stack.pop(0)
        nodes = graph[vertex]

        for node in nodes:
            if node not in visited:
                stack.append(node)
                visited.add(node)

        print(vertex)

g = {
    'a' : ['b', 'c'],
    'b' : ['a', 'c', 'd'],
    'c' : ['a','b', 'd','e'],
    'd' : ['b' , 'c', 'e', 'f'],
    'e' : ['c', 'd'],
    'f' : ['d']
}

print(DFS(g, 'a'))