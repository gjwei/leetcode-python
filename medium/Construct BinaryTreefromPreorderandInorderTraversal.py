#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/25/17
  
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root = TreeNode(preorder[0])

            root_index_inorder = inorder.index(root.val)
            left_part_length = len(inorder[:root_index_inorder])

            root.left = self.buildTree(preorder[1:left_part_length + 1], inorder[:left_part_length])
            root.right = self.buildTree(preorder[left_part_length + 1:], inorder[left_part_length:])
            return root



    