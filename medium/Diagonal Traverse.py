#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 7/27/17
  
"""


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not matrix:
            return result
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        while len(result) < m * n:
            result.append(matrix[i][j])
            if (i + j) & 1 == 0:
                
                
                
        
        
    #     result = []
    #     self.up_right(matrix, 0, 0, result)
    #     return result
    #
    # def down_left(self, matrix, i, j, result):
    #     m, n = len(matrix), len(matrix[0])
    #     if len(result) == m * n:
    #         return
    #     while 0 <= i < m and 0 <= j < n:
    #         result.append(matrix[i][j])
    #         i += 1
    #         j -= 1
    #     if i < n:
    #         self.up_right(matrix, i, 0, result)
    #     else:
    #         self.up_right(matrix, m - 1, j + 2, result)
    #
    # def up_right(self, matrix, i, j, result):
    #     m, n = len(matrix), len(matrix[0])
    #     if len(result) == m * n:
    #         return
    #     while 0 <= i < m and 0 <= j < n:
    #         result.append(matrix[i][j])
    #         i -= 1
    #         j += 1
    #     if j < m:
    #         self.down_left(matrix, 0, j, result)
    #     else:
    #         self.down_left(matrix, i + 2, n - 1, result)
s = Solution()
a = [[2,5],[8,4],[0,-1]]
print s.findDiagonalOrder(a)
        