'''
@Description: 
@Date: 2020-04-12 22:51:44
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-06-12 23:56:41
'''


'''
Next Greater Element:
给你一个元素，返回一个等长的数组，对应索引存储着下一个更大的元素，如果没有更大的元素，就存 -1

可以理解成站队高矮问题：
站在队伍末尾的人的视线会被比自己更高的人挡住，
站在队伍开头的人不会有人挡住视线，则应该返回 -1

借助栈的特性，从队伍开头遍历到队伍末尾。

'''

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
	s = Stack() # 借助栈来实现
	for i in my_list[::-1]: # 倒叙遍历
		while not s.is_empty() and i >= s._top.data: # 当前遍历的元素 比 栈顶元素大，即 当前元素比较高，则 栈顶元素可以出栈
			s.pop()
		# 不满足上述条件后，取栈顶元素或者取 -1
		val = -1 if s.is_empty() else s._top.data
		# res.append(val)
		# 因为是倒叙遍历的，所以最终的结果也是从后向前插入的
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

