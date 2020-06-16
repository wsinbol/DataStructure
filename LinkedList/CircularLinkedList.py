'''
循环单链表

'''


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

	def insert_new_value_to_end(self, value):
		new_node = Node(value)
		if self._head == None:
			self._head = new_node
			new_node._next = new_node
		else:
			current = self._head
			while current._next != self._head:
				current = current._next

			new_node._next = self._head
			current._next = new_node
			

	def find_by_value(self, value):
		# 不能调用Node类生成目标结点，current != target_node 是永远成立的！！！
		# 因为：新生成的结点与链表中任何一个结点的地址是完全不一样的！！！
		# 所以只能根据值来判断，不要用地址来判断
		'''
		target_node = Node(value)
		current = self._head
		while current != target_node and current._next != self._head:
			current = current._next

		if current == target_node:
			return current
		else:
			return None
		'''

		'''
		# So 改成如下形式：
		current = self._head
		while current.data != value and current._next != self._head:
			current = current._next

		if current.data == value:
			return current
		else:
			return
		'''
		
		current = self._head
		while current and current.data != value and current._next != self._head:
			current = current._next
   
		if current.data == value:
			return current
		else:
			return 
		

	def delete_target_node(self, node):
    
		if node == None:
			return 

		cur = self._head
		nxt = cur._next

		# 遍历非头结点，要么nxt指向尾结点，要么 nxt 找到要删除的结点
		while nxt != node and nxt._next != self._head:
			cur = cur._next
			nxt = nxt._next
		# 如果头结点是要删除的节点
		if self._head == node:
			self._head = self._head._next
			nxt._next = self._head
		# 命中 nxt 节点
		if nxt == node:
			cur._next = nxt._next

		# 要删除的节点不存在什么都做

	def print_all(self):
	    current = self._head
	    if current:
	        print(f"{current.data}", end="")
	        current = current._next
	    # while current:
	    while current != self._head:
	        print(f"->{current.data}", end="")
	        current = current._next

if __name__ == '__main__':
	l = CircularLinkedList()
	# l.insert_new_value_to_head(1)
	l.insert_new_value_to_end(2)
	l.insert_new_value_to_end(3)
	l.insert_new_value_to_end(4)
	l.insert_new_value_to_head(5)
	l.print_all()
	# print()
	node2 = l.find_by_value(2)
	# 使用的时候需要判断是否为 None
	print('find:',node2)
	# print(node2.data)
	# exit()
	l.delete_target_node(node2)
	l.print_all()

