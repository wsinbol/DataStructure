
'''
烧饼排序：
假设盘子上有 n 块面积大小不一的烧饼，你如何用一把锅铲进行若干次翻转，让这些烧饼的大小有序（小的在上，大的在下）？

算法核心：
1. 找到 N 个饼中最大的饼
2. 把最大的饼移到最底层
3. 递归调用 pancake_sort(n-1)

说明：该问题涉及多个解哦，要想到如何寻找最优解情况
'''
from collections import defaultdict
def pancake_sort(cakes, n):
	if n == 1:
		return

	max_cake = 0
	max_cake_index = 0
	for i in range(n):
		if cakes[i] > max_cake:
			max_cake = cakes[i]
			max_cake_index = i

	# 第一次翻转，将最大的饼翻到最上面，即索引0的位置
	reverse(cakes, 0, max_cake_index)
	res[n].append(max_cake_index + 1)
	# print('1',cakes)
	# res.append(max_cake_index + 1)
	# 第二次翻转, 将最大的饼翻到最下面，即索引为 len(cakes)-1
	reverse(cakes, 0, n-1)
	# print('2',cakes)
	# res.append(n)
	res[n].append(n)

	pancake_sort(cakes, n-1)

def reverse(cakes, i, j):
	while i < j:
		cakes[i],cakes[j] = cakes[j],cakes[i]
		i += 1
		j -= 1


if __name__ == '__main__':
	cakes = [3,2,4,1]
	res = defaultdict(list)
	pancake_sort(cakes,len(cakes))
	print('操作一次翻转的烧饼数量',res)
	print('最终烧饼序列',cakes)