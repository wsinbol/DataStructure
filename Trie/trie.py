'''
@Description: Trie树
Trie 树，也叫“字典树”。顾名思义，它是一个树形结构。它是一种专门处理字符串匹配的数据结构，用来解决在一组字符串集合中快速查找某个字符串的问题。
属于多模式串匹配算法。

单模式串匹配算法，是在一个模式串和一个主串之间进行匹配，也就是说，在一个主串中查找一个模式串。
多模式串匹配算法，就是在多个模式串和一个主串之间做匹配，也就是说，在一个主串中查找多个模式串

@Date: 2020-06-22 15:35:22
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-06-23 15:57:23
'''

class TreeNode():
    def __init__(self, data):
        self.data = data
        self._children = [None] * 26
        self._is_ending_char = False
        
        
class Trie():
    def __init__(self):
        self._root = TreeNode('/')

    def insert(self, text):
        node = self._root
        for index, char in map(lambda x: (ord(x) - ord("a"), x), text):
            if not node._children[index]:
                node._children[index] = TreeNode(char)
            node = node._children[index]
        node._is_ending_char = True

    def find(self, pattern):
        node = self._root
        for index in map(lambda x:ord(x) - ord('a'), pattern):
            if not node._children[index]:
                return False
            node = node._children[index]
        return node._is_ending_char
    
    # 递归遍历整个trie树
    def show(self,root_node,pre='',level=0):
        '''
        root_node:当前节点
        pre:当前节点前缀
        level:层级
        '''
        if root_node:
            print(pre,root_node.data,level)
            for child in root_node._children:
                self.show(child,pre+root_node.data,level+1)
    
if __name__ == "__main__":
    strs = ["how", "hi", "her", "hello", "so", "see"]
    trie = Trie()
    for s in strs:
        trie.insert(s)

    trie.show(trie._root)
    # print(trie.find("her"))
        
            
