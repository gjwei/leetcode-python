#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 6/2/17
  
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket = dict([('[', ']'), ('{','}'), ('(', ')')])
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                t = stack.pop() if len(stack) > 0 else ''
                if bracket[t] != c:
                    return False
        return False if stack else True

s = Solution()
print s.isValid("()")