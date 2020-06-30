'''
@Description: 盛最多水的容器
@Date: 2020-06-30 16:33:17
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-06-30 16:41:58
'''

'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
归纳：
1.看到题目要想到分别用 左指针、右指针 向中间遍历完成面积的计算
2.面积的宽度为 j-i,高度取决于两个柱子中最矮的那个
3.i和j的移动过程，遵循谁矮谁移动，谁高谁不动的原则
'''


def maxArea(height) -> int:
    i,j,res = 0,len(height)-1,0

    while i < j:
        if height[i] > height[j]:
            res = max(res, height[j]*(j-i))
            j -= 1
        else:
            res = max(res, height[i]*(j-i))
            i += 1
    return res


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    r = maxArea(height)
    print(r)