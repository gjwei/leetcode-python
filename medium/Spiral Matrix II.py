#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/28/17
  
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0 for i in xrange(n)] for j in xrange(n)]
        x, y, num, max_num = 0, 0, 2, n * n
        result[0][0] = 1
        while num <= max_num:
            while y + 1 < n and not result[x][y + 1]:
                result[x][y + 1] = num
                y, num = y + 1, num + 1
            while x + 1 < n and not result[x + 1][y]:
                result[x + 1][y] = num
                x, num = x + 1, num + 1
            while y - 1 >= 0 and not result[x][y - 1]:
                result[x][y - 1] = num
                y, num = y - 1, num + 1
            while x - 1 >= 0 and not result[x - 1][y]:
                result[x - 1][y] = num
                x, num = x - 1, num + 1
        return result

s = Solution()
print s.generateMatrix(0)
    