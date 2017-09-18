#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 7/27/17
  
"""


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        brick = {1: 0}
        result = 0
        for w in wall:
            s = 0
            for x in w[:-1]:
                s += x
                brick[s] = brick.get(s, 0) + 1
                result = max(result, brick[s])
        print brick
        return len(wall) - result
        
        
a = [[1],[1],[1]]
s = Solution()
print s.leastBricks(a)