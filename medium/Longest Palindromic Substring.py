#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/30/17
  
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

    def longestPalindrome_with_one(self, s, index):
        left, right = index - 1, index + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right - 1
        return s[left + 1: right]

    def lonestPalindrome_with_two(self, s, left, right):

