#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 3/13/17
  
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n] * m
        for x in xrange(m):
            for y in xrange(n):
                if x == 0 and y == 0:
                    dp[x][y] = grid[x][y]
                elif x == 0 and y > 0:
                    dp[x][y] = dp[x][y - 1] + grid[x][y]
                elif y == 0 and x > 0:
                    dp[x][y] = dp[x - 1][y] + grid[x][y]
                else:
                    dp[x][y] = min(dp[x - 1][y], dp[x][y - 1]) + grid[x][y]
        return dp[m - 1][n - 1]
