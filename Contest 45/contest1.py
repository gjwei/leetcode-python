#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/13/17
  
"""


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        count = [0, 0]
        for m in moves:
            if m == 'U':
                count[0] += 1
            elif m == 'D':
                count[0] -= 1
            elif m == 'L':
                count[1] += 1
            else:
                count[1] -= 1
        return count[0] == 0 and count[1] == 0
    
s = Solution()
print s.judgeCircle("UD")
            
        
