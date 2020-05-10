
'''
最长递增子序列

题目：给定一个无序的整数数组，找到其中最长上升子序列的长度


'''

# 解法1：动态规划法
# 因为题目要求返回最长子序列的长度，所以 dp[i] 的值表示当前 i 的子序列最长长度

from collections import defaultdict
nums = [10,9,2,5,3,7,101,18]

dp = [1]*len(nums) # 初始化
res = defaultdict(list)


for i in range(1,len(nums)):
	flag = False
	for j in range(i,-1,-1):
		
		if nums[i] > nums[j]:
			flag = True
			num = j if dp[j] + 1 > dp[i] else i
			res[nums[i]].append(nums[num])
			res[nums[i]].append(nums[i])
			dp[i] = max(dp[j] + 1, dp[i])

			# print(nums[i],res)
			index = min(res[nums[i]])
			if index in res:
				res[nums[i]].extend(res[index])
				res[nums[i]] = list(set(res[nums[i]]))
			if flag:
				break

print(res)
print(dp)

