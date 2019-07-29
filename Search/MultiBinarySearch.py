# -*- coding:utf-8 -*-

'''
二分查找的四种变形：
	查找第一个等于给定值的索引 FindFirstEqTargetBinarySearch
	查找最后一个等于给定值的索引 FindLastEqTargetBinarySearch
	查找第一个大于等于给定值的索引 FindFirstGEqTargetBinarySearch
	查找最后一个小于等于给定值的索引 FindLastLEqTargetBinarySearch
'''

def FindFirstEqTargetBinarySearch(arr, value):
	low = 0
	high = len(arr) - 1

	while low <= high:
		mid = int((low + high) / 2)

		if arr[mid] > value:
			high = mid - 1
		elif arr[mid] < value:
			low = mid + 1
		else:
			# 在所有等于给定值的数据中进行操作且索引值尽可能的小
			if mid == 0 or arr[mid - 1] != value:
				return mid
			else:
				high = mid - 1
	return

def FindLastEqTargetBinarySearch(arr, value):
	low = 0
	high = len(arr) - 1
	while low <= high:
		mid = int((low + high) / 2)

		if arr[mid] > value:
			high = mid - 1
		elif arr[mid] < value:
			low = mid + 1
		else:
			# 在所有等于给定值的数据中进行操作且索引值尽可能的大
			if mid == len(arr) - 1 or arr[mid + 1] != value:
				return mid
			else:
				low = mid + 1

	return 

def FindFirstGEqTargetBinarySearch(arr, value):
	low = 0
	high = len(arr) - 1

	while low <= high:
		mid = int((low + high) / 2)
		if arr[mid] < value:
			low = mid + 1
		else:
			# 在所有大于等于给定值的元素中操作，当找出的mid的前一个小于给定元素，则此mid为最终目标
			if mid == 0 or arr[mid - 1] < value:
				return mid
			else:
				high = mid - 1
	return

def FindLastLEqTargetBinarySearch(arr, value):
	low = 0
	high = len(arr) - 1

	while low <= high:
		mid = int( (low + high) / 2)
		if arr[mid] > value:
			high = mid - 1
		else:
			# 在所有小于等于给定值的元素中操作，当找出的mid的后一个大于给定元素，则此mid为最终目标
			if (mid == len(arr) - 1) or (arr[mid + 1] > value):
				return mid
			else:
				low = mid + 1

	return 


if __name__ == '__main__':
	arr = [1,1,1,1,3,4]
	print(FindFirstEqTargetBinarySearch(arr, 1))
	print(FindLastEqTargetBinarySearch(arr, 1))
	print(FindFirstGEqTargetBinarySearch(arr, 1))
	print(FindLastLEqTargetBinarySearch(arr, 1))

