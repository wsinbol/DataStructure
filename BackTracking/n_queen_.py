
def isValid(queenPos, rowIndex):
	if len(set(queenPos[:rowIndex+1])) != len(queenPos[:rowIndex+1]):
		return False

	for i in range(rowIndex):
		if abs(queenPos[i] - queenPos[rowIndex]) == int(rowIndex - i):
			return False
	return True

def backtrack(queenPos, rowIndex, num):

	if rowIndex == num:
		# print(queenPos)
		res.append(queenPos.copy())
		return
	# print(rowIndex)
	for col in range(num):
		queenPos[rowIndex] = col
		if isValid(queenPos, rowIndex):
			backtrack(queenPos, rowIndex+1, num)

def printSolution(columnPosition, n):
	for row in range(n):
		line = ""
		for column in range(n):
			if columnPosition[row] == column:
				line += "Q\t"
			else:
				line += ".\t"
		print(line, "\n")
	print('\n')

res = []
backtrack([-1] * 8, 0, 8)
print(res[0])
print(len(res))

printSolution(res[0], 8)

