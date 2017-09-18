#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/27/17
  
"""
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums) == 0:
            return False
        one = 1
        nums = [0] + nums
        for i in xrange(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if one == 1:
                    nums[i] = nums[i - 1]
                    one -= 1
                else:
                    return False
        return True

s = Solution()
print s.checkPossibility([4,2,3])
