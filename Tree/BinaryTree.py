'''
@Description: 
@Date: 2020-06-04 00:02:32
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-06-04 00:53:42
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


if __name__ == '__main__':
    A = TreeNode('A')
    B = TreeNode('B')
    C = TreeNode('C')
    
    bt = BinaryTree(A)
    A.add2left(B)
    A.add2right(C)

    print('pre order is:')
    bt.pre_order(bt._root)
    
    
    print('mid order is:')
    bt.mid_order(bt._root)
        


        
    