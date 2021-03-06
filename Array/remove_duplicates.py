
'''
@Description: 去除有序数组的重复元素
@Date: 2020-05-06 23:47:09
@Author: Wong Symbol
LastEditors: Please set LastEditors
LastEditTime: 2020-08-26 23:00:32
'''

'''
去除有序数组的重复元素

思路：

我们知道对于数组来说，在尾部插入、删除元素是比较高效的，时间复杂度是 O(1)，但是如果在中间或者开头插入、删除元素，就会涉及数据的搬移，时间复杂度为 O(N)，效率较低。

所以对于一般处理数组的算法问题，我们要尽可能只对数组尾部的元素进行操作，以避免额外的时间复杂度。

题目：

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用O(1)额外空间的条件下完成。

显然，由于数组已经排序，所以重复的元素一定连在一起，找出它们并不难，但如果毎找到一个重复元素就立即删除它，就是在数组中间进行删除操作，整个时间复杂度是会达到 O(N^2)。而且题目要求我们原地修改，也就是说不能用辅助数组，空间复杂度得是 O(1)。

其实，对于数组相关的算法问题，有一个通用的技巧：要尽量避免在中间删除元素，那我就想先办法把这个元素换到最后去。这样的话，最终待删除的元素都拖在数组尾部，一个一个 pop 掉就行了，每次操作的时间复杂度也就降低到 O(1) 了。

按照这个思路呢，又可以衍生出解决类似需求的通用方式：双指针技巧。具体一点说，应该是快慢指针。

我们让慢指针 slow 走左后面，快指针 fast 走在前面探路，找到一个不重复的元素就告诉 slow 并让 slow 前进一步。这样当 fast 指针遍历完整个数组 nums 后，nums[0..slow] 就是不重复元素，之后的所有元素都是重复元素。

TIPS:

去除单链表的重复元素原理同！

From:

https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

'''

def remove_duplicates(nums):
	length = len(nums)
	slow = 0
	fast = 1
	while fast < length:
		if nums[fast] != nums[slow]:
			slow += 1
			nums[slow] = nums[fast]
		
		fast += 1

	print(nums[:slow+1])

nums = [0,0,1,1,2]
remove_duplicates(nums)