#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/3/5
  
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        while len(result) < numRows:
            if len(result) == 0:
                result.append([1])
            else:
                t = result[-1]
                helpT = [1]
                for i in range(len(t) - 1):
                    helpT.append(t[i] + t[i + 1])
                helpT.append(1)
                result.append(helpT)
        return result

    