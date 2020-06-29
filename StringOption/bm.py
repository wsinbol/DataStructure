'''
@Description: bm字符串匹配算法

算法核心：
结合 坏字符规则 和 好后缀规则 进行滑动
匹配过程中，模式串是从后向前遍历。
针对主串而言：
把成功匹配的字符串称为好后缀
把遇到的第一个不匹配的字符称为坏字符
1.坏字符规则后移幅度：将当前坏字符在模式串对应的字符下标 - 坏字符在模式串中匹配的下标（不存在时值为-1）
但是，坏字符会存在负数的情况，所以需要辅助 好后缀
2.好后缀规则后移幅度：在模式串中寻找另一个跟好后缀同样的字符串，
如果可以找到就将模式串移动到和主串相匹配的位置；
如果找不到，直接将模式串滑动到主串的好后缀后面；

@Date: 2020-06-24 17:26:52
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-06-29 13:14:29
'''

# 坏字符规则,有bug，会出现死循环的情况

def bm_with_bug(main, pattern):
    m = len(main)
    n = len(pattern)

    i = 0
    while i < m-n:
        j = n - 1
        while j >= 0:
            if main[i+j] != pattern[j]:
                break
            else:
                j -= 1
        # 用for in 结构不好处理
        '''
        for j in range(n-1,0-1,-1):
            if main[i+j] != pattern[j]:
                break
        '''
        
        if j < 0:
            return i    
        
        si = j
        # 从后向前找出其索引
        xi = pattern.rfind(main[i+j])
        # 向后移动，更新i
        i = i + (si - xi)
  
        
        '''
        if pattern.find(main[i+j],-1) < 0:
            i = j + i
        else:
            t = j - pattern.find(main[i+j],-1)
            i = i + t
        '''
        
        print(i,j)
        
    return -1

# bm算法正式版

def bm(main, pattern):
    m = len(main)
    n = len(pattern)
    
    # gs规则
    suffix = [-1] * n
    prefix = [False] * n
    generate_gs(pattern,suffix,prefix)

    i = 0
    while i < m-n:
        j  = n-1
        while j >= 0:
            if main[i+j] != pattern[j]:
                break
            else:
                j -= 1
                
        if j < 0:
            return i
        
        si = j
        # 从后向前找出其索引
        xi = pattern.rfind(main[i+j])
        # 向后移动，更新i
        x = (si - xi)
        
        
        y = 0
        if j != n-1:
            y = move_by_gs(j,n,suffix,prefix)

        i += max(x,y)
        
    return -1
        


# 好后缀规则的预处理

def generate_gs(pattern,suffix,prefix):
    
    n = len(pattern)
    
    for i in range(0,n-1):
        k = 0
        for j in range(i,-1,-1):
            if pattern[j] == pattern[n-1-k]:
                k += 1
                suffix[k] = j
                if j == 0:
                    prefix[k] = True
            else:
                break
            
def move_by_gs(j,n,suffix, prefix):
    '''
    j 坏字符对应的模式串中的字符下标; 
    n 模式串长度
    '''
    
    k = n-1-j # 好后缀的最长长度
    if suffix[k] != -1:
        return j - suffix[k] + 1
    else:
        for r in range(j+2,n):
            if prefix[n-r]:
                return r
        return m

if __name__ == '__main__':
    main = 'dfasdeeeetewtweyyyhtruuueyytewtweyyhtrhrth'
    pattern = 'eyytewtweyy'
    r = bm(main, pattern)
    print(r)
    

    


