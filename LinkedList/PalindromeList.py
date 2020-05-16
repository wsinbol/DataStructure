

class Node:
	def __init__(self, data=None):
		self.data = data
		self._next = None

class LinkedList:
	def __init__(self):
		self._head = None

	def push(self, val):
		new_node = Node(val)
		if self._head == None:
			self._head = new_node
		else:
			new_node._next = self._head
			self._head = new_node

	def show(self):
		current = self._head
		while current:
			print(current.data,end='->')
			current = current._next
		print(None)

	def get_middle(self):
		slow,fast = self._head, self._head
		while fast != None and fast._next != None:

			slow = slow._next
			fast = fast._next._next

		print('middle node:',slow.data)

		if fast != None:
			slow = slow._next
		return slow

	def get_reverse_start_node(self):
		slow,fast = self._head, self._head
		while fast != None and fast._next != None:

			slow = slow._next
			fast = fast._next._next

		mid = slow
		# 处理链表长度为奇数时的逆转链表开始节点
		if fast != None:
			slow = slow._next


		# return slow,mid # 最好的返回方式,即返回逆转链表的开始节点，也返回链表的中间节点
		return slow

	def traverse(self, head_node):
		prev = None
		curr = head_node
		nex = head_node

		while curr != None:
			nex = curr._next
			curr._next = prev

			prev = curr
			curr = nex

		return prev

	def is_palindrome(self):
		left = self._head
		right = self.traverse(self.get_reverse_start_node())

		'''
		print('test...')
		while right:
			print(right.data)
			right = right._next
		'''
		
		while right != None:
			if left.data != right.data:
				return False
			left = left._next
			right = right._next

		# left._next = self.traverse(right)
		return True
		

if __name__ == '__main__':
	l = LinkedList()
	l.push(1)
	l.push(2)
	l.push(3)
	l.push(2)
	l.push(1)
	l.show()
	l.get_middle()

	t = LinkedList()
	t.push(1)
	t.push(2)
	t.push(3)
	t.push(1)
	t.show()
	t.get_middle()

	tips = '''
	通过两个例子对比发现，链表长度为奇数时，中间节点完全正确；而链表长度为偶数时，中间节点是靠后的那个节点；
	但是对于反转中间节点后的单链表而言，长度为奇数时还需要将slow节点指向下一个，那么判断条件呢？
	就是 fast != None
	'''
	print(tips)

	print('开始进行判断回文链表：')
	p = LinkedList()
	p.push(1)
	p.push(2)
	p.push(3)
	p.push(2)
	p.push(1)
	print('原来链表：')
	p.show()
	mid = p.get_middle()
	print('[!important] 反转单链表的开始节点：',mid.data)
	r = p.is_palindrome()
	print(r)
	print('当前链表：')
	p.show()

exit()
def palindrome(s,i,j):
	# 防止数组越界，i >= 0 and j < len(s)要写在前面,s[i] == s[j]要写在后面
	while i >= 0 and j < len(s) and s[i] == s[j]:
		i -= 1
		j += 1

	return s[i+1:j]

def all_palindrome(s):

	res = []

	for i in range(len(s)):
		s1 = palindrome(s,i,i)
		s2 = palindrome(s,i,i+1)

		tmp = s1 if len(s1) > len(s2) else s2
		res.append(tmp)

	return res

def longest_palindrome(s):

	res = ''

	for i in range(len(s)):
		s1 = palindrome(s,i,i)
		s2 = palindrome(s,i,i+1)

		tmp = s1 if len(s1) > len(s2) else s2
		res = res if len(res) > len(tmp) else tmp

	return res


def is_palindrome(s):
	left = 0
	right = len(s) - 1

	while left < right:
		if s[left] != s[right]:
			return False
		left += 1
		right -= 1

	return True

s = '1221'
print(longest_palindrome(s))
print(is_palindrome(s))

'''
i = 4
j = 4
print(palindrome(s,i,j))
'''