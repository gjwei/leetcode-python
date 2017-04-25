#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/2/21
 
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        id = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[id] = nums[i]
                id += 1
        return id






S = Solution()
print(S.removeDuplicates([1, 2, 3, 3]))