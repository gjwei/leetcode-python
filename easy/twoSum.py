#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 Created by gjwei on 2016/12/6
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        elements = {}

        for i in range(len(nums)):
            if nums[i] not in elements:
                elements[target - nums[i]] = i
            else:
                return list([elements[nums[i]], i])


s = Solution()
a = [3, 2, 4]
print(s.twoSum(a, 6))

