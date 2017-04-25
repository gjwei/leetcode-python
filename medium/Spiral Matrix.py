#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/28/17
  
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        result, matrix[0][0] = [matrix[0][0]], None
        x, y= 0, 0
        while len(result) < m * n:
            while y + 1 < n and matrix[x][y + 1] != None:
                result.append(matrix[x][y + 1])
                y, matrix[x][y + 1] = y + 1, None
            while x + 1 < m and not matrix[x][y + 1] != None:
                result.append(matrix[x + 1][y])
                x, matrix[x + 1][y] = x + 1, None
            while y - 1 >= 0 and not matrix[x][y - 1] != None:
                result.append(matrix[x][y - 1])
                y, matrix[x][y - 1] = y - 1, None
            while x - 1 >= 0 and not matrix[x - 1][y] != None:
                result.append(matrix[x - 1][y])
                x, matrix[x - 1][y] = x - 1, None
        return result

a = [[1, 3], [4, 5]]
s = Solution()
print s.spiralOrder(a)

    