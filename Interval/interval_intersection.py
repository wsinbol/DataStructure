'''
@Description: 
@Date: 2020-05-06 23:47:09
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-05-29 20:24:23
'''

'''
区间交集问题

问题描述：快速找出两组区间的交集

'''

def intervalIntersection(A, B):
	i,j = 0,0 # 指针
	res = [] # 保存结果

	while i < len(A) and j < len(B):
		a1,a2 = A[i][0],A[i][1]
		b1,b2 = B[j][0],B[j][1]

		# 两个区间存在交集
		if b2 >= a1 and a2 >= b1:
			# 计算出交集，保存结果
			start = max(a1,b1)
			end = min(a2,b2)
			res.append([start, end])

		# 指针前进
		if b2 < a2:
			j += 1
		else:
			i += 1
	return res

A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
print(intervalIntersection(A, B))
