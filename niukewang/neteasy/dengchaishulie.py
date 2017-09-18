#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/27/17
  
"""
import sys

class Solution(object):
    
    def is_valid(self, nums):
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return True
        nums = sorted(nums)
        gap = nums[1] - nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] - nums[i - 1] != gap:
                return False
        return True

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    nums = map(int, sys.stdin.readline().strip().split())
    s = Solution()
    if s.is_valid(nums):
        print("Possible")
    else:
        print("Impossible")
    
#     s = sys.stdin.readline().strip()
        

