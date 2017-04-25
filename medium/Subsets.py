#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/16/17
  
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        for x in nums:
            result += [item + [x] for item in result]
        return result

    def dfs(self, a, index, result, current_list):
        # result.append(current_list[:])
        # if index == len(a):
        #     return
        # for i in xrange(index, len(a)):
        #     current_list.append(a[i])
        #     self.dfs(a, i + 1, result, current_list)
        #     current_list.pop()
        result.append(current_list)
        for i in xrange(index, len(a)):
            self.dfs(a, i + 1, result, current_list + [a[i]])

    def subset2(self, nums):
        n = len(nums)
        result = []
        for x in xrange(1 << n):
            sub_list = []
            for j in xrange(n):
                if (x >> j & 1) != 0:
                    sub_list.append(nums[j])
            result.append(sub_list)
        return result





s = Solution()
a = [1, 2, 3]
print s.subset2(a)