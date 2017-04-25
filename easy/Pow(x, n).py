#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/19/17
  
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        a = x
        while n > 1:
            x *= x
            n >>= 1
        if n:
s = Solution()
print s.myPow(2, 5)
    