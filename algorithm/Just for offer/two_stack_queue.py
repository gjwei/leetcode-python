#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/27/17
  
"""


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)
        # write code here

    def pop(self):
        # return xx
        if len(self.stack2):
            return self.stack2.pop()

        if len(self.stack1):
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())
                return self.stack2.pop()
s = Solution()
s.push(2)
s.push(3)
s.push(4)
print s.pop()
print s.pop()
print s.pop()