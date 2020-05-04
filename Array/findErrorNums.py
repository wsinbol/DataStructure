

'''
给一个长度为 N 的数组 nums，其中本来装着 [1..N] 这 N 个元素，无序。但是现在出现了一些错误，nums 中的一个元素出现了重复，也就同时导致了另一个元素的缺失。请你写一个算法，找到 nums 中的重复元素和缺失元素的值。


总结：

对于这种数组问题，关键点在于元素和索引是成对儿出现的，常用的方法是排序、异或、映射。

映射的思路就是我们刚才的分析，将每个索引和元素映射起来，通过正负号记录某个元素是否被映射。

排序的方法也很好理解，对于这个问题，可以想象如果元素都被从小到大排序，如果发现索引对应的元素如果不相符，就可以找到重复和缺失的元素。

异或运算也是常用的，因为异或性质 a ^ a = 0, a ^ 0 = a，如果将索引和元素同时异或，就可以消除成对儿的索引和元素，留下的就是重复或者缺失的元素。可以看看前文「寻找缺失元素」，介绍过这种方法。
'''

# 修改版
# 暂且将 nums 中的元素变为 [0..N-1]，这样每个元素就和一个数组索引完全对应了，这样方便理解一些

def findErrorNums(nums):
	length = len(nums)
	dup = -1

	for i in range(length):
		index = abs(nums[i])

		if nums[index] < 0:
			dup = nums[i]
		else:
			nums[i] *= -1

	print('dup',dup)

	missing = -1
	for i in range(length):
		if nums[i] > 0:
			missing = i

	print('missing',missing)

# 题目版

def findErrorNumsFormal(nums):
	length = len(nums)
	dup = -1

	for i in range(length):
		index = abs(nums[i]) - 1

		if nums[index] < 0:
			dup = nums[i]
		else:
			nums[i] *= -1

	print('dup',dup)

	missing = -1
	for i in range(length):
		if nums[i] > 0:
			missing = i+1
			break

	print('missing',missing)

nums = [1,1,3,4]
findErrorNumsFormal(nums)