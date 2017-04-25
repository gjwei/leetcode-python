#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/24/17
  
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix_length = 0
        if len(strs) == 0: return ''
        is_break = False
        while not is_break and common_prefix_length < len(strs[0]):

            for s in strs:
                if common_prefix_length >= len(s) or s[common_prefix_length] != strs[0][common_prefix_length]:
                    is_break = True
            if not is_break:
                common_prefix_length += 1
        if common_prefix_length == 0:
            return ''
        else:
            return strs[0][:common_prefix_length]


s = Solution()
a = ['abc', 'ab', 'abv']
print s.longestCommonPrefix(a)


    