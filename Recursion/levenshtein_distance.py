# -*- coding:utf-8 -*-

'''
递归&回溯求莱文斯坦距离
'''

stra = 'a'
strb = 'ca'
result = 999

def distance(i,j,edit_num):
	global result
	if i == len(stra) or j == len(strb):
		if i < len(stra):
			edit_num += len(stra) - i
		if j < len(strb):
			edit_num += len(strb) - j
		if edit_num < result:
			result = edit_num
		return

	if stra[i] == strb[j]:
		distance(i+1, j+1, edit_num)
	else:
		distance(i+1, j, edit_num+1)
		distance(i, j+1, edit_num+1)
		distance(i+1, j+1, edit_num+1)

distance(0,0,0)
print(result)








