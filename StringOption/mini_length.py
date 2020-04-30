

'''
最小覆盖子串
给你一个字符串S，一个字符串T，请在字符串S里面找出：包含T所有字母的最小子串
注意：顺序可以不同
'''
s = 'acbbobdef'
t = 'bc'

left, right = 0,0
start,minLen = 0, float('inf')

need = {}
for item in t:
	need[item] = 1

# 滑动窗口
window = {}
# 滑动窗口中符合条件的字符串个数
match = 0
while right < len(s):
	c1 = s[right]
	if need.get(c1):
		window.setdefault(c1, 1)
		if c1 in need:
			match += 1

	right += 1

	while match == len(t):
		if (right - left) < minLen:
			start = left
			minLen = right - left

		c2 = s[left]
		if need.get(c2):
			window[c2] -= 1
			if window[c2] < need[c2]:
				match -= 1
		left += 1

minStr = s[start:start+minLen] if minLen < float('inf') else ""


print(window, match)
print(minLen)
print(minStr)






