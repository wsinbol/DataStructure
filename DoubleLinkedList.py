# -*- coding:utf-8 -*-

class Node(object):

	def __init__(self, data, _prev=None, _next=None):
		self.data = data
		self._prev = _prev
		self._next = _next

class DoubleLinkedList(object):
	'''
	方法：
	insert_new_value_to_head 在头部插入新结点
	insert_new_value_after_target_node 在给定结点后
	插入新结点
	insert_new_value_before_target_node 在给定结点前插入新结点
	delete_target_node 删除给定结点
	print_double_linked_list 打印链表信息
	get_node_by_value 返回给定结点
	'''

	def __init__(self, node=None):
		self._head = node

	def insert_new_value_to_head(self, value):
		new_node = Node(value)
		current = self._head
		if current == None:
			self._head = new_node
		else:
			new_node._next = self._head
			self._head._prev = new_node
			self._head = new_node
			new_node._prev = None

	def insert_new_value_after_target_node(self, target_node, value):
		new_node = Node(value)
		new_node._next = target_node._next
		target_node._next._prev = new_node
		target_node._next = new_node
		new_node._prev = target_node

	def insert_new_value_before_target_node(self, target_node, value):
		new_node = Node(value)
		new_node._prev = target_node._prev
		target_node._prev._next = new_node
		new_node._next = target_node
		target_node._prev = new_node

	def delete_target_node(self, target_node):
		target_node._next._prev = target_node._prev
		target_node._prev._next = target_node._next


	def print_double_linked_list(self):
		current = self._head
		while current:
			if current == self._head:
				print(f"{current.data}", end="")
			else:
				print(f"⇄{current.data}", end="")
			current = current._next


	def get_node_by_value(self, value):
		current = self._head
		while current and current.data != value:
			current = current._next

		if current:
			return current
		else:
			return


if __name__ == '__main__':
	dl = DoubleLinkedList()
	dl.insert_new_value_to_head(1)
	dl.insert_new_value_to_head(2)
	# dl.print_double_linked_list()

	'''
	# test data2
	data2 = dl.get_node_by_value(2)
	print(data2._prev)
	print(data2.data)
	print(data2._next.data)
	'''

	'''
	# test data1
	data1 = dl.get_node_by_value(1)
	print(data1._prev.data)
	print(data1.data)
	print(data1._next)
	'''


	# 在数据2后插入新结点
	data2 = dl.get_node_by_value(2)
	dl.insert_new_value_after_target_node(data2, 3)
	dl.insert_new_value_after_target_node(data2, 4)

	# 删除数据4这个结点
	data4 = dl.get_node_by_value(4)
	dl.delete_target_node(data4)
	

	'''
	# 在数据1前插入新结点
	data1 = dl.get_node_by_value(1)
	dl.insert_new_value_before_target_node(data1, 3)
	dl.insert_new_value_before_target_node(data1, 4)
	'''

	dl.print_double_linked_list()



