'''
@Description: KMP字符串查找算法
@Date: 2020-06-27 18:43:36
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-06-27 23:43:11
'''

# 更多资料
# https://www.zhihu.com/question/21923021

def get_next(pattern):
    n = len(pattern)
    nxt = [-1] * n
    
    i = 0
    j = -1
    
    for i in range(1,n-1):
        j = nxt[i-1]
        
        while j != -1 and pattern[j+1] != pattern[i]:
            j = nxt[j]

        if pattern[j+1] == pattern[i]:
            j += 1
        
        nxt[i] = j
    return nxt


def kmp(main, pattern):
    m,n = len(main), len(pattern)

    nxt = get_next(pattern)
    
    j = 0
    for i in range(m):
        while j > 0 and main[i] != pattern[j]:
            j = nxt[j-1] + 1

        if main[i] == pattern[j]:
            if j == n-1:
                return i-n+1
            else:
                j += 1
                
    return -1


if __name__ == '__main__':
    main = 'aabbbbaaabbababbabbbabaaabb'
    pattern = 'abbabbbabaa'
    r = kmp(main,pattern)
    print(r)
    

        
