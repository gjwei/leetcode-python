#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/11/17
  
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        for c in t:
            d[c] = d.get(c, 0) + 1
        min_length = 1 << 30
        start, end = 0, 0
        result = ''
        while end <= len(s):
            while end < len(s) and not self._valid(d):
                t = s[end]
                if s[end] in d:
                    d[s[end]] -= 1
                end += 1
            if not self._valid(d):
                break
            if end - start < min_length:
                result = s[start: end]
                min_length = end - start
            if s[start] in d:
                d[s[start]] += 1
            start += 1
        return result
                 
    def _valid(self, d):
        for k, v in d.items():
            if v > 0:
                return False
        return True
    
    
s = Solution()
a = "a"
t = 'a'
print s.minWindow(a, t)