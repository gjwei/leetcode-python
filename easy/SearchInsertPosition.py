#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/2/19
 
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low, high = 0, len(nums) - 1
        while low < high:
            if target <= nums[low]:
                return low
            if target == nums[high]:
                return high
            if target > nums[high]:
                return high + 1
            mid = (low + high) / 2
            if nums[mid] >= target:
                high = mid - 1
            elif nums[mid] < target and nums[mid + 1] >= target:
                return mid + 1
            else:
                low = mid + 1
        return low if nums[low] >= target else low + 1
s = Solution()
a = [1, 3, 5, 6]
print(s.searchInsert(a, 0))








    