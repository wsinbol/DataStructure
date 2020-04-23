

'''
无重复字符的最长子串及其长度

'''

'''
left, right = 0, 0

s = 'abcc'
window = {}

res = 0 # 最长长度
while right < len(s):
	c1 = s[right]
	window.setdefault(c1,1)
	right += 1

	while window[c1] > 1:
		c2 = s[left]
		window[c2] -= 1
		left += 1

	res = max(res, right - left)

print(res)
'''

left, right = 0, 0
# s = 'pwwkew'
s = 'abccc'
s = 'bbbabbb'
window = {}
start = 0
res = 0 # 最长长度
while right < len(s):
	c1 = s[right]
	window.setdefault(c1,0)
	window[c1] += 1
	right += 1

	while window[c1] > 1:
		if right - left > res:
			start = left
			# res = right - left
		c2 = s[left]
		window[c2] -= 1
		left += 1
	res = max(res, right - left)

print(res)
print(start)
print(s[start:start+res])


