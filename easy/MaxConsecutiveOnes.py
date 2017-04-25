#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/3/5
  
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index, result, seq = 0, 0, 0
        while index < len(nums):
            if index == 0:
                seq = 1
            elif nums[index] == nums[index - 1]:
                seq += 1
            else:
                seq = 1
            index += 1
            result = max(result, seq)
        return result


    