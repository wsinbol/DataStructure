# -*- coding:utf-8 -*-

class TreeNode(object):
	def __init__(self, data=None):
		self.data = data
		self._left = None
		self._right = None

class BinaryTree(object):
	def __init__(self):
		self._root = None

	def insert2root(self, value):
		if not self._root:
			self._root = TreeNode(value)
		else:
			print('Root Already exists!')

	def find_by_value(self, value):

		def make_val_addr_dict(node):
			# 树节点的值和地址的转换
			if node:
				yield {
					"data":node.data,
					"addr": node
				}
				yield from make_val_addr_dict(node._left)
				yield from make_val_addr_dict(node._right)

		node = self._root
		if node and node.data == value:
			return node

		val_addr = list(make_val_addr_dict(node))
		for item in val_addr:
			if item['data'] == value:
				return item['addr']

	def insert2left_of_target(self, value, target):
		if not target:
			print('Cannot insert because target node goes wrong!')
		new_node = TreeNode(value)
		target._left = new_node

	def insert2right_of_target(self, value, target):
		if not target:
			print('Cannot insert because target node goes wrong!')
		new_node = TreeNode(value)
		target._right = new_node

	def pre_order(self, node):
		if node:
			yield node.data
			yield from self.pre_order(node._left)
			yield from self.pre_order(node._right)

	def in_order(self, node):
		if node:
			yield from self.in_order(node._left)
			yield node.data
			yield from self.in_order(node._right)

	def post_order(self, node):
		if node:
			yield from self.post_order(node._left)
			yield from self.post_order(node._right)
			yield node.data

if __name__ == '__main__':
	bt = BinaryTree()
	bt.insert2root(2)

	node2 = bt.find_by_value(2)
	bt.insert2left_of_target(3, node2)
	bt.insert2right_of_target(4, node2)
	

	node4 = bt.find_by_value(3)
	bt.insert2left_of_target(5, node4)
	bt.insert2right_of_target(6, node4)

	node4 = bt.find_by_value(5)
	bt.insert2left_of_target(7, node4)
	bt.insert2right_of_target(8, node4)

	node4 = bt.find_by_value(8)
	bt.insert2left_of_target(9, node4)
	bt.insert2right_of_target(10, node4)

	print(list(bt.pre_order(node2)))
	print(list(bt.in_order(node2)))
	print(list(bt.post_order(node2)))


