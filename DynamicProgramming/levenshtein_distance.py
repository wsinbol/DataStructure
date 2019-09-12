# -*- coding:utf-8 -*-

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
