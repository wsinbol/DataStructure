

class Node:
	def __init__(self, val=None, _next=None):
		self.data = val
		self._next = _next

	def add(self, old_node, new_node):
		old_node._next = new_node

class CircularLinkedList:
	def __init__(self,head_node=None):
		self._head = head_node

	def hasCircle(self):
		fast,slow = self._head, self._head
		while fast != None and fast._next != None:
			fast = fast._next._next
			slow = slow._next
			if fast == slow:
				return True

		return False

	# 返回环的起始节点
	def getCircleHead(self):
		fast,slow = self._head, self._head
		while fast != None and fast._next != None:
			fast = fast._next._next
			slow = slow._next
			if fast == slow:
				break

		# 下面代码是关键
		# 当快慢指针相遇时，让其中任一个指针指向头节点，然后让它俩以相同速度前进，
		# 再次相遇时所在的节点位置就是环开始的位置。
		slow = self._head
		while fast != slow:
			fast = fast._next
			slow = slow._next
		return slow

	def deleteCircle(self):
		circle_head = self.getCircleHead()
		circle_head_next = circle_head._next

		while circle_head_next != self.getCircleHead():
			circle_head = circle_head._next
			circle_head_next = circle_head_next._next

		circle_head._next = None

	# 获取链表的中间节点（不能是带环的链表）
	def getMiddleNode(self):
		fast, slow = self._head, self._head
		while fast != None:
			fast = fast._next._next
			slow = slow._next

		return slow.data

	# 获取最后K个结点
	def getLastKNode(self, k):
		fast, slow = self._head, self._head
		while k > 0:
			fast = fast._next
			k -= 1

		while fast != None:
			fast = fast._next
			slow = slow._next

		return slow



	def print(self):
		head = self._head
		while head:
			print(f"{head.data}->", end="")
			head = head._next



	def show(self):
	    current = self._head
	    circle_head = self.getCircleHead()

	    # 
	    # 非头结点环的遍历
	    # part 1 先遍历头结点到环初始结点
	    while current:
	    	print(f"{current.data}->", end="")
	    	if current == circle_head:
	    		break
	    	current = current._next

	    # part 2 遍历整个环
	    current = current._next
	    while current != circle_head:
	    	print(f"{current.data}->", end="")
	    	current = current._next

if __name__ == '__main__':
	A = Node('A')
	B = Node('B')
	C = Node('C')
	D = Node('D')
	N = Node()
	N.add(A,B)
	N.add(B,C)
	N.add(C,D)
	N.add(D,B)

	cll = CircularLinkedList(A)
	print('是否有环？',cll.hasCircle())
	print('环的起始节点',cll.getCircleHead().data)
	# print('链表的中点',cll.getMiddleNode().data)
	print('遍历带环的链表：')
	cll.show()
	print(D._next)
	print()
	print('拆除环：')
	cll.deleteCircle()
	cll.print()
	print(D._next)
	print('获取链表中间节点', cll.getMiddleNode())
	print('获取第Last 2个节点')
	print(cll.getLastKNode(2).data)


	'''
	head = A
	if head:
		print(head.data)
		head = head._next

	while head != A and head != None:
		print(head.data)
		head = head._next
	'''

