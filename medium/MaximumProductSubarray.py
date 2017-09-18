#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 3/13/17
  
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        max_dp = [nums[0]]
        min_dp = [nums[0]]
        for i in xrange(1, len(nums)):
            max_temp = max(max(nums[i], nums[i] * max_dp[-1]), nums[i] * min_dp[-1])
            min_temp = min(min(nums[i], nums[i] * min_dp[-1]), nums[i] * max_dp[-1])
            max_dp.append(max_temp)
            min_dp.append(min_temp)
        return max(max(max_dp), max(min_dp))

a = [-2, 3, -2, 4, -5]
s = Solution()
print(s.maxProduct(a))

    