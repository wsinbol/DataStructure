# -*- coding:utf-8 -*-
# 



class HashTable(object):
	def __init__(self, _size = 0):
		self._table = [None for i in range(_size)]
		self._size = _size

	def hash_function(self,key):
		return key % self._size

	def insert(self, val):
		if self._table[self.hash_function(val)] == None:
			self._table[self.hash_function(val)] = val
		else:
			key = self.linear_probing(self.hash_function(val))
			if key:
				print(val,'-触发寻址,原本下标为:',self.hash_function(val),'实际下标为:',key)
				self._table[key] = val
			else:
				print('Full,',val,'cannot insert')

	def search(self, val):
		key = self.hash_function(val)
		if self._table[key] == val:
			return key

		start_key = key + 1
		while self._table[start_key] != None and key != start_key:
			if self._table[start_key] == val:
				return start_key
			else:
				start_key += 1
				if start_key == self._size:
					start_key = 0
		return None


	'''
	线性探测寻址
	'''
	def linear_probing(self, key):
		start_key = key + 1
		while start_key != key:
			if start_key == self._size:
				start_key = 0
			if self._table[start_key] == None:
				return start_key
			else:
				start_key += 1
		return

	def print_table(self):
		for k,v in enumerate(self._table):
			print(k,'-->',v)

if __name__ == '__main__':
	h = HashTable(6)
	# h.print_table()
	h.insert(12)
	h.insert(0)
	h.insert(5)
	h.insert(11)
	h.insert(9)
	h.insert(10)
	h.insert(2)
	h.print_table()

	print('Search....')
	print(h.search(0))

