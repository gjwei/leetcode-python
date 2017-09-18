#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/7/17
  
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max_num_index = self.get_max_index(nums)
        root = TreeNode(nums[max_num_index])
        root.left = self.constructMaximumBinaryTree(nums[0:max_num_index])
        root.right = self.constructMaximumBinaryTree(nums[max_num_index+1:])
        return root
        
    def get_max_index(self, nums):
        m = 0
        for i, n in enumerate(nums):
            if n > nums[m]:
                m = i
        return m