#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/25/17
  
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0
        common_bit_mask = 0
        for i in xrange(len(nums)):
            twos |= (ones & nums[i])
            ones ^= nums[i]
            common_bit_mask = ~(ones & twos)
            ones &= common_bit_mask
            twos &= common_bit_mask
        return ones

s = Solution()
print s.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])
