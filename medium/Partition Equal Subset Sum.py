class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sum = sum(nums)
        if nums_sum & 1 == 1:
            return False
        nums_sum >>= 1
        nums = sorted(nums)
        
        dp = [False for _ in xrange(nums_sum+1)]
        dp[0] = True
        for n in nums:
            for i in xrange(nums_sum, n - 1, -1):
                dp[i] = dp[i] or dp[i - n]
        return dp[nums_sum]
        
    def _partition(self, nums, s):
        if (s < 0) or (len(nums) == 0 and s > 0):
            return False
        if s == 0:
            return True
        result = self._partition(nums[1:], s) or self._partition(nums[1:], s-nums[0])
        return result
s = Solution()
print s.canPartition([1, 2, 5])