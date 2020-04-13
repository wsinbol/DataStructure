
class Node:
	def __init__(self, data=None):
		self.data = data
		self._next = None

class Stack:
	def __init__(self):
		self._top = None

	def push(self, val):
		new_node = Node(val)
		if self._top == None:
			self._top = new_node
		else:
			new_node._next = self._top
			self._top = new_node

	def pop(self):
		if self._top:
			self._top = self._top._next

	def is_empty(self):
		if self._top == None:
			return True
		else:
			return False

	def show(self):
		top = self._top
		while top:
			print(top.data)
			top = top._next

if __name__ == '__main__':
	my_list = [2,1,2,4,3]
	res = []
	s = Stack()
	for i in my_list[::-1]:
		while not s.is_empty() and i >= s._top.data:
			s.pop()
		val = -1 if s.is_empty() else s._top.data
		# res.append(val)
		res.insert(0,val)
		s.push(i)

	print(res)
	exit()
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	s.show()
	for _ in range(10):
		s.pop()
	print('*'*5)
	s.show()

