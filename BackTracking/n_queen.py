import numpy as np

def isValid(board, row, col):
	n = len(board)
	# 检测列是否有皇后互相冲突
	for i in range(n):
		if board[i][col] == 1:
			return False

	# 检测右上方是否有皇后互相冲突
	i = row - 1
	j = col + 1
	while i >=0 and j < n:
		if board[i][j] == 1:
			return False
		i -= 1
		j += 1

	# 检测左上方是否有皇后互相冲突
	m = row - 1
	w = col - 1
	while m >= 0 and w >= 0:
		if board[m][w] == 1:
			return False
		m -= 1
		w -= 1

	return True

def backtrack(board, row):

	# 只寻找一种满足条件的即可
	if row == len(board):
		res.append(board.copy())
		return True


	# 寻找所有情况
	'''
	if row == len(board):
		res.append(board.copy())
		return
	'''


	num = len(board[row])
	for i in range(num):
		if not isValid(board, row, i):
			continue

		board[row][i] = 1
		# 找寻所有情况时
		# backtrack(board, row+1)

		# 只寻找一种情况时
		if backtrack(board, row + 1):
			return True

		board[row][i] = 0


n = 8
res = []
board = np.zeros((n,n))
backtrack(board, 0)
print(res)
print(len(res))

