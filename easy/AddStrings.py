#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/3/5
  
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        i, carry, l1, l2 = 0, 0, len(num1), len(num2)
        while i < len(num1) and i < len(num2):
            t = int(num1[l1 - 1 - i]) + int(num2[l2 - 1 - i]) + carry
            result.insert(0, str(t % 10))
            carry = t / 10
            i += 1
        while i < l1:
            t = int(num1[l1 - 1 - i]) + carry
            result.insert(0, str(t % 10))
            carry = t / 10
            i += 1
        while i < l2:
            t = int(num2[l2 - 1 - i]) + carry
            result.insert(0, str(t % 10))
            carry = t / 10
            i += 1
        if carry > 0:
            result.insert(0, str(carry))
        return str("".join(result))


    def addStrings2(self, num1, num2):
        if len(num1) == 0:
            return num2
        if len(num2) == 0:
            return num1
        if int(num1[-1]) + int(num2[-1]) < 10:
            return self.addStrings2(num1[:-1], num2[:-1]) + str(int(num1[-1]) + int(num2[-1]))
        else:
            return str(self.addStrings2(self.addStrings2(num1[:-1], num2[:-1]), '1')) + str((int(num1[-1]) + int(num2[-1])) % 10)






c = Solution()
print(c.addStrings2("1", '9'))



    