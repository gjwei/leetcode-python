#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 6/1/17
  
"""
from math import sqrt


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        divisors = set([1])
        num = num if num > 0 else -num
        for n in xrange(2, int(sqrt(num)) + 1):
            if num % n == 0:
                divisors.add(n)
                divisors.add(num / n)
        if num == sum(divisors):
            return True
        else:
            return False
s = Solution()
print s.checkPerfectNumber(1)


    