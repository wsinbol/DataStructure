
# 大顶推
class pqmax:
	def __init__(self):
		self.value = [0]
		self.count = 0

	def insert(self, val):
		self.count += 1
		# 每次新增数据时都将其添加到最后
		self.value.append(val)
		# 将最后的元素执行上浮操作
		self.swim(self.count)

	def del_max(self):
		max_value = self.value[1]
		self.exch(1,self.count)
		self.value = self.value[:self.count]
		self.count -= 1
		self.sink(1)
		return max_value

	def parent(self, k):
		return int(k / 2)

	def left(self, k):
		return int(k * 2)

	def right(self, k):
		return int(k * 2 + 1)

	def exch(self, i, j):
		self.value[i],self.value[j] = self.value[j],self.value[i]

	def less(self, i, j):
		if self.value[i] < self.value[j]:
			return True
		else:
			return False

	# 上浮过程
	def swim(self, k):
		# 两个判断条件
		# 1.k <= 1 时，没必要执行上浮操作
		# 2.新加入的元素比其父节点的值大，没必要执行上浮操作
		while k > 1 and self.less(self.parent(k), k):
			self.exch(self.parent(k), k)
			k = self.parent(k)

	def sink(self, k):
		while k <= self.count:
			# 假设左边节点较大
			older = self.left(k)
			# 和右边节点再比一下
			if self.right(k) <= self.count and older < self.value[self.right(k)]:
				older = self.right(k)
			# 两边的最大值都比当前索引的值小，不需要下沉操作
			if self.less(older, k):
				break
			# 交换节点
			self.exch(k,older)
			# 更新索引
			k = older

	def show(self):
		print(self.count)
		print(self.value)


pq = pqmax()
pq.insert(1)
pq.insert(2)
pq.insert(3)
pq.insert(4)
pq.insert(5)
pq.del_max()
pq.insert(9)
# pq.show()


class Heap(object):
	def __init__(self,value=[],count=0):
		self.data = [0] + value
		# self.data = [0].extend(value)
		# 排除索引为0的元素
		self.count = len(self.data) - 1

	def parent(self, k):
		return int(k / 2)

	def left(self, k):
		return int(k * 2)

	def right(self, k):
		return int(k * 2 + 1)

	def exch(self, i, j):
		self.data[i],self.data[j] = self.data[j],self.data[i]

	def build_heap(self):
		leaf_index = int(self.count/2)
		for i in range(leaf_index, 0, -1):
			self.heapify(i)
			

	def heapify(self,i):
		while True:
			max_pos = i
			if self.left(i) <= self.count and self.data[self.left(i)] > self.data[i]:
				max_pos = self.left(i)
			if self.right(i) <= self.count and self.data[self.right(i)] > self.data[max_pos]:
				max_pos = self.right(i)

			if max_pos == i:
				break

			self.exch(i,max_pos)
			i = max_pos


	def show(self):
		print(self.count)
		print(self.data)

my_list = [1,2,3,4,5,6,7,8]
h = Heap(my_list)
h.build_heap()
h.show()

pq = pqmax()
for i in my_list:
	pq.insert(i)
pq.show()


