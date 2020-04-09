
'''
def fib(n):
	index_value = [0] * (n+1)
	return helper(n, index_value)


def helper(n, index_value):
		if n == 1 or n == 2:
			return 1

		if index_value[n] != 0:
			return index_value[n]

		index_value[n] = helper(n-1, index_value) + helper(n-2, index_value)
		return index_value[n]


v = fib(6)

print(v)
'''

'''
def fib(n):
	index_val = [0] * (n+1)
	if n == 1 or n == 2:
		return 1
	if index_val[n] != 0:
		return index_val[n]
	else:
		return helper(n,index_val)

def helper(val, index_val):
	index_val[val] = fib(val-1) + fib(val-2)
	return index_val[val]




v = fib(6)
print(v)
'''

'''
def coinChange(coins,amount):
	def dp(n):
		if n == 0:
			return 0
		if n < 0:
			return -1
		res = float('inf')
		for coin in coins:
			subproblem = dp(n-coin)
			# 无解时应该跳过，避免 -1 操作发生
			if subproblem == -1: 
				continue
			res = min(res, 1 + subproblem)
		return res if res != float('INF') else -1
	return dp(amount)

coins = [1,3,5]
amount = 11
print(coinChange(coins,amount))
'''

'''
def coinChange(coins, amount):
	mem = dict()
	def dp(n):
		if n in mem:
			return mem[n]
		if n == 0:
			return 0
		if n < 0:
			return -1
		res = float('inf')
		for coin in coins:
			subproblem = dp(n-coin)
			if subproblem == -1:
				continue
			res = min(res, 1+subproblem)
		mem[n] = res if res != float('INF') else -1
		return mem[n]
	return dp(amount)

coins = [1,3,5]
amount = 11
print(coinChange(coins,amount))
'''

import numpy as np
def coinChange(coins,amount):
	dp = [amount+1] * (amount + 1)
	dp[0] = 0
	for i in range(len(dp)):
		for coin in coins:
			if i - coin < 0:
				continue
			dp[i] = min(dp[i], dp[i - coin] + 1)
	return dp

coins = [1,3,5]
amount = 11
print(coinChange(coins,amount))
