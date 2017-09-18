#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 7/25/17
  
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # 使用桶排序的思想，将数组按照t+1进行分桶，同一个桶之间差小于w
        # 相邻桶之间差值可能小于w,也可能大于w
        # 之后进行判断，是否超出k的范围，如果超出，则删除这个桶
        if k < 1 or t < 0:
            return False
        d = {}
        w = t + 1
        for i, n in enumerate(nums):
            m = nums[i] // w
            if m in d:
                # 存在同一个桶
                return True
            if m - 1 in d and abs(n - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(n - d[m + 1]) < w:
                return True
            d[m] = n
            if i >= k:
                d.pop(nums[i - k] // w)
        return False