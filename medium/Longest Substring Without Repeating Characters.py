#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/30/17
  
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        help_dict = {}
        left, right, result = 0, 0, 0
        for right in xrange(len(s)):
            if s[right] in help_dict:
                left = max(left, help_dict[s[right]] + 1)
            help_dict[s[right]] = right
            result = max(result, right - left + 1)
        return result
s = Solution()
a = 'abcabcd'
print s.lengthOfLongestSubstring(a)

