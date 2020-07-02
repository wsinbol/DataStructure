# DataStructure Content

> Language: Python 

> 菜鸡码农的自我救赎之路

## 数组
- 寻找无序数组的错误值
- 去除有序数组的重复元素

## 链表 LinkedList
- [单链表](LinkedList/SinglyLinkedList.py)
    - 删除链表倒数第 n 个结点
- [循环单链表](LinkedList/CircularLinkedList.py)
- [双向链表](LinkedList/DoubleLinkedList.py)
- [双向循环链表](LinkedList/DoubleCircularLinkedList.py)
- [快慢指针链表](LinkedList/DoublePointerLinkedList.py) ***
    - 检测是否有环
    - 寻找环的起点
    - 删除环
    - 获取链表的中间结点（非环链表）
    - 获取最后K个结点
    - 带环链表的遍历

- [回文链表](LinkedList/PalindromeList.py) ***
    - 判断是否为回文链表
- [K个一组反转链表](LinkedList/ReverseKGroup.py) ***
    - 递归式反转
    - 遍历式反转
    - 区间内反转
    - K个结点为一组型反转
- [反转链表](LinkedList/ReverseList.py)
    - 正序访问 VS 倒叙访问

## 栈 Stack
- 链式栈
    - 基于链表实现的栈
    - 双栈构建的队列
- 顺序栈
    - 基于数组实现的栈
- [站队高矮问题](Stack/nextGreaterElement.py)
- [浏览器前进后退功能](Stack/Browser.py)

## 队列
- [顺序队列](Queue/ArrayQueue.py)(尚未实现)
    - 基于数组实现的队列
- [链式队列](Queue/LinkedQueue.py)
    - 基于链表实现的队列
    - 基于队列实现的栈
- [循环队列](Queue/CircularQueue.py) ***
    - 循环队列的特性
- [双端队列](Queue/Deque.py)
    - 双端队列的特性

## 哈希表
- [简易哈希表](HashTable/SimplyHashTable.py) ***
    - 基于开放寻址法-线性探测的散列表
- [链式哈希表](HashTable/LinkedHashTable.py) ***
    - 基于单链表的散列表数据结构

## 树
- [二叉树](Tree/BinaryTree.py)
    - 二叉树的最小高度
    - 二叉树的最大深度
- [二叉搜索树](Tree/binary_search_tree.py) ***
    - 二叉搜索树的框架
    - 二叉搜索树的特性
    - 二叉搜索树的遍历方式插入
    - 二叉搜索树的递归方式插入
- [多叉树](Tree/multi_tree.py)
    - DFS
    - BFS

## Trie
- [Trie树](Trie/trie.py)
    - Trie树的特性

## 图
- [图的表示](Graph/Graph.py)
    - 邻接链表法
    - 邻接矩阵法
- [广度优先搜索BFS](Graph/BFS.py) ***
    - 起点 到 终点 的最短路径问题(具体路径、最少扩散次数)
    - 按层遍历
- [深度优先搜索DFS](Graph/DFS.py) ***
- [迪杰斯特拉算法](Graph/dijkstra.py) ***

## 堆
- [二叉堆](Heap/priority_heap_max.py) ***
    - 大顶堆
    - 二叉堆实现优先级队列


---

## 排序

- 插入排序
- 冒泡排序
- 选择排序
- 快速排序
- 归并排序
- 烧饼排序

## 查找、搜索
- 二分查找
- 变形二分查找
- koko吃香蕉问题

## 递归
- 莱文斯坦距离

## 区间
- 区间插入
- 区间合并
- 区间调度

## 数学
- 质数
- 前缀和

## 随机
- 洗牌算法

## 字符串
- [BF算法](StringOption/bf.py)
    - 暴力匹配算法、朴素匹配算法
- [RK算法](StringOption/rk.py)
    - 在BF算法的基础上借助哈希函数
- [BM算法](StringOption/bm.py) ***
    - 坏字符规则 & 好后缀规则
- [KMP算法](StringOption/kmp.py)
    - 好前缀规则
    - 失效函数（next数组）
    - 部分匹配表 PMT
- [最小覆盖子串](StringOption/mini_length.py)
    - 给你一个字符串S，一个字符串T，请在字符串S里面找出：包含T所有字母的最小子串，顺序可以不同
- 无重复字符的最长子串及其长度
- 接水问题

## 回溯算法
- 回溯算法框架
- 组合问题
- 八皇后问题

## 动态规划
- 动态规划框架
- 0-1背包问题
- 0-1背包问题+价值
- 矩阵路线
- 杨辉三角路线
- 硬币找零
- 莱文斯坦距离
- 最长公共子串长度
- 戳气球问题
- 高楼扔鸡蛋
- 最长公共子串长度
- 最长递增子串长度
- 最长回文子串长度
- 最大子数组和
- [四键按键问题](DynamicProgramming/print_most_a.py)
- [二分数组等和问题](DynamicProgramming/split_eq_sum_set.py)


## 综合
- LRU




