'''
二叉搜索树
二叉查找树（Binary Search Tree），（又：二叉搜索树，二叉排序树）它或者是一棵空树，或者是具有下列性质的二叉树： 
若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值
'''

'''
void BST(TreeNode root, int target) {
	if (root.val == target)
		// 找到目标，做点什么
	if (root.val < target) 
		BST(root.right, target);
	if (root.val > target)
		BST(root.left, target);
}
'''

class Node:
	def __init__(self,data=None):
		self.data = data
		self._left = None
		self._right = None

class BST:
	def __init__(self):
		self._root = None

	def set_root(self, data):
		self._root = Node(data)

	# 遍历方式插入
	def insert_into_bst_by_traverse(self,val):
		if not self._root:
			self._root = Node(val)
			return

		parent = None
		cur = self._root
		while cur:
			parent = cur
			cur = cur._left if cur.data > val else cur._right

		new_node = Node(val)
		if parent.data > val:
			parent._left = new_node
		else:
			parent._right = new_node


	# 递归方式插入新结点
	def insert_into_bst(self, target_node, val):

		# 放在这里有些不妥
		# 因为 递归调用时每次都会产生 new_node 节点
		# 并且大多数都是无用的
		# new_node = Node(val)
		# print('test:',new_node,val)

		if self._root == None:
			new_node = Node(val)
			self._root = new_node

		if target_node == None:
			new_node = Node(val)
			return new_node

		if target_node.data < val:
			target_node._right = self.insert_into_bst(target_node._right, val)
		if target_node.data > val:
			target_node._left =self.insert_into_bst(target_node._left, val)
		return target_node

	def get_min_node(self, target_node):
		while target_node._left != None:
			target_node._left = target_node
		return target_node

	def delete_node(self, target_node, val):

		if target_node.data == val:
			'''
			3种删除情况
			#1 要删除的节点是末端节点，两个子节点都为空，可以直接删除
			#2 要删除的节点只有一个非空节点，则让其孩子接替自己的位置
			#3 要删除的节点拥有两个子节点，为了不破坏BST的性质，必须找到要删除节点的左子树中值最大的，或者右子书中值最小的
			'''

			#1
			if target_node._left == None and target_node._right == None:
				target_node = None
			#3 
			elif target_node._left != None and target_node._right != None:
				# 寻找右子树中值最小的
				min_node = self.get_min_node(target_node._right)
				# 将右子树的最小值替换给要删除的节点
				target_node.data = min_node.data
				# 将右子树的最小值删除
				target_node._right = self.delete_node(target_node._right, min_node.data)
			#2
			else:
				return target_node._left if target_node._left != None else target_node._right

		elif target_node.data < val:
			target_node._right = self.delete_node(target_node._right, val)
		elif target_node.data > val:
			target_node._left = self.delete_node(target_node._left, val)
		return target_node



	# 弃用
	def insert_node_to_left(self, target_node, data):
		new_node = Node(data)
		target_node._left = new_node
	# 弃用
	def insert_node_to_right(self, target_node, data):
		new_node = Node(data)
		target_node._right = new_node

	def traverse(self,tree_node):
		if tree_node:
			print(tree_node.data)
			# print('left')
			self.traverse(tree_node._left)
			# print('right')
			self.traverse(tree_node._right)

	def is_in_bst(self, tree_node, val):
		if tree_node:
			if tree_node.data == val:
				return tree_node
			else:
				# 此种方式较为低效，可以利用BST的性质进行查找
				# return self.is_in_bst(tree_node._left, val) or self.is_in_bst(tree_node._right, val)
				if val < tree_node.data:
					return self.is_in_bst(tree_node._left, val)
				else:
					return self.is_in_bst(tree_node._right, val)
		else:
			return -1

	def plus_one(self,tree_node):
		if tree_node == None:
			return

		tree_node.data += 1
		self.plus_one(tree_node._left)
		self.plus_one(tree_node._right)

if __name__ == '__main__':
	bst = BST()
	bst.insert_into_bst_by_traverse(1)
	bst.insert_into_bst_by_traverse(2)
	bst.insert_into_bst_by_traverse(0)
	bst.traverse(bst._root)
	exit()
	# bst.set_root(1)
	# bst.insert_node_to_left(bst._root,2)
	# bst.insert_node_to_right(bst._root,3)

	bst.insert_into_bst(bst._root, 2)
	# print(bst._root.data)
	bst.insert_into_bst(bst._root, 1)
	bst.insert_into_bst(bst._root, 3)
	bst.insert_into_bst(bst._root, 4)
	bst.insert_into_bst(bst._root, 0)
	bst.insert_into_bst(bst._root, 1.5)
	print('origin data:')
	bst.traverse(bst._root)
	print('delete node:')
	bst.delete_node(bst._root, 2)
	bst.traverse(bst._root)

	bst.plus_one(bst._root)
	print('after plus one:')
	bst.traverse(bst._root)
	print('is_in_bst:')
	find = bst.is_in_bst(bst._root, 5)
	print(find)



