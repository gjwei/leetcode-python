#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 7/25/17
  
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # if len(s) == 0:
        #     return False
        #
        # for l in xrange(1, len(s)):
        #
        #     if len(s) % l == 0:
        #         repeat = True
        #         for j in xrange(0, len(s), l):
        #             if s[j: j+l] != s[:l]:
        #                 repeat = False
        #                 break
        #         if repeat:
        #             return repeat
        # return False
    def kmp(self, s):
        res = [0 for _ in xrange(len(s))]
        i, j = 0, 1
        while i < len(s) and j < len(s):
            if s[i] == s[j]:
                res[j] = i + 1
                i += 1
                j += 1
            else:
                if i == 0:
                    res[j] = 0
                    j += 1
                else:
                    i = res[i - 1]
        return res
    
s = Solution()
print s.repeatedSubstringPattern('abac')