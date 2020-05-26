
'''
四键键盘问题-打印最多次A

'''

# 原始版

def max_a(N):

	def dp(n, a_num, copy):

		if n <= 0:
			return a_num

		return max(dp(n-1, a_num+1, copy), dp(n-1, a_num+copy, copy), dp(n-2, a_num, a_num))

	return dp(N,0,0)

# 消除重叠子

def max_a(N):
	memo = dict()
	def dp(n, a_num, copy):

		if n <= 0:
			return a_num

		if (n, a_num, copy) in memo:
			return memo[(n,a_num,copy)]

		memo[(n,a_num,copy)] = max(dp(n-1, a_num+1, copy), dp(n-1, a_num+copy, copy), dp(n-2, a_num, a_num))
		return memo[(n,a_num,copy)]

	return dp(N,0,0)


# 高配版

def max_a(N):

	dp = [None] * (N+1)
	dp[0] = 0

	for i in range(1,N+1):
		dp[i] = dp[i-1] + 1 # 按 A
		for j in range(2,i):
			# 全选 & 复制 dp[j-2]，连续粘贴 i - j 次
			# 屏幕上共 dp[j - 2] * (i - j + 1) 个 A
			dp[i] = max(dp[i], dp[j-2] * (i-j+1))

	print(dp)
	return dp[N]

# 上面 `高配版` 的 dp 记录的是 整个N(0-N)的最高次数，空间复杂度为O(N)，而实际中我们只需要数组的最后一个，所以可以继续优化

r = max_a(9)
print(r)