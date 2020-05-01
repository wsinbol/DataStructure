
'''
Koko 每小时最多吃一堆香蕉，如果吃不下的话留到下一小时再吃；
如果吃完了这一堆还有胃口，也只会等到下一小时才会吃下一堆。
在这个条件下，让我们确定 Koko 吃香蕉的最小速度（根/小时）
'''

# 第一版解法


def min_eating_speed_1(piles, hour):
	max_num = max(piles)
	speed = 1
	while speed <= max_num:
		if can_finish(piles, speed, hour):
			return speed

		speed += 1
	return max_num


# 第二版解法

def min_eating_speed_2(piles, hour):

	left, right = 1, max(piles)+1

	while left < right:
		mid = left + int((right - left) / 2)
		if can_finish(piles, mid, hour):
			right = mid
		else:
			left = mid + 1

	return left


# 下面的函数都为辅助函数

def can_finish(piles, speed, hour):
	time = 0
	for pile in piles:
		time += time_of(pile, speed)

	if time < hour:
		return True
	else:
		return False


def time_of(pile, speed):
	need_another_hour = 1 if pile % speed > 0 else 0
	return (pile / speed) +  need_another_hour


piles = [1,3,6,9]
hour = 120
res_1 = min_eating_speed_1(piles, hour)
res_2 = min_eating_speed_2(piles, hour)
print(res_1, res_2)