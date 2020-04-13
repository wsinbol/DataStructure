
class Node:
	def __init__(self, data=None):
		self.data = data
		self._next = None
# 双端队列
class Deque:
	def __init__(self, _head=None, _tail=None):
		self._head = _head
		self._tail = _tail

	def push_front(self, val):
		new_node = Node(val)
		if self._head == None:
			self._head = new_node
			self._tail = new_node
		else:
			new_node._next = self._head
			self._head = new_node

	def push_back(self, val):
		new_node = Node(val)
		if self._head == None:
			self._head = new_node
			self._tail = new_node
		else:
			self._tail._next = new_node
			self._tail = new_node

	def pop_front(self):
		head = self._head
		if head:
			val = head.data
			self._head = head._next
			return val
		return -1

	# 单向链式节点想要实现此方法较为复杂，因为要删除节点的前一个节点不容易获取
	# 需要双指针遍历
	def pop_back(self):
		tail = self._tail
		if tail:
			val = tail.data


	def show(self):
		head = self._head
		while head:
			print(head.data)
			head = head._next

if __name__ == "__main__":
	d = Deque()
	d.push_front(1)
	d.push_front(2)
	d.push_back(3)
	print(d.pop_front())
	print(d.pop_front())
	print(d.pop_front())
	d.show()
	print('#'*4)
	# print('tail:', d._tail.data)
	# print('head:', d._head.data)
