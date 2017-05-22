#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 5/18/17
  
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        temp_node = [root]
        while temp_node:
            l = []
            