#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/13/17
  
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
        counter = len(t)
        start, end = 0, 0
        result = ''
        min_length = 2 << 30
        while end < len(s):
            if s[end] in d:
                d[s[end]] -= 1
                if d[s[end]] >= 0:
                    counter -= 1
                end += 1
                
            while counter == 0:
                if end - start + 1 < min_length:
                    min_length = end - start + 1
                    result = s[start: end+1]
                if s[start] in d:
                    if d[s[start]] == 0:
                        counter += 1
                    d[s[start]] += 1
                start += 1
        return result
            
            
        return result
                
    def is_valid(self, d):
        for _, v in d.iteritems():
            if v == 0:
                return False
        return True
    
        
        
s = Solution()
print s.minWindow("a", 'a')