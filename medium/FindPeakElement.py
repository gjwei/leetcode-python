#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/14/17
  
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:



    