

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        result = []
        self.dfs(candidates, target, 0, result, [], 0)
        return result
        
    def dfs(self, nums, target, cur_sum, result, l, index):
        if cur_sum == target:
            result.append(l[:])
            return
        if index >= len(nums) or cur_sum > target:
            return
        
        for i in xrange(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            l.append(nums[i])
            self.dfs(nums, target, cur_sum+nums[i], result, l, i + 1)
            l.pop()
            
s = Solution()
t = s.combinationSum2([1], 1)
for i in t:
    print i
