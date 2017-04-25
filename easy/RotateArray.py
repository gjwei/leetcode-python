#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/3/5
  
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.list_reverse(nums, 0, len(nums) - 1)
        print a
        self.list_reverse(nums, 0, k - 1)
        self.list_reverse(nums, k, len(nums) - 1)


    def list_reverse(self, nums, left, right):
        """Rotate array from left to right"""
        if left >= right:
            return
        mid = (left + right) / 2
        for i in range(mid - left + 1):
            #print i
            nums[left + i], nums[right - i] = nums[right - i], nums[left + i]

s = Solution()
a = [1, 2, 3, 4, 5, 6]
s.rotate(a, 3)
print a