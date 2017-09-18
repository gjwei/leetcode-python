#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/11/17
  
"""


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        pass
        
    
    def _printMatrix(self, matrix, left, right, up, down):
        print("matrix", matrix)
        if len(matrix) == 0:
            return []
        result = self.get_surrund(matrix, left, right, up, down)
        return result + self.printMatrix(matrix[1:-1][1:-1])

    def get_surrund(self, matrix, left, right, up, down):
        if len(matrix) == 0:
            return []
        result = []
        m, n = right - left + 1, down - up + 1
        if m == 1:
            return matrix[0]
        if n == 1:
            return matrix[:][0]
        for j in xrange(n):
            result.append(matrix[0][j])
        for i in xrange(1, m):
            result.append(matrix[i][n - 1])
        for j in xrange(n - 2, -1, -1):
            result.append(matrix[m - 1][j])
        for i in xrange(m - 2, 0, -1):
            result.append(matrix[i][0])
        return result

a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
s = Solution()
print s.printMatrix(a)