#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/10/17
  
"""


class Solution:
    def Power(self, base, exponent):
        if exponent < 0:
            return 1 / self.Power(base, -exponent)
        result = 1.0
        while exponent:
            if exponent & 1 == 0:
                base *= base
                exponent >>= 1
            else:
                result *= base
                exponent -= 1
        return result
    
s = Solution()
print s.Power(2, 4)
            
        

