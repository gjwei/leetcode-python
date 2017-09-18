#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/3/17
  
"""


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if len(matrix) == 0:
            raise ValueError
        m, n = len(matrix), len(matrix[0])
        left, right = matrix[0], matrix[m * n - 1] + 1
        while left < right:
            mid = (left + right) >> 1
            count, j = 0, n - 1
            for i in xrange(m):
                while matrix[i][j] > mid:
                    j -= 1
                count += (j + 1)
            if count < mid:
                left = mid + 1
            else:
                right = mid - 1
        return left

            

