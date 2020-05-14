
'''

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

s = 'abccba'
longestPalindromeSubseq(s)