#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/29/17
  
"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0
        for i in xrange(32):
            if num >> i:
                result += (1 - (num >> i & 1)) << i
            else:
                break
        return result
s = Solution()
print s.findComplement(1)
