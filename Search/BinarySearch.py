# -*- coding:utf-8 -*-
# 

'''
二分查找算法：
	基于有序数据集合的查找算法

易错点：
	循环退出条件为low <= high，而不是low < high；同时注意和各排序算法的临界条件
	mid取值：low和hight很大时有可能溢出
'''
def BinarySearch(arr, value):
	low = 0
	high = len(arr) -1

	while low <= high:
		mid = int((low + high) / 2)
		if arr[mid] == value:
			return mid
		elif arr[mid] > value:
			high = mid - 1
		else:
			low = mid + 1

	return -1


if __name__ == '__main__':
	arr = [1,3,4,5,7]
	print(BinarySearch(arr, 6))