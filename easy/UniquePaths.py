#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 3/13/17
  
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n] * m
        for x in xrange(m):
            for y in xrange(n):
                if x == 0 and y == 0:
                    dp[x][y] = 1
                elif x == 0 and y > 0:
                    dp[x][y] = dp[x][y - 1]
                elif y == 0 and x > 0:
                    dp[x][y] = dp[x - 1][y]
                else:
                    dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
        return dp[m - 1][n - 1]

m = 1
n = 2
print Solution().uniquePaths(m, n)
    