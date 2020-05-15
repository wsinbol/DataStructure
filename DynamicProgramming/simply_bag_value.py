# -*- coding:utf-8 -*-

'''
求可装入背包的物品的最大价值总和
'''

import numpy as np

w = [2,1,3] # 每个物品的重量
v = [4,2,3] # 每个物品的价值
N = 3 # 物品个数
W = 4 # 背包承受的最大重量

# 对于 dp[i][j] 的理解一定要透彻
# dp[i][j] 表示 对于前 i 个物品，当前背包的容量 j，这种情况装的最大价值是

dp = np.zeros((N+1,W+1))

for i in range(1,N+1):
	for j in range(1,W+1):
		# if j - w[i-1] < 0:
		if j < w[i-1]:
			dp[i][j] = dp[i-1][j]
		else:
			dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1])
print(dp)
exit()

# 争哥版

import numpy as np
goods_num = 5 # 物品总个数
goods_weight = [2,2,4,6,3] # 每个物品的重量
goods_value = [3,4,8,9,6] # 对应物品的价值
max_weight = 9 # 背包中最大重量

arr = [-1]*50
states = np.reshape(arr, (5,10))
# print(states)
states[0][0] = 0
if goods_weight[0] <= max_weight:
	states[0][goods_weight[0]] = goods_value[0]

for i in range(1, goods_num):
	for j in range(max_weight + 1):
		if states[i-1][j] > 0:
			states[i][j] = states[i-1][j]

	for j in range(max_weight - goods_weight[i] + 1):
		if states[i-1][j] > 0:
			current_value = states[i-1][j] + goods_value[i]
			if current_value > states[i][j+goods_weight[i]]:
				states[i][j+goods_weight[i]] = current_value

for i in range(max_weight,-1,-1):
	if states[goods_num-1][i] > 0:
		print('最大价值为：',states[goods_num-1][i])
		exit()
# print(states)



