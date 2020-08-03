'''
Description: union-find 并查集算法
Date: 2020-08-03 20:50:13
Author: Wong Symbol
LastEditors: Wong Symbol
LastEditTime: 2020-08-03 21:08:08
'''

class UF:
    def __init__(self,n):
        # 连通分量，一开始互不连通
        self.count = n
        # 记录父节点，父节点指针初始指向自己
        self.parent = [i for i in range(n)]

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x
        
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return True
        self.parent[root_x] = root_y
        self.count -= 1

    def get_count(self):
        return self.count
    
    
if __name__ == '__main__':
    uf = UF(3)
    uf.union(0,1)
    uf.union(0,2)
    c = uf.get_count()
    print(c)
        
        
        
        


