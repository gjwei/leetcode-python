#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/11/17
  
"""


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        for s in strs:
            s_0, s_1 = self.count(s)
            for i in xrange(m, s_0 - 1, -1):
                for j in xrange(n, s_1 - 1, -1):
                    dp[i][j] = max(1 + dp[i - s_0][j - s_1], dp[i][j])
        return dp[m][n]
            

        # if (m == 0 and n == 0) or len(strs) == 0:
        #     return 0
        # s_m, s_n = self.count(strs[0])
        # if s_m > m or s_n > n:
        #     return self.findMaxForm(strs[1:], m, n)
        # else:
        #     result = max(1 + self.findMaxForm(strs[1:], m-s_m, n-s_n),
        #                  self.findMaxForm(strs[1:], m, n))
        #     return result
        
        
    def count(self, s):
        m, n = 0, 0
        for c in s:
            if c == '1':
                n += 1
            if c == '0':
                m += 1
        return m, n
s = Solution()
a = ["10", "1", "0"]
m = 1
n = 1
print s.findMaxForm(a, m, n)