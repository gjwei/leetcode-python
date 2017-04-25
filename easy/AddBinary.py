#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/2/19
 
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = []
        i,  carry = 0, 0
        while i < len(a) and i < len(b):
            a_i = int(a[-i-1])
            b_i = int(b[-i-1])
            c_i = (carry + a_i + b_i) % 2
            carry = (carry + a_i + b_i) / 2
            c.append(str(c_i))
            i = i + 1
        while i < len(a):
            a_i = ord(a[len(a) - i - 1]) - ord('0')
            c_i = (carry + a_i) % 2
            c.append(str(c_i))
            carry = (carry + a_i) / 2
            i = i + 1
        while i < len(b):
            b_i = ord(b[len(b) - i - 1]) - ord('0')
            c_i = (carry + b_i) % 2
            c.append(str(c_i))
            carry = (carry + b_i) / 2
            i = i + 1
        if carry > 0:
            c.append(str(carry))

        #print c
        return ("".join(c[::-1]))


    def addBinaryRecursize(self, a, b):
        """

        :param a: str
        :param b: str
        :return: str
        """
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinaryRecursize(self.addBinaryRecursize(a[:-1], b[:-1]), '1') + '0'
        else:
            return self.addBinaryRecursize(a[:-1], b[:-1]) + str(int(a[-1]) + str(int(b[-1])))


s = Solution()
print (s.addBinary('11', '1'))



