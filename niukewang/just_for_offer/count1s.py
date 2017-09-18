#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/10/17
  
"""
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        result = 0
        index = 0
        while index < 32:
            result += ((n >> index) & 1)
            index += 1
        return result
s = Solution()
print s.NumberOf1(-5)