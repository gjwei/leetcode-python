#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/1/17
  
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_num = sorted(nums)
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] == sorted_num[left]:
                left += 1
            if nums[right] == sorted_num[right]:
                right -= 1
        
        return right - left + 1
        
        
    