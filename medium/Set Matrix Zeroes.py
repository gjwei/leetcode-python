#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/29/17
  
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        ##将为0的行和列的值设置为None
        if len(matrix) == 0:
            return
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == 0:
                    self.setRowAndColZeros(matrix, i, j)
        ##将所有为None的设置为0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == None:
                    matrix[i][j] = 0


    def setRowAndColZeros(self, matrix, x, y, fullfill=None):
        ##设置行为fullfill
        for i in xrange(len(matrix)):
            if matrix[i][y] != 0:
                matrix[i][y] = fullfill
        ##设置列为fullfill
        for j in xrange(len(matrix[0])):
            if matrix[x][j] != 0:
                matrix[x][j] = fullfill

    