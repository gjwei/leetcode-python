#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 6/2/17
  
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        if len(nums) < 3: return -1
        result = sum(nums[:3])
        for i in xrange(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target: return current_sum
                if abs(target - current_sum) < abs(target - result):
                    result = current_sum
                if current_sum > target:
                    right -= 1
                else:
                    left += 1
        return result

s = Solution()
a = [-3,-2,-5,3,-4]
print s.threeSumClosest(a, -1)
