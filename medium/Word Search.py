#!/usr/env/python
# -*- coding: utf-8 -*-

__author__ = "gjwei"


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word or len(board) == 0:
            return False
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == word[0]:
                    result = self._exist(board, i, j, word)
                    if result:
                        return result
        return False
    
    def _exist(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if board[i][j] == word[0]:
            board[i][j] = ' '
            left = self._exist(board, i - 1, j, word[1:])
            right = self._exist(board, i + 1, j, word[1:])
            top = self._exist(board, i, j - 1, word[1:])
            bottom = self._exist(board, i, j + 1, word[1:])
            board[i][j] = word[0]
            return left or right or top or bottom
        return False


s = Solution()
a = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
print s.exist(a, 'ABCCED')