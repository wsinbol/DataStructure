
class TreeNode:
	def __init__(self, val=None):
		self.data = val
		self.children = []

	def add_children(self, node=None):
		self.children.append(node)


class Node:
	def __init__(self, val=None):
		self.data = val
		self._next = None

class Queue:
	def __init__(self, _head=None, _tail=None):
		self._head = _head
		self._tail = _tail

	def push(self, val):
		new_node = Node(val)
		if self._tail:
			self._tail._next = new_node
		else:
			self._head = new_node
		self._tail = new_node

	def pop(self):
		head = self._head
		if head:
			self._head = head._next
			if not self._head:
				self._tail = None
		return head

	def is_empty(self):
		if self._head is None and self._tail is None:
			return True
		else:
			return False


class MultiTree:
	def __init__(self, root_node=None):
		self._root = root_node

	def add_child(self, parent_node, val):
		new_node = TreeNode(val)
		if self._root is None:
			self._root = TreeNode(val)
		else:
			parent_node.children.append(new_node)

	# 深度遍历
	def traverse(self, root_node):
		if root_node:
			print(root_node.data)
			for child in root_node.children:
				self.traverse(child)
    
    # 递归遍历，与深度遍历同
	def traverse_(self, root):
		if not root:
			return []
		
		res = [root.data]
		for child in root.children:
			res.extend(self.traverse_(child))
		
		return res

	# 迭代式遍历
	def traverse_iter(self,root):

		res = []
		stack = [root]
		while stack:
			node = stack.pop()
			if node:
				res.append(node.data)
				# 这里是重点，要倒序插入
				stack.extend(node.children[::-1])
		return res
    
	# 广度遍历
	def breadth_traverse(self, root):
		"""借助队列实现树的层次遍历"""
		if root == None:
			return
		queue = Queue()
		queue.push(root)
		res = []
		while not queue.is_empty():
			node = queue.pop()
			if node:
				print(node.data.data)
				res.append(node.data.data)
				for child in node.data.children:
					queue.push(child)
		return res

if __name__ == '__main__':
    # No.1 通过MultiTree类添加子节点，略显麻烦
	
	mt = MultiTree()
	mt.add_child(None,1)
	mt.add_child(mt._root, 2)
	mt.add_child(mt._root, 3)
	mt.add_child(mt._root, 4)
	mt.add_child(mt._root, 5)
	r = mt.traverse_iter(mt._root)
	print(r)
	
	exit()

	# No.2 通过TreeNode类直接添加子节点
	A = TreeNode('A')
	mt = MultiTree(A)
	B = TreeNode('B')
	C = TreeNode('C')
	D = TreeNode('D')


	E = TreeNode('E')
	F = TreeNode('F')
	G = TreeNode('G')

	A.add_children(B)
	A.add_children(C)
	A.add_children(D)

	C.add_children(E)
	E.add_children(G)
	D.add_children(F)
	mt.traverse(A)
	print('###')
	res = mt.breadth_traverse(A)
	print(res)


