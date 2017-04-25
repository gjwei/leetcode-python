#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 3/13/17
  
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n] * m
        for x in xrange(m):
            for y in xrange(n):

                if x == 0 and y == 0:
                    dp[x][y] = 1
                elif x > 0 and y == 0:
                    dp[x][y] = dp[x - 1][y]
                elif x == 0 and y > 0:
                    dp[x][y] = dp[x][y - 1]
                else:
                    dp[x][y] = dp[x][y - 1] + dp[x - 1][y]
                if obstacleGrid[x][y] == 1:
                    dp[x][y] = 0

                # if x == 0 and y == 0:
                #     dp[x][y] == 1
                # elif x == 0 and y > 0:
                #     if obstacleGrid[x][y] == 1:
                #         dp[x][y] = 0
                #     else:
                #         dp[x][y] = dp[x][y - 1]
                # elif x > 0 and y == 0:
                #     if obstacleGrid[x][y] == 1:
                #         dp[x][y] = 0
                #     else:
                #         dp[x][y] = dp[x - 1][y]
                # else:
                #     if obstacleGrid[x][y] == 1:
                #         dp[x][y] = 0
                #     else:
                #         dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
        return dp[m - 1][n - 1]


    