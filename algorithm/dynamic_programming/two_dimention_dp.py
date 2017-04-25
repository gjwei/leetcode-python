#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 3/13/17
  
"""
def get_max_numger_apple(apples):
    """
    在一个二维方格中，每个方格内放有一定数量的苹果，小明从起始位置（0， 0）出发，
    每次移动只能向下和向右移动，计算到达重点时，小明最多可以得到多少苹果
    :param apples:
    :return:
    """
    if len(apples) == 0:
        return 0
    m = len(apples)
    n = len(apples[0])
    dp = [[0] * n] * m
    #dp.map(get_local_max_number_apple(dp, x, y) for x in xrange(m) y in xrange(n))
    for x in xrange(m):
        for y in xrange(n):
            dp[x][y] = get_local_max_number_apple(dp, x, y) + apples[x][y]
    return dp[m - 1][n - 1]

def get_local_max_number_apple(dp, x, y):
    if x == 0 and y == 0:
        return 0
    if x == 0:
        return dp[x][y - 1]
    if y == 0:
        return dp[x - 1][y]
    return max(dp[x - 1][y], dp[x][y - 1])