
'''
最大子序和

dp 数组的定义：以 nums[i] 为结尾的「最大子数组和」为 dp[i]
'''

def max_sub_array_sum(nums):

	n = len(nums)
	dp = [0] * n

	dp[0] = nums[0]

	for i in range(1,n):
		# 此步骤可以继续优化，可以看出dp[i] 仅与 dp[i-1] 和 他自己的值有关
		dp[i] = max(dp[i-1]+nums[i], nums[i])

	print(dp)
	return max(dp)


def max_sub_array_sum(nums):

	n = len(nums)

	dp_0 = nums[0]
	res = dp_0

	for i in range(1,n):
		dp_1 = max(dp_0+nums[i], nums[i])
		dp_0 = dp_1

		res = max(res, dp_0)

	return res



nums = [-2, 1, -3, 4,-1,2,1,-5,4]
r = max_sub_array_sum(nums)
print('max value:', r)