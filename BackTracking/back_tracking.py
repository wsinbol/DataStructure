'''
@Description: 全排列-回溯算法
@Date: 2020-04-17 09:51:51
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-05-31 16:10:30
'''

'''
全排列问题


'''

import sys
sys.path.append("C:\\Users\\symbol_woo\\Desktop\\DataStructure")

import Tree.multi_tree as tree

if __name__ == '__main__':

	my_list = ['A','B','C'] # 选择列表
	track = [] # 路径
	res = []

	

	def backtrace(my_list, track):
		if len(track) == len(my_list):
			# 为啥始终是空呢？但是定值却可以写进去，track却不行
			# 直接打印track也是没有问题的！
			# res.append(track)
			# 下面写是正确的
			res.append(track[:])
			# print(res)
			return
		for item in my_list:
			if item in track:
				continue
			track.append(item)
			backtrace(my_list, track)
			track.remove(item)

	backtrace(my_list, track)
	print(res)
