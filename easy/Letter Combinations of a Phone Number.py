#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/25/17
  
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        num_to_string = ['', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        strings = [num_to_string[int(i) - 1] for i in digits]
        result = []
        self.dfs(strings, 0, result, [])
        return result



    def dfs(self, strings, index, result, s):
        if index == len(strings):
            result.append(''.join(s))
            return
        for i in xrange(len(strings[index])):
            s.append(strings[index][i])
            self.dfs(strings, index + 1, result, s)
            s.pop()



s = Solution()
print s.letterCombinations(23)
