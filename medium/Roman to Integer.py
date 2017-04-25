#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/24/17
  
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, 'V': 5, 'I': 1}
        last_priority = 1
        priority_dict = {"M": 7, "D": 6, "C": 5, "L": 4, "X": 3, 'V': 2, 'I': 1}
        result = 0
        for i in s[::-1]:
            if priority_dict[i] < last_priority:
                result -= roman_dict[i]
            else:
                result += roman_dict[i]
                last_priority = priority_dict[i]
        return result