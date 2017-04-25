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
#
#         self.right = None
from TreeNode import TreeNode


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.buildTreeRecursive(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)


    def buildTreeRecursive(self, inorder, in_left, in_right, postorder, post_left, post_right):
        if in_left > in_right or post_left > post_right:
            return None

        root = TreeNode(postorder[post_right])
        root_index_inorder = self.find_root_position_in_inorder(inorder, root)

        left_part_length = root_index_inorder - in_left

        root.left = self.buildTreeRecursive(inorder, in_left, root_index_inorder - 1, postorder, post_left, post_left + left_part_length - 1)
        root.right = self.buildTreeRecursive(inorder, root_index_inorder + 1, in_right, postorder, post_left + left_part_length, post_right - 1)
        return root



    def find_root_position_in_inorder(self, inorder, root):
        for i in xrange(len(inorder)):
            if root.val == inorder[i]:
                return i
        return -1


    