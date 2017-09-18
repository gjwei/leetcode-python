#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/17/17
  
"""
"""计算字符串相似度"""

def calculate(s1, s2):
    if not s1 and not s2:
        return 0
    elif not s1:
        return len(s1)
    elif not s2:
        return len(s2)
    else:
        if s1[0] == s2[0]:
            return calculate(s1[1:], s2[:])
        else:
            return min([calculate(s1[:1], s2), calculate(s1, s2[1:]), calculate(s1[1:], s2[1:])]) + 1
            
            
