
'''
寻找素数
'''

# 第一版
def is_primes_1(num):
	for i in range(2,num+1):
		# 除了该数字本身和1（已被排除在外）外还存在整除因子，则该数字不是素数，返回False
		if num % i == 0 and i != num:
			return False
	return True

# 第二版
'''
举个例子：
12 = 2 × 6
12 = 3 × 4
12 = sqrt(12) × sqrt(12)
12 = 4 × 3
12 = 6 × 2

可以看到，后两个乘积就是前面两个反过来，反转临界点就在 sqrt(n)
所以在 第一版 的基础上，i 只需要遍历到 sqrt(num) 就可以判断出结果了
'''

'''
import math
def is_primes(num):
	border = int(math.sqrt(num)) # 计算出的border要包括在遍历的数据内，所以下面的 range 要+1
	for i in range(2, border+1):
		# 除了该数字本身和1（已被排除在外）外还存在整除因子，则该数字不是素数，返回False
		if num % i == 0 and i != num:
			return False
	return True
'''

# 前两版核心函数
'''
def count_primes(n):
	count = 0
	prime_arr = []
	for i in range(2,n+1):
		if is_primes(i):
			prime_arr.append(i)
			count += 1
	print(count)
	print(prime_arr)
'''

# ----------------------分界线------------------------------
# 第三版
'''
排除法

'''

'''
def count_primes_1(num):
	nums = [True] * num
	

	i = 2
	while i < num:
		j = 2
		while j * i < num:
			# i 作为基准，i 的倍数（所以从 2 开始）不可能是质数
			nums[i * j] = False
			j += 1
		i += 1

	count = 0
	for i,val in enumerate(nums):
		if val == True:
			print(i)
			count += 1

	print(count-2)
'''

# 第四版 - Sieve of Eratosthenes
# 重点体会

def count_primes(num):

	nums = [True] * num
	i = 2
	while i * i <= num:
		j = i * i # 如果j 继续从2开始，则会大量的重复计算过程，尤其是数字较大的情况，
		while j < num:
			nums[j] = False
			j += i # j 不是 +1, 而是 成倍数的i,也当做倍数来理解

		i += 1

	count = 0
	for i,val in enumerate(nums):
		if val == True:
			print(i)
			count += 1
	print('total',count-2)

count_primes(100)

