
'''
洗牌算法，也称为 随机乱置算法


'''
import random
def make_rand(min_num, max_num):
	return random.randint(min_num, max_num)

def shuffle(arr):
	arr_count = len(arr)

	'''
	# 第一种解法
	for i in range(arr_count):
		# 返回从第一个索引到最后一个索引的随机
		rand_num = make_rand(i, arr_count - 1)
		# 交换元素
		arr[i],arr[rand_num] = arr[rand_num],arr[i]
	'''

	# 第二种解法
	for i in range(arr_count-1): # 与第一种解法的区别在这里，因为最后一次计算是make_rand(4,4), 所以可以arr_count - 1
		# 返回从第一个索引到最后一个索引的随机
		rand_num = make_rand(i, arr_count - 1)
		# 交换元素
		arr[i],arr[rand_num] = arr[rand_num],arr[i]

	# 还有另外两种方式，是倒叙遍历，for i in range(arr_count-1,0)
	# 特别说明，下面的方式是错的：
	'''
    for (int i = 0 ; i < n; i++) {
        // 每次都从闭区间 [0, n-1]
        // 中随机选取元素进行交换
        int rand = randInt(0, n - 1);
        swap(arr[i], arr[rand]);
    }
	'''

'''
总结：
分析洗牌算法正确性的准则：产生的结果必须有 n! 种可能，否则就是错误的。
因为一个长度为 n 的数组的全排列就有 n! 种，也就是说打乱结果总共有 n! 种
所以每次都从闭区间[0,n-1]选择会产生 n^n 个结果，而不是 n! 个结果
'''



arr = [1,3,5,6,7]
shuffle(arr)
print(arr)