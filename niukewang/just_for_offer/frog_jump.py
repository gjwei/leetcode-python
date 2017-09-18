#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/10/17
  
"""
class Solution:
    def jumpFloorII(self, number):
        # write code here
        dp = [0 for _ in xrange(number + 1)]
        dp[0] = 1
        for i in xrange(1, number + 1):
            for j in xrange(1, number+1):
                dp[i] += dp[i - j]
        return dp[number]

s = Solution()
print s.jumpFloorII(4)
                

