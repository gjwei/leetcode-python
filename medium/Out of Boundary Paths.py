#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/12/17
  
"""


class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        d = {}
        return self.dfs(m, n, N, i, j, d)
        
    def dfs(self, m, n, N, i, j, d):
        if N < 0:
            return 0
        if N >= 0 and (i < 0 or i >= m or j < 0 or j >= n):
            return 1
        if (N, i, j) in d:
            return d[(N, i, j)]
        result = 0
        result += (self.dfs(m, n, N - 1, i + 1, j, d)
                   + self.dfs(m, n, N - 1, i - 1, j, d)
                   + self.dfs(m, n, N - 1, i, j + 1, d)
                   + self.dfs(m, n, N - 1, i, j - 1, d))
        d[(N, i, j)] = result % (10 ** 9 + 7)
        return result
        
s = Solution()
print s.findPaths(8,50,23,5,26)