#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 7/27/17
  
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
    
    
    def union_find(self, grid, id):
        count = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j] == '1': count += 1
                id[i] = len(grid[i]) * i + j
        return count
    
    def find(self, id, x):
        if id[x] != x:
            id[x] = self.find(id, id[x])
        return id[x]
    
    def union(self, id, x, y, count):
        id_x = id[x]
        id_y = id[y]
        if id_x == id_y:
            return count
        id[id_x] = id_y
        return count - 1
    
    def is_connected(self, id, p, q):
        p_root = self.find(id, p)
        q_root = self.find(id, q)
        return p_root == q_root
    
    
        
                    
        
    
    
#     # dfs
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         result = 0
#         for i in xrange(len(grid)):
#             for j in xrange(len(grid[i])):
#                 if grid[i][j] == '1':
#                     result += 1
#                     self.dfs(grid, i, j)
#         return result
#
#
#     def dfs(self,  grid, i, j):
#         if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0' or grid[i][j] == '-1':
#             return
#         if grid[i][j] == '1':
#             grid[i][j] = '-1'
#             self.dfs(grid, i - 1, j)
#             self.dfs(grid, i + 1, j)
#             self.dfs(grid, i, j - 1)
#             self.dfs(grid, i, j + 1)
#             grid[i][j] = '1'
#         return
#
# s = Solution()
