#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/11/17
  
"""
class Solution:
    data = []
    min_data = []
    min_value = (1 << 30) - 1
    
    def push(self, node):
        # write code here
        if len(self.data) == 0:
            self.min_value = node
        else:
            self.min_value = min(self.min_value, node)
        self.data.append(node)
        self.min_data.append(self.min_value)
    
    def pop(self):
        # write code here
        if len(self.data) == 0:
            raise ValueError
        else:
            result = self.data.pop()
            _ = self.min_data.pop()
            return result
    
    def top(self):
        # write code here
        if len(self.data) == 0:
            raise ValueError
        else:
            return self.data[-1]
    
    def min(self):
        # write code here
        if len(self.min_data) == 0:
            raise ValueError
        else:
            return self.min_data[-1]
        
s = Solution()
s.push(3)
print s.min()
