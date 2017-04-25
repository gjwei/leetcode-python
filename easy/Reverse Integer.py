#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/24/17
  
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        while x:
            tail = x % 10
            new_result = result * 10 + tail
            if (new_result - tail) / 10 != result:
                return 0
            result = new_result
            x /= 10
        return result


s = Solution()
print s.reverse(12)