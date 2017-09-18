#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 7/27/17
  
"""


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        h = [0 for _ in xrange(10)]
        for c in s:
            h[0] += (c == 'z')
            h[1] += (c == 'o')
            h[2] += (c == 'w')
            h[3] += (c == 'r')
            h[4] += (c == 'u')
            h[5] += (c == 'v')
            h[6] += (c == 'x')
            h[7] += (c == 's')
            h[8] += (c == 'g')
            h[9] += (c == 'i')
        h[1] -= (h[0] + h[2] + h[4])
        h[3] -= (h[4] + h[0])
        h[7] -= h[6]
        h[5] -= h[7]
        h[9] -= (h[5] + h[6] + h[8])
        result = []
        for i in xrange(10):
            result.append(str(i) * h[i])
        return ''.join(result)
        
s = Solution()
print s.originalDigits("owoztneoer")
