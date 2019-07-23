# !/usr/bin/env python3
# -*- coding:utf-8 -*-

class CircularQueue(object):

	def __init__(self, capacity):
		# 根据循环队列的特性，大小为capacity的队列最多只能存储capacity-1大小的数据
		# 队满时的tail位置并不存储数据，所以循环队列会浪费一个存储空间
		# 针对这种情况，避免造成和数组等类型的不一致，所以再封装循环队列的时候可以将capacity+1以保证确实能存储capacity个数据
		# 这样也不会给调用者造成迷惑
		
		# self._capacity = capacity
		self._capacity = capacity + 1
		self._items = [None] * self._capacity # 基于列表实现
		self._head = 0
		self._tail = 0


	def enqueue(self, value):
		if (self._tail + 1) % self._capacity == self._head:
			print('The queue is full! The data %s ignored!' % value)
			return False
		# self._items.append(value)
		self._items[self._tail] = value
		self._tail = (self._tail + 1) % self._capacity
	
	def dequeue(self):
		if self._head == self._tail:
			print('The queue is empty')
			return False
		value = self._items[self._head]
		self._head = (self._head + 1) % self._capacity
		return value

	def printQueue(self):
		current = self._head
		while current != self._tail:
			print(self._items[current], end=',')
			current = (current + 1) % self._capacity
		print()
		

if __name__ == '__main__':
	q = CircularQueue(5)
	q.enqueue(2)
	q.enqueue(0)
	q.enqueue(1)
	q.enqueue(3)
	q.enqueue(2)
	q.printQueue()
	for _ in range(4):
		q.dequeue()
		# print(q.dequeue())
	q.printQueue()
	# q.enqueue(4)
	# q.enqueue(1)
	# q.enqueue(1)
	q.enqueue(4)
	q.enqueue(5)
	q.enqueue(6)
	q.enqueue(7)
	q.enqueue(8)
	q.printQueue()
