#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/29/17
  
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(s[::-1])

s = "hello"
so = Solution()
print so.reverseString(s)