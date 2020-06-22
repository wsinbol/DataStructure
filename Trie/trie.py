'''
@Description: Trie树
@Date: 2020-06-22 15:35:22
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-06-22 23:43:13
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
    
    def show(self,root_node):
        if root_node:
            print(root_node.data)
            for child in root_node._children:
                self.show(child)
    
if __name__ == "__main__":
    strs = ["how", "hi", "her", "hello", "so", "see"]
    trie = Trie()
    for s in strs:
        trie.insert(s)

    # trie.show(trie._root)
    print(trie.find("how"))
        
            
