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
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0: mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root