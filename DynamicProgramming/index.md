
# 动态规划解题思路

> 本文根据 [labuladong的算法小抄](https://labuladong.gitbook.io/algo/) 整理所得，并根据自己的理解略有调整，欢迎访问原文出处。

## 解题步骤

0. 确定 【状态】 和 【选择】
1. 明析 dp 数组的含义
2. 确定 base case
3. 找出 状态转移关系

## 适用问题

1. 子序列问题：最长递增子序列、最长公共子序列、最长回文子序列
2. 最值问题：最长递增子序列长度、最长公共子序列、最长回文子序列长度

可以发现，dp 问题要求的是最终的一个值，而不是构成这个值的元素。比如求最长递增子序列的长度，而不是哪个最长递增子序列。

## dp数组

1. 一维的 dp 数组
2. 二维的 dp 数组
3. dp 数组的构建 & i,j 的遍历
- 因为dp[i][j] 的状态大多数情况都来自于 dp[i-1][j]、dp[i][j-1]或者dp[i-1][j-1],则 i,j 遍历时要么反正遍历，要么正着遍历（遍历时 i,j 多从 1 开始）

## dp数组的解释&状态转换理解

### 1. 求最长回文子序列长度

dp 数组的定义：在子串 s[i..j] 中，最长回文子序列的长度为 dp[i][j]，我们的最终目标就是就dp[0][数组长度-1]中的最长回文子序列，即二维数组的右上角的数字为最终答案。此时，引入双指针的左右指针，i为左指针，j为右指针，可以发现，当 i == j 时，i 和 j 中只有一个字符且肯定是回文，所以最长回文子序列的长度就是 1。 随着 i 逐渐扩大，j 逐渐减小，当 i > j 时，根本不存在子序列，故全都应该是0。所以在二维数组中的体现就是：左上右下的对角线全是1，对角线以下全是0，对角线以上才是我们要求的值！

状态转换的理解：找状态转移需要归纳思维，说白了就是如何从已知的结果推出未知的部分。欲求的 dp[i][j]， 其转换来源只能是 dp[i][j-1],dp[i+1][j],dp[i+1][j-1]。假设我们已经知道了 dp[i+1][j-1] 的结果（s[i+1..j-1] 中最长回文子序列的长度），如何求出 dp[i][j] 的值呢？

看 s[i] 和 s[j] 的字符！！！

如果它两相等，则 s[i+1...j-1] 中最长回文子序列 +2 就是 s[i...j] 的最长回文子序列！
如果它两不相等，则 s[i]、s[j] 不可能同时出现在 s[i...j] 的最长回文子序列中，则 s[i][j] 的最长回文子序列长度要么来自 s[i+1][j], 要么来自 s[i][j-1]，取二者最大值即为 s[i...j] 的最长回文子序列长度。

代码如下：


```
if s[i] == s[j]:
	dp[i][j] = dp[i+1][j-1] + 2
else:
	dp[i][j] = max(dp[i+1][j], dp[i][j-1])

```

状态转移方程已经搞定，那么如何遍历呢？

为了计算 dp[i][j]，则需要保证 dp[i+1][j-1]、dp[i][j-1]、dp[i][j-1] 已经被计算出来！则可以选择 斜着 或者 反着 遍历，推荐 反着 遍历。

```
for(i = n-1; i >=0; i--){
	for(j = i+1, j < n, j++){
		if s[i] == s[j]:
			dp[i][j] = dp[i+1][j-1] + 2
		else:
			dp[i][j] = max(dp[i+1][j], dp[i][j-1])
	}
}
```

### 2.最长公共子序列长度

dp 数组的定义：对于 s1[1..i] 和 s2[1..j]，它们的 LCS 长度是 dp[i][j]，我们的最终目标就是求 dp[i][j]，即二维数组的右下角的数字为最终答案。此时，引入双指针i,j分别遍历 s1、s2。

状态转移方程：状态转移说简单些就是做选择，是求 s1 和 s2 的最长公共子序列 lcs, 那么对于 s1 和 s2 中的每个字符，有什么选择？很简单，两种选择，要么在 lcs 中，要么不在。

【递归解法】 用两个指针 i 和 j 从后往前遍历 s1 和 s2，如果 s1[i]==s2[j]，那么这个字符一定在 lcs 中；否则的话，s1[i] 和 s2[j] 这两个字符至少有一个不在 lcs 中，需要丢弃一个。
对于第一种情况，找到一个 lcs 中的字符，同时将 i j 向前移动一位，并给 lcs 的长度加一；对于后者，则尝试两种情况，取更大的结果。

而【动态规划法】 用两个指针i，j 从前向后 正着 遍历即可，二维数组中从左上角一直计算到右下角即可

```
# s1,s2

for i in range(1,len(s1)+1):
	for j in range(1, len(s2)+1):
		if s1[i-1] == s2[j-1]:
			dp[i][j] = dp[i-1][j-1] + 1
		else:
			dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

### 3.最长递增子序列（Longest Increasing Subsequence，简写 LIS）长度

dp 数组的定义：dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度。

状态转移方程：根据对 dp 数组的定义，当 nums[i] 这个数比前 i-1 个数中最大值 加1，即可以得出 dp[i] 的值。故利用 j 遍历 0...i-1，找出满足条件(nums[i] > nums[j])的最大值后 加1 即可。

欲求 dp[i]，必已知 dp[0...i-1]

```
for i in range(0, len(nums)):
	for j in range(0,i):
		if nums[i] > nums[j]:
			dp[i] = max(dp[j]+1, dp[i])
```

### 4. 0-1 背包问题

dp 数组的定义： dp[i][j] 表示 对于前 i 个物品，当前背包的容量为 j, 此时背包内物品的价值为 dp[i][j]。所以我们最终的目标就是 dp[物品个数][背包容量]

框架：

```
for 状态1 in 状态1的所有取值：
    for 状态2 in 状态2的所有取值：
        for ...
            dp[状态1][状态2][...] = 择优(选择1，选择2...)
```

解释：

状态：【背包的容量】 和 【可供选择的物品】
选择：【装进背包】 或 【不装进背包】

细化：

```
int dp[N+1][W+1]
dp[0][..] = 0
dp[..][0] = 0

for i in [1..N]:
    for w in [1..W]:
        dp[i][w] = max(
            把物品 i 装进背包,
            不把物品 i 装进背包
        )
return dp[N][W]
```

状态转移的逻辑：

重申 dp 数组的定义：dp[i][j] 表示 对于前 i 个物品，当前背包的容量为 j, 此时背包内物品的价值为 dp[i][j]

1. 如果没有把第 i 个物品装入背包，则 dp[i][j] 应该等于 dp[i-1][j],继承之前的结果,背包内的价值无变化,背包内的总量也没有变化

2. 如果把第 i 个物品装入背包，则 dp[i][j] 应该等于 dp[前i-1个物品][前i-1个物品时背包的容量(当前背包容量j - 第 i 个物品的重量)] + 第 i 个物品的价值，即dp[i-1][j-weight[i-1]] + val[i-1]

注意：val[i-1] 表示第 i 个物品的价值

完整代码：

```
# N:物品的个数
# W:背包的容量

for(i=1; i<N;i++)
	for(j=1;j<W;j++)
		if(j - weight[i-1] < 0) # 当前背包容量 - 第 i 个物品的容量 < 0: 说明背包装不下这个物品，所以只能选择不装入背包
			dp[i][j] = dp[i-1][j]
		else:
			dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight[i-1]] + val[i-1])

