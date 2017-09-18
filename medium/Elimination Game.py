#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 7/30/17
  
"""


class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        remain, left, head, step = n, True, 1, 1
        while remain > 1:
            if left or remain & 1 == 1:
                head += step
            remain /= 2
            step *= 2
            left = ~left
        return head
            