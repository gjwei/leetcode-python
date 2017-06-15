#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 5/18/17
  
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.backtrace(result, [], 0, 0, n)
        return result
        
    def backtrace(self, result, parentheses, open, close, max):
        if len(parentheses) == 2 * max:
            result.append(''.join(parentheses))
        if open < max:
            parentheses.append('(')
            self.backtrace(result, parentheses, open + 1, close, max)
            parentheses.pop()
        if close < open:
            parentheses.append(')')
            self.backtrace(result, parentheses, open, close + 1, max)
            parentheses.pop()

s = Solution()
print s.generateParenthesis(3)    