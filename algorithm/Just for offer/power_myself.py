#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/27/17
  
"""


# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if exponent < 0:
            return 1.0 / self.Power(base, -exponent)
        result = base
        while exponent:
            if exponent > 1:
                result *= result
            if (exponent % 2) & 1:
                result *= base
            exponent >>= 1
        return result

s = Solution()
print s.Power(2, -4)
    