# -*- coding:utf-8 -*-
'''
基于开放寻址法-线性探测的散列表
'''
class HashTable(object):
	def __init__(self, _size = 0):
		self._table = [None for i in range(_size)]
		self._size = _size

	def hash_function(self,key):
		return key % self._size

	def insert(self, val):
		# 千万别用 == 
		if self._table[self.hash_function(val)] is None or self._table[self.hash_function(val)] is False:
			self._table[self.hash_function(val)] = val
		else:
			key = self.linear_probing(self.hash_function(val))
			if key != None:
				print(val,'-触发寻址,原本下标为:',self.hash_function(val),'实际下标为:',key)
				self._table[key] = val
			else:
				print('Full,',val,'cannot insert')

	def search(self, val):
		key = self.hash_function(val)
		if self._table[key] == val:
			return key

		start_key = key + 1
		if start_key == self._size:
			start_key = 0
		while self._table[start_key] is not None and key != start_key:
			if self._table[start_key] == val:
				return start_key
			else:
				start_key += 1
				if start_key == self._size:
					start_key = 0
		return None

	def delete(self, val):
		key = self.hash_function(val)
		if self._table[key] == val:
			self._table[key] = False
			return

		start_key = key + 1
		is_loop = 0

		if start_key == self._size:
			start_key = 0

		while not is_loop:
			if self._table[start_key] == val:
				self._table[start_key] = False
				break
			else:
				start_key += 1
				if start_key == self._size:
					start_key = 0
				if start_key+1 == key:
					is_loop = 1
		return None

	'''
	线性探测寻址
	'''
	def linear_probing(self, key):
		start_key = key + 1
		while start_key != key:
			if start_key == self._size:
				start_key = 0
			#  0 == Fasle return True; so replace with 'is False'
			if self._table[start_key] is None or self._table[start_key] is False:
				return start_key
			else:
				start_key += 1
		return

	def print_table(self):
		for k,v in enumerate(self._table):
			print(k,'-->',v)

if __name__ == '__main__':
	h = HashTable(6)
	h.insert(12)
	h.insert(0)
	h.insert(5)
	h.insert(11)
	h.insert(15)
	h.print_table()
	print('delete...')
	h.delete(5)
	h.delete(15)
	h.print_table()
	print('insert...')
	h.insert(17)
	h.insert(23)
	print()
	h.print_table()


