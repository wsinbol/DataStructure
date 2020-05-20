
'''
Longest Common Subsequence

1. dp[i][j] 的含义是：对于 s1[1..i] 和 s2[1..j]，它们的 LCS 长度是 dp[i][j]
2. 定义 base case： 任何一个索引为 -1 时，表示其中一个已经遍历完了，则 lcs 长度不可能再增加了
3. 找状态转移方程：状态转移说简单些就是做选择，比如说这个问题，是求 s1 和 s2 的最长公共子序列，
不妨称这个子序列为 lcs。那么对于 s1 和 s2 中的每个字符，有什么选择？很简单，两种选择，要么在 lcs 中，要么不在。

用两个指针 i 和 j 从后往前遍历 s1 和 s2，如果 s1[i]==s2[j]，那么这个字符一定在 lcs 中；
否则的话，s1[i] 和 s2[j] 这两个字符至少有一个不在 lcs 中，需要丢弃一个。
'''

# 递归解法


def LongestCommonSubsequence(s1, s2):

	def dp(i,j):
		if i == -1 or j == -1:
			return 0

		if s1[i] == s2[j]:
			# 元素存在于 lcs 中，结果 加1，并继续向前找
			return dp(i-1, j-1)+1
		else:
			# 分别报纸一个不动，一个向前异动，结果取能让 lcs 更大的值
			return max(dp(i,j-1), dp(i-1, j))

	return dp(len(s1)-1, len(s2)-1)

# s1 = 'abcde'
# s2 = 'ace'
# r = LongestCommonSubsequence(s1, s2)
# print(r)


def LongestCommonSubsequence(s1, s2):
	m = len(s1)
	n = len(s2)

	dp = [[0] * (n+1) for _ in range(m+1)]

	for i in range(1,m+1):
		for j in range(1, n+1):

			if s1[i-1] == s2[j-1]: # 这个 条件 要注意！！！ 因为 i,j 都是从 1 开始的！

				dp[i][j] = dp[i-1][j-1] + 1
			else:
				dp[i][j] = max(dp[i][j-1], dp[i-1][j])

	print('dp 数组',dp)
	return dp[-1][-1]



s1 = 'abcde'
s2 = 'ace'
r = LongestCommonSubsequence(s1, s2)
print('lcs: ', r)