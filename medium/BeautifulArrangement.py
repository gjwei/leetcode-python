#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/15/17
  
"""

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        count  = [0]
        nums = range(1, N + 1)
        subset = []
        is_visited = [False] * N
        self.dfs(subset, nums, 0, count, is_visited)
        return count[0]



    def dfs(self, subset, nums, index, count, is_visited):
        if len(subset) == len(nums):
            count[0] += 1
            return
        for i in xrange(len(nums)):
            if len(subset) > 0 and (not self.is_beautiful(len(subset), nums[i])):
                continue
            if not is_visited[i]:
                is_visited[i] = True
                subset.append(nums[i])
                self.dfs(subset, nums, index + 1, count, is_visited)
                subset.pop()
                is_visited[i] = False


    def is_beautiful(self, a, i):
        return a % i == 0 or i % a == 0

s = Solution()
print s.countArrangement(5)