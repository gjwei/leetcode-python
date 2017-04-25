#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/29/17
  
"""


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        ##将由死亡复活的细胞设置为0-->2
        ##将要死亡的细胞设置为1 --> -1
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                neighbors = self.calculate_neighbor(board, i, j)
                if board[i][j]:  # 细胞现在正在活着
                    if neighbors < 2 or neighbors > 3:
                        board[i][j] = -1
                else:
                    if neighbors == 3:
                        board[i][j] = 2
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1

    def calculate_neighbor(self, a, i, j):
        result = 0
        for x in [i - 1, i, i + 1]:
            for y in [j - 1, j, j + 1]:
                if x != i and y != j:
                    result += self.cell_live_or_dead(a, x, y)
        return result

    def cell_live_or_dead(self, a, i, j):
        if i < 0 or j < 0 or i >= len(a) or j >= len(a[0]):
            return 0
        else:
            if a[i][j] == 2:
                return 0
            elif a[i][j] == -1:
                return 1
            return a[i][j]

s = Solution()
a = [[1, 1], [1, 0]]
s.gameOfLife(a)
print a