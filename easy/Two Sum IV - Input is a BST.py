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
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nums = []
        p = root
        stack = []
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                q = stack.pop()
                nums.append(q.val)
                p = q.right
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == k:
                return True
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return False
                
    #     if not root:
    #         return False
    #     stack = [root]
    #     while stack:
    #         p = stack.pop()
    #         r = self.bst_search(root, k - p.val)
    #         if r and r != p:
    #             return True
    #         if p.left:
    #             stack.append(p.left)
    #         if p.right:
    #             stack.append(p.right)
    #     return False
    #
    #
    # def bst_search(self, root, t):
    #     if not root:
    #         return None
    #     if root.val == t:
    #         return root
    #     elif root.val > t:
    #         return self.bst_search(root.left, t)
    #     else:
    #         return self.bst_search(root.right, t)
    #
    #
    #