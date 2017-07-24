#!/usr/env/python
# -*- coding: utf-8 -*-

__author__ = "gjwei"


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] <= 0 or nums[i] == i + 1 or nums[i] > len(nums):
                i += 1
            elif nums[i] != nums[nums[i] - 1]:
                t = nums[i]
                nums[i], nums[t - 1] = nums[t - 1], nums[i]
            else:
                i += 1
        for i in xrange(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
s = Solution()
print s.firstMissingPositive([1, 1])
