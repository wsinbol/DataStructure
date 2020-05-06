
class Node:
	def __init__(self, data=None):
		self.data = data
		self._next = None

class LinkedList:
	def __init__(self):
		self._head = None
		self.blank_node = Node()

	def push(self, val):
		new_node = Node(val)
		if self._head == None:
			self._head = new_node
		else:
			new_node._next = self._head
			self._head = new_node

	# 重点体会
	def iteration(self, head_node):
		if head_node == None:
			return head_node
		# 正序遍历
		# print(head_node.data)
		self.iteration(head_node._next)
		# 倒叙遍历
		print(head_node.data)

	def traverse(self, head_node, new_head):

		'''
		if head_node is None:
			return ;
		if head_node._next is None:
			new_head = head_node
		else:
			new_head = self.traverse(head_node._next, new_head)
			head_node._next._next = head_node
			head_node._next = None
		return new_head
		'''

		global i
		i = 0
		if head_node._next is None:
			return head_node
		blank_node = self.traverse(head_node._next, new_head)
		# print(blank_node)
		head_node._next._next = head_node
		head_node._next = None
		i += 1
		print('迭代：',i)
		print(head_node.data)
		return blank_node
		


	def show(self):
		current = self._head
		while current:
			print(current.data)
			current = current._next

if __name__ == '__main__':
	l = LinkedList()
	l.push(1)
	l.push(2)
	l.push(3)
	l.show()
	l.iteration(l._head)

	exit()
	print('#'*4)
	new_head = None
	# 以为t还是LinkedList结构，其实不然
	t = l.traverse(l._head,new_head)
	print('type of t:',type(t))
	while t:
		print(t.data)
		t = t._next