#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 6/2/17
  
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ret = [[] for i in xrange(numRows)]
        i = 0
        while i < len(s):
            for j in xrange(numRows):
                if i < len(s):
                    ret[j].append(s[i])
                    i += 1
                else:
                    break
            for j in xrange(numRows - 2, 0, -1):
                if i < len(s):
                    ret[j].append(s[i])
                    i += 1
                else:
                    break
        result = []
        for r in ret:
            for c in r:
                result.append(c)
        return ''.join(result)

s = Solution()
print s.convert("PAYPALISHIRING", 3)


    