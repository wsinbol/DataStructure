
# Recursion Tutorial

# 树的递归

## 开篇立意

- Solve tree problem with recursion first.
- passing info downwards -- by arguments
- passing info upwards -- by return value

## 求值类问题 I

### Top-Down solution

从上到下方法最大的特点是在递归调用之前先进行必要的业务处理！也就是先把该节点的作用发挥，后面不需要理会该节点的作用，只需要向上返回值就好了！

从上到下 的方法一般是从上到下进行调用，并携带一定的参数，然后从下到上返回目标值，对于最终结果而言，一般不需要任何辅助数据结构。

```python

[1026. Maximum Difference Between Node and Ancestor](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/) 

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.dfs(root, root.val, root.val)
        
    def dfs(self, node, mmin, mmax):
        if node == None:
            # 1.对于空节点，返回差值
            return mmax - mmin 
        mmax = max(mmax, node.val)
        mmin = min(mmin, node.val)
        left = self.dfs(node.left, mmin, mmax)
        right = self.dfs(node.right, mmin, mmax)
        # 2.对于非空节点（即对于当前节点），返回其左子树、右子树中的最大值
        return max(left, right) 
```

### Down-Top solution

从下到上方法的最大特点是在递归调用之后进行业务处理！也就是先一股脑的跑到叶子节点，然后根据需要返回特定值或者数据结构，并不断向上传递值！

对于 求值 类问题：
从下到上 的方法对于最终的结果而言，需要辅助的数据结构，而且最终的结果也在这个辅助的数据结构中。

```python

[1026. Maximum Difference Between Node and Ancestor](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/) 

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return None
            
            l = dfs(root.left)
            r = dfs(root.right)
            if not l and not r:
                return root.val, root.val
            mx, mn = float('-inf'), float('inf')
            if l:
                mx = max(mx, l[0])
                mn = min(mn, l[1])
            if r:
                mx = max(mx, r[0])
                mn = min(mn, r[1])
                
            self.max = max(self.max, abs(root.val-mn), abs(root.val-mx))
            
            return max(mx, root.val), min(mn, root.val)
        self.max = 0
        dfs(root)
        return self.max
```

### 总结

通过 1026 可以发现：从上到下方法中的参数 与 从下到上方法中 return 的返回值有很大的关联！

## 求值类问题 II

```python

# Top-down solutions

# [1373. Maximum Sum BST in Binary Tree](https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/)

class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        res = {}
        def dfs(node):
            if not node:
                #       isBST,node.val,nodeSize,currentMin,currentMax
                return (True, 0, 0, float('inf'),float('-inf'))
            
            isLeftBST,left,left_size,left_min,left_max = dfs(node.left)            
            isRightBST,right,right_size,right_min,right_max = dfs(node.right)
            
            if isLeftBST and isRightBST:
                val = node.val + left + right
                size = 1 + left_size + right_size
                
                if left_max < node.val < right_min:
                    res[node.val] = (True, val, size, min(node.val, left_min), max(node.val, right_max))
                    return (True, val, size, min(node.val, left_min), max(node.val, right_max))
                else:
                    res[node.val] = (False, val, size, min(node.val, left_min), max(node.val, right_max))
                    return (False, val,size, min(node.val, left_min), max(node.val, right_max))
            else:
                val = node.val + left + right
                size = 1 + left_size + right_size
                res[node.val] = (False, val, size, min(node.val, left_min), max(node.val, right_max))
                return (False, val,size, min(node.val, left_min), max(node.val, right_max))
                    
        dfs(root)

```

## 求某个节点 类问题

```python

# Down-up solution(I think)

# [1123. Lowest Common Ancestor of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/)

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return 0,None
            h1, lca1 = dfs(node.left)
            h2, lca2 = dfs(node.right)
            if h1 > h2:
                return h1+1, lca1
            if h1 < h2:
                return h2+1, lca2
            return h1+1, node
        
        return dfs(root)[1]

```

```python

## [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

## [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
        if not root or root == q or root == p:
            return root
        
        left = self.lowestCommonAncestor(root.left, p,q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 对于后序遍历，一般而言当左右子树都为空时，应该return node，但此题中除了匹配出p or q, 其他情况全都返回 None!
        if left == None and right == None:
            return None
        if left != None and right != None:
            return root
        
        return left if left != None else right

# DIY solution

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node, p, q):
            if not node:
                return None

            if node == p or node == q:
                return node

            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            if left == None and right == None:
                return None
            if left != None and right != None:
                return node
            return left if left != None else right
        
        return dfs(root, p, q)

```

## 构造树、删除树类问题

### 解题框架

```python
def helper(node):
    if not node:
        return None

    node.left = helper(node.left)
    node.right = helper(node.right)
    return node

```

从框架中可以看出，不同于上面求值类型的题目，树的构造、删除等问题除递归子节点外，还要将子节点本身返回给父节点以维持树的结构。

```python

[1110. Delete Nodes And Return Forest](https://leetcode.com/problems/delete-nodes-and-return-forest/)

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        def helper(node, parent_exists):
            if not node:
                return None
            
            if node.val in to_delete:
                node.left = helper(node.left, False)
                node.right = helper(node.right, False)
                return None
            else:
                if not parent_exists:
                    res.append(node)
                node.left = helper(node.left, True)
                node.right = helper(node.right, True)
                return node
            
        helper(root, False)
        return res

```

## 最大路径和问题

> For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

对于路径问题，首先要注意的就是不能出现折返的现象！而在二叉树中，可以通过左右子树选择最大值来保证这一规则。所以采用 Bottom-up 的方式计算最大和即可。

```python

# [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        self.sum = float('-inf')
        def dfs(node):
            if not node:
                return 0
                
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.sum = max(self.sum, node.val+left+right)
            return max(left, right)+node.val
        
        dfs(root)
        return self.sum

```

## 无返回值类型的树问题

这种题考查的是对树的操作能力、理解能力！操作起来要远比上面的简单，困难的是想到解决的核心！

> If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.

```python

# [114. Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.res = None
        def pre_order(node):
            if node:
                pre_order(node.right)
                pre_order(node.left)
                print(node.val)
                node.right = self.res
                node.left = None
                self.res = node
            
        pre_order(root)

```

上述代码的递归过程：

```python

    1
   / \
  2   5
 / \   \
3   4   6

preorder(1)
    preorder(5)
        preorder(6)
            6.right is None
            6.left is None
            # 当前层递归调用全部结束，开始执行下面的代码
            6.right = None(self.res 默认 None)
            6.left = None
            self.res = 6
        preorder(5.left)
        5.right = 6
        5.left = None
        self.res = 5
    preorder(2)
        preorder(4)
            4.right is None
            4.left is None
            4.right = 5
            4.left = None
            self.res = 4
        preorder(3)
            3.right is None
            3.left is None
            3.right = 4
            3.left = None
            self.res = 3
        2.right = 3
        2.left = None
        self.res = 2
    1.right = 2
    1.left = NOne
    self.res = 1

What A Amazing Solution!
```