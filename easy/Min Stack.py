#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 6/1/17
  
"""

from heapq import *

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        min_value = self.getMin()
        if x < min_value:
            min_value = x
        self.data.append((x, min_value))

    def pop(self):
        """
        :rtype: void
        """
        if self.data:
            self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1][0]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1][1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

    