#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/2/17
  
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0 for _ in xrange(len(num1) + len(num2))]
        for i in xrange(len(num1)):
            start = i
            carry = 0
            for j in xrange(len(num2)):
                t = int(num1[len(num1) - 1 - i]) * int(num2[len(num2) - 1 - j]) +carry + result[start]
                result[start] = t % 10
                carry = t / 10
                start += 1
            result[start] += carry
        r = []
        is_valid = False
        for i in xrange(len(result)-1, -1, -1):
            if result[i] == 0 and not is_valid:
                continue
            else:
                r.append(str(result[i]))
                is_valid = True
        return ''.join(r) or '0'
s = Solution()
print s.multiply('123', '456')


