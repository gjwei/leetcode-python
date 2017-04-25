#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/24/17
  
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == -(2 << 30):
            return False
        x = t = abs(x)
        num_length = 0
        while t:
            t /= 10
            num_length += 1
        i = 0
        while i <= (num_length - 1 >> 1):
            if x / int(pow(10, i)) % 10 != x / int(pow(10, num_length - 1 - i)) % 10:
                return False
            i += 1
        return True
s = Solution()
print s.isPalindrome(-2147447412)




    