# -*- coding:utf-8 -*-

def QuickSort(arr, left, right): 

	if left > right:
		return 

	l, r = left, right
	pivot = int((l+r)/2)
	pivotValue = arr[pivot]

	while l < r:
		# while句中不添加 l < r条件，会出现 l > r 情况，与上面的while冲突！
		while arr[l] < pivotValue and l < r:
			l += 1
			print(l,r,arr)
		arr[pivot] = arr[l]
		pivot = l

		while arr[r] > pivotValue and l < r:
			r -= 1
			print(l,r,arr)
		arr[pivot] = arr[r]
		pivot = r

	arr[pivot] = pivotValue
	# 不需要再对pivot位进行操作
	QuickSort(arr, left, pivot-1)
	QuickSort(arr,pivot+1, right)

if __name__ == '__main__':
	arr = [3,1,4,2,5,0]
	QuickSort(arr,0,len(arr)-1)
	print(arr)



