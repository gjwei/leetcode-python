class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 0, 1]
        for i in xrange(3, n+1):
            max_product = i - 1
            for j in xrange(2, i // 2+1):
                max_product = max(max_product, max(j, dp[j]) * max(i - j, dp[i - j]))
            dp.append(max_product)
        return dp[n]
            
            
s = Solution()
print s.integerBreak(10)
            
        
        