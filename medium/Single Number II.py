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
        help_list = [0 for i in xrange(32)]
        for num in nums:
            for j in xrange(32):
                help_list[j] += (num >>  j & 1)

        for i in xrange(32):
            help_list[i] %= 3
        s = ''.join([str(i) for i in help_list[::-1]])
        print help_list
        return int(s, 2)

s = Solution()
print s.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])
