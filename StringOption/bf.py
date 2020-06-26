'''
@Description: BF算法(暴力匹配算法，朴素匹配算法)
@Date: 2020-06-24 10:14:02
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-06-24 17:13:27
'''


def bf(main, pattern):
    m = len(main)
    n = len(pattern)

    for i in range(0, m-n+1):
        for j in range(0,n):
            if main[i+j] == pattern[j]:
                if j == n-1:
                    return i
                else:
                    continue
            else:
                break
            
    return -1
                
                
        
if __name__ == "__main__":
    main = '012345'
    pattern = '23'
    r = bf(main,pattern)
    print(r)
    



