'''
要求：
从矩阵左上角出发，最终走到右下角，只能向下或者向右移动
求所经过路径的最小和！
'''

import numpy as np

arr = [
	[1,3,5,9],
	[2,1,3,4],
	[5,2,6,7],
	[6,8,4,3]
]

matrix = np.array(arr)
row, col = np.shape(matrix)

sum_arr = np.zeros((4,4))
route = [(0,0)]

# 初始化第一行
sum = 0
for i in range(col):
	sum += arr[0][i]
	sum_arr[0][i] =  sum

# 初始化第一列
sum = 0
for i in range(row):
	sum += arr[i][0]
	sum_arr[i][0] = sum

for i in range(1, col): # 行数据
	for j in range(1, row): # 列数据
		# 如此打印路径会将回退的路径页打印出来！
		if sum_arr[i-1][j] <= sum_arr[i][j-1]:
			# route.append((i-1,j))
			min_index = (i-1,j)
		else:
			# route.append((i,j-1))
			min_index = (i,j-1)

		if min_index in route:
			route = route[0:route.index(min_index)]
		route.append(min_index)

		sum_arr[i][j] = arr[i][j] + min(sum_arr[i-1][j], sum_arr[i][j-1])
route.append((row-1,col-1))
print('最佳路线为：',route)
print(sum_arr)
