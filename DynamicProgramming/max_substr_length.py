# -*- coding:utf-8 -*-

'''
动态规划求最长公共子串长度
求解思路：
将字符串a按列算，字符串b按行算，如下结构：
  m t a c n u
m
i
t
c
m
u
'''

import numpy as np
str_a = 'mtacnuw'
str_b = 'mitcmuw'

len_a = len(str_a)
len_b = len(str_b)

sub_str = []

states = np.zeros((len_a, len_b))

# 处理第一行，遍历字符串a
for j in range(len_a):
	if str_a[j] == str_b[0]:
		
		states[0][j] = 1
	else:
		states[0][j] = states[0][j-1]

# 处理第一列，遍历字符串b
for i in range(len_b):
	if str_b[i] == str_a[0]:
		states[i][0] = 1
	else:
		states[i][0] = states[i-1][0]

if states[0][0]:
	sub_str.append(str_a[0])

# 从第二行，第二列开始处理
for i in range(1, len_b):
	for j in range(1, len_a):
		if str_a[j] == str_b[i]:
			sub_str.append(str_b[i])
			states[i][j] = max(states[i-1][j]+1, states[i][j-1]+1, states[i-1][j-1]+1)
		else:
			states[i][j] = max(states[i-1][j], states[i][j-1], states[i-1][j-1])

print('最长公共子串:',sub_str)
print(states)
print('最长公共子串长度',states[len_a-1][len_b-1])
