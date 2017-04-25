#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 3/13/17
  
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        top_dp = [0] * n
        bottom_dp = [0] * n
        for i in xrange(n):
            if i == 0:
                top_dp[0] = triangle[0][0]
            else:
                for j in xrange(i + 1):


    def get_top_two(self, triangle, i, j):


