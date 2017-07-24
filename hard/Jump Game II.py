#!/usr/env/python
# -*- coding: utf-8 -*-

__author__ = "gjwei"


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = len(nums) - 1
        for i, n in enumerate(nums):
            step = nums[i]
            max_reach = i
            for j in xrange(i, i + step + 1):
                max_reach = max(max_reach, j + nums[j])
                