#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/15/17
  
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        subset = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            result.append(subset[:])
            self.dfs(nums, i + 1, result, subset)
            subset.pop()

        return result

    def dfs(self, nums, index, result, subset):
        if index == len(nums):
            return
        for i in xrange(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            result.append(subset[:])
            self.dfs(nums, i + 1, result, subset)
            subset.pop()



s = Solution()
a = [1, 2, 2]
result = s.subsetsWithDup(a)
print result