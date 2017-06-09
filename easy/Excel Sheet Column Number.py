#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 6/1/17
  
"""

import string
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_dict = dict(zip(string.ascii_uppercase, range(1, 27)))
        current_position_value, result = 1, 0
        for c in s[::-1]:
            result += hash_dict[c] * current_position_value
            current_position_value *= 26
        return result

s = Solution()
print s.titleToNumber('AB')




    