# !/usr/bin/env python3
# -*- coding:utf-8 -*-

class Node(object):
	def __init__(self, data=None, _next=None):
		self.data = data
		self._next = _next

# 栈是操作受限的链表
class LinkedStack(object):
	def __init__(self, _top=None):
		self._top = _top

	# 入栈操作
	def push(self, value):
		new_top = Node(value)
		new_top._next = self._top
		self._top = new_top

	def pop(self):
		top = self._top
		if top:
			value = top.data
			self._top = top._next
			return value

	def print(self):
		top = self._top
		while top:
			print(top.data)
			top = top._next

if __name__ == '__main__':
	s = LinkedStack()
	for i in range(0,5):
		s.push(i)
	# s.print()
	print(s.pop())
	print(s.pop())
	print(s.pop())
	print(s.pop())
	print(s.pop())




