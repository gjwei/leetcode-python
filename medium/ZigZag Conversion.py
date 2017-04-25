#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/24/17
  
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        period = 2 * (numRows - 1)
        lines = ["" for i in range(numRows)]
        d = {i: i if i < numRows else (period - i) for i in xrange(period)}

        for i in xrange(len(s)):
            lines[d[i % period]] += s[i]

        return "".join(lines)












