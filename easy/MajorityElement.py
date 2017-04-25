#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/3/5
  
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        result = nums[1]
        count = 1
        for i in nums[1:]:
            if result == i:
                count += 1
            else:
                count -= 1
                if count == 0:
                    result = i
                    count = 1
        return result
    