#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/9/17
  
"""


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        n = len(s)
        l = [[0 for _ in xrange(n)] for _ in xrange(n)]
        return self._lps(s, l, 0, n-1)
        
    def _lps(self, s, l, i, j):
        if i > j:
            return 0
        if l[i][j] > 0:
            return l[i][j]
        if s[i] == s[j]:
            if i == j:
                l[i][j] = 1
            else:
                l[i][j] = 2 + self._lps(s, l, i + 1, j - 1)
        else:
            l[i][j] = max(self._lps(s, l, i + 1, j), self._lps(s, l, i, j - 1))
        return l[i][j]
        # elif l[i][j] > 0:
        #     return l[i][j]
        # elif i == j:
        #     l[i][j] = 1
        # elif s[i] == s[j]:
        #     l[i][j] = 2 + self._lps(s, l, i + 1, j - 1)
        # else:
        #     l[i][j] = max(self._lps(s, l, i + 1, j), self._lps(s, l, i, j - 1))
        # return l[i][j]
    
s = Solution()
print(s.longestPalindromeSubseq("bbbab"))