class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in xrange(n + 1)]
        for i in xrange(n + 1):
            if i == 1:
                dp[1] = 1
            else:
                for j in xrange(1, i + 1):
                    dp[i] += (dp[i - j] + dp[j - 1])
        print dp
        return dp[n]


s = Solution()
print s.numTrees(3)
