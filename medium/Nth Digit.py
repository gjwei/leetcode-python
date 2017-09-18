#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 7/25/17
  
"""


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits_len = 1
        count = 9
        start = 1
        while n > digits_len * count:
            n -= digits_len * count
            digits_len += 1
            count *= 10
            start *= 10
        num = start + (n - 1) // digits_len
        return str(num)[(n - 1) % digits_len]
s = Solution()
print s.findNthDigit(15)
            
            