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
        if not root:
            return [[]]
        stack1, stack2 = [root], []
        result = []
        while stack1:       
            l = []
            while stack1:
                p = stack1.pop()
                l.append(p.val)
                if not p.left:
                    stack2.append(p.left)
                if not p.right:
                    stack2.append(p.right)
            result.append(l)
            stack1, stack2 = stack2, stack1
        return result

                        

