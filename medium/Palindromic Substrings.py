#!/usr/env/python
# -*- coding: utf-8 -*-
# __author__ = ‘gjwei‘
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in xrange(len(s)):
            if i < len(s) - 1:
                count += (self._count(s, i, i)) + (self._count(s, i, i + 1))
            else:
                count += 1
        return count
        
    def _count(self, s, left, right):
        result = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
            else:
                break
        return result

s = Solution()
print s.countSubstrings("aaa")