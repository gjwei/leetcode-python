#!/usr/env/python
# -*- coding: utf-8 -*-
# __author__ = ‘gjwei‘

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set()
        result = [0, 0]
        for n in nums:
            if n in s:
                result[0] = n
            else:
                s.add(n)
        result[1] = (set(range(1, len(nums) + 1)) - s).pop()
        return result
s = Solution()
print s.findErrorNums([3,3,1])

