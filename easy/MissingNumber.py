#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/2/20
 
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(nums)):
            result ^= ((i + 1) ^ nums[i])
        return result
s = Solution()
print s.missingNumber([0, 1, 3])