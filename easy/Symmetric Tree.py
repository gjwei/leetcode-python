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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_symmetric(root, root)

    def is_symmetric(self, left_node, right_node):
        #left_node, right_node = root, root
        if not left_node and not right_node:
            return True
        if left_node and right_node and (left_node.val == right_node.val):
            return self.is_symmetric(left_node.left, right_node.right) and self.is_symmetric(left_node.right, right_node.left)
        else:
            return False


    