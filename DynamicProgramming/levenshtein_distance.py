# -*- coding:utf-8 -*-

# 递归解法

'''
解决两个字符串的动态规划问题，一般都是用两个指针 i,j 分别指向两个字符串的最后，然后一步步往前走，缩小问题的规模。
'''

'''
dp(i, j)的定义：返回 s1[0..i] 和 s2[0..j] 的最小编辑距离

'''

def min_distance(s1, s2):
	def dp(i,j):
		if i == -1:
			return j + 1
		if j == -1:
			return i + 1

		if s1[i] == s2[j]:
			return dp(i-1, j-1)
		else:
						# 插入情况     # 删除情况      # 替换情况  # 这个需要明确操作对象是哪个？
			return min(dp(i,j-1) + 1, dp(i-1, j) + 1, dp(i-1,j-1) + 1)

	return dp(len(s1)-1, len(s2)-1)

# 上面方法存在重叠子问题，可以用备忘录或DP table 进行优化
# 对于重叠子问题，优化方法无非是备忘录或者 DP table
# 
# 备忘录优化

def min_distance(s1, s2):
	memo = dict()
	def dp(i,j):
		if (i,j) in memo:
			return memo[(i,j)]

		if i == -1:
			return j + 1
		if j == -1:
			return i + 1


		if s1[i] == s2[j]:
			memo[(i,j)] =  dp(i-1, j-1)
		else:
			memo[(i,j)] =  min(dp(i,j-1) + 1, dp(i-1, j) + 1, dp(i-1,j-1) + 1)
		return memo[(i,j)]

	return dp(len(s1)-1, len(s2)-1)

# DP table 优化
# DP table 是自底向上求解，递归解法是自顶向下求解

import numpy as np
def min_distance(s1, s2):
	m = len(s1)
	n = len(s2)
	
	dp = np.zeros((m+1,n+1))
 
	for i in range(1,m+1):
		dp[i][0] = i
  
	for j in range(1,n+1):
		dp[0][j] = j
  
	for i in range(1,m+1):
		for j in range(1,n+1):
			if s1[i-1] == s2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+1)
 
	print('dp table is:\n',dp)
	return dp[m][n]

def min_distance(s1, s2):
	m = len(s1)
	n = len(s2)
	
	dp = np.zeros((m+1,n+1))
	op = np.zeros((m+1,n+1))
 
	for i in range(1,m+1):
		dp[i][0] = i
  
	for j in range(1,n+1):
		dp[0][j] = j
  
	for i in range(1,m+1):
		for j in range(1,n+1):
			if s1[i-1] == s2[j-1]:
				dp[i][j] = dp[i-1][j-1]
				op[i][j] = 0
			else:
				arr = [dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+1]
				# 0-插入，1-删除，2-替换
				opt_choice = [1,2,3]
				index = arr.index(int(min(arr)))
				opt = opt_choice[index]
				dp[i][j] = arr[index]
				op[i][j] = opt
    
 
	print('dp table is:\n',op)
	return dp[m][n]


s1 = 'mt'
s2 = 'ma'
r = min_distance(s1, s2)
print('the minimum value is: ',r)
exit()
'''
动态规划求莱文斯坦距离
求解思路：
将字符串a按列算，字符串b按行算，如下结构：
  m t a c n u
m
i
t
c
m
u
莱文斯坦距离衡量的是字符串的差异化程度
'''

# 争哥版

import numpy as np

def levenshtein_distance(str_a, str_b):
	# str_a的长度是列的大小
	# str_b的长度是行的大小
	# 所以定义states矩阵时要写成(len_b, len_a)
	# 同理，在返回最终结果时也是一样的！
	len_a = len(str_a) 
	len_b = len(str_b) 
	states = np.zeros((len_b, len_a))

	for j in range(len_a):
		if j == 0 and str_b[0] == str_a[j]:
			states[0][0] = 0
		else:
			states[0][j] = states[0][j-1] + 1

	for i in range(len_b):
		if i == 0 and str_a[0] == str_b[i]:
			states[i][0] = 0
		else:
			states[i][0] = states[i-1][0] + 1

	for i in range(1, len_b):
		for j in range(1, len_a):
			if str_b[i] == str_a[j]:
				states[i][j] = min(states[i-1][j-1], states[i-1][j] + 1, states[i][j-1]+1)
			else:
				states[i][j] = min(states[i-1][j-1]+1, states[i-1][j] + 1, states[i][j-1]+1)

	print(states[len_b-1][len_a-1])


str_a = 'mtacnu'
str_b = 'mitcm'
levenshtein_distance(str_a, str_b)
exit()



len_a = len(str_a)
len_b = len(str_b)

states = np.zeros((len_b, len_a))

# 处理第一行，遍历字符串a
for j in range(len_a):
	if str_a[j] == str_b[0] and j == 0:
		states[0][0] = 0
	else:
		states[0][j] = states[0][j-1] + 1

# 处理第一列，遍历字符串b
for i in range(len_b):
	if str_b[i] == str_a[0] and i == 0:
		states[i][0] = 0
	else:
		states[i][0] = states[i-1][0] + 1



# 从第二行，第二列开始处理
 
for i in range(1, len_b):
	for j in range(1, len_a):
		if str_a[j] == str_b[i]:
			# 状态转换方程
			# 从操作层面来理解states[i-1][j]和states[i][j-1]为什么需要+1？
			# 如果a[i]和b[j]不相等,可以删除a[i]，然后递归考察a[i+1]和b[i],则操作+1
			# 现在反过来想，a[i]和b[j]相等了，则在a[i-1]和b[j]状态时，势必进行了一次操作
			states[i][j] = min(states[i-1][j]+1, states[i][j-1]+1, states[i-1][j-1])
		else:
			states[i][j] = min(states[i-1][j]+1, states[i][j-1]+1, states[i-1][j-1]+1)

print(states)
print(states[len_b-1][len_a-1])
