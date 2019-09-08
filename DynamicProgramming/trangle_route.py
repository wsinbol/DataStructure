# -*- coding:utf-8 -*-

'''
value数据是杨辉三角结构
要求：
从顶层走到最后一层，把移动到最底层所经过的所有数字之和，定义为路径的长度。
求 最短路径长度
'''

value = [[5],[7,8],[2,3,4],[4,9,6,1]]

low_level = 0
high_level = len(value)

final = [[5]]
for i in range(1,len(value)):
	result = []
	for j in range(len(value[i])):
		if j == 0:
			result.append(value[i][j] + final[i-1][j])
		elif j == i:
			result.append(value[i][j] + final[i-1][j-1])
		else:
			result.append(value[i][j] + min(final[i-1][j-1],final[i-1][j]))
	final.append(result)

print(min(final[-1]))


