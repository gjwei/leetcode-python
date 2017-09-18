#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/27/17
  
"""


class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        # max_depth = max([n // 100 for n in nums])
        tree = [-1 for _ in xrange((2 ** 5) + 1)]
        for n in nums:
            d, p, v = n / 100, n / 10 % 10, n % 10
            tree[(2 ** (d - 1) - 1) + p] = v
        sums = []
        self._pathSum(tree, 1, sums, 0)
        print sums
        print tree
        return sum(sums)
    
    def _pathSum(self, tree, index, sums, cur_sum):
        if not self.is_leave(tree, index):
            sums.append(cur_sum)
            return
        print 'tree[index]', tree[index]
        cur_sum += tree[index]
        if self.is_leave(tree, index * 2):
            self._pathSum(tree, index * 2, sums, cur_sum)
        if self.is_leave(tree, index * 2 + 1):
            self._pathSum(tree, index * 2 + 1, sums, cur_sum)
        # left = tree[index] + self._pathSum(tree, index * 2)
        # right = tree[index] + self._pathSum(tree, index * 2 + 1)
    
    def is_leave(self, tree, index):
        if index < len(tree) and tree[index] >= 0:
            return True
        else:
            return False
        
            
        
    
s = Solution()
print s.pathSum([113,229,349,470,485])
    