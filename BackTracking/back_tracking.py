
import sys
sys.path.append("C:\\Users\\symbol_woo\\Desktop\\DataStructure")

import Tree.multi_tree as tree

if __name__ == '__main__':

	my_list = ['A','B','C']
	track = []
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
