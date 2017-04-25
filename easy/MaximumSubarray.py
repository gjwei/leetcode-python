#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/3/6
  
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = result = 0
        for x in nums:
            if dp + x > 0:
                dp = dp + x
            else:
                dp = 0
            result = max(result, dp)
        return result

s = Solution()
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print s.maxSubArray(a)
