#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal == 0:
            return True
        d = {}
        visited = ['0' for i in xrange(maxChoosableInteger + 1)]
        return self.dfs(desiredTotal, visited, d)
        
    def dfs(self, disired, visited, d):
        if disired <= 0:
            return False
        key = ''.join(visited)
        if key in d:
            return d[key]
        for i in xrange(1, len(visited)):
            if visited[i] == '0':
                visited[i] = '1'
                if not self.dfs(disired - i, visited, d):
                    k = ''.join(visited)
                    d[k] = True
                    visited[i] = '0'
                    return True
                visited[i] = '0'
        d[key] = False
        return False
    
    
        
    
s = Solution()
print s.canIWin(10, 16)
        
        
        