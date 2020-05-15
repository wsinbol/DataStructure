

'''
高楼扔鸡蛋问题

你面前有一栋从 1 到 N 共 N 层的楼，
然后给你 K 个鸡蛋（K 至少为 1）。
现在确定这栋楼存在楼层 0 <= F <= N，在这层楼将鸡蛋扔下去，
鸡蛋恰好没摔碎（高于 F 的楼层都会碎，低于 F 的楼层都不会碎）。
现在问你，最坏情况下，你至少要扔几次鸡蛋，才能确定这个楼层 F 呢？
'''

def drop_egg(egg_num, building_height):

	def dp(k,n):
		# 当鸡蛋数 K 为 1 时，显然只能线性扫描所有楼层
		if k == 1:
			return n
		# 当楼层数 N 等于 0 时，显然不需要扔鸡蛋
		if n == 0:
			return 0
		res = float('INF')

		for i in range(1,n+1):
			                   # 鸡蛋碎了    # 鸡蛋没碎   # 在第i楼扔了一次
			res = min(res, max(dp(k-1, i-1),dp(k,n-i)) + 1)
		return res

	return dp(egg_num, building_height)

egg_num = 3
building_height = 14
r = drop_egg(egg_num, building_height)
print(r)
