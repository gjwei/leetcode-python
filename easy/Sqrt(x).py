#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/19/17
  
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        left, right = 1, x
        while (left < right):
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid == x:
                return mid
            elif mid * mid < x and (mid + 1) * (mid + 1) > x:
                return mid
            else:
                left = mid + 1
        return left
s = Solution()
print s.mySqrt(25)