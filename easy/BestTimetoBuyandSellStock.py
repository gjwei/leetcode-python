#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/3/5
  
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        leftMin = []
        rightMax = []
        for i in range(len(prices)):
            if i == 0:
                leftMin[i] = prices[i]
                rightMax[-1-i] = prices[-1-i]
            else:
                leftMin[i] = min(leftMin[i - 1], prices[i])
                rightMax[-1-i] = max(prices[-1-i], rightMax[-i])
        result = 0
        for i in range(len(prices)):
            result = max(result, rightMax[i] - leftMin[i])
        return result