'''
@Description: KMP字符串查找算法
@Date: 2020-06-27 18:43:36
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-06-28 20:42:29
'''

# 争哥版
# 对于next数组值的理解是通过下标的形式 来计算的

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
    print(nxt)
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

# 知乎版
# https://www.zhihu.com/question/21923021 
# 作者 海纳版
# 对于next数组值的理解是通过 前缀子串与后缀子串能匹配的最长长度 来计算的

def getNexts(pattern):
    n = len(pattern)
    nxt = [-1] * n

    i = 0
    j = -1

    while i < n-1:
        if j == -1 or pattern[i] == pattern[j]:
            i += 1
            j += 1
            nxt[i] = j
        else:
            j = nxt[j]
        
    print(nxt)
    return nxt

def kmp_from_zhihu(main, pattern):
    m = len(main)
    n = len(pattern)

    i,j = 0,0
    nxt = getNexts(pattern)

    while i < m and j < n:
        if main[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = nxt[j]
            
    if j == n:
        return i - j
    else:
        return -1


# 知乎版
# https://www.zhihu.com/question/21923021
# 作者 灵茶山艾府



if __name__ == '__main__':
    main = 'aabbbbaaabbababbabbbabaaabb'
    pattern = 'abbabbbabaa'
    r = kmp_from_zhihu(main,pattern)
    print(r)
    
    q = kmp(main,pattern)
    print(q)
    
    '''
    s = 'ababacd'
    s = 'abababca'
    print('length:')
    getNexts(s)
    print('index')
    get_next(s)
    '''
    

        
