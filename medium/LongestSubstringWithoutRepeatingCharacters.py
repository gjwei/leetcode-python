#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/3/5
  
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashTable = [-1] * 256
        if len(s) == 0 or len(s) == 1:
            return len(s)
        i, j, result = 0, 0, 0
        while j < len(s):
            if hashTable[ord(s[j])] == -1:
                hashTable[ord(s[j])] = j
                j += 1
            else:
                pass




    