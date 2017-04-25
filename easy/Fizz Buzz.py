#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/29/17
  
"""
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for x in xrange(1, n + 1):
            if x % 3 == 0 and x % 5 == 0:
                result.append("FizzBuzz")
            elif x % 3 == 0:
                result.append("Fizz")
            elif not x % 5:
                result.append("Buzz")
            else:
                result.append(str(x))
        return result

s = Solution()
print s.fizzBuzz(15)
    