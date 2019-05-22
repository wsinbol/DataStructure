#-*- coding:utf-8 -*-

class Node(object):

	def __init__(self, data, _next=None):
		self.data = data
		self._next = _next

class CircularLinkedList(object):

	def __init__(self, node=None):
		self._head = None

	def insert_new_value_to_head(self, value):
		new_node = Node(value)
		if self._head == None:
			self._head = new_node
			new_node._next = new_node
		else:
			current = self._head
			while current._next != self._head:
				# 让指针走到最后一个结点
				current = current._next

			new_node._next = self._head
			self._head = new_node
			current._next = new_node

	def print_all(self):
	    current = self._head
	    if current:
	        print(f"{current.data}", end="")
	        current = current._next
	    while current != self._head:
	        print(f"->{current.data}", end="")
	        current = current._next

if __name__ == '__main__':
	l = CircularLinkedList()
	l.insert_new_value_to_head(1)
	l.insert_new_value_to_head(2)
	l.print_all()
