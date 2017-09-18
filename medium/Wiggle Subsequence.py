#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/11/17
  
"""


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        if nums[0] > nums[1]:
            for i in xrange(len(nums)-1):
                if nums[i+1] > nums[i]:
                    return self.wiggleMaxLength(nums[i:]) + 1
            return 2
        is_big = True
        result = 2
        for i in xrange(1, len(nums)-1):
            if is_big:
                if nums[i+1] > nums[i]:
                    i += 1
                else:
                    result += 1
                    i += 1
                    is_big = False
            else:
                if nums[i+1] < nums[i]:
                    i += 1
                else:
                    result += 1
                    i += 1
                    is_big = True
        return result
    
s = Solution()
print s.wiggleMaxLength([1,2,3,4,5,6,7,8,9])
        
        
        