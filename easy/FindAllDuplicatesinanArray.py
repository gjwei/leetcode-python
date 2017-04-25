#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/3/8
  
"""


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums:
            temp = abs(i)
            if nums[temp - 1] < 0:
                result.append(temp)
            nums[temp - 1] = - nums[temp - 1]
        return result


s = Solution()
a = [5,4,6,7,9,3,10,9,5,6]
print s.findDuplicates(a)

