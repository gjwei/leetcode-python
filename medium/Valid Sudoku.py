#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/2/17
  
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        h = set()
        for i in xrange(10):
            for j in xrange(10):
                if board[i][j] != '.':
                    in_row = board[i][j] + ' in row ' + str(i)
                    in_col = board[i][j] + ' in col ' + str(j)
                    in_middle = board[i][j] + 'in row ' + str(i // 3) + ' and in col ' + str(j // 3)
                    if in_row in h or in_col in h or in_middle in h:
                        return False
                    h.add(in_row)
                    h.add(in_col)
                    h.add(in_middle)
        return True
        
        
    #     return self.is_valid_horizontial(a) and self.is_valid_vertical(a) and self.is_valid_middle(a)
    #
    # def is_valid_horizontial(self, board):
    #     for i in xrange(len(board)):
    #         h = [0 for _ in xrange(10)]
    #         for j in xrange(len(board[i])):
    #             if board[i][j] != '.':
    #                 t = int(board[i][j])
    #                 if h[t] != 0:
    #                     return False
    #                 else:
    #                     h[t] += 1
    #     return True
    #
    # def is_valid_vertical(self, board):
    #     m, n = len(board), len(board[0])
    #     for j in xrange(n):
    #         h = [0 for _ in range(10)]
    #         for i in xrange(m):
    #             if board[i][j] != '.':
    #                 t = int(board[i][j])
    #                 if h[t] != 0:
    #                     return False
    #                 else:
    #                     h[t] += 1
    #
    #     return True
    #
    # def is_valid_middle(self, board):
    #     for r in xrange(0, 9, 3):
    #         for c in xrange(0, 9, 3):
    #             h = [0 for _ in range(10)]
    #             for i in xrange(r, r+3):
    #                 for j in xrange(c, c+3):
    #                     if h[i][j] != '.':
    #                         t = int(h[i][j])
    #                         if h[t] != 0:
    #                             return False
    #                         else:
    #                             h[t] += 1
    #     return True
    #
        
a = [".........",".........",".9......1","8........",".99357...",".......4.","...8.....",".1....4.9","...5.4..."]
s = Solution()
print s.isValidSudoku(a)