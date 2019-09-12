# -*- coding:utf-8 -*-

'''
硬币找零问题：
我们有 3 种不同的硬币，1 元、3 元、5 元，我们要支付9元，最少需要几个硬币
'''

import numpy as np

'''
money = [1,3,5]
total = 9

states = np.zeros((total, total+1))
# states[次数][金额]
for i in money:
	states[0][i] = 1

for i in range(1,total):
	for j in range(total+1):
		if states[i-1][j]:
			if j + 1 <= total:
				states[i][j+1] = 1
			if j + 3 <= total:
				states[i][j+3] = 1
			if j + 5 <= total:
				states[i][j+5] = 1

			if states[i][total]:
				print(states)
				print(i+1)
				exit()
'''

def coins_change(money, total):
	states = np.zeros((total+1, total+1))

	for i in money:
		states[0][i] = 1
	for i in range(1, total+1):
		for j in range(total+1):
			if states[i-1][j]:
				for value in money:
					if j+value <= total:
						states[i][j+value] = 1

			if states[i][total] == 1:
				return i+1

money = [1,3,5]
total = 9
print('最少需要硬币：',coins_change(money, total))





