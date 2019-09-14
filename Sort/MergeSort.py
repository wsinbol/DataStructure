# -*- coding:utf-8 -*-

def MergeSort(arr):
	SplitMergeSort(arr, 0, len(arr)-1)

def SplitMergeSort(arr, low, high):
	# print(low, high)
	if low < high:
		mid = low + ((high - low) >> 1)
		SplitMergeSort(arr, low, mid)
		SplitMergeSort(arr, mid+1, high)
		print(low, mid, high)
		merge(arr, low, mid, high)

def merge(a, low, mid, high):
	i, j = low, mid + 1
	tmp = []
	while i <= mid and j <= high:
	    if a[i] <= a[j]:
	        tmp.append(a[i])
	        i += 1
	    else:
	        tmp.append(a[j])
	        j += 1
	start = i if i <= mid else j
	end = mid if i <= mid else high
	tmp.extend(a[start:end + 1])
	a[low:high + 1] = tmp


if __name__ == '__main__':
	arr = [2,3,1,5,0]
	MergeSort(arr)
