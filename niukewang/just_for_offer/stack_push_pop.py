#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/11/17
  
"""


class Solution:
    def IsPopOrder(self, pushV, popV):
        stack = []
        index_pop = 0
        while index_pop < len(popV):
            if len(stack) == 0 or stack[-1] != popV[index_pop]:
                if len(pushV) == 0:
                    return False
                stack.append(pushV.pop(0))
            else:
                stack.pop()
                index_pop += 1
        return True
    
s = Solution()
push = [1, 2, 3, 4, 5]
pop = [4,3,5,1,2]
print s.IsPopOrder(push, pop)
                
            
            
            
