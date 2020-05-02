'''
接雨水问题

[链接地址](https://github.com/wsinbol/fucking-algorithm/blob/master/%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E7%B3%BB%E5%88%97/%E6%8E%A5%E9%9B%A8%E6%B0%B4.md)

water[i] = min(
           # 左边最高的柱子
           max(height[0..i]),  
           # 右边最高的柱子
           max(height[i..end]) 
        ) - height[i]
'''


# 第一版
# 暴力法
'''
def get_rain(rains):

	num = len(rains)
	res = 0

	for i in range(num):
		max_left = 0
		max_right = 0

		for j in range(i,num):
			max_right = max(max_right, rains[j])

		for j in range(0,i):
			max_left = max(max_left, rains[j])

		# print(i,max_right, max_left, rains[i],end='\t')
		cur = min(max_right, max_left) - rains[i]
		if cur > 0:
			res += cur

	print(res)
'''

# 第二版：备忘录方法
# 之前的暴力解法，不是在每个位置 i 都要计算 r_max 和 l_max 吗？我们直接把结果都缓存下来，通过备忘录方法：降低时间复杂度
# 开两个数组 r_max 和 l_max 充当备忘录，
# l_max[i] 表示位置 i 左边最高的柱子高度，r_max[i] 表示位置 i 右边最高的柱子高度。
# 预先把这两个数组计算好，避免重复计算：

'''
def get_rains(rains):
	num = len(rains)
	res = 0

	left_max = {}
	right_max = {}

	left_max[0] = rains[0]
	right_max[num-1] = rains[num - 1]

	for i in range(1,num):
		left_max[i] = max(rains[i], left_max[i - 1])

	for i in range(num-2, 0-1,-1):
		right_max[i] = max(rains[i], right_max[i + 1])

	for i in range(num):
		cur = min(left_max[i], right_max[i]) - rains[i]
		if cur > 0:
			res += cur

	print(res)
'''

# 双指针方法：时间复杂度O(N),空间复杂度O(1)
# 要重点看

def get_rains(rains):
	num = len(rains)

	left = 0
	right = num - 1

	left_max = rains[0]
	right_max = rains[num -1]

	res = 0

	while left <= right:
		left_max = max(rains[left], left_max)
		right_max = max(rains[right], right_max)

		if left_max < right_max:
			res += left_max - rains[left]
			left += 1
		else:
			res += right_max - rains[right]
			right -= 1

	print(res)


rains = [0,1,0,2,1,0,1,3,2,1,2,1]
get_rains(rains)
