# !/usr/bin/env python
# -*- coding:utf-8 -*-

class Node(object):

	def __init__(self, data, _prev=None, _next=None):
		self.data = data
		self._prev = _prev
		self._next = _next

class DoubleCircularLinkedList(object):

	def __init__(self, node=None):
		self._head = node

	def insert_new_value_to_head(self, value):
		new_node = Node(value)
		current = self._head

		if current == None:
			new_node._next = new_node
			new_node._prev = new_node
			self._head = new_node
		else:
			# self._head._prev # 指向尾结点
			# 先记录尾结点
			tail = self._head._prev
			# 新结点后继指向头结点的位置
			new_node._next = self._head
			# 头结点前驱指向新结点
			self._head._prev = new_node
			# 新结点的前驱指向尾结点
			new_node._prev = tail
			# 尾结点的后继指向新结点
			tail._next = new_node
			# 更新头结点
			self._head = new_node

	# target_node cannot be tail node
	def insert_new_value_after_target_node(self, value, node):
		new_node = Node(value)
		new_node._next = node._next
		node._next._prev = new_node
		new_node._prev = node
		node._next = new_node

	def is_empty(self):
		if self._head == None:
			return True
		else:
			return False

	def insert_new_value_before_target_node(self, value, node):
		
		# 判断基准结点是否为头结点
		if self._head == node:
			self.insert_new_value_to_head(value)
		else:
			new_node = Node(value)

			node._prev._next = new_node
			new_node._prev = node._prev
			new_node._next = node
			node._prev = new_node

	def delete_target_node(self, node):
		if self._head == node:
			tail = self._head._prev
			node._next._prev = tail
			tail._next = node._next
			self._head = self._head._next
		else:
			node._prev._next = node._next
			node._next._prev = node._prev


	def find_by_value(self, value):
		current = self._head
		while current.data != value and current._next != self._head:
			current = current._next

		if current.data == value:
			return current
		else:
			return

	def get_linked_list_length(self):

		current = self._head
		length = 0
		if current:
			length += 1
			current = current._next

		while current != self._head:
			length += 1
			current = current._next

		return length


	def print_linked_list(self):
		current = self._head
		if current:
			print(current.data)
			current = current._next

		while current != self._head:
			print(current.data)
			current = current._next

if __name__ == '__main__':
	l = DoubleCircularLinkedList()
	l.insert_new_value_to_head(1)
	l.insert_new_value_to_head(2)

	# print(l.is_empty())

	node1 = l.find_by_value(2)
	# print(node1)
	l.print_linked_list()
	l.delete_target_node(node1)
	# print(l.get_linked_list_length())

	'''
	l.insert_new_value_to_head(2)
	l.insert_new_value_to_head(3)
	node2 = l.find_by_value(2)
	l.insert_new_value_after_target_node(4, node2)
	l.insert_new_value_after_target_node(5, node2)

	l.insert_new_value_before_target_node(6, node2)
	l.insert_new_value_before_target_node(7, node2)
	l.delete_target_node(node2)
	node1 = l.find_by_value(1)
	l.insert_new_value_after_target_node(8, node1)
	l.insert_new_value_after_target_node(9, node1)

	node3 = l.find_by_value(3)
	l.insert_new_value_before_target_node(10, node3)
	'''

	l.print_linked_list()
	# print(l.find_by_value(2).data)

