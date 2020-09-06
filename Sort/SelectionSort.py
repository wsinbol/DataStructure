# -*- coding:utf-8 -*-
'''
选择排序算法：
	基于比较的排序算法
	将数据分为已排区间和未排区间
	从未排区间中遍历出最小值及其索引
	将其和当前遍历的索引位置互换
'''

def SelectionSort(arr):
	length = len(arr)
	for i in range(length):
		minIndex = i
		minValue = arr[i]
		for j in range(i+1,length):
			if arr[j] < minValue:
				minIndex = j
				minValue = arr[minIndex]
		arr[i],arr[minIndex] = arr[minIndex], arr[i]


if __name__ == '__main__':
	arr = [9,3,5,-1,1,4,0]
	SelectionSort(arr)
	print(arr)

