#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/28/17
  
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (not p and not q) or (p.val == q.val):
            return True
        return self.isSameTree(p.left, q.left) or self.isSameTree(p.right, q.right)


    