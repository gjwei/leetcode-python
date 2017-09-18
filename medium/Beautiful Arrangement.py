#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 7/27/17
  
"""

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        is_visited = [False for _ in xrange(N)]
        count = [0]
        self.dfs(count, 0, is_visited, N)
        return count[0]
        
        
    def dfs(self, count, pos, is_visited, n):
        if pos == n:
            count[0] += 1
            return
        if pos > n:
            return
        for i in xrange(n):
            if not is_visited[i] and self.is_beautiful(i+1, pos+1):
                is_visited[i] = True
                self.dfs(count, pos+1, is_visited, n)
                is_visited[i] = False
    
    def is_beautiful(self, a, i):
        return a % i == 0 or i % a == 0
            
s = Solution()
print s.countArrangement(2)