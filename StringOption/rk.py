'''
@Description: RK算法（BF算法的升级版）
@Date: 2020-06-24 11:00:01
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-06-24 11:39:09
'''

def simple_hash(str,start,end):
    '''
    计算子串的哈希值
    每个字符取acs-ii码后求和
    '''
    ret = 0
    for char in str[start:end+1]:
        ret += ord(char)

    return ret


def rk(main, pattern):
    m = len(main)
    n = len(pattern)
    
    # 模式串的哈希值
    hash_pattern = simple_hash(pattern, 0, n-1)
    
    hash_memo = [None] * (m-n+1)

    # 子串的哈希值
    # 方法1
    '''
    for i in range(m-n+1):
        hash_memo[i] = simple_hash(main,i,i+n-1)
    '''
        
    # 方法2
    hash_memo[0] = simple_hash(main, 0, n-1)
    for i in range(1,m-n+1):
        hash_memo[i] = hash_memo[i-1] - simple_hash(main,i-1,i-1) + simple_hash(main,i+n-1,i+n-1)
    
    # 模式串与子串的对比
    for index, val in enumerate(hash_memo):
        if val == hash_pattern:
            if pattern == main[index:index+n]:
                return index

    return -1
    

if __name__ == '__main__':
    main = 'ABC'
    pattern = 'C'
    r = rk(main, pattern)
    print(r)
