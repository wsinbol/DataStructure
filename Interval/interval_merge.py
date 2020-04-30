
'''
区间合并
'''

def merge(intervals):

	intervals.sort(key = lambda x:x[0])
	# 记录已经合并的区间对
	res = []
	res.append(intervals[0])
	# print(intervals)
	for i in range(1,len(intervals)):
		# 当前区间对
		curr = intervals[i]
		# 获得最后一个区间对，由于已经是排序好的，所以，最后一个区间对的start一定大于前面的区间对
		last = res[-1]
		# 当前区间对的start小于等于已经合并的区间对的最大值，则表明出现交叉区域，可以进一步合并，找出二者中end的最大值并更新
		if curr[0] <= last[1]:
			last[1] = max(curr[1], last[1])
		# 当前区间对的start值大于已经合并的区间对的最大值，则没有出现交叉区域，可以将当前区间对入库
		else:
			res.append(curr)
	return res

intervals = [[2,5],[3,4],[1,3],[4,7]]
print(merge(intervals))