

def intervalIntersection(A, B):
	i,j = 0,0
	res = []

	while i < len(A) and j < len(B):
		a1,a2 = A[i][0],A[i][1]
		b1,b2 = B[j][0],B[j][1]

		if b2 >= a1 and a2 >= b1:
			start = max(a1,b1)
			end = min(a2,b2)
			res.append([start, end])

		if b2 < a2:
			j += 1
		else:
			i += 1

	return res

A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
print(intervalIntersection(A, B))