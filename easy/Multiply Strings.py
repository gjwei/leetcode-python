#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 6/1/17
  
"""

"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
Subscribe to see which companies asked this question.

Show Tags
Show Similar Problems

"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result_len = len(num1) + len(num2) + 1
        result = [0 for _ in xrange(result_len)]

    def multiply_single(self, num, n):
        result, charge = [], 0
        for c in num[::-1]:
            t = int(c) * int(n) + charge
            charge = t / 10
            result.append(t % 10)
        if charge:
            result.append(charge)
        return ''.join(result[::-1])




    