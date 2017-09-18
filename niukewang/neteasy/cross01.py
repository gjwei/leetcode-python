#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/27/17
  
"""
import sys

def max_substring_01(s):
    if len(s) == 0:
        return 0
    result, count = 1, 1
    for i in xrange(1, len(s)):
        if int(s[i]) == 1 - int(s[i - 1]):
            count += 1
        else:
            count = 1
        result = max(result, count)
    return result

if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    print max_substring_01(s)
            
