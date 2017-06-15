class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_step, i = 0, 0
        while i <= max_step:
            max_step = max(max_step, i + nums[i])
            i += 1
        return True if max_step >= len(nums) - 1 else False
        