```

返回 dp[N][W] 即为 最终结果！


### 4. 完全背包问题

总金额： amount
硬币面值：coins

dp 数组的定义：使用前 i 个物品，当背包容量为 j 时，有 dp[i][j] 种方法可以装满背包。

翻译：若只使用 coins 中的前 i 个硬币的面值，若想凑出金额 j，有 dp[i][j] 种凑法

则 base case 有：
dp[0][...] = 0
dp[...][0] = 1 (凑出金额0，啥都不用做就是一种凑法喽)

那么，我们要求的最终目标就是 dp[N][amount]

状态转移的逻辑：

1. 如果不把第 i 个物品装入背包，也就是不使用 coins[i]这个面值的硬币，那么凑出金额为 j 的方法数 dp[i][j] 应该等于 dp[i-1][j],继承之前的结果

2. 如果把第 i 个物品装入背包，即使用 coins[i] 这个面值的硬币，则凑出金额为 j 的方法数 dp[i][j] 应该等于 dp[前i个硬币][前i-1个硬币凑成的金额(当前金额-coins[i]的结果)]

而我们要求的 dp[i][j] 是 共有多少种凑法，所以应该是 装入 和 不装入 背包的方法总和！！！

```
for(i=1,i<=n,i++)
	for(j=1;j<=amount;j++)
		if j - coins[i-1] >= 0：
			dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
		else:
			dp[i][j] = dp[i-1][j]
