'''
要求：算出一共有几个和为 k 的子数组

前缀和
pre_sum[i]就是nums[0]到nums[i-1]的和
则 nums[i]到nums[j]的和即为：pre_sum[j+1] - pre_sum[i]

ps:
这个题有点问题
'''


def sub_array_sum(nums, k):
	n = len(nums)
	sum_n = [0]

	for i in range(n):
		sum_n.append(sum_n[i]+nums[i])
	print('the pre_sum:',sum_n)
	total = 0
	for i in range(1,n+1):
		for j in range(i):
			if sum_n[i]-sum_n[j] == k:
				print(i,j)
				total += 1
	print(total)

'''
上面代码的事件复杂度是O(N^2)
所以可以利用字典 在记录前缀和的同时记录该前缀和出现的次数
'''

def sub_array_sum(nums, k):
	n = len(nums)
	pre_sum = {}
	pre_sum[0] = 1

	total = 0
	sum_i = 0
	for i in range(n):
		# 逐步求和
		sum_i += nums[i]
		# 前缀和
		sum_j = sum_i - k
		
		# if sum_j in pre_sum:
		# 	total += pre_sum[sum_j]

		pre_sum.setdefault(sum_i,0)

		# 从左到右依次求的和作key
		if pre_sum[sum_i]:
			pre_sum[sum_i] += pre_sum[sum_i]+1 
		else:
			pre_sum[sum_i] += 1

		# 
		if sum_j in pre_sum:
			total += pre_sum[sum_j]

	print(pre_sum)
	print(total)

num_list = [1,2,2,4,6]
sub_array_sum(num_list, 6)

'''
nums = [1,2,3,4,6]
num_count = len(nums)

pre_sum = [0]

for index,val in enumerate(nums):
	pre_sum.append(pre_sum[index] + val)

print(pre_sum)

def subarraySum(nums, k):
	count = len(nums)
	total = 0
	for i in range(1,count):
		for j in range(0,i):
			if nums[i] - nums[j] == k:
				total += 1


	for i in range(1, count):


	print(total)

subarraySum(pre_sum,6)
'''