#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/10/17
  
"""
class Solution(object):
    def Single_Number_III(self, nums):
        xor = 0
        for n in nums:
            xor ^= n
        last_1 = xor & (-xor)
        

