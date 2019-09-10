# -*- coding:utf-8 -*-
'''
基于单链表的散列表数据结构
'''
class Node(object):
	def __init__(self, _data=None, _next=None):
		self._data = _data
		self._next = _next

class HashTable(object):
	def __init__(self, _size = 0):
		self._table = [Node() for i in range(_size)]
		self._size = _size

	def hash_function(self,key):
		return key % self._size

	def insert(self, val):
		key = self.hash_function(val)
		node = Node(val)
		node._next = self._table[key]._next
		self._table[key]._next = node

	def search(self, val):
		key = self.hash_function(val)

		if self._table[key]._next is None:
			return (key, None)
		else:
			head = self._table[key]._next

		if head._data == val:
			return (key, head)

		head_next = head._next
		while head_next is not None:
			if head_next._data == val:
				return (key, head_next)
			head_next = head_next._next

		return None

	def delete(self, val):
		key = self.hash_function(val)
		if self._table[key]._next is None:
			return None

		head = self._table[key]._next
		if head._data == val:
			_, addr = self.search(val)
			self._table[key]._next = addr._next

		next_point = head._next
		while next_point is not None and next_point._data != val:
			head = next_point
			next_point = next_point._next
			
		if next_point:
			head._next = next_point._next
		return


	def print_table(self):
		for i in range(self._size):
			print(i,end=":")
			current = self._table[i]._next
			while current is not None:
				print(current._data,end="->")
				current = current._next
			print('None')

if __name__ == '__main__':
	h = HashTable(6)
	h.insert(3)
	h.insert(9)
	h.insert(15)

	h.insert(10)
	h.insert(4)
	print('search...')
	index, addr = h.search(6)
	if addr:
		print(addr._data)
	else:
		print('Not Found')

	print('delete...')
	h.delete(3)
	h.print_table()



