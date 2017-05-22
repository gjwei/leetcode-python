#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/25/17
  
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.index(needle)

s = Solution()
print s.strStr('abvcs', 'g')