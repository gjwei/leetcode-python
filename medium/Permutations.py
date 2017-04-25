#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/15/17
  
"""
###backtracing


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        is_visited = [False] * len(nums)
        result = []

        self.dfs(nums, 0, is_visited, result, [])
        return result


    def dfs(self, nums, index, is_visited, result, subset):
        if len(subset) == len(nums) or index == len(nums):
            result.append(subset[:])
            return
        else:
            for i in xrange(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and (not is_visited[i - 1]):
                    """
                    ？？？当上一个元素与本元素相同时候，这个时候，如果上个元素没有被访问，说明同样的序列（至今）已经被
                    加入到了结果之中，所以，要选择跳过
                    """
                    continue
                if not is_visited[i]:
                    subset.append(nums[i])
                    is_visited[i] = True
                    self.dfs(nums, index + 1, is_visited, result, subset)
                    is_visited[i] = False
                    subset.pop()

s = Solution()
a = [1, 1, 3]
print s.permute(a)