# [486. Predict the Winner](https://leetcode.com/problems/predict-the-winner/description/)
这道题目，我是看了MIT公开课才理解的，首先这道题是考虑两个维度的和累加，和之前
做的不太一样。
首先分析它的子问题，
当len(nums) == 0的时候，返回为0
当len(nums) == 1的时候，返回为nums[0]
当len(nums) == 2的时候，返回max(nums)
```python
def predict(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    return max(predict(nums[1:]) + nums[0],
                        predict(nums[:-1]) + nums[-1])
````

这是没有考虑对手的情况下的状态转移方程
当存在一个对手的情况时候，对手肯定想让我的到的子问题的结果尽可能小，于是就可以将上述答案写成一下形式
```python
def predict(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return max(nums)
    return max(nums[0] + min(predict(nums[2:]), predict(nums[1:-1])),
               nums[-1] + min(predict(nums[1:-1]), predict(nums[0:-2])))
```

比较难得部分就是怎么去写成dp形式
```python
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[0 for _ in xrange(n)] for _ in xrange(n)]
        s = 0
        for i in xrange(n):
            dp[i][i] = nums[i]
            s += nums[i]
        for j in xrange(1, n):
            for i in xrange(j - 1, -1, -1):
                a = dp[i+2][j] if i + 2 < n else 0
                b = dp[i+1][j-1] if i+1 < n and j - 1 >= 0 else 0
                c = dp[i][j-2] if j - 2 >= 0 else 0
                dp[i][j] = max(min(a, b) + nums[i], min(b, c) + nums[j])
        return dp[0][n-1] * 2 >= s
```

