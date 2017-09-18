#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 7/30/17
  
"""


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        h = [0 for _ in xrange(n + 1)]
        for i in xrange(2, n+1):
            if i & 1 == 0:
                h[i] = h[i >> 1] + 1
            else:
                h[i] = min(h[(i-1) >> 1], h[(i + 1) >> 1]) + 2
        return h[n]
s = Solution()
print s.integerReplacement(1000000)
