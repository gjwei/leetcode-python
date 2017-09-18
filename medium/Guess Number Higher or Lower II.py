#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/11/17
  
"""
import math

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in xrange(n+1)]
        cnt = [0 for _ in xrange(n + 1)]
        dp[1] = 1
        for i in xrange(2, n+1):
            dp[i] = 1 << 31
            for j in xrange(1, i+1):
                left = dp[i - j]
                right = dp[i - j] + j * cnt[i - j]
                if dp[i] > j + max(left, right):
                    dp[i] = j + max(left, right)
                    cnt[i] = 1 + max(cnt[i - j], cnt[j - 1])
                elif dp[i] == j + max(left, right):
                    cnt[i] = min(cnt[i], 1 + max(cnt[i - j], cnt[j - 1]))
        return dp[n]
                    
                
s = Solution()
print s.getMoneyAmount(4)
