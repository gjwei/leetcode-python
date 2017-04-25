#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/15/17
  
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(candidates, target, 0, result, 0, [])
        return result


    def dfs(self, nums, target, index, result, subset_sum, subset):
        if subset_sum == target:
            result.append(subset[:])
            return
        elif subset_sum > target or index == len(nums):
            return
        for i in xrange(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, target, index, result, subset_sum, subset)
            subset.pop()
            #self.dfs(nums, target, index + 1, result, subset_sum, subset)

s = Solution()
a = [2, 3, 6, 7]
print s.combinationSum(a, 7)