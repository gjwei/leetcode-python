#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/2/20
 
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero, non_zero = 0, 1
        while zero < len(nums) and non_zero < len(nums):
            while zero < len(nums) and nums[zero] != 0:
                zero += 1
            non_zero = zero + 1
            while non_zero < len(nums) and nums[non_zero] == 0:
                non_zero += 1
            if zero < non_zero and non_zero < len(nums):
                nums[zero], nums[non_zero] = nums[non_zero], nums[zero]
        return nums

s = Solution()
print(s.moveZeroes([0, 1, 0, 3, 12]))