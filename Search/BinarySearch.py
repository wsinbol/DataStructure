'''
@Description: 二分查找算法
@Date: 2019-07-29 16:07:55
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-06-13 16:39:09
'''
# -*- coding:utf-8 -*-
# 

'''
二分查找算法：
    基于有序数据集合的查找算法
    底层必须依赖数据结构
    对于较小规模的数据查找，推荐使用直接遍历的方式
    比较适合处理静态数据（无频繁的数据插入、删除操作）

易错点：
    1. 最外层 while 的循环退出条件；同时注意和各排序算法的临界条件的异同（如快速排序）
    2. mid取值：low和hight很大时有可能溢出（Python中是不会存在溢出情况的）
'''


'''
总结：
初始化的 high 的赋值是 len(arr)-1，而不是 len(arr)；
前者相当于两端都是闭区间 [left, right]；后者相当于左闭右开的区间 [left, right)
'''

# while 是 小于等于 的情况：

def BinarySearch(arr, value):
    low = 0
    high = len(arr) -1 # 注意

    # while 的终止是 low > high 时
    while low <= high: # 注意
        # mid = int((low + high) / 2)
        mid = low + int((high - low) / 2)
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            high = mid - 1
        else:
            low = mid + 1

    return -1

# while 是 小于 的情况：

def BinarySearch(arr, value):
    low = 0
    high = len(arr) - 1 # 注意

    # while 的终止是 low == high 时
    while low < high: # 注意
        mid = low + int((high - low)/2)
        
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            high = mid - 1
        elif arr[mid] < value:
            low = mid + 1
        else:
            print('Something Error...')
            break
    
    # 就是因为 while 的条件没有等于号，导致在 while 内部无法处理 low == high 的情况，故需要单独打个补丁
    return low if arr[low] == value else -1

def BinarySearch(arr, value):
    low = 0
    high = len(arr)

    while low < high:
        mid = low + int( (high - low) / 2)
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            high = mid
        elif arr[mid] < value:
            low = mid + 1
            
    return low

'''
总结：
对于 high = len(arr)，则 while 必须是 low < high,不能是 low <= high
对于 high = len(arr)-1，则 while 可以是 low < high, 也可以是 low <= high
'''


if __name__ == '__main__':
    arr = [1,3,4,5,7,8]
    print(BinarySearch(arr, 9))