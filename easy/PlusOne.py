#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/3/4
  
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        index = 0
        while carry > 0 and index < len(digits):
            t = int(digits[-1-index]) + carry
            digits[-1-index] = t % 10
            carry =  t / 10
        if carry > 0:
            digits.insert(0, carry)
        return digits


