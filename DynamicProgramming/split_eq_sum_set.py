
'''
分割等和子集

题目要求：

给定一个只包含正整数的非空数组，是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

'''

import numpy as np

def split_eq_sum(nums):

	length = len(nums)
	total = sum(nums)

	if total % 2 == 1:
		return 0.0

	target = int(total / 2)

	dp = np.zeros((length+1, target+1))

	for i in range(length+1):
		dp[i][0] = 1

	
	for i in range(1, length+1):
		for j in range(1, target+1):
			if j < nums[i-1]:
				dp[i][j] = dp[i-1][j]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i-1]])
	

	return dp[length][target]

# 升级版
# 降低空间复杂度

def split_eq_sum_optimization(nums):

	length = len(nums)
	total = sum(nums)

	if total % 2 == 1:
		return 0.0

	target = int(total / 2)

	dp = [False] * (target+1)

	dp[0] = True

	for i in range(1,length+1):
		# for j in range(target+1): # 这么写是错误的
		# j 应该从后往前反向遍历，因为每个物品（或者说数字）只能用一次，以免之前的结果影响其他的结果。
		for j in range(target,0-1,-1):
			if j >= nums[i-1]:
				dp[j] = dp[j] | dp[j-nums[i-1]]

	# print(dp)
	return dp[target]

# 0.0 means False, 1.0 means True
nums = [2,2,3,5]
print(split_eq_sum_optimization(nums))

