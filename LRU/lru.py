# 双向循环链表的节点类
class Node:
	def __init__(self,k=None,v=None):
		self.data = {k:v}
		self._prev = None
		self._next = None

# 哈希字典类，完全可以用python自带的dict结构实现
# k:node 字典结构
class HashMap:
	def __init__(self):
		self._dict = {}

	def indexed(self, k,node):
		self._dict[k] = node

	def show_hash(self):
		return self._dict

	def get_len(self):
		return len(self._dict)

# 双向循环列表类
class DCLinkedList():
	def __init__(self):
		self._head = None

	def add_first(self, new_node):
		# new_node = Node(k,v)
		current = self._head
		if current == None:
			new_node._next = new_node
			new_node._prev = new_node
			self._head = new_node
		else:
			tail = current._prev
			new_node._next = current
			current._prev = new_node
			new_node._prev = tail
			tail._next = new_node
			self._head = new_node


	def del_last(self, last_node):
		last_node._prev._next = last_node._next
		last_node._next._prev = last_node._prev

	def print_linked_list(self):
		current = self._head
		if current:
			print(current.data)
			current = current._next

		while current != self._head:
			print(current.data)
			current = current._next


class LRU:
	def __init__(self, capacity):
		self.capacity = capacity
		self.hash_map = HashMap()
		self.cache = DCLinkedList()

	def get(self, k):
		if k in self.hash_map._dict:
			find = self.hash_map._dict[k]
			val = find.data[k]
			self.put(k, val)
			return val
		else:
			return -1


	def put(self, k,v):
		new_node = Node(k,v)

		if k in self.hash_map._dict:
			target_node = self.hash_map._dict[k]
			self.cache.del_last(target_node)
			# target_node._next._prev = target_node._prev
			# target_node._prev._next = target_node._next

			self.cache.add_first(new_node)
			self.hash_map.indexed(k,new_node)
		else:
			if self.capacity > self.hash_map.get_len():
				self.cache.add_first(new_node)
				self.hash_map.indexed(k,new_node)
			else:
				header = self.cache._head
				tailer = header._prev

				last_node = tailer.data
				k_node, = last_node
				v_node, = last_node.values()
				val = self.hash_map._dict[k_node]

				self.cache.del_last(tailer)
				# self.cache._head._prev = tailer._prev
				# tailer._prev._next = self.cache._head

				# tailer._next._prev = tailer._prev
				# tailer._prev._next = tailer._next

				# print(val.data)
				# print(val._next.data)
				# print(val._prev.data)

				del self.hash_map._dict[k_node]
				self.cache.add_first(new_node)
				self.hash_map.indexed(k,new_node)


	def show(self):
		print(self.capacity)
		map = self.hash_map.show_hash()
		# print(map[1].data)
		print(map)
		self.cache.print_linked_list()


if __name__ == '__main__':
	lru = LRU(3)
	lru.put(1,1)
	lru.put(2,2)
	lru.put(3,3)
	lru.put(4,4)
	lru.put(5,5)
	lru.put(4,1)
	print('-'*10)
	lru.show()
	print('-'*10)
	print(lru.get(5))
	lru.show()
	print('-'*10)
	print(lru.get(3))
	lru.show()
