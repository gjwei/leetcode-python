class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp,result = [],0
        for i, n in enumerate(nums):
            if i < 2:
                dp.append(n)
            elif i == 2:
                dp.append(n + dp[i - 2])
            else:
                dp.append(n + max(dp[i - 2], dp[i - 3]))
            result = max(result, dp[-1])
        return result
s = Solution()
a = [5, 2, 1, 4, 7, 1]
print s.rob(a)
