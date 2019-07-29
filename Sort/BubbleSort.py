# -*- coding:utf-8 -*-

'''
冒泡排序：
	基于比较的排序算法
	只会操作相邻的两个数据
	不满足大小关系时则互换两个元素位置
	一“趟”排序会让至少一个元素移动到他应该在的位置
'''
def BubbleSort(arr):
	length = len(arr)
	if length <= 1:
		return
	for i in range(length):
		is_swap = False
		for j in range(length- i - 1):
			if arr[j+1] < arr[j]:
				arr[j+1], arr[j] = arr[j], arr[j+1]
				is_swap = True
		# 此趟未发生数据交换，则表示整个数据已经有序，可以提前退出
		if not is_swap:
			break

	# arr为list类型，是可变对象，所以不需要返回值；这样写更简洁
	# return arr


if __name__ == '__main__':
	arr = [1,3,0,4]
	BubbleSort(arr)
	print(arr)
