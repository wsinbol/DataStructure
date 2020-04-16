# !/usr/bin/env python3
# -*- coding:utf-8 -*-

class Node(object):

	def __init__(self, data=None, _next=None):
		self.data = data
		self._next = _next

# 链式队列
class LinkedQueue(object):

	def __init__(self, _head=None, _tail=None):
		self._head = _head
		self._tail = _tail

	def enqueue(self, value):
		new_node = Node(value)
		if self._tail:
			self._tail._next = new_node
		else:
			self._head = new_node
		self._tail = new_node

	def get_head(self):
		if self._head:
			return self._head.data

	def get_tail(self):
		if self._tail:
			return self._tail.data

	def dequeue(self):
		if self._head:
			value = self._head.data
			self._head = self._head._next
			if not self._head:
				self._tail = None
			return value

	def is_empty(self):
		if self._head is None:
			return True
		else:
			return False

	def __repr__(self):
		values = []
		current = self._head

		while current:
			values.append(current.data)
			current = current._next
		return "->".join(value for value in values)

# 队列实现的栈

class Stack:
	def __init__(self):
		self._top = LinkedQueue()
		self.top_element = None

	def push(self, val):
		self._top.enqueue(val)
		self.top_element = val

	def show(self):
		head = self._top._head
		while head:
			print(head.data)
			head = head._next

	def get_top(self):
		# return self._top._tail.data
		if self._top._head:
			return self.top_element
		else:
			return


	def pop(self):
		# 推荐写法
		target = self.top_element
		cur = self._top.dequeue()
		while cur != target:
			self.push(cur)
			cur = self._top.dequeue()
		return cur
		

		'''
		cur = self._top.dequeue()
		while cur != self.top_element:
			self._top.enqueue(cur)
			cur = self._top.dequeue()
		return cur
		'''
		

if __name__ == '__main__':
	s = Stack()
	s.push(1)
	# s.push(2)
	# s.push(3)
	# s.push(4)
	print(s.pop())
	print('***')
	s.show()
	print('***')
	print(s.get_top())


	'''
	q = LinkedQueue()
	for i in range(10):
		q.enqueue(str(i))
	print(q)

	for _ in range(3):
		q.dequeue()
	print(q)

	q.enqueue('10')
	print(q)
	'''

