'''
@Description: 
@Date: 2019-06-26 22:36:53
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-06-20 17:32:28
'''
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

class Node(object):
	def __init__(self, data=None, _next=None):
		self.data = data
		self._next = _next

# 栈是操作受限的线性表，只允许在一端插入和删除数据
# 栈的特性先进后出

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

	def isEmpty(self):
		if self._top == None:
			return True
		else:
			return False

	def print(self):
		top = self._top
		while top:
			print(top.data,end="->")
			top = top._next

# 双栈构建一个队列
class Queue:
	def __init__(self):
		self._head = LinkedStack()
		self._tail = LinkedStack()

	# 入队操作，将新增的数据添加至尾栈中
	def enqueue(self,val):
		self._tail.push(val)

	# 出队操作，将尾栈中的数据出栈，同时将其入栈到头栈中，则头栈的栈顶元素即是队列的队首
	def dequeue(self):
		while self._head.isEmpty():
			while not self._tail.isEmpty():
				self._head.push(self._tail.pop())
		return self._head.pop()

	def isEmpty(self):
		if self._head.isEmpty() and self._tail.isEmpty():
			return True
		else:
			return False

if __name__ == '__main__':
	'''
	s = LinkedStack()
	for i in range(0,5):
		s.push(i)
	print(s.pop())
	print(s.pop())
	print(s.pop())
	print(s.pop())
	print(s.pop())
	'''

	q = Queue()
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	print(q.dequeue())
	print(q.dequeue())



