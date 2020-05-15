
'''
最长回文子序列

dp数组的运用：

1) 涉及两个字符串/数组时（比如最长公共子序列），dp 数组的含义如下：

在子数组 arr1[0..i] 和子数组 arr2[0..j] 中，我们要求的子序列（最长公共子序列）长度为 dp[i][j]

2) 只涉及一个字符串/数组时（比如本文要讲的最长回文子序列），dp 数组的含义如下：

在子数组 array[i..j] 中，我们要求的子序列（最长回文子序列）的长度为 dp[i][j]
'''

from collections import defaultdict
import numpy as np

def longestPalindromeSubseq(s):

	num = len(s)
	dp = np.zeros((num, num))

	for i in range(num):
		dp[i][i] = 1

	'''
	# 这么写是错误的
	for i in range(0,num-1):
		for j in range(0,i+1):
			if s[i] == s[j]:
				dp[i][j] = dp[i+1][j-1] + 2
			else:
				dp[i][j] = max(dp[i+1][j], dp[i][j-1])
	'''
	
	
	# 反着遍历
	for i in range(num-1, 0-1, -1):
		for j in range(i+1,num):
			if s[i] == s[j]:
				dp[i][j] = dp[i+1][j-1] +2
			else:
				dp[i][j] = max(dp[i][j-1], dp[i+1][j])

	print(dp)
	# 返回 最长回文子串长度，即最右上角位置的值
	return dp[0][num-1]

s = 'abccba'
longestPalindromeSubseq(s)