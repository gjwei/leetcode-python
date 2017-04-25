#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/3/6
  
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if prices[0] < prices[1]:
            buy = 0
        else:buy = -1
        for i in range(1, len(prices) - 1):
            if prices[i] <= prices[i - 1] and prices[i] <= prices[i + 1]:
                #zuidi
                buy = i
            if prices[i] >= prices[i - 1] and prices[i] >= prices[i+1]:
                #zuigao
                profit += (prices[i] - prices[buy])
        if prices[len(prices) - 1] >= prices[len(prices) - 2]:
            profit += prices[i] - prices[buy]
        return profit

s = Solution()
a = [2, 1, 5]
print s.maxProfit(a)