

def palindrome(s,i,j):
	# 防止数组越界，i >= 0 and j < len(s)要写在前面,s[i] == s[j]要写在后面
	while i >= 0 and j < len(s) and s[i] == s[j]:
		i -= 1
		j += 1

	return s[i+1:j]

def all_palindrome(s):

	res = []

	for i in range(len(s)):
		s1 = palindrome(s,i,i)
		s2 = palindrome(s,i,i+1)

		tmp = s1 if len(s1) > len(s2) else s2
		res.append(tmp)

	return res

def longest_palindrome(s):

	res = ''

	for i in range(len(s)):
		s1 = palindrome(s,i,i)
		s2 = palindrome(s,i,i+1)

		tmp = s1 if len(s1) > len(s2) else s2
		res = res if len(res) > len(tmp) else tmp

	return res


def is_palindrome(s):
	left = 0
	right = len(s) - 1

	while left < right:
		if s[left] != s[right]:
			return False
		left += 1
		right -= 1

	return True

s = '1221'
print(longest_palindrome(s))
print(is_palindrome(s))

'''
i = 4
j = 4
print(palindrome(s,i,j))
'''