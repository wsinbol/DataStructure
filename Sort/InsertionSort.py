# -*- coding:utf-8 -*-
'''
插入排序算法：
	基于比较的排序算法
	将数据分为已排区间和未排区间
	从未排区间中取出首个元素，按倒序方式依次遍历已排区间
	将未排元素置于已排区间的合适位置
'''                

def InsertionSort(arr):
	length = len(arr)
	for i in range(1,length):# 未排序好的队列
		value = arr[i]
		for j in range(i-1,-1,-1): # 已排序好的队列
			if arr[j] > value:
				arr[j+1] = arr[j]
				arr[j] = value  # 此时不更新，就不知道应该啥时候更新了
			# 不转移数据时，会将数据覆盖丢失
			# arr[j] = value
		# 最终的j都会是0,所以不可以在这里更新arr[j]的值
		# arr[j] = value



'''
def InsertionSort(arr):
	length = len(arr)
	for i in range(1,length):
		value = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > value:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = value
'''

if __name__ == '__main__':
	arr = [3,5,1,4]
	InsertionSort(arr)
	print(arr)

