#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2016/12/14
 
"""


def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    """
    思路：
    用一个hash表存储字母位置，之后进行比较，用两点法算出其位置
    """
    hashtable = []
    for i in range(255):
        hashtable.append(-1)
    result = 0
    low = 0
    for high in range(len(s)):
        if hashtable[ord(s[i])] != -1:
            low = max(low, hashtable[ord(s[high])] + 1)
        hashtable[ord(s[high])] = high
        result = max(result, high - low + 1)
    return result

n = 0
def traiange():
    if n == 0:
        yield [1]
    else:
        result = [0] * (n + 1)
        for i in


    