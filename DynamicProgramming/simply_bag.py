# -*- coding:utf-8 -*-

'''
求可装入背包的物品的最大总和
'''

import numpy as np
goods_num = 5 # 物品总个数
goods_weight = [2,2,4,6,3] # 每个物品的重量
max_weight = 9 # 背包中最大重量

states = np.zeros((5,10))
states[0][0] = 1 # 初始化第0个物品不入背包状态，行表示第i个物品，列表示入背包后的重量，值为标识状态
if goods_weight[0] < max_weight:
	states[0][goods_weight[0]] = 1 # 初始化第0个物品入背包状态

for i in range(1,goods_num): # 从第1个物品开始处理
	for j in range(max_weight+1): # 不把第i个物品放入背包，背包重量与上第i-1次时一致
		if states[i-1][j] == 1: 
			states[i][j] = states[i-1][j] 

	for j in range(max_weight - goods_weight[i] + 1): # 把第i个物品放入背包，背包重量等于上次背包重量＋当前物品重量
		if states[i-1][j] == 1:
			states[i][j+goods_weight[i]] = 1

# print(states)
cols = max_weight
while cols >= 0:
	if states[goods_num-1][cols] == 1:
		print('当前物品最多装：', cols)
		exit()
	cols -= 1
print('None')


