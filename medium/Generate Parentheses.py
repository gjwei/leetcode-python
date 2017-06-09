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
        self.backtrack(result, [], 0, 0, n)
        return result

    def backtrack(self, result, s, open, close, n):
        if len(s) == n * 2:
            result.append(''.join(s))
        if open < n:
            self.backtrack(result, s, open + 1, close, n)
        if close < open:
            self.backtrack(result, s, open, close + 1, n)

    