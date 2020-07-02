'''
@Description: BinaryTree Library
@Date: 2020-06-04 00:02:32
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-07-02 23:28:37
'''


class TreeNode():
    def __init__(self, data=None):
        self.data = data
        self._left = None
        self._right = None
        
    def add2left(self,new_node):
        # parent_node._left = new_node
        self._left = new_node

    def add2right(self,new_node):
        # parent_node._right = new_node
        self._right = new_node
        
class BinaryTree():
    def __init__(self,root_node=None):
        self._root = root_node
        
    def pre_order(self, tree_node):
        if tree_node != None:
            print(tree_node.data)
            self.pre_order(tree_node._left)
            self.pre_order(tree_node._right)
            
    def mid_order(self, tree_node):
        if tree_node != None:
            self.mid_order(tree_node._left)
            print(tree_node.data)
            self.mid_order(tree_node._right)
            
    def post_order(self,tree_node):
        pass
    
    # 求二叉树的最小高度
    def min_depth(self, tree_node):
        if tree_node == None:
            return 0
        
        q = [tree_node]
        depth = 1
        
        while len(q) > 0:
            size = len(q)
            
            # 注意下面两种循环的不同
            for i in range(0,size): # 相当于按层去遍历
            # for i in q: # 该语句不会执行 depth += 1 操作！！！
                print('the length of q:', len(q))
                cur = q.pop(0)

                if cur._left == None and cur._right == None:
                    return depth
                
                if cur._left != None:
                    q.append(cur._left)

                if cur._right != None:
                    q.append(cur._right)
                
                print([p.data for p in q])
            depth += 1
        
        return None
    
    def max_depth(self, root):
        if not root:
            return 0
        
        left_depth = self.max_depth(root._left)
        right_depth = self.max_depth(root._right)
        return max(left_depth, right_depth) + 1
        


if __name__ == '__main__':
    A = TreeNode('A')
    B = TreeNode('B')
    C = TreeNode('C')
    
    bt = BinaryTree(A)
    A.add2left(B)
    A.add2right(C)

    '''
    print('pre order is:')
    bt.pre_order(bt._root)
    
    print('mid order is:')
    bt.mid_order(bt._root)
    '''
    
    d = bt.min_depth(bt._root)
    print('the binary tree min depth is :', d)
    
    w = bt.max_depth(bt._root)
    print('the binary tree max depth is : ',w)



        
    