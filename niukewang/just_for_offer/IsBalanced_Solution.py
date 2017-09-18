#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/13/17
  
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        return self._is_balance(pRoot) != -1

        
    def _is_balance(self, root):
        if root is None:
            return 0
        left_depth = self._is_balance(root.left)
        if left_depth == -1:
            return -1
        right_depth = self._is_balance(root.right)
        if right_depth == -1:
            return -1
        if abs(left_depth - right_depth) > 1:
            return -1
        else:
            return max(left_depth, right_depth) + 1
