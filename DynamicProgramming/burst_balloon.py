
'''
戳气球问题

有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量


'''

# 回溯算法

def backtrace(nums, score):
	global res

	if len(nums) == 0:
		# res_list.append(score)
		res = max(score, res)
		return res
		
	for i in range(len(nums)):
		tmp = nums[i]
		if i-1 < 0:
			left = 1
		else:
			left = nums[i-1]


		if i+1 > len(nums)-1:
			right = 1
		else:
			right = nums[i+1]

		point = left * nums[i] * right
		del nums[i]
		backtrace(nums, score + point)
		nums.insert(i, tmp)


nums = [3,1,5,8]
score = 0
res = 0
r = backtrace(nums, score)
# 直接输入 r 是不会返回任何值的
print(r)
print(res)


# 动态规划解法 重点理解算法
# 有种双指针的味道
'''
dp[i][j] = x 表示，戳破气球 i 和气球 j 之间（开区间，不包括 i 和 j）的所有气球，可以获得的最高分数为 x
'''

import numpy as np
def burst_balloon(nums):

	n = len(nums)
	points = [1] + nums + [1]
	dp = np.zeros((n+2,n+2))

	for i in range(n,0-1,-1):
		for j in range(i+1, n+1+1):
			for k in range(i+1, j):
				dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + points[i]*points[j]*points[k])

	print(dp)

nums = [3,1,5,8]
burst_balloon(nums)
