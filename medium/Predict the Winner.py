class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # r = self.get_max_sum(nums)
        # print r
        # return 2 * r > sum(nums)
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
        return dp[0][n-1] * 2 > s
        
    def get_max_sum(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(min(nums[0] + self.get_max_sum(nums[2:]),
                       nums[0] + self.get_max_sum(nums[1:-1])
                           ),
                       min(nums[-1] + self.get_max_sum(nums[1:-1]),
                       nums[-1] + self.get_max_sum(nums[0:-2]))
                       )
    
a = [1, 5, 2, ]
s = Solution()
print s.PredictTheWinner(a)