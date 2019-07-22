# -*- coding:utf-8 -*-
'''
插入排序算法：
	基于比较的排序算法
	将数据分为已排区间和未排区间
	从未排区间中取出首个元素，按倒序方式依次遍历已排区间
	将未排元素置于已排区间的合适位置
'''

def InsertSort(arr):
	length = len(arr)
	for i in range(1,length):# 未排序好的队列
		value = arr[i]
		for j in range(i-1,-1,-1): # 已排序好的队列
			if arr[j] > value:
				arr[j+1] = arr[j]
				arr[j] = value


'''
def InsertSort(arr):
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
	arr = [5,4,7,10,0,2]
	InsertSort(arr)
	print(arr)

