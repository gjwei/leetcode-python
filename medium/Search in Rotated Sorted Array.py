#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/2/17
  
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        rot = left
        print rot
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            realmid = (mid + rot) % len(nums)
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
                                
                    
a = [3, 1]
s = Solution()
print s.search(a, 1)
                    
        
