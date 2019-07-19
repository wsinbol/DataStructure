# !/usr/bin/env python3
# -*- coding:utf-8 -*-

class Node(object):

	def __init__(self, data=None, _next=None):
		self.data = data
		self._next = _next

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

	def dequeue(self):
		if self._head:
			value = self._head.data
			self._head = self._head._next
			if not self._head:
				self._tail = None
			return value

	def __repr__(self):
		values = []
		current = self._head

		while current:
			values.append(current.data)
			current = current._next
		return "->".join(value for value in values)

if __name__ == '__main__':
	q = LinkedQueue()
	for i in range(10):
		q.enqueue(str(i))
	print(q)

	for _ in range(3):
		q.dequeue()
	print(q)

	q.enqueue('10')
	print(q)


