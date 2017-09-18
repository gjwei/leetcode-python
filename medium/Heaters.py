#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 7/25/17
  
"""


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        r = heaters[0] - 1
        for i in xrange(len(heaters)):
            if i < len(heaters) - 1:
                t = (heaters[i+1] - heaters[i]) >> 1
                if t <
                # r = max(r, (heaters[i + 1] - heaters[i]) >> 1)
            else:
                r = max(r, houses[-1] - heaters[i])
        return r
        
a = [1, 2, 3, 5, 15]
b = [2, 30]
s = Solution()
print s.findRadius(a, b)
