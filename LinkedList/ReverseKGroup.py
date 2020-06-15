
class Node:
	def __init__(self, data=None):
		self.data = data
		self._next = None


class LinkedList:
	def __init__(self):
		self._head = None

	def push(self, val):
		new_node = Node(val)
		if self._head == None:
			self._head = new_node
		else:
			new_node._next = self._head
			self._head = new_node

	# 递归式反转
	def reverse_recursion(self, head_node):
		'''
		blank_node:原链表的最后一个结点，反转后的头结点，不是递归函数的参数，每次都是定值
		head_node:递归函数的参数，每次都是变化的，有入栈和出栈的流程
		'''

		if head_node._next == None:
			return head_node

		blank_node = self.reverse_recursion(head_node._next)

		head_node._next._next = head_node
		head_node._next = None
		print('head node is', head_node.data)
		print('blank node is', blank_node.data)
		return blank_node

	# 遍历式反转
	def reverse_traverse(self, head_node):
		pre = None
		cur = head_node
		nxt = head_node

		while cur != None:
			nxt = cur._next
			cur._next = pre

			pre = cur
			# 遍历下一个节点，准备反转
			cur = nxt

		return pre

	# 反转 node1 到 node2 区间之间的节点
	def reverse_traverse_interval(self,node1, node2):
		pre = None
		cur = node1
		nxt = node1

		while cur != node2:
			nxt = cur._next
			cur._next = pre

			pre = cur
			# 遍历下一个节点，准备反转
			cur = nxt

		return pre

	# k 个节点为一组进行反转
	def reverse_k_group(self,head_node,k):
		if head_node == None:
			return None

		a = head_node
		b = head_node

		for i in range(k):
			if b == None:
				return head_node
			b = b._next
		# 计算a,b区间的新头结点
		new_head = self.reverse_traverse_interval(a, b)
		# 结点连接
		a._next = self.reverse_k_group(b,k)
		return new_head

	def show(self):
		current = self._head
		while current:
			print(current.data,end="->")
			current = current._next

if __name__ == '__main__':
	l = LinkedList()
	l.push(5)
	l.push(4)
	l.push(3)
	l.push(2)
	l.push(1)
	print('print linked list:')
	l.show()
	print()

	node1 = l._head
	node2 = node1._next
	node3 = node2._next
	node4 = node3._next
 
	'''
	q = l.reverse_recursion(l._head)
	while q:
		print(q.data)
		q = q._next
	exit()
	'''

	'''
	print('\n part reverse:')
	t = l.reverse_traverse_interval(node1,node3._next)
	while t:
		print(t.data)
		t = t._next
	'''

	print('\n reverse k')
	g = l.reverse_k_group(node1,3)
	print('type of g:', type(g))
	while g:
		print(g.data)
		g = g._next
	exit()

	r = l.reverse_traverse(l._head)
	print('\nreverse:')
	while r:
		print(r.data)
		r = r._next

