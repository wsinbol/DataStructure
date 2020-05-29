'''
@Description: 
@Date: 2020-05-29 16:16:44
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-05-29 17:56:26
'''

'''
区间调度问题:最多多少个区间不重叠

问题描述：给你很多形如 [start, end] 的闭区间，请你设计一个算法，算出这些区间中最多有几个互不相交的区间

现实场景：比如你今天有好几个活动，每个活动都可以用区间 [start, end] 表示开始和结束的时间，请问你今天最多能参加几个活动呢？
显然你一个人不能同时参加两个活动，所以说这个问题就是求这些时间区间的最大不相交子集。

核心算法：贪心算法
1. 从区间集合 intvs 中选择一个区间 x，这个 x 是在当前所有区间中结束最早的（end 最小）
2. 把所有与 x 区间相交的区间从区间集合 intvs 中删除
3. 重复步骤 1 和 2，直到 intvs 为空为止。之前选出的那些 x 就是最大不相交子集
'''


def interval_scheduling(intvs):
    intvs.sort(key=lambda x:x[1])
    # count 为啥从 1 开始？
    count = 1
    x_end = intvs[0][1]

    for intv in intvs:
        start = intv[0]
        if start >= x_end:
            count += 1
            x_end = intv[1]

    print(count)
    return count


intvs = [[3,6],[1,3], [2,4]]
interval_scheduling(intvs)


'''
移除最少的区间数量，使剩余区间互补重叠

其实就是上一个问题的补集啦！
'''

n = interval_scheduling(intvs)

print('number of erasing:',len(intvs) - n)



