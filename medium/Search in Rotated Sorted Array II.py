#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/28/17
  
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            print mid
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[left] > target:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[left] > target:
                    left = mid + 1
                else:
                    right = mid
        return -1
s = Solution()
a = [4,5,6,7,0,1,2]
print s.search(a, 2)
        


    