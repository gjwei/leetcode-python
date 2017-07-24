class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates = sorted(candidates)
        self.dfs(candidates, target, 0, 0, result, [])
        return result

    def dfs(self, nums, target, index, cur_sum, result, l):
        if cur_sum == target:
            result.append(l[:])
            return
        elif cur_sum > target or index >= len(nums):
            return

        for i in xrange(index, len(nums)):
            self.dfs(nums, target, i, cur_sum+nums[i], result, l+[nums[i]])

s = Solution()
print s.combinationSum([2, 3, 6, 7, 4], 7)