```

返回 dp[n][amount] 即为最终结果！



### 5. 最大子数组和

```
给定一个整数数组 nums，找到一个具有最大和的连续子数组(子数组最少包含一个元素)，返回其最大和。
```

dp 数组的定义：以 nums[i] 为结尾的「最大子数组和」为 dp[i],注意关键词【结尾】，而不是 nums[0..i] 中的「最大的子数组和」为 dp[i]，着重体会一下两者的区别！在dp数组的定义方面，该题与前面的 #3 如出一辙！

dp 数组定义的分析：

以 “nums[0..i] 中的「最大的子数组和」为 dp[i]” 为例分析：那么位置 i 的数 可以是任意子数组的一部分，要想求出最大值，只能对每一个子数组暴力穷举，而且 i+1 和 i 并不构成状态转移关系，这样就没法使用 dp 数组了！

状态转移的逻辑：

假设我们已经算出了 dp[i-1]，如何推导出 dp[i] 呢？

可以做到，dp[i] 有两种「选择」，要么与前面的相邻子数组连接，形成一个和更大的子数组；要么不与前面的子数组连接，自成一派，自己作为一个子数组。

则：

```
# dp[i-1]+nums[i]：与前面的子数组连接在一起
# nums[i]: 自成一派
# 将二者的最大值赋值给 dp[i]
dp[i] = max(dp[i-1]+nums[i], nums[i])
```

### 6. 四键键盘问题

```
假设你有一个特殊的键盘，键盘上有如下键:

键1: (A): 在屏幕上打印一个’A’。
键2: (Ctrl-A): 选择整个屏幕。
键3: (Ctrl-C): 复制选择到缓冲区。
键4: (Ctrl-V): 在屏幕上已有的内容后面追加打印缓冲区的内容。

现在，你只能按键盘上N次(使用以上四个键)，找出你可以在屏幕上打印的“A”的最大数量
```

状态&选择：

状态：剩余按键的次数`n`，打印的A的个数`a_num`，缓冲区中A的个数`copy`

选择：可操作的4个按键

状态转移方程：

键1：dp(n-1, a_num+1, copy)
键2：dp(n-1, a_num, copy)
键3：dp(n-1, a_num, copy+a_num)
键4：dp(n-1, a_num+copy, copy[这里的copy应该是键3的a_num+copy，即前一个的结果])

压缩优化：

dp(n-1, a_num+1, copy)
解释：按下 A 键，屏幕上加一个字符
同时消耗 1 个操作数

dp(n-1, a_num+copy, copy)
解释：按下 C-V 粘贴，剪切板中的字符加入屏幕
同时消耗 1 个操作数

dp(n-2, a_num, a_num)
解释：全选和复制必然是联合使用的，
剪切板中 A 的数量变为屏幕上 A 的数量
同时消耗 2 个操作数

base case：就是 n=0 时，a_num 即为最终答案

实现代码如下，真TM easy! 细节及优化见文件[print_most_a.py](print_most_a.py)

```
def max_a(N):

	def dp(n, a_num, copy):

		if n <= 0:
			return a_num

		return max(dp(n-1, a_num+1, copy), dp(n-1, a_num+copy, copy), dp(n-2, a_num, a_num))

	return dp(N,0,0)
```

---

上面的解法我们定义了3种【选择】，3种【状态】。
下面我们只定义1种【状态】，【选择】是不能再压缩了！

状态：剩余的敲击次数`n`

这个算法基于这样一个事实，最优按键序列一定只有两种情况：

要么一直按 A：A,A,...A（当 N 比较小时）;

要么是这么一个形式：A,A,...C-A,C-C,C-V,C-V,...C-V（当 N 比较大时）;

> 因为字符数量少（N 比较小）时，C-A C-C C-V 这一套操作的代价相对比较高，可能不如一个个按 A；而当 N 比较大时，后期 C-V 的收获肯定很大。这种情况下整个操作序列大致是：开头连按几个 A，然后 C-A C-C 组合再接若干 C-V，然后再 C-A C-C 接着若干 C-V，循环下去。

换句话说，最后一次按键要么是 A 要么是 C-V。明确了这一点，可以通过这两种情况来设计算法。所以，我们定义：

dp[i] 表示 i 次操作后最多能显示多少个 A

```
dp = [None] * (N+1)
for(i = 0; i<= N; i++){
	dp[i] = max(
		这次按 A 键,
		这次按 C-V 键
	)
}
```

对于 `这次按A键`，则

dp[i] = dp[i-1] + 1;

对于 `这次按 C-V 键`，则需要考虑是在哪里 C-A,C-C的，然后我们用变量 `j` 作为若干个 C-V 的起点，那么 j 之前的两个操作就是C-A,C-V:

dp[i] = dp[j-2] * 连续粘贴的次数

```
dp[j-2] * (i-j+1)
```

完整版见 [print_most_a.py](print_most_a.py)

