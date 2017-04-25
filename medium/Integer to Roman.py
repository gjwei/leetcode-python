#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/24/17
  
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
                 ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                 ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
                 ["", "M", "MM", "MMM"]]
        result = []
        result.append(roman[3][num / 1000])
        result.append(roman[2][num / 100 % 10])
        result.append(roman[1][num / 10 % 10])
        result.append(roman[0][num % 10])

        return ''.join(result)

s = Solution()
print s.intToRoman(1022)

    