#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 5/31/17
  
"""

import string

class Solution(object):

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        alphas = string.ascii_uppercase
        result = []
        while n:
            if n < 27:
                result.append(alphas[n - 1])
                break
            else:
                result.append(alphas[n % 26 - 1])
                n -= n % 26 if n % 26 else 26
                n /= 26
        return ''.join(result[::-1])


s = Solution()
print s.convertToTitle(82)
