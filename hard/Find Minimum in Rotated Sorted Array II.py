#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 5/27/17
  
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

s = Solution()
a = [3, 3, 1, 3,3]
print s.findMin(a)
    