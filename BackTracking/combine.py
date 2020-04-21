'''
组合：
输入两个数字 n, k，算法输出 [1..n] 中 k 个数字的所有组合。
组合的顺序无所谓，但是不能包含重复（按照组合的定义，[1,2] 和 [2,1] 也算重复）
'''
def backtrack(n,k,start,track):
	if k == len(track):
		res.append(track[:])
		return

	for i in range(start,n+1):
		track.append(i)
		backtrack(n,k,start+1, track)
		track.remove(i)


if __name__ == "__main__":
	res  = []
	track = []
	backtrack(4,2,1,track)
	print(res)
