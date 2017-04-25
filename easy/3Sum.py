#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/25/17
  
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        help_map = {}
        for key, value in enumerate(nums):
            help_map[value] = key
        result = []
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in xrange(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                t = nums[i] + nums[j]
                if -t in help_map and help_map[-t] > j:
                    result.append([nums[i], nums[j], -t])
        return result

s = Solution()
nums = [0, 0, 0, 0]
print s.threeSum(nums)